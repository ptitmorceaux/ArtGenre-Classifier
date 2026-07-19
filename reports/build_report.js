// Regenere Rapport_Tests_ArtGenre-Classifier.docx a partir de runs_data.json
//   + images/run_XX.png              (matrice de confusion, un fichier par run)
//   + tensorboard/run_XX*.png        (courbes TensorBoard, 0..N fichiers par run, optionnel)
// A relancer (node build_report.js) a chaque mise a jour de runs_data.json ou des dossiers d'images.
// Necessite : npm install docx image-size  (deja fait, voir reports/node_modules)

const fs = require("fs");
const path = require("path");
const sizeOf = require("image-size").default || require("image-size");
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  ImageRun, Header, Footer, AlignmentType, LevelFormat, TabStopType,
  TabStopPosition, HeadingLevel, BorderStyle, WidthType, ShadingType,
  PageNumber, PageBreak,
} = require("docx");

const HERE = __dirname;
const data = JSON.parse(fs.readFileSync(path.join(HERE, "runs_data.json"), "utf-8"));

const CONTENT_WIDTH = 9360; // US Letter, marges 1"
const MAX_IMG_WIDTH_PX = 560; // ~5.83in a 96dpi, tient dans la largeur de page

function imageParagraph(imgPath, altTitle) {
  const buffer = fs.readFileSync(imgPath);
  const dims = sizeOf(buffer);
  const scale = Math.min(1, MAX_IMG_WIDTH_PX / dims.width);
  const width = Math.round(dims.width * scale);
  const height = Math.round(dims.height * scale);

  return new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { after: 120 },
    children: [new ImageRun({
      type: path.extname(imgPath).slice(1).toLowerCase() === "jpg" ? "jpg" : path.extname(imgPath).slice(1).toLowerCase(),
      data: buffer,
      transformation: { width, height },
      altText: { title: altTitle, description: altTitle, name: altTitle },
    })],
  });
}

function findTensorboardImages(runId) {
  const dir = path.join(HERE, "tensorboard");
  if (!fs.existsSync(dir)) return [];
  const prefix = `run_${String(runId).padStart(2, "0")}`;
  return fs.readdirSync(dir)
    .filter(f => f.toLowerCase().startsWith(prefix) && /\.(png|jpe?g)$/i.test(f))
    .sort()
    .map(f => path.join(dir, f));
}
const border = { style: BorderStyle.SINGLE, size: 1, color: "CCCCCC" };
const borders = { top: border, bottom: border, left: border, right: border };
const HEADER_FILL = "1F4E79";
const ALT_FILL = "D5E8F0";

function labelValueTable(rows) {
  const colWidths = [3120, 6240];
  return new Table({
    width: { size: CONTENT_WIDTH, type: WidthType.DXA },
    columnWidths: colWidths,
    rows: rows.map(([label, value], i) => new TableRow({
      children: [
        new TableCell({
          borders,
          width: { size: colWidths[0], type: WidthType.DXA },
          shading: { fill: i % 2 === 0 ? "F2F7FB" : "FFFFFF", type: ShadingType.CLEAR },
          margins: { top: 60, bottom: 60, left: 120, right: 120 },
          children: [new Paragraph({ children: [new TextRun({ text: label, bold: true, size: 20 })] })],
        }),
        new TableCell({
          borders,
          width: { size: colWidths[1], type: WidthType.DXA },
          shading: { fill: i % 2 === 0 ? "F2F7FB" : "FFFFFF", type: ShadingType.CLEAR },
          margins: { top: 60, bottom: 60, left: 120, right: 120 },
          children: [new Paragraph({ children: [new TextRun({ text: String(value), size: 20 })] })],
        }),
      ],
    })),
  });
}

