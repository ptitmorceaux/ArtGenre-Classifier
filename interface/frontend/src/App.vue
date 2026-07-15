<script setup>
import { ref } from 'vue'
import PredictionView from './views/PredictionView.vue'
import TrainingView from './views/TrainingView.vue'

const currentTab = ref('prediction')
</script>

<template>
  <div class="app-layout">
    <header class="top-nav">
      <div class="logo">
        <span class="icon">🎨</span> ArtClassifier
      </div>
      <nav class="tabs">
        <button 
          class="tab-btn" 
          :class="{ active: currentTab === 'prediction' }" 
          @click="currentTab = 'prediction'"
        >
          Prédiction
        </button>
        <button 
          class="tab-btn" 
          :class="{ active: currentTab === 'training' }" 
          @click="currentTab = 'training'"
        >
            Entraînement <span class="badge-wip">WIP</span>
        </button>
      </nav>
    </header>

    <main class="main-content">
      <Transition name="fade" mode="out-in">
        <PredictionView v-if="currentTab === 'prediction'" />
        <TrainingView v-else-if="currentTab === 'training'" />
      </Transition>
    </main>
  </div>
</template>

<style>
body {
  margin: 0;
  font-family: 'Inter', system-ui, Avenir, Helvetica, Arial, sans-serif;
  background-color: #f4f7f6;
  color: #2c3e50;
}

.app-layout {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.top-nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 2rem;
  background: white;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
}

.logo {
  font-size: 1.5rem;
  font-weight: 800;
  letter-spacing: -0.5px;
}

.tabs {
  display: flex;
  gap: 1rem;
}

.tab-btn {
  background: none;
  border: none;
  padding: 0.5rem 1rem;
  font-size: 1rem;
  font-weight: 600;
  color: #7f8c8d;
  cursor: pointer;
  border-radius: 8px;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.tab-btn:hover {
  background-color: #f0f3f5;
  color: #34495e;
}

.tab-btn.active {
  background-color: #ebf5ff;
  color: #3498db;
}

.badge-wip {
  background-color: #f39c12;
  color: white;
  font-size: 0.7rem;
  padding: 2px 6px;
  border-radius: 12px;
  font-weight: bold;
}

.main-content {
  flex: 1;
  padding: 2rem;
  max-width: 1200px;
  margin: 0 auto;
  width: 100%;
  box-sizing: border-box;
}

/* Animations de transition entre onglets */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.2s ease, transform 0.2s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
  transform: translateY(10px);
}
</style>