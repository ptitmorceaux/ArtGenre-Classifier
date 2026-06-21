<template>
  <div id="app">
    <header>
      <h1>ArtGenre Classifier</h1>
    </header>
    
    <main>
      <ArtClassifier />
    </main>
  </div>
</template>

<script setup>
import ArtClassifier from './components/ArtClassifier.vue'
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
  padding: 40px 20px;
}

header {
  text-align: center;
  margin-bottom: 30px;
}

header h1 {
  margin: 0 0 5px 0;
}

header p {
  color: #7f8c8d;
  margin: 0;
}
</style>