function recallTable(recall) {
  const cols = [3120, 3120, 3120];
  const header = new TableRow({
    children: Object.keys(recall).map((cls, i) => new TableCell({
      borders,
      width: { size: cols[i], type: WidthType.DXA },
      shading: { fill: HEADER_FILL, type: ShadingType.CLEAR },
      margins: { top: 60, bottom: 60, left: 120, right: 120 },
      children: [new Paragraph({
        alignment: AlignmentType.CENTER,
        children: [new TextRun({ text: cls, bold: true, size: 20, color: "FFFFFF" })],
      })],
    })),
  });
  const values = new TableRow({
    children: Object.values(recall).map((v, i) => new TableCell({
      borders,
      width: { size: cols[i], type: WidthType.DXA },
      shading: { fill: "FFFFFF", type: ShadingType.CLEAR },
      margins: { top: 60, bottom: 60, left: 120, right: 120 },
      children: [new Paragraph({
        alignment: AlignmentType.CENTER,
        children: [new TextRun({ text: `${v}%`, size: 22 })],
      })],
    })),
  });
  return new Table({
    width: { size: CONTENT_WIDTH, type: WidthType.DXA },
    columnWidths: cols,
    rows: [header, values],
  });
}

function confusionMetricsTable(cats, metrics) {
  // metrics: [{ label, values: {cat: pct} }, ...] -> tableau label en ligne, categories en colonne
  const labelColWidth = 2160;
  const catColWidth = Math.floor((CONTENT_WIDTH - labelColWidth) / cats.length);
  const cols = [labelColWidth, ...cats.map(() => catColWidth)];

  const header = new TableRow({
    children: ["", ...cats].map((label, i) => new TableCell({
      borders,
      width: { size: cols[i], type: WidthType.DXA },
      shading: { fill: HEADER_FILL, type: ShadingType.CLEAR },
      margins: { top: 50, bottom: 50, left: 100, right: 100 },
      children: [new Paragraph({
        alignment: AlignmentType.CENTER,
        children: [new TextRun({ text: label, bold: true, size: 18, color: "FFFFFF" })],
      })],
    })),
  });

  const rows = metrics.map((m, ri) => new TableRow({
    children: [m.label, ...cats.map(c => m.values[c] !== undefined && m.values[c] !== null ? `${m.values[c]}%` : "—")].map((cell, i) => new TableCell({
      borders,
      width: { size: cols[i], type: WidthType.DXA },
      shading: { fill: ri % 2 === 0 ? "F2F7FB" : "FFFFFF", type: ShadingType.CLEAR },
      margins: { top: 50, bottom: 50, left: 100, right: 100 },
      children: [new Paragraph({
        alignment: i === 0 ? AlignmentType.LEFT : AlignmentType.CENTER,
        children: [new TextRun({ text: String(cell), size: 18, bold: i === 0 })],
      })],
    })),
  }));

  return new Table({
    width: { size: CONTENT_WIDTH, type: WidthType.DXA },
    columnWidths: cols,
    rows: [header, ...rows],
  });
}

function bulletList(items) {
  return items.map(text => new Paragraph({
    numbering: { reference: "bullets", level: 0 },
    spacing: { after: 60 },
    children: [new TextRun({ text, size: 20 })],
  }));
}

function sectionDivider() {
  return new Paragraph({
    border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: "1F4E79", space: 1 } },
    spacing: { after: 200 },
  });
}

