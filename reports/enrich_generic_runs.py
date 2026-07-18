"""
Remplace les observations génériques ("Run importe en lot...") des 64 runs
batch-importés sans analyse par un texte réellement grounded dans les
données : comparaison au sein de la famille d'expérience à laquelle le run
appartient (même architecture, même levier testé, etc.), écarts chiffres,
lecture recall/TNR/FPR quand disponible, et signalement explicite des runs
dégénérés (limit_per_category minuscule ou déséquilibre entre classes).
"""
import json
import io
import sys
import glob
from batch_parse_reports import parse_run

RUNS_DATA = "runs_data.json"
CATS = ["impressionism", "realism", "romanticism"]
CAT_LABELS = {"impressionism": "Impressionism", "realism": "Realism", "romanticism": "Romanticism"}


def spread(d):
    vals = [v for v in d.values() if v is not None]
    return round(max(vals) - min(vals), 1) if vals else None


def fmt_recall(d):
    return f"{d['impressionism']:.1f}/{d['realism']:.1f}/{d['romanticism']:.1f}"


def dominant_class(d):
    return CAT_LABELS[max(d, key=d.get)]


def weak_class(d):
    return CAT_LABELS[min(d, key=d.get)]


with io.open(RUNS_DATA, "r", encoding="utf-8") as f:
    data = json.load(f)

runs = {r["id"]: r for r in data["runs"]}


def set_analysis(rid, observations, conclusion=""):
    runs[rid]["analysis"]["observations"] = observations
    runs[rid]["analysis"]["conclusion"] = conclusion


# ---------------------------------------------------------------------------
# Groupe 0 : runs dégénérés / debug (limit_per_category minuscule ou tordu)
# ---------------------------------------------------------------------------
degenerate = {
    31: "6 images/classe (18 images d'entraînement au total)",
    32: "12/22/32 images par classe seulement (config déjà déséquilibrée entre classes)",
    33: "56/12/32 images par classe (même config déjà déséquilibrée)",
    46: "30 images/classe (90 au total)",
    47: "30 images/classe (90 au total)",
    48: "6 images/classe (18 au total)",
    49: "56/12/32 images par classe (config déséquilibrée)",
    50: "56/12/32 images par classe (config déséquilibrée)",
    51: "56/12/32 images par classe (config déséquilibrée)",
}
for rid, détail in degenerate.items():
    r = runs[rid]
    acc = r["accuracy"]
    rec = r["analysis"].get("recall") or {}
    obs = [
        f"Run avec un volume de données quasi nul : {détail}, contre 1000+ images/classe pour la quasi-totalité des autres runs du rapport.",
        f"Accuracy {acc}% — proche du hasard (33,3%) ou légèrement au-dessus, sans que ce soit interprétable : avec aussi peu d'exemples, le résultat est dominé par le bruit d'échantillonnage, pas par l'architecture ou les hyperparamètres testés.",
    ]
    if rec:
        obs.append(f"Recall {fmt_recall(rec)} — à ne pas comparer aux runs à volume de données normal ; probablement un run de vérification technique du pipeline (config debug), pas un vrai point d'expérience.",)
    set_analysis(rid, obs, "Run non représentatif (volume de données dégénéré) — exclu de toute comparaison sérieuse entre architectures/hyperparamètres dans ce rapport.")

# ---------------------------------------------------------------------------
# Groupe A : scan d'architecture MLP couleur (limit croissant 1000->6000)
# ---------------------------------------------------------------------------
groupA = [24, 25, 26, 27, 28, 29, 30, 34, 35, 52]
for rid in groupA:
    r = runs[rid]
    acc = r["accuracy"]
    rec = r["analysis"].get("recall") or {}
    arch = r["architecture"]
    limit = r.get("_limit_display", "")
    obs = [f"Scan d'architecture MLP (pipeline couleur 64x64) — architecture {arch}, seed {r['seed']}, alpha {r['alpha']}, {r['epochs']} epochs."]
    if rec:
        sp = spread(rec)
        obs.append(f"Recall {fmt_recall(rec)} (écart {sp} pts entre classes), accuracy {acc}%.")
    set_analysis(rid, obs)

