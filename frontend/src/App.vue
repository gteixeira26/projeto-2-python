<template>
  <div id="app">
    <h1>Buscar Operadora</h1>
    <input v-model="termo" placeholder="Digite o nome da operadora" />
    <button @click="buscar">Buscar</button>
    <ul>
      <li v-for="op in resultados" :key="op.REG_ANS">
        {{ op.Nome_Fantasia || 'Sem nome' }}
      </li>
    </ul>
    <p v-if="erro" style="color: red;">Erro: {{ erro }}</p>
  </div>
</template>

<script>
import axios from 'axios'

axios.defaults.baseURL = 'http://127.0.0.1:5000'

export default {
  data() {
    return {
      termo: '',
      resultados: [],
      erro: null
    }
  },
  methods: {
    async buscar() {
      this.erro = null
      try {
        const resp = await axios.get(`/buscar?q=${this.termo}`)
        this.resultados = resp.data
      } catch (error) {
        this.erro = "Não foi possível realizar a busca. Verifique o backend e tente novamente."
        console.error('Erro na requisição:', error)
      }
    }
  }
}
</script>

<style>
</style>