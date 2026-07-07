<template>
  <div class="test-container">
    <h2>Test de la tuyauterie Django</h2>
    
    <button @click="testConnection" :disabled="isLoading">
      {{ isLoading ? 'Test en cours...' : 'Ping Django' }}
    </button>

    <div v-if="response" :class="['result-box', 'success']">
      <strong>Statut :</strong> {{ response.status }} <br/>
      <strong>Message :</strong> {{ response.message }}
    </div>

    <div v-if="error" class="result-box error">
      <strong>Erreur :</strong> Impossible de joindre le serveur. As-tu bien lancé Django (runserver) ?
      <br/><small>{{ error }}</small>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const isLoading = ref(false)
const response = ref(null)
const error = ref(null)

const testConnection = async () => {
  isLoading.value = true
  response.value = null
  error.value = null

  try {
    // On appelle la route bidon qu'on a créée dans Django
    const res = await fetch('http://127.0.0.1:8000/api/ping/')
    
    if (!res.ok) {
      throw new Error(`Erreur HTTP: ${res.status}`)
    }
    
    response.value = await res.json()
  } catch (err) {
    error.value = err.message
  } finally {
    isLoading.value = false
  }
}
</script>

<style scoped>
.test-container {
  padding: 2rem;
  border: 1px solid #ccc;
  border-radius: 8px;
  max-width: 500px;
  margin: 2rem auto;
  text-align: center;
  background-color: white;
}
button {
  padding: 12px 24px;
  font-size: 16px;
  font-weight: bold;
  cursor: pointer;
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 6px;
  transition: background-color 0.3s;
}
button:hover {
  background-color: #45a049;
}
.result-box {
  margin-top: 20px;
  padding: 15px;
  border-radius: 4px;
  text-align: left;
}
.success { background-color: #e8f5e9; border: 1px solid #4caf50; color: #2e7d32; }
.error { background-color: #ffebee; border: 1px solid #f44336; color: #c62828; }
</style>