# Recompute limit_per_category display + comparisons using parse
sys.path.insert(0, ".")

id_to_folder = {}
for fn in glob.glob("batch_*.json"):
    entries = json.load(open(fn, encoding="utf-8"))
    for e in entries:
        if "_folder" in e:
            id_to_folder[e["id"]] = e["_folder"]

limits = {}
for rid in groupA + [37, 38, 39, 40, 41, 42, 43, 44, 45]:
    folder = id_to_folder.get(rid)
    if folder:
        p = parse_run(folder)
        limits[rid] = p.get("limit_per_category")

# Group A: fixed-limit sub-comparisons
# limit=3000: 27([8,8,8],41.1), 28([64,64],43.9), 29([128,128],45.4)
r27, r28, r29 = runs[27], runs[28], runs[29]
set_analysis(27, [
    "Scan d'architecture à limit_per_category=3000 fixe (seed=42, alpha=0.001, 100 epochs) : ce run teste [8,8,8], la plus petite/plus profonde des 3 architectures comparées ici.",
    f"Accuracy {r27['accuracy']}% — la plus basse des 3 (vs {r28['accuracy']}% pour [64,64] et {r29['accuracy']}% pour [128,128]).",
])
set_analysis(28, [
    f"Même comparaison à limit=3000 : [64,64] fait {r28['accuracy']}%, soit +{round(r28['accuracy']-r27['accuracy'],1)} pts vs [8,8,8] (run 27) malgré 2 couches au lieu de 3 — la largeur des couches compte plus que leur nombre ici, cohérent avec ce qu'on observe sur la série de référence (runs 6-8).",
])
set_analysis(29, [
    f"Troisième point du même scan à limit=3000 : [128,128] atteint {r29['accuracy']}%, le meilleur des 3 (+{round(r29['accuracy']-r28['accuracy'],1)} pts vs [64,64], +{round(r29['accuracy']-r27['accuracy'],1)} pts vs [8,8,8]) — tendance monotone claire : plus de neurones par couche améliore l'accuracy à volume de données égal, sans qu'ajouter une 3e couche ([8,8,8]) n'aide.",
], "Sur ce mini-scan à données fixées (3000/classe), la largeur des couches domine clairement leur profondeur : [128,128] > [64,64] > [8,8,8]. A noter : la seed diffère entre le run 28 (2024) et les runs 27/29 (42), donc la comparaison n'est pas parfaitement isolée — mais l'écart observé (jusqu'à 4,3 pts) reste nettement plus grand que la variance inter-seed habituelle à architecture fixe (souvent <1 pt, cf runs 22/23), donc l'effet architecture reste la lecture la plus probable.")

