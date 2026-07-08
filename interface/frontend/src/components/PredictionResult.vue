<script setup>
defineProps({
  data: {
    type: Object,
    required: true
  }
})
</script>

<template>
  <div class="result-card">
    <div class="header-result">
      <h3>Résultat de l'analyse</h3>
      <span class="model-badge">{{ data.model_used }}</span>
    </div>

    <div class="winner-banner">
      <div class="winner-label">Catégorie dominante</div>
      <div class="winner-name">{{ data.best_category }}</div>
    </div>

    <div v-if="data.chart_base64" class="chart-section">
      <h4>Cheminement des scores (Logique interne)</h4>
      <div class="image-wrapper">
        <img :src="'data:image/png;base64,' + data.chart_base64" alt="Graphique Matplotlib" />
      </div>
      <p class="help-text">
        Produit scalaire / Sortie brute des neurones avant l'activation finale. 
        Les valeurs les plus hautes indiquent la meilleure correspondance.
      </p>
    </div>

    <div class="raw-scores">
      <h4>Détail des calculs</h4>
      <ul>
        <li v-for="(score, category) in data.raw_prediction" :key="category">
          <span class="cat-name">{{ category }}</span>
          <span class="cat-score" :class="{ positive: score > 0, negative: score <= 0 }">
            {{ score.toFixed(4) }}
          </span>
        </li>
      </ul>
    </div>
  </div>
</template>

<style scoped>
.result-card {
  background: white;
  padding: 2rem;
  border-radius: 16px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.03);
  animation: slideIn 0.4s ease-out;
}

@keyframes slideIn {
  from { opacity: 0; transform: translateX(20px); }
  to { opacity: 1; transform: translateX(0); }
}

.header-result {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1.5rem;
  border-bottom: 1px solid #f1f2f6;
  padding-bottom: 1rem;
}

h3 { margin: 0; color: #2c3e50; }
.model-badge { background: #f1f2f6; color: #576574; padding: 4px 10px; border-radius: 6px; font-size: 0.8rem; font-weight: bold; }

.winner-banner {
  background: linear-gradient(135deg, #10ac84, #1dd1a1);
  color: white;
  padding: 1.5rem;
  border-radius: 12px;
  text-align: center;
  margin-bottom: 2rem;
  box-shadow: 0 4px 15px rgba(29, 209, 161, 0.3);
}

.winner-label { font-size: 0.9rem; opacity: 0.9; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 0.5rem; }
.winner-name { font-size: 2.5rem; font-weight: 800; text-transform: capitalize; letter-spacing: -1px; }

.chart-section {
  margin-bottom: 2rem;
}

.chart-section h4 { color: #34495e; margin-bottom: 1rem; }

.image-wrapper {
  background: #fdfdfd;
  border: 1px solid #dfe6e9;
  border-radius: 12px;
  padding: 10px;
  text-align: center;
}

.image-wrapper img {
  max-width: 100%;
  height: auto;
  border-radius: 8px;
}

.help-text { font-size: 0.85rem; color: #7f8c8d; text-align: center; margin-top: 0.5rem; font-style: italic; }

.raw-scores h4 { color: #34495e; margin-bottom: 1rem; border-bottom: 1px solid #f1f2f6; padding-bottom: 0.5rem; }
.raw-scores ul { list-style: none; padding: 0; margin: 0; }
.raw-scores li {
  display: flex;
  justify-content: space-between;
  padding: 10px 0;
  border-bottom: 1px dashed #ecf0f1;
}

.cat-name { text-transform: capitalize; font-weight: 600; color: #2c3e50; }
.cat-score { font-family: 'Courier New', Courier, monospace; font-weight: bold; }
.cat-score.positive { color: #10ac84; }
.cat-score.negative { color: #ee5253; }
</style>