function buildRunSection(run) {
  const children = [];

  children.push(new Paragraph({
    heading: HeadingLevel.HEADING_2,
    children: [new TextRun(`${run.id}. ${run.title}`)],
  }));

  const paramRows = [
    ["Modèle", run.model === "mlp" ? `MLP ${run.architecture}` : run.model === "mlp_multiclass" ? `MLP multiclasse ${run.architecture}` : run.model === "rbf" ? `RBF (${run.architecture})` : run.architecture],
    ["Seed", run.seed],
    ["Alpha (learning rate)", run.alpha],
    ["Epochs", run.epochs],
    ["Normalisation", run.normalization],
    ["Train / Test", `${run.train} / ${run.test}`],
    ["Accuracy globale (test)", `${run.accuracy}%`],
  ];
  children.push(labelValueTable(paramRows));
  children.push(new Paragraph({ spacing: { before: 160, after: 160 } }));

  const imgPath = path.join(HERE, "images", `run_${String(run.id).padStart(2, "0")}.png`);
  if (fs.existsSync(imgPath)) {
    children.push(imageParagraph(imgPath, `Matrice de confusion - ${run.title}`));
  } else {
    children.push(new Paragraph({
      children: [new TextRun({ text: `[Image manquante : images/run_${String(run.id).padStart(2, "0")}.png]`, italics: true, color: "CC0000", size: 18 })],
    }));
  }
  children.push(new Paragraph({ spacing: { after: 160 } }));

  children.push(new Paragraph({
    heading: HeadingLevel.HEADING_3,
    children: [new TextRun("Recall par classe (test)")],
  }));
  children.push(recallTable(run.analysis.recall));
  children.push(new Paragraph({ spacing: { after: 120 } }));

  const hasDetailedMetrics = run.analysis.tnr && Object.keys(run.analysis.tnr).length > 0;
  if (hasDetailedMetrics) {
    const cats = Object.keys(run.analysis.recall);
    children.push(new Paragraph({
      heading: HeadingLevel.HEADING_3,
      children: [new TextRun("Métriques détaillées par classe (test)")],
    }));
    children.push(confusionMetricsTable(cats, [
      { label: "TPR (recall)", values: run.analysis.recall },
      { label: "TNR (spécificité)", values: run.analysis.tnr },
      { label: "FPR (fausses alertes)", values: run.analysis.fpr },
      { label: "FNR (ratés)", values: run.analysis.fnr },
      { label: "Balanced Accuracy", values: run.analysis.balanced_accuracy },
    ]));
    children.push(new Paragraph({ spacing: { after: 120 } }));
  }

  if (run.analysis.train_accuracy) {
    children.push(new Paragraph({
      heading: HeadingLevel.HEADING_3,
      children: [new TextRun("Diagnostics d'entraînement (résumé)")],
    }));
    const diagRows = Object.keys(run.analysis.train_accuracy).map(cls => {
      const loss = run.analysis.train_loss ? run.analysis.train_loss[cls] : undefined;
      return [
        `Accuracy train — ${cls}`,
        loss !== undefined ? `${run.analysis.train_accuracy[cls]}%  (loss: ${loss})` : `${run.analysis.train_accuracy[cls]}%`,
      ];
    });
    children.push(labelValueTable(diagRows));
    children.push(new Paragraph({ spacing: { after: 120 } }));
  }

  const tbImages = findTensorboardImages(run.id);
  if (tbImages.length > 0) {
    children.push(new Paragraph({
      heading: HeadingLevel.HEADING_3,
      children: [new TextRun("Courbes TensorBoard")],
    }));
    tbImages.forEach(imgFile => {
      children.push(imageParagraph(imgFile, `TensorBoard - ${run.title}`));
    });
    children.push(new Paragraph({ spacing: { after: 120 } }));
  }

  children.push(new Paragraph({
    heading: HeadingLevel.HEADING_3,
    children: [new TextRun("Observations")],
  }));
  children.push(...bulletList(run.analysis.observations));
  children.push(new Paragraph({ spacing: { after: 100 } }));

  children.push(new Paragraph({
    spacing: { before: 100, after: 300 },
    children: [
      new TextRun({ text: "Conclusion : ", bold: true, italics: true, size: 20 }),
      new TextRun({ text: run.analysis.conclusion, italics: true, size: 20 }),
    ],
  }));

  children.push(sectionDivider());

  return children;
}

function summaryTable(runs) {
  const cols = [700, 4360, 1400, 1450, 1450];
  const headerCells = ["#", "Run", "Modèle", "Epochs", "Accuracy"].map((t, i) => new TableCell({
    borders,
    width: { size: cols[i], type: WidthType.DXA },
    shading: { fill: HEADER_FILL, type: ShadingType.CLEAR },
    margins: { top: 60, bottom: 60, left: 100, right: 100 },
    children: [new Paragraph({ children: [new TextRun({ text: t, bold: true, size: 18, color: "FFFFFF" })] })],
  }));

  const rows = [new TableRow({ children: headerCells })];
  runs.forEach((run, i) => {
    const cellsData = [
      String(run.id),
      run.title,
      run.model === "mlp" ? `MLP ${run.architecture}` : run.model === "mlp_multiclass" ? "MLP multiclasse" : run.model === "rbf" ? "RBF" : "Linear",
      String(run.epochs),
      `${run.accuracy}%`,
    ];
    rows.push(new TableRow({
      children: cellsData.map((v, j) => new TableCell({
        borders,
        width: { size: cols[j], type: WidthType.DXA },
        shading: { fill: i % 2 === 0 ? "F2F7FB" : "FFFFFF", type: ShadingType.CLEAR },
        margins: { top: 50, bottom: 50, left: 100, right: 100 },
        children: [new Paragraph({ children: [new TextRun({ text: v, size: 18 })] })],
      })),
    }));
  });

  return new Table({ width: { size: CONTENT_WIDTH, type: WidthType.DXA }, columnWidths: cols, rows });
}