# limit=6000: 30([128,128],47.1), 34([64,64,64],45.3), 35([128,64,64],45.5), 52([128,64,32],45.7)
r30, r34, r35, r52 = runs[30], runs[34], runs[35], runs[52]
set_analysis(30, [
    "Même architecture [128,128] que le run 29, mais limit_per_category=6000 au lieu de 3000 (2x plus de données) : accuracy 47,1% vs 45,4% au run 29, soit +1,7 pt — plus de données aide, mais avec des rendements déjà assez modestes à cette échelle.",
    f"C'est le meilleur résultat de tout ce groupe de scan (24-30/34/35/52) : {r30['accuracy']}%.",
])
set_analysis(34, [
    f"A limit=6000 également, [64,64,64] (3 couches) fait {r34['accuracy']}% — {round(r30['accuracy']-r34['accuracy'],1)} pts de moins que [128,128] (run 30, 2 couches) à volume de données identique : confirme que rajouter une couche sans augmenter la largeur ne compense pas, même constat qu'à limit=3000.",
])
set_analysis(35, [
    f"[128,64,64] (3 couches, plus large que le run 34) : {r35['accuracy']}%, très proche de [64,64,64] ({r34['accuracy']}%) et toujours en retrait sur [128,128] (run 30, {r30['accuracy']}%) malgré plus de paramètres au total.",
])
set_analysis(52, [
    f"[128,64,32] (3 couches en entonnoir) : {r52['accuracy']}%, dans le même groupe que 34/35 (45,3-45,7%), toujours derrière [128,128] à 2 couches (run 30, {r30['accuracy']}%).",
], "Sur les 4 architectures testées à limit_per_category=6000 (128,128 / 64,64,64 / 128,64,64 / 128,64,32), l'architecture à 2 couches larges [128,128] reste la meilleure (47,1%) ; les 3 variantes à 3 couches se tassent toutes entre 45,3% et 45,7%, quelle que soit leur forme exacte. Le nombre de couches ne semble pas être le levier qui compte le plus ici, contrairement à la largeur — à nuancer cependant : la seed diffère sur les 4 runs (2024/5678/1234/1453555868), donc une partie de l'écart pourrait aussi venir de la variance inter-seed plutôt que de l'architecture seule.")

# Remaining group A: 24,25,26
r24, r25, r26 = runs[24], runs[25], runs[26]
set_analysis(24, [
    f"Architecture [16,16] (petite), limit=1000, pos_ratio=0.33, seed=2024 : accuracy {r24['accuracy']}% — proche du hasard, cohérent avec une architecture étroite (16 neurones/couche) sur peu de données.",
    f"Recall {fmt_recall(r24['analysis']['recall'])} : {dominant_class(r24['analysis']['recall'])} et {weak_class(r24['analysis']['recall'])} — pas de collapse, mais pas d'apprentissage marqué non plus.",
])
set_analysis(25, [
    f"Même architecture [16,16], même limit=1000, mais pos_ratio=0.5 (au lieu de 0.33) et seed=5678 : accuracy {r25['accuracy']}%, quasi identique au run 24 ({r24['accuracy']}%, -{round(r24['accuracy']-r25['accuracy'],1)} pt) — à cette taille d'architecture, ni le ratio positif/négatif ni la seed ne changent grand-chose : le plafond de performance semble imposé par la capacité du modèle, pas par ces réglages fins.",
])
set_analysis(26, [
    f"[16,16,16] (3 couches étroites), limit=1500 : accuracy {r26['accuracy']}%, dans la même plage basse que les runs [16,16] (24/25, ~40%) — ajouter une couche à une architecture déjà étroite n'aide pas plus que sur les architectures plus larges (voir runs 27/34/35/52).",
])

