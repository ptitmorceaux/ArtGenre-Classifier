<script setup>
import { ref } from 'vue'
import PredictionResult from '../components/PredictionResult.vue'

const selectedModel = ref('mlp')
const selectedFile = ref(null)
const imagePreview = ref(null)
const isLoading = ref(false)
const result = ref(null)
const error = ref(null)

const handleFileChange = (event) => {
  const file = event.target.files[0]
  if (file) {
    selectedFile.value = file
    imagePreview.value = URL.createObjectURL(file)
    result.value = null
    error.value = null
  }
}

const submitPrediction = async () => {
  if (!selectedFile.value) return
  isLoading.value = true
  result.value = null
  error.value = null

  const formData = new FormData()
  formData.append('image', selectedFile.value)
  formData.append('model', selectedModel.value)

  try {
    const res = await fetch('http://127.0.0.1:8000/api/predict/', {
      method: 'POST',
      body: formData,
    })
    const responseData = await res.json()
    if (res.ok && responseData.status === 'success') {
      result.value = responseData.data
    } else {
      error.value = responseData.message || "Une erreur est survenue."
    }
  } catch (err) {
    error.value = "Impossible de joindre le backend. Le serveur Django est-il lancé ?"
  } finally {
    isLoading.value = false
  }
}
</script>

<template>
  <div class="prediction-view">
    <div class="card setup-card">
      <h2>Analyser une œuvre</h2>
      
      <div class="form-group">
        <label for="model-select">Modèle d'inférence :</label>
        <select id="model-select" v-model="selectedModel">
          <option value="mlp">Perceptron Multi-Couches (C)</option>
          <option value="linear">Modèle Linéaire (C)</option>
        </select>
      </div>

      <div class="form-group upload-zone" :class="{ 'has-image': imagePreview }">
        <label for="image-input" class="file-label">
          <div v-if="!imagePreview" class="empty-state">
            <span class="upload-icon">📁</span>
            <p>Glissez ou cliquez pour uploader une image</p>
          </div>
          <img v-else :src="imagePreview" class="preview-img" alt="Aperçu" />
        </label>
        <input type="file" id="image-input" accept="image/*" @change="handleFileChange" style="display: none;" />
      </div>

      <button @click="submitPrediction" :disabled="!selectedFile || isLoading" class="btn-primary">
        <span v-if="isLoading" class="spinner">⚙️</span>
        {{ isLoading ? 'Analyse en cours...' : 'Lancer la classification' }}
      </button>

      <div v-if="error" class="alert-error">
        <strong>Erreur :</strong> {{ error }}
      </div>
    </div>

    <div class="results-container">
      <PredictionResult v-if="result" :data="result" />
    </div>
  </div>
</template>

<style scoped>
.prediction-view {
  display: grid;
  grid-template-columns: 1fr;
  gap: 2rem;
  align-items: start;
}

@media (min-width: 900px) {
  .prediction-view {
    grid-template-columns: 400px 1fr; /* Le formulaire à gauche, les résultats à droite */
  }
}

.card {
  background: white;
  padding: 2rem;
  border-radius: 16px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.03);
}

h2 {
  margin-top: 0;
  margin-bottom: 1.5rem;
  color: #2c3e50;
}

.form-group {
  margin-bottom: 1.5rem;
}

.form-group label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: 600;
  font-size: 0.9rem;
  color: #b30000;
}

select {
  width: 100%;
  padding: 12px;
  border: 1px solid #dfe6e9;
  border-radius: 8px;
  font-size: 1rem;
  background-color: #f8fafc;
  color: #2c3e50;
  outline: none;
  transition: border-color 0.2s;
}

select option {
  color: #2c3e50;
  background-color: white;
}

.upload-zone {
  border: 2px dashed #b2bec3;
  border-radius: 12px;
  text-align: center;
  transition: all 0.3s;
  background: #fdfdfd;
  overflow: hidden;
}

.upload-zone:hover {
  border-color: #3498db;
  background: #f0f8ff;
}

.file-label {
  display: block;
  padding: 3rem 1rem;
  cursor: pointer;
  margin: 0;
}

.empty-state p { margin: 0; color: #636e72; font-size: 0.9rem; }
.upload-icon { font-size: 2.5rem; display: block; margin-bottom: 10px; }

.preview-img {
  width: 100%;
  height: auto;
  max-height: 300px;
  object-fit: contain;
  display: block;
}

.btn-primary {
  width: 100%;
  padding: 14px;
  font-size: 1rem;
  font-weight: bold;
  color: white;
  background: linear-gradient(135deg, #3498db, #2980b9);
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: transform 0.1s, box-shadow 0.2s;
}

.btn-primary:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 4px 15px rgba(52, 152, 219, 0.4);
}

.btn-primary:disabled {
  background: #bdc3c7;
  cursor: not-allowed;
  transform: none;
  box-shadow: none;
}

.alert-error {
  margin-top: 1rem;
  padding: 1rem;
  background-color: #fee2e2;
  color: #991b1b;
  border-radius: 8px;
  border-left: 4px solid #ef4444;
  font-size: 0.9rem;
}
</style>