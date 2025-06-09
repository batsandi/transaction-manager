<template>
  <div class="flex items-center justify-center min-h-screen bg-gray-100">
    <div class="p-8 bg-white rounded-lg shadow-md text-center">
      <h1 class="text-2xl font-bold mb-4">Transaction Manager</h1>
      <p class="text-gray-600">Backend Status: <span class="font-semibold text-blue-600">{{ healthMessage }}</span></p>

    </div>
  </div>
</template>

<script>
import apiService from '@/services/apiService';

export default {
  name: 'LoginView',
  data() {
    return {
      healthMessage: 'Connecting to backend...'
    };
  },
  

  async mounted() {
    try {
      const response = await apiService.get('/');
      this.healthMessage = response.data.health;
    } catch (error) {
      this.healthMessage = 'Failed to connect to the backend.';
      console.error('API connection error:', error);
    }
  }
}
</script>

<style scoped>
</style>