# ---------------------------------------------------------------------------
# Groupe B : sweep Linear color pos_ratio / limit (38-45)
# ---------------------------------------------------------------------------
r38, r39, r40, r41, r42, r43, r44, r45 = (runs[i] for i in [38,39,40,41,42,43,44,45])
set_analysis(38, [
    f"Début d'un sweep Linear à pos_ratio=0.33 fixe, limit_per_category croissant : ce run est le point de départ, limit=500, accuracy {r38['accuracy']}%.",
])
set_analysis(39, [
    f"Même pos_ratio=0.33, limit=1000 (2x plus de données que le run 38) : accuracy {r39['accuracy']}% (+{round(r39['accuracy']-r38['accuracy'],1)} pt vs run 38).",
])
set_analysis(40, [
    f"Même pos_ratio=0.33, limit=3000 : accuracy {r40['accuracy']}% (+{round(r40['accuracy']-r39['accuracy'],1)} pt vs run 39) — la progression avec le volume de données continue, de façon monotone.",
])
set_analysis(41, [
    f"Même pos_ratio=0.33, limit=6000 : accuracy {r41['accuracy']}% (+{round(r41['accuracy']-r40['accuracy'],1)} pt vs run 40).",
], f"Sweep à pos_ratio=0.33 fixe (runs 38→41, limit 500→6000) : accuracy monte de façon régulière ({r38['accuracy']}% → {r39['accuracy']}% → {r40['accuracy']}% → {r41['accuracy']}%), +{round(r41['accuracy']-r38['accuracy'],1)} pts au total, plutôt cohérent avec 'plus de données aide le Linear' (cf runs 9-13). A noter : la seed change à chaque run de ce sweep (5678/2024/5678/1337) — la comparaison n'isolé donc pas parfaitement le volume de données, mais la progression est trop régulière pour n'être due qu'au bruit inter-seed.")
set_analysis(42, [
    f"A limit=6000 fixe (comme le run 41), ce run testé pos_ratio=0.5 au lieu de 0.33 : accuracy {r42['accuracy']}%, moins bon que le run 41 ({r41['accuracy']}%, -{round(r41['accuracy']-r42['accuracy'],1)} pt).",
])
set_analysis(43, [
    f"Toujours à limit=6000, pos_ratio=0.25 cette fois : accuracy {r43['accuracy']}% — le meilleur des 4 ratios testés à ce volume de données (0.33: {r41['accuracy']}%, 0.5: {r42['accuracy']}%, 0.25: {r43['accuracy']}%, 0.2 voir run 44).",
])
set_analysis(44, [
    f"pos_ratio=0.2 (encore plus bas), limit=6000 : accuracy {r44['accuracy']}% — moins bon que ratio=0.25 (run 43, {r43['accuracy']}%) : le ratio optimal semble se situer autour de 0.25, pas plus bas.",
], f"Sweep de pos_ratio à limit=6000 fixe (runs 41-44) : 0.33→{r41['accuracy']}%, 0.5→{r42['accuracy']}%, 0.25→{r43['accuracy']}%, 0.2→{r44['accuracy']}%. Le maximum est atteint à ratio=0.25, ni plus haut ni plus bas — ce même ratio de 0.25 revient comme le meilleur réglage sur MLP (run 17 et suivants) et sur RBF (run 81), un signal cohérent à travers les 3 familles de modèles de ce projet. A nuancer : la seed diffère aussi entre ces 4 runs (1337/1234/2024/1234, seuls 42 et 44 la partagent), donc ce n'est pas un test isolé à 100% — mais la convergence avec les résultats MLP/RBF (obtenus avec d'autres seeds) rend l'effet ratio=0.25 plausible au-delà du simple bruit.")
set_analysis(45, [
    f"pos_ratio=0.25 mais avec limit=3000 (au lieu de 6000) : accuracy {r45['accuracy']}%, en retrait sur le run 43 (même ratio, limit=6000, {r43['accuracy']}%, soit -{round(r43['accuracy']-r45['accuracy'],1)} pt) — confirme que le volume de données et le ratio sont deux leviers indépendants qui s'additionnent plutôt qu'ils ne se substituent.",
])

