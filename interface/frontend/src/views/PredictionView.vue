<script setup>
import { ref, onMounted, computed, watch } from 'vue'
import PredictionResult from '../components/PredictionResult.vue'

const allModels = ref([])
const selectedType = ref('linear')
const selectedResolution = ref(32) // Par défaut on affiche les modèles 32x32
const selectedSessionId = ref('')
const currentMetrics = ref(null)

const selectedFile = ref(null)
const imagePreview = ref(null)
const isLoading = ref(false)
const result = ref(null)
const error = ref(null)

const API_URL = import.meta.env.VITE_API_URL || 'http://127.0.0.1:8000';

// 1. Filtrage combiné : Type + Résolution
const filteredModels = computed(() => {
  return allModels.value.filter(m => 
    m.type === selectedType.value && 
    m.resolution === selectedResolution.value
  )
})

const selectedModelDetails = computed(() => {
  return allModels.value.find(m => m.id === selectedSessionId.value)
})

onMounted(async () => {
  try {
    const res = await fetch(`${API_URL}/api/models/`)
    const data = await res.json()
    if (data.status === 'success') {
      allModels.value = data.models
      setDefaultSession()
    }
  } catch (err) {
    console.error("Impossible de charger les modèles :", err)
  }
})

// Relance le focus dès qu'on change de type ou de résolution
watch([selectedType, selectedResolution], () => {
  setDefaultSession()
})

const setDefaultSession = () => {
  currentMetrics.value = null
  result.value = null
  if (filteredModels.value.length > 0) {
    selectedSessionId.value = filteredModels.value[0].id
    fetchMetrics()
  } else {
    selectedSessionId.value = ''
  }
}

