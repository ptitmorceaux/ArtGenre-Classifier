<script setup>
import { ref } from 'vue'

const selectedModel = ref('mlp')
const selectedFile = ref(null)
const imagePreview = ref(null)
const isLoading = ref(false)
const result = ref(null)
const error = ref(null)

// Gestion du choix de l'image et création de l'aperçu visuel
const handleFileChange = (event) => {
  const file = event.target.files[0]
  if (file) {
    selectedFile.value = file
    imagePreview.value = URL.createObjectURL(file) // Crée un lien local temporaire pour la balise <img>
    result.value = null
    error.value = null
  }
}

// Envoi de l'image en POST multipart à Django
const submitPrediction = async () => {
  if (!selectedFile.value) return

  isLoading.value = true
  result.value = null
  error.value = null

  // Construction du corps de la requête au format multipart/form-data
  const formData = new FormData()
  formData.append('image', selectedFile.value)
  formData.append('model', selectedModel.value)

  try {
    const res = await fetch('http://127.0.0.1:8000/api/predict/', {
      method: 'POST',
      body: formData, // Le navigateur gère automatiquement le Content-Type approprié
    })

    const responseData = await res.json()

    if (res.ok && responseData.status === 'success') {
      result.value = responseData.data
    } else {
      error.value = responseData.message || responseData.error || "Une erreur est survenue."
    }
  } catch (err) {
    error.value = "Impossible de joindre l'API Django. Vérifie tes serveurs."
    console.error(err)
  } finally {
    isLoading.value = false
  }
}
</script>

<template>
  <div class="classifier-container">
    <h2>Analyse d'Image d'Art</h2>
    
    <div class="form-group">
      <label for="model-select">Modèle à utiliser :</label>
      <select id="model-select" v-model="selectedModel">
        <option value="mlp">Perceptron Multi-Couches (PMC)</option>
        <option value="linear">Modèle Linéaire</option>
      </select>
    </div>

    <div class="form-group upload-zone" :class="{ 'has-image': imagePreview }">
      <label for="image-input" class="file-label">
        <span v-if="!imagePreview">📁 Cliquez pour choisir une œuvre d'art</span>
        <img v-else :src="imagePreview" class="preview-img" alt="Aperçu" />
      </label>
      <input 
        type="file" 
        id="image-input" 
        accept="image/*" 
        @change="handleFileChange" 
        style="display: none;" 
      />
    </div>

    <button 
      @click="submitPrediction" 
      :disabled="!selectedFile || isLoading"
      class="btn-predict"
    >
      {{ isLoading ? 'Classification en cours...' : 'Lancer la classification' }}
    </button>

    <div v-if="result" class="result-box success">
      <h3>Résultat de l'analyse :</h3>
      <p><strong>Modèle utilisé :</strong> {{ result.model_used }}</p>
      
      <div class="winner-box">
        <p><strong>Catégorie prédite :</strong> <span class="winner-text">{{ result.best_category }}</span></p>
      </div>

      <div v-if="result.chart_base64" class="chart-container">
        <h4>Cheminement des scores (Logique interne) :</h4>
        <img :src="'data:image/png;base64,' + result.chart_base64" alt="Graphique d'analyse Matplotlib" />
        <p class="help-text">
          <em>Ce graphique montre la valeur de sortie de chaque sous-modèle avant l'application du seuil de classification. Plus la barre est haute, plus le modèle "reconnaît" cette catégorie.</em>
        </p>
      </div>

      <p><strong>Scores précis par catégorie :</strong></p>
      <ul class="score-list">
        <li v-for="(score, category) in result.raw_prediction" :key="category">
          <span class="cat-name">{{ category }}</span> : 
          <span class="cat-score">{{ typeof score === 'number' ? score.toFixed(4) : score }}</span>
        </li>
      </ul>
    </div>

    <div v-if="error" class="result-box error">
      <strong>Erreur :</strong> {{ error }}
    </div>
  </div>
</template>

<style scoped>

.classifier-container {
  max-width: 500px;
  margin: 0 auto;
  padding: 2rem;
  background: white;
  border-radius: 12px;
  box-shadow: 0 4px 15px rgba(0,0,0,0.05);
}

.form-group {
  margin-bottom: 1.5rem;
  text-align: left;
}

label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: bold;
}

select {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 6px;
  font-size: 16px;
}

.upload-zone {
  border: 2px dashed #bbb;
  border-radius: 8px;
  text-align: center;
  cursor: pointer;
  background: #fbfbfb;
  transition: all 0.3s;
}

.upload-zone:hover {
  border-color: #3498db;
  background: #f2f8fc;
}

.file-label {
  display: block;
  padding: 2rem;
  cursor: pointer;
}

.preview-img {
  max-width: 100%;
  max-height: 250px;
  border-radius: 6px;
}

.btn-predict {
  width: 100%;
  padding: 12px;
  font-size: 16px;
  font-weight: bold;
  color: white;
  background-color:
  #3498db; border:
  none; border-radius:
  6px; cursor: pointer;
  transition: background 0.2s;
}

.btn-predict:hover {
  background-color: #2980b9;
}

.btn-predict:disabled {
  background-color: #bdc3c7;
  cursor: not-allowed;
}

.result-box {
  margin-top: 1.5rem;
  padding: 1rem;
  border-radius: 6px;
  text-align: left;
}

.success {
  background-color: #e8f5e9;
  border: 1px solid #4caf50;
  color: #2e7d32;
}

.error {
  background-color: #ffebee;
  border: 1px solid #f44336;
  color: #c62828;
}

/* Styles spécifiques au panneau de vainqueur et la liste de scores */
.winner-box {
  margin: 1rem 0;
  padding: 1rem;
  background: rgba(255, 255, 255, 0.6);
  border-left: 4px solid #4caf50;
  border-radius: 4px;
}

.winner-text {
  font-size: 1.2rem;
  font-weight: bold;
  text-transform: capitalize;
  color: #2e7d32;
}

.score-list {
  list-style-type: none;
  padding-left: 0;
  margin-top: 0.5rem;
}

.score-list li {
  padding: 6px 0;
  border-bottom: 1px solid #c8e6c9;
  display: flex;
  justify-content: space-between;
}

.cat-name {
  text-transform: capitalize;
  font-weight: 500;
}

.cat-score {
  font-family: monospace;
}

.chart-container {
  margin: 1.5rem 0;
  text-align: center;
  background: white;
  padding: 10px;
  border-radius: 8px;
  border: 1px solid #ddd;
}

.chart-container img {
  max-width: 100%;
  border-radius: 4px;
}

.help-text {
  font-size: 0.85rem;
  color: #666;
  margin-top: 10px;
}
</style>