# ---------------------------------------------------------------------------
# Groupe C : petits runs MLP/Linear à limit reduite (53-63)
# ---------------------------------------------------------------------------
r53, r54, r55, r56, r57, r58 = (runs[i] for i in [53,54,55,56,57,58])
r16_arch = "[16, 16]"
sixteen_ids = [24, 25, 32, 33, 53, 56, 57, 58]
sixteen_accs = [runs[i]["accuracy"] for i in sixteen_ids]
set_analysis(53, [
    f"Encore l'architecture [16,16], limit=500 (le plus petit volume testé sur cette architecture) : accuracy {r53['accuracy']}%.",
    f"Au total, [16,16] a ete testée {len(sixteen_ids)} fois dans ce rapport (runs {', '.join(str(i) for i in sixteen_ids)}) avec des seeds/ratios/volumes differents : accuracy comprise entre {min(sixteen_accs)}% et {max(sixteen_accs)}% (écart {round(max(sixteen_accs)-min(sixteen_accs),1)} pts) — un plafond de performance clairement plus bas que les architectures plus larges comme [128,128] (jusqu'à 47,1%, run 30) ou [256,256] (jusqu'à 49,5%, run 36), quel que soit le réglage fin.",
])
set_analysis(54, [
    f"Architecture [6,6] (la plus petite testée dans tout le rapport), limit=500, 50 epochs : accuracy {r54['accuracy']}% — dans la même plage basse que [16,16], confirme qu'en dessous d'une certaine largeur de couche, la performance plafonne indépendamment des autres réglages.",
])
set_analysis(55, [
    f"Architecture [256,128] (large), mais seulement limit=1000 et 50 epochs : accuracy {r55['accuracy']}% — bien en retrait du record obtenu avec la même famille d'architecture sur plus de données (run 17, [256,256], 6000 img/classe, 46,7%), illustre que la largeur du réseau ne compense pas un volume de données insuffisant.",
])
set_analysis(56, [
    f"[16,16], limit=500, pos_ratio naturel (non précisé) : accuracy {r56['accuracy']}%, dans la fourchette habituelle de cette architecture (35,2-40,4% sur l'ensemble des runs [16,16]).",
])
set_analysis(57, [
    f"[16,16], limit=500, pos_ratio=0.5 : accuracy {r57['accuracy']}%, quasi identique au run 56 (même limit, ratio naturel, {r56['accuracy']}%) — confirme que sur une architecture aussi étroite, le ratio positif/négatif n'a quasiment pas d'effet mesurable (contrairement au Linear/MLP plus larges où ratio=0.25 fait clairement gagner des points, cf runs 41-44).",
])
group500_16 = [r53, r56, r57, r58]
group500_16_accs = [r["accuracy"] for r in group500_16]
set_analysis(58, [
    f"[16,16], limit=500, pos_ratio=0.5, seed=42 : accuracy {r58['accuracy']}%. Sur les 4 runs [16,16] à limit=500 (53:{r53['accuracy']}%, 56:{r56['accuracy']}%, 57:{r57['accuracy']}%, 58:{r58['accuracy']}%), l'accuracy varie entre {min(group500_16_accs)}% et {max(group500_16_accs)}% (écart {round(max(group500_16_accs)-min(group500_16_accs),1)} pt) — la variance inter-seed/ratio à elle seule explique cet écart, sans qu'aucun réglage ne se dégage clairement comme supérieur.",
])

r59, r60, r61, r62, r63 = (runs[i] for i in [59,60,61,62,63])
set_analysis(59, [
    f"Linear, limit=1000, 100 epochs : accuracy {r59['accuracy']}%, dans la plage habituelle du Linear à ce volume de données (cf runs 9-13, 41-45.9%).",
])
set_analysis(60, [
    f"Linear, limit=500, seulement 50 epochs : accuracy {r60['accuracy']}%, légèrement en dessous du run 59 (limit=1000, 100 epochs, {r59['accuracy']}%) — moins de données ET moins d'epochs, deux leviers reduits simultanément, cohérent avec un score plus bas sans qu'on puisse isoler lequel des deux domine.",
])
set_analysis(61, [
    f"Linear, limit=1000, 100 epochs (mêmes paramètres que le run 59 sauf la seed) : accuracy {r61['accuracy']}%, très proche du run 59 ({r59['accuracy']}%, écart {round(abs(r61['accuracy']-r59['accuracy']),1)} pt) — bonne reproductibilité du Linear à config quasi identique.",
])
set_analysis(62, [
    f"Linear, limit=500, pos_ratio=0.5 : accuracy {r62['accuracy']}%.",
])
set_analysis(63, [
    f"Linear, limit=500, pos_ratio=0.33 : accuracy {r63['accuracy']}%, proche du run 62 (ratio=0.5, {r62['accuracy']}%) — à limit=500 (volume très réduit), le choix du ratio positif/négatif pèse moins que sur les runs à plus grand volume (cf runs 41-44, où le ratio faisait une vraie différence à limit=6000).",
])