const mlpRuns = data.runs.filter(r => r.model === "mlp");
const linearRuns = data.runs.filter(r => r.model === "linear");
const rbfRuns = data.runs.filter(r => r.model === "rbf");
const mlpMulticlassRuns = data.runs.filter(r => r.model === "mlp_multiclass");

const now = new Date();
const dateStr = now.toLocaleDateString("fr-FR", { year: "numeric", month: "long", day: "numeric" });

const doc = new Document({
  styles: {
    default: { document: { run: { font: "Arial", size: 20 } } },
    paragraphStyles: [
      { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 32, bold: true, font: "Arial", color: "1F4E79" },
        paragraph: { spacing: { before: 320, after: 220 }, outlineLevel: 0 } },
      { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 26, bold: true, font: "Arial", color: "1F4E79" },
        paragraph: { spacing: { before: 260, after: 160 }, outlineLevel: 1 } },
      { id: "Heading3", name: "Heading 3", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 21, bold: true, font: "Arial", color: "2E75B6" },
        paragraph: { spacing: { before: 160, after: 100 }, outlineLevel: 2 } },
    ],
  },
  numbering: {
    config: [
      { reference: "bullets",
        levels: [{ level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 560, hanging: 280 } } } }] },
    ],
  },
  sections: [{
    properties: {
      page: {
        size: { width: 12240, height: 15840 },
        margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 },
      },
    },
    headers: {
      default: new Header({
        children: [new Paragraph({
          children: [new TextRun({ text: "ArtGenre-Classifier — Rapport de tests", size: 16, color: "888888" })],
        })],
      }),
    },
    footers: {
      default: new Footer({
        children: [new Paragraph({
          alignment: AlignmentType.CENTER,
          children: [
            new TextRun({ text: "Page ", size: 16, color: "888888" }),
            new TextRun({ children: [PageNumber.CURRENT], size: 16, color: "888888" }),
            new TextRun({ text: " / ", size: 16, color: "888888" }),
            new TextRun({ children: [PageNumber.TOTAL_PAGES], size: 16, color: "888888" }),
          ],
        })],
      }),
    },
    children: [
      new Paragraph({
        spacing: { before: 400, after: 100 },
        children: [new TextRun({ text: "Rapport de tests — ArtGenre Classifier", bold: true, size: 44, color: "1F4E79" })],
      }),
      new Paragraph({
        spacing: { after: 400 },
        children: [new TextRun({ text: `Classification de styles artistiques (Impressionism / Realism / Romanticism) — mis à jour le ${dateStr}`, italics: true, size: 22, color: "555555" })],
      }),

      new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun("Comprendre les métriques par classe (TPR / TNR / FPR / FNR)")] }),
      new Paragraph({
        spacing: { after: 160 },
        children: [new TextRun({ text: "L'accuracy globale (un seul chiffre) peut cacher des problèmes qui n'apparaissent qu'en regardant chaque classe séparément. Ces 4 métriques, calculées par catégorie (raisonnement \"cette classe vs les 2 autres\"), permettent de voir précisément où et comment un modèle se trompe — pas juste combien.", size: 20 })],
      }),
      new Paragraph({
        heading: HeadingLevel.HEADING_3,
        children: [new TextRun("Définitions (pour une classe donnée, ex. Realism)")],
      }),
      ...bulletList([
        "TPR (True Positive Rate, = recall) : parmi les images qui SONT vraiment Realism, quelle proportion le modèle a correctement identifiée comme Realism. Un TPR bas veut dire que le modèle \"rate\" cette classe — il la confond avec les autres.",
        "TNR (True Negative Rate, = spécificité) : parmi les images qui NE SONT PAS Realism, quelle proportion le modèle a correctement écartée (n'a pas prédit Realism). Un TNR bas veut dire que le modèle prédit Realism \"trop souvent\", y compris sur des images d'autres styles.",
        "FPR (False Positive Rate = 1 − TNR) : le taux de \"fausses alertes\" — proportion d'images d'autres classes que le modèle étiquette à tort comme Realism. Un FPR élevé signifie que cette classe \"aspire\" des prédictions qui ne lui reviennent pas.",
        "FNR (False Negative Rate = 1 − TPR) : le taux de \"ratés\" — proportion d'images vraiment Realism que le modèle n'a pas su reconnaître. Un FNR élevé signifie que cette classe est systématiquement ignorée au profit des autres.",
        "Balanced Accuracy : moyenne de TPR et TNR pour cette classe. Contrairement à l'accuracy globale, elle n'est pas biaisée par le déséquilibre naturel (dans une décision one-vs-rest à 3 classes, il y a 2x plus d'exemples \"négatifs\" que \"positifs\" pour chaque catégorie)."
      ]),
      new Paragraph({
        heading: HeadingLevel.HEADING_3,
        children: [new TextRun("Comment les lire dans ce projet")],
      }),
      ...bulletList([
        "TPR bas + FNR haut sur une classe = elle est \"boudée\" par le modèle (cas classique de Realism sur beaucoup de runs Linear et RBF de ce rapport — TPR souvent sous 40%).",
        "FPR très haut sur une classe (proche de 100%, TNR proche de 0%) = signe d'un EFFONDREMENT (\"collapse\") : le modèle prédit presque toujours cette classe, quelle que soit l'image réelle. On l'observe nettement sur plusieurs runs RBF de ce rapport (ex. runs 77, 82, 107) où une classe capte artificiellement l'essentiel des prédictions pendant que les 2 autres s'effondrent en TPR.",
        "Un bon run \"sain\" a des Balanced Accuracy proches les unes des autres entre les 3 classes (écart faible) — c'est le signal le plus fiable d'un modèle réellement équilibré, plus fiable que l'accuracy globale seule qui peut masquer un déséquilibre compensé entre classes.",
        "TNR est structurellement plus facile à obtenir haut que TPR dans ce contexte one-vs-rest (2 négatifs pour 1 positif) : un TNR élevé n'est pas forcément un signe de bonne performance, c'est en partie mécanique. C'est pour ça que FPR (qui capture la même information mais normalisée différemment) et surtout la Balanced Accuracy sont plus informatifs que le TNR brut pour comparer des runs entre eux."
      ]),
      new Paragraph({ children: [new PageBreak()] }),

      new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun("Synthèse des runs")] }),
      summaryTable(data.runs),
      new Paragraph({ children: [new PageBreak()] }),

      new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun("Résultats — MLP")] }),
      ...mlpRuns.flatMap(buildRunSection),

      new Paragraph({ children: [new PageBreak()] }),
      new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun("Résultats — Linear (Perceptron)")] }),
      ...linearRuns.flatMap(buildRunSection),

      ...(rbfRuns.length > 0 ? [
        new Paragraph({ children: [new PageBreak()] }),
        new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun("Résultats — RBF")] }),
        ...rbfRuns.flatMap(buildRunSection),
      ] : []),

      ...(mlpMulticlassRuns.length > 0 ? [
        new Paragraph({ children: [new PageBreak()] }),
        new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun("Résultats — MLP multiclasse")] }),
        ...mlpMulticlassRuns.flatMap(buildRunSection),
      ] : []),
    ],
  }],
});

Packer.toBuffer(doc).then(buffer => {
  const outPath = path.join(HERE, "Rapport_Tests_ArtGenre-Classifier.docx");
  fs.writeFileSync(outPath, buffer);
  console.log(`Document genere : ${outPath}`);
});
