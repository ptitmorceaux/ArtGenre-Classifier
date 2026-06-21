<template>
  <div id="app">
    <header>
      <h1>🎨 ArtGenre Classifier</h1>
      <p>Projet Annuel - Machine Learning en C</p>
    </header>
    
    <main>
      <TestConnection />
    </main>
  </div>
</template>

<script setup>
import TestConnection from './components/TestConnection.vue'
</script>

<style>
body {
  margin: 0;
  padding: 0;
  background-color: #f4f7f6;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  color: #2c3e50;
}

#app {
  text-align: center;
  padding-top: 50px;
}

header h1 {
  margin-bottom: 5px;
  color: #2c3e50;
}

header p {
  color: #7f8c8d;
  margin-bottom: 40px;
}
</style>