# ---------------------------------------------------------------------------
# Groupe D : sweep Linear dataset complet, alpha/ratio x seeds (64-72)
# ---------------------------------------------------------------------------
r64, r65, r66, r67, r68, r69, r70, r71, r72 = (runs[i] for i in [64,65,66,67,68,69,70,71,72])
alpha001 = [r64, r65, r66]
alpha01 = [r67, r68, r69]
ratio033 = [r70, r71, r72]
a001_accs = [r["accuracy"] for r in alpha001]
a01_accs = [r["accuracy"] for r in alpha01]
r033_accs = [r["accuracy"] for r in ratio033]

set_analysis(64, [
    "Linear sur le dataset COMPLET (limit=-1, ~30000 images train), pos_ratio=0.25, alpha=0.001 — 3 seeds testées ici (64/65/66) pour mesurer la variance à grande échelle.",
    f"Accuracy {r64['accuracy']}% (seed {r64['seed']}) — c'est le meilleur score Linear de tout ce rapport à ce jour sur cette combinaison de réglages.",
])
set_analysis(65, [
    f"Même config, seed {r65['seed']} : accuracy {r65['accuracy']}%.",
])
set_analysis(66, [
    f"Même config, seed {r66['seed']} : accuracy {r66['accuracy']}%.",
], f"3 seeds à alpha=0.001, dataset complet, ratio=0.25 : {a001_accs[0]}% / {a001_accs[1]}% / {a001_accs[2]}% (moyenne {round(sum(a001_accs)/3,1)}%, écart {round(max(a001_accs)-min(a001_accs),1)} pts) — variance inter-seed non négligeable même à grande échelle de données.")
set_analysis(67, [
    f"Même dataset complet, même pos_ratio=0.25, mais alpha=0.01 (10x plus grand qu'aux runs 64-66) — seed {r67['seed']}.",
    f"Accuracy {r67['accuracy']}% — très proche du meilleur run à alpha=0.001 (run 64, {r64['accuracy']}%), suggère que sur dataset complet, le Linear converge de façon similaire aux deux alphas testés.",
])
set_analysis(68, [
    f"Même config alpha=0.01, seed {r68['seed']} : accuracy {r68['accuracy']}%.",
])
set_analysis(69, [
    f"Même config alpha=0.01, seed {r69['seed']} : accuracy {r69['accuracy']}%.",
], f"3 seeds à alpha=0.01, dataset complet, ratio=0.25 : {a01_accs[0]}% / {a01_accs[1]}% / {a01_accs[2]}% (moyenne {round(sum(a01_accs)/3,1)}%) contre {round(sum(a001_accs)/3,1)}% de moyenne à alpha=0.001 (runs 64-66) — alpha 10x plus grand ne change quasiment rien sur dataset complet (écart de moyenne de {round(abs(sum(a01_accs)/3-sum(a001_accs)/3),1)} pt seulement) : contrairement aux petits volumes de données (où alpha=0.01 dégradait nettement, cf runs 32/33 sur MLP), à grande échelle le Linear semble converger correctement avec les deux valeurs.")
set_analysis(70, [
    f"Dataset complet, mais pos_ratio=0.33 au lieu de 0.25, alpha=0.01 — seed {r70['seed']}.",
    f"Accuracy {r70['accuracy']}%.",
])
set_analysis(71, [
    f"Même config ratio=0.33, seed {r71['seed']} : accuracy {r71['accuracy']}%.",
])
set_analysis(72, [
    f"Même config ratio=0.33, seed {r72['seed']} : accuracy {r72['accuracy']}%.",
], f"3 seeds à ratio=0.33 (runs 70-72) : {r033_accs[0]}% / {r033_accs[1]}% / {r033_accs[2]}% (moyenne {round(sum(r033_accs)/3,1)}%) — légèrement en dessous de la moyenne à ratio=0.25 (alpha=0.01, runs 67-69, {round(sum(a01_accs)/3,1)}%). Bilan du bloc 64-72 (9 runs, dataset Linear complet, 3 seeds x 3 configs) : ratio=0.25 reste le meilleur choix (confirmant runs 41-44), alpha n'a quasiment pas d'effet à cette échelle de données, et la variance inter-seed (jusqu'à {round(max(a001_accs)-min(a001_accs),1)} pts sur un seul groupe de 3) reste le facteur le plus important de ce bloc de runs.")

