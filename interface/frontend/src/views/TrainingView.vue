<template>
  <div class="training-view card">
    <div class="wip-container">
      <div class="icon-gear">⚙️</div>
      <h2>Module d'Entraînement</h2>
      <p>
        Cet espace permettra de relancer l'entraînement des modèles C (Linear/MLP)
        directement depuis l'interface web, de visualiser la courbe de perte (loss), 
        et de gérer les datasets.
      </p>
      <div class="progress-bar">
        <div class="progress-fill"></div>
      </div>
      <p class="status">En cours de développement...</p>
    </div>
  </div>
</template>

<style scoped>
.card {
    background: white;
    padding: 3rem;
    border-radius: 16px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.03);
    text-align: center;
}

.wip-container {
    max-width: 500px;
    margin: 0 auto;
}

.icon-gear {
    font-size: 4rem;
    margin-bottom: 1rem;
    animation: spin 10s linear infinite;
    display: inline-block;
}

h2 {
    color: #2c3e50;
    margin-top: 0;
}

p {
    color: #7f8c8d;
    line-height: 1.6;
}

.progress-bar {
    height: 8px;
    background: #ecf0f1;
    border-radius: 4px;
    overflow: hidden;
    margin: 2rem 0 1rem;
}

.progress-fill {
    width: 35%;
    height: 100%;
    background:
    linear-gradient(90deg, #f39c12, #f1c40f);
    border-radius: 4px;
}

.status {
    font-size: 0.9rem;
    font-weight: bold;
    color: #f39c12;
}

@keyframes spin {
    100% { transform: rotate(360deg); }
}
</style>