const fetchMetrics = async () => {
  if (!selectedSessionId.value) return
  currentMetrics.value = null
  result.value = null
  try {
    const res = await fetch(`${API_URL}/api/models/${selectedSessionId.value}/metrics/`)
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

  const formData = new FormData()
  formData.append('image', selectedFile.value)
  formData.append('session_id', selectedSessionId.value)

  try {
    const res = await fetch(`${API_URL}/api/predict/`, {
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
    
    <!-- COLONNE GAUCHE : CONTRÔLE -->
    <div class="column-left">
      <div class="card setup-card">
        <h2>Analyser une œuvre</h2>
        
        <!-- Sélection du type de modèle -->
        <div class="form-group">
          <label>1. Algorithme :</label>
          <select v-model="selectedType">
            <option value="linear">Modèle Linéaire (Linear)</option>
            <option value="mlp">Perceptron Multicouches (MLP)</option>
            <option value="mlp_multiclass">Perceptron Multicouches (MLP-MC)</option>
            <option value="rbf">Réseau RBF</option>
          </select>
        </div>

        <!-- Sélection de la Résolution -->
        <div class="form-group">
          <label>2. Résolution :</label>
          <select v-model="selectedResolution">
            <option :value="32">Basse définition (32x32 Gris)</option>
            <option :value="64">Haute définition (64x64 RGB)</option>
          </select>
        </div>

        <!-- Sélection de la session -->
        <div class="form-group">
          <label>3. Modèle entraîné (Classé par performance) :</label>
          <select v-model="selectedSessionId" @change="fetchMetrics">
            <option v-if="filteredModels.length === 0" disabled value="">Aucun modèle de ce type trouvé...</option>
            <option v-for="model in filteredModels" :key="model.id" :value="model.id">
              {{ model.label }}
            </option>
          </select>
        </div>

        <!-- Upload Image -->
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

        <!-- Bouton Prédiction -->
        <button @click="submitPrediction" :disabled="!selectedFile || !selectedSessionId || isLoading" class="btn-primary">
          <span v-if="isLoading" class="spinner">⚙️</span>
          {{ isLoading ? 'Analyse en cours...' : 'Lancer la classification' }}
        </button>

        <div v-if="error" class="alert-error">
          <strong>Erreur :</strong> {{ error }}
        </div>
      </div>
    </div>

    <!-- COLONNE DROITE : RÉSULTATS & MÉTRIQUES -->
    <div class="column-right">
      
      <!-- Fiche détaillée du modèle -->
      <div v-if="selectedModelDetails" class="card info-card">
        <h3>Détails du Modèle</h3>
        <div class="hyperparams-grid">
          <div class="param-box">
            <span class="param-title">Taux d'apprentissage (α)</span>
            <span class="param-val">{{ selectedModelDetails.hyperparameters.alpha }}</span>
          </div>
          <div class="param-box">
            <span class="param-title">Époques</span>
            <span class="param-val">{{ selectedModelDetails.hyperparameters.epochs }}</span>
          </div>
          <div class="param-box">
            <span class="param-title">Normalisation</span>
            <span class="param-val">{{ selectedModelDetails.hyperparameters.normalization }}</span>
          </div>
          <div class="param-box" v-if="selectedModelDetails.type === 'mlp'">
            <span class="param-title">Architecture (Couches)</span>
            <span class="param-val">{{ selectedModelDetails.hyperparameters.npl }}</span>
          </div>
        </div>
      </div>

      <!-- Résultat d'inférence (composant enfant) -->
      <PredictionResult v-if="result" :data="result" />

      <!-- Matrice de Confusion & Métriques -->
      <div v-if="currentMetrics && currentMetrics.confusion_matrix" class="card metrics-card">
        <h3 class="metrics-title">Matrice de Confusion (Validation)</h3>
        <img :src="'data:image/png;base64,' + currentMetrics.confusion_matrix" alt="Matrice de Confusion" class="metric-img" />
        
        <!-- Tableau des Métriques TPR/TNR -->
        <div v-if="currentMetrics.metrics && Object.keys(currentMetrics.metrics).length > 0" class="table-responsive">
          <table class="metrics-table">
            <thead>
              <tr>
                <th>Catégorie</th>
                <th title="Vrais Positifs">TPR</th>
                <th title="Vrais Négatifs">TNR</th>
                <th title="Faux Positifs">FPR</th>
                <th title="Faux Négatifs">FNR</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(stats, cat) in currentMetrics.metrics" :key="cat">
                <td class="cat-name">{{ cat }}</td>
                <td class="tpr">{{ (stats.TPR * 100).toFixed(1) }}%</td>
                <td class="tnr">{{ (stats.TNR * 100).toFixed(1) }}%</td>
                <td class="fpr">{{ (stats.FPR * 100).toFixed(1) }}%</td>
                <td class="fnr">{{ (stats.FNR * 100).toFixed(1) }}%</td>
              </tr>
            </tbody>
          </table>
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
  .prediction-view {
    grid-template-columns: 400px 1fr;
  }
}

.column-left, .column-right {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.card {
  background: white;
  padding: 2rem;
  border-radius: 16px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.03);
}

h2, h3 {
  margin-top: 0;
  color: #2c3e50;
}

h2 { margin-bottom: 1.5rem; }
h3 { margin-bottom: 1rem; border-bottom: 1px solid #f1f2f6; padding-bottom: 0.8rem; }

.form-group { margin-bottom: 1.5rem; }
.form-group label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: 600;
  font-size: 0.9rem;
  color: #576574;
}

select {
  width: 100%;
  padding: 12px;
  border: 1px solid #dfe6e9;
  border-radius: 8px;
  font-size: 0.9rem;
  background-color: #f8fafc;
  color: #2c3e50;
  outline: none;
  transition: border-color 0.2s;
}

select:focus { border-color: #3498db; }

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

.btn-primary:disabled { background: #bdc3c7; cursor: not-allowed; }

.alert-error {
  margin-top: 1rem;
  padding: 1rem;
  background-color: #fee2e2;
  color: #991b1b;
  border-radius: 8px;
  border-left: 4px solid #ef4444;
  font-size: 0.9rem;
}

/* Hyperparameters Grid */
.hyperparams-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
  gap: 1rem;
}

.param-box {
  background: #f8fafc;
  padding: 1rem;
  border-radius: 8px;
  text-align: center;
  border: 1px solid #f1f2f6;
}

.param-title {
  display: block;
  font-size: 0.75rem;
  text-transform: uppercase;
  color: #7f8c8d;
  margin-bottom: 0.5rem;
  letter-spacing: 0.5px;
}

.param-val {
  display: block;
  font-size: 1.1rem;
  font-weight: 700;
  color: #2c3e50;
}

.metrics-title { text-align: center; }
.metric-img { width: 100%; border-radius: 8px; border: 1px solid #eee; margin-bottom: 1.5rem; }

/* Table Styles */
.table-responsive { overflow-x: auto; }
.metrics-table { width: 100%; border-collapse: collapse; margin-top: 0.5rem; font-size: 0.85rem; }
.metrics-table th, .metrics-table td { padding: 10px; text-align: center; border-bottom: 1px solid #f1f2f6; }
.metrics-table th { background-color: #f8fafc; color: #576574; font-weight: 600; text-transform: uppercase; font-size: 0.75rem; letter-spacing: 0.5px; }
.metrics-table .cat-name { text-align: left; text-transform: capitalize; font-weight: 600; color: #2c3e50; }
.tpr, .tnr { color: #10ac84; font-weight: bold; }
.fpr, .fnr { color: #ee5253; font-weight: bold; }
</style>