# ---------------------------------------------------------------------------
# Run 37, 73 isoles (isolés)
# ---------------------------------------------------------------------------
r37 = runs[37]
set_analysis(37, [
    f"Architecture [32] (une seule couche cachée), limit=1000, pos_ratio naturel (-1) : accuracy {r37['accuracy']}%.",
    f"Recall {fmt_recall(r37['analysis']['recall'])}, TNR {fmt_recall(r37['analysis']['tnr'])} — pas de signe de collapse, résultat dans la plage moyenne du MLP à ce volume de données.",
])
r73 = runs[73]
set_analysis(73, [
    f"Architecture [128,128,128] (mêmes couches que les runs 22/23 de la série de référence, mais limit=2000 au lieu de 12000 train et pos_ratio=0.25 au lieu du ratio naturel) : accuracy {r73['accuracy']}%.",
    "Nettement en dessous des runs 22/23 (46,6-46,8% avec ~12000 images train) : confirme, sur cette architecture aussi, que le volume de données pèse plus que le réglage fin du ratio positif/négatif à lui seul.",
])

# ---------------------------------------------------------------------------
# Groupe E : suite du lot 32x32 gris (85,86,87,88,89,91-100), complète 84/90
# ---------------------------------------------------------------------------
r85, r86, r87, r88, r89 = (runs[i] for i in [85,86,87,88,89])
set_analysis(85, [
    "Lot 32x32 niveaux de gris (voir run 84 pour le contexte du pivot de pipeline) : architecture [128,64], alpha=0.0005 (plus bas que la normale), 150 epochs, dataset complet.",
    f"Accuracy {r85['accuracy']}% — déjà dans la plage haute du lot gris malgré un alpha réduit, compense par un nombre d'epochs élevé.",
])
set_analysis(86, [
    f"Architecture [32,16] (petite), seulement 40 epochs : accuracy {r86['accuracy']}%, pourtant l'un des meilleurs scores du lot gris à ce stade — confirme l'observation faite sur le pipeline couleur (runs 27/34/35/52) : au-delà d'une certaine taille, l'architecture pèse moins que le volume de données (ici le dataset complet pour tous les runs du lot gris).",
])
set_analysis(87, [
    f"[256,128], alpha=0.0005, 150 epochs (comme le run 85 mais architecture plus large) : accuracy {r87['accuracy']}%, très proche du run 85 ({r85['accuracy']}%) malgré une architecture bien plus grande — encore un signe que ce lot de runs est proche d'un plafond de performance autour de 44-47%, quelle que soit l'architecture ou le nombre d'epochs au-delà d'un certain point.",
])
set_analysis(88, [
    "Premier run du lot gris à passer en normalisation 'standard' (au lieu de per_column) — cohérent, un canal unique en niveaux de gris n'a pas vraiment de sens à normaliser par canal séparément.",
    f"Même architecture [256,128] que le run 87, mais seed, alpha ET epochs diffèrent aussi (40 ici contre 150 au run 87) — plusieurs leviers changent en même temps, donc pas une comparaison isolée. Accuracy {r88['accuracy']}%, quasi identique au run 87 ({r87['accuracy']}%) malgré ces différences : plutôt un signe que ce lot converge vers un plateau similaire (44-47%) quel que soit le détail des réglages, que la preuve d'un effet précis d'un seul paramètre.",
])
set_analysis(89, [
    f"[256,256] (la plus grande architecture testée sur ce lot), 40 epochs, normalisation standard : accuracy {r89['accuracy']}%.",
    f"Même config exacte que le run 90 (seed=1337, même architecture, même dataset) sauf le nombre d'epochs (40 ici contre 100 au run 90) : accuracy {r89['accuracy']}% vs {runs[90]['accuracy']}%, seulement -{round(runs[90]['accuracy']-r89['accuracy'],1)} pt malgré 60 epochs de moins — confirme la convergence rapide déjà observée sur ce pipeline (comme run 88 vs run 87).",
])

