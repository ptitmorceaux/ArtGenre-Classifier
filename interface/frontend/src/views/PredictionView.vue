<script setup>
import { ref, onMounted } from 'vue'
import PredictionResult from '../components/PredictionResult.vue'

const availableModels = ref([])
const selectedSessionId = ref('')
const currentMetrics = ref(null)

const selectedFile = ref(null)
const imagePreview = ref(null)
const isLoading = ref(false)
const result = ref(null)
const error = ref(null)

// 1. Au chargement de la page, on récupère la liste des modèles depuis Django
onMounted(async () => {
  try {
    const res = await fetch('http://127.0.0.1:8000/api/models/')
    const data = await res.json()
    if (data.status === 'success' && data.models.length > 0) {
      availableModels.value = data.models
      // On sélectionne le meilleur modèle par défaut
      selectedSessionId.value = data.models[0].id
      // On charge ses courbes
      fetchMetrics()
    }
  } catch (err) {
    console.error("Impossible de charger les modèles :", err)
  }
})

// 2. Fonction pour charger les courbes quand l'utilisateur change de modèle
const fetchMetrics = async () => {
  if (!selectedSessionId.value) return
  currentMetrics.value = null
  try {
    const res = await fetch(`http://127.0.0.1:8000/api/models/${selectedSessionId.value}/metrics/`)
    const data = await res.json()
    if (data.status === 'success') {
      currentMetrics.value = data
    }
  } catch (err) {
    console.error("Impossible de charger les métriques :", err)
  }
}

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
  if (!selectedFile.value || !selectedSessionId.value) return
  isLoading.value = true
  result.value = null
  error.value = null

  // On retrouve le type de modèle (linear ou mlp) à partir de la sélection pour l'envoyer au backend
  const selectedModelObj = availableModels.value.find(m => m.id === selectedSessionId.value)
  
  const formData = new FormData()
  formData.append('image', selectedFile.value)
  formData.append('model', selectedModelObj.type)
  formData.append('session_id', selectedSessionId.value)
  // ATTENTION : Il faudra aussi que tu modifies ton services.py (predict) pour qu'il prenne l'ID de session exact au lieu de chercher "le plus récent".
  
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
    error.value = "Impossible de joindre le backend."
  } finally {
    isLoading.value = false
  }
}
</script>

<template>
  <div class="prediction-view">
    <div class="config-column">
      <div class="card setup-card">
        <h2>Analyser une œuvre</h2>
        
        <div class="form-group">
          <label for="session-select">Modèle entraîné (Classé par performance) :</label>
          <select id="session-select" v-model="selectedSessionId" @change="fetchMetrics">
            <option disabled value="">Chargement des modèles...</option>
            <option v-for="model in availableModels" :key="model.id" :value="model.id">
              {{ model.label }}
            </option>
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

        <button @click="submitPrediction" :disabled="!selectedFile || !selectedSessionId || isLoading" class="btn-primary">
          <span v-if="isLoading" class="spinner">⚙️</span>
          {{ isLoading ? 'Analyse en cours...' : 'Lancer la classification' }}
        </button>

        <div v-if="error" class="alert-error">
          <strong>Erreur :</strong> {{ error }}
        </div>
      </div>
    </div>

    <div class="results-column">
      <div v-if="result" class="results-container">
        <PredictionResult :data="result" />
      </div>
      
      <div v-if="currentMetrics" class="card metrics-card">
        <h3>Métriques de ce modèle</h3>
        <div class="metrics-grid">
          <div v-if="currentMetrics.confusion_matrix" class="metric-item">
            <h4>Matrice de Confusion</h4>
            <img :src="'data:image/png;base64,' + currentMetrics.confusion_matrix" />
          </div>
          <div v-if="currentMetrics.accuracy_curve" class="metric-item">
            <h4>Courbe d'Accuracy</h4>
            <img :src="'data:image/png;base64,' + currentMetrics.accuracy_curve" />
          </div>
          <div v-if="currentMetrics.loss_curve" class="metric-item">
            <h4>Courbe de Loss</h4>
            <img :src="'data:image/png;base64,' + currentMetrics.loss_curve" />
          </div>
        </div>
      </div>
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
  .prediction-view { grid-template-columns: 400px 1fr; }
}

.card { background: white; padding: 2rem; border-radius: 16px; box-shadow: 0 10px 30px rgba(0,0,0,0.03); margin-bottom: 2rem; }
h2, h3 { margin-top: 0; color: #2c3e50; }

.form-group { margin-bottom: 1.5rem; }
.form-group label { display: block; margin-bottom: 0.5rem; font-weight: 600; font-size: 0.9rem; color: #34495e; }

select {
  width: 100%; padding: 12px; border: 1px solid #dfe6e9; border-radius: 8px; 
  font-size: 0.95rem; background-color: #f8fafc; color: #2c3e50; outline: none; transition: border-color 0.2s;
}
select option { color: #2c3e50; font-weight: 500; }
select:focus { border-color: #3498db; }

.upload-zone { border: 2px dashed #b2bec3; border-radius: 12px; text-align: center; transition: all 0.3s; background: #fdfdfd; overflow: hidden; }
.upload-zone:hover { border-color: #3498db; background: #f0f8ff; }
.file-label { display: block; padding: 3rem 1rem; cursor: pointer; margin: 0; }
.empty-state p { margin: 0; color: #636e72; font-size: 0.9rem; }
.upload-icon { font-size: 2.5rem; display: block; margin-bottom: 10px; }
.preview-img { width: 100%; height: auto; max-height: 300px; object-fit: contain; display: block; }

.btn-primary {
  width: 100%; padding: 14px; font-size: 1rem; font-weight: bold; color: white;
  background: linear-gradient(135deg, #3498db, #2980b9); border: none; border-radius: 8px;
  cursor: pointer; transition: transform 0.1s, box-shadow 0.2s;
}
.btn-primary:hover:not(:disabled) { transform: translateY(-2px); box-shadow: 0 4px 15px rgba(52, 152, 219, 0.4); }
.btn-primary:disabled { background: #bdc3c7; cursor: not-allowed; }

.alert-error { margin-top: 1rem; padding: 1rem; background-color: #fee2e2; color: #991b1b; border-radius: 8px; border-left: 4px solid #ef4444; font-size: 0.9rem; }

/* Styles pour les courbes d'entraînement */
.metrics-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 1.5rem;
}
.metric-item {
  background: #f8fafc;
  border: 1px solid #dfe6e9;
  border-radius: 12px;
  padding: 10px;
  text-align: center;
}
.metric-item h4 { margin: 0 0 10px 0; color: #7f8c8d; font-size: 0.9rem; }
.metric-item img { max-width: 100%; height: auto; border-radius: 8px; }
</style>