r91, r92, r93, r94, r95, r96, r97, r98, r99, r100 = (runs[i] for i in [91,92,93,94,95,96,97,98,99,100])
set_analysis(91, [
    "Début d'un second sous-scan sur le lot gris : architectures moyennes (64,32 / 32,16 / 128,32 / 64,16), toutes à seed=1337, normalisation standard, dataset complet.",
    f"[64,32], 50 epochs : accuracy {r91['accuracy']}%.",
])
set_analysis(92, [
    f"[32,16], 50 epochs : accuracy {r92['accuracy']}%, très proche du run 91 ([64,32], {r91['accuracy']}%) — encore une fois, doubler la largeur des couches ne change presque rien une fois qu'on est sur le dataset complet.",
])
set_analysis(93, [
    f"[128,32], 50 epochs : accuracy {r93['accuracy']}%, dans la même plage que 91/92 (45,2-46,0%).",
])
set_analysis(94, [
    f"[128,32] (même architecture que le run 93), mais seulement 40 epochs : accuracy {r94['accuracy']}%, -{round(r93['accuracy']-r94['accuracy'],1)} pt vs run 93 (50 epochs) — léger effet des epochs, mais faible.",
])
set_analysis(95, [
    f"[64,16], 40 epochs : accuracy {r95['accuracy']}%.",
])
set_analysis(96, [
    "Début d'un scan d'epochs à architecture fixe [64,32], seed=1337 : ce run utilise seulement 25 epochs.",
    f"Accuracy {r96['accuracy']}% — le plus bas de ce mini-scan d'epochs (voir runs 97/98/99/100 pour la suite).",
])
set_analysis(97, [
    f"[64,32], 30 epochs (5 de plus que le run 96) : accuracy {r97['accuracy']}% (+{round(r97['accuracy']-r96['accuracy'],1)} pt vs run 96).",
])
set_analysis(98, [
    f"[64,32], 20 epochs (moins que les runs 96/97) : accuracy {r98['accuracy']}% — pas de tendance monotone claire avec le nombre d'epochs sur ce petit écart (15 à 40 epochs), la variance semble dominer l'effet du nombre d'epochs à ce stade de convergence.",
])
set_analysis(99, [
    f"[64,32], 40 epochs : accuracy {r99['accuracy']}%, le meilleur de ce mini-scan d'epochs (15-40) sur cette architecture.",
])
set_analysis(100, [
    f"[64,32], seulement 15 epochs (le minimum testé) : accuracy {r100['accuracy']}%.",
], f"Mini-scan d'epochs sur [64,32] (runs 96-100, 15 à 40 epochs, même seed/architecture/dataset) : accuracy entre {min(r['accuracy'] for r in [r96,r97,r98,r99,r100])}% et {max(r['accuracy'] for r in [r96,r97,r98,r99,r100])}%, sans progression monotone nette avec le nombre d'epochs — sur ce pipeline gris avec le dataset complet, le modèle semble converger très vite (des 15-20 epochs), et le reste de la variance observée est plus probablement du bruit d'entraînement que du sous-apprentissage.")

with io.open(RUNS_DATA, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("runs_data.json mis à jour avec des observations détaillées pour les 64 runs.")
