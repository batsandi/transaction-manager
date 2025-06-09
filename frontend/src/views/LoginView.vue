<template>
  <div class="flex items-center justify-center min-h-screen bg-gray-100">
    <div class="p-8 bg-white rounded-lg shadow-xl w-full max-w-md">
      <h1 class="text-3xl font-bold mb-6 text-center text-gray-800">Transaction Manager</h1>

      <!-- Login / Register Toggle -->
      <div class="flex justify-center mb-6 border-b">
        <button 
          @click="isLogin = true" 
          :class="['px-4 py-2 font-semibold', isLogin ? 'border-b-2 border-blue-500 text-blue-600' : 'text-gray-500']">
          Login
        </button>
        <button 
          @click="isLogin = false" 
          :class="['px-4 py-2 font-semibold', !isLogin ? 'border-b-2 border-blue-500 text-blue-600' : 'text-gray-500']">
          Register
        </button>
      </div>

      <!-- Form -->
      <form @submit.prevent="handleSubmit">
        <div class="mb-4">
          <label for="username" class="block text-gray-700 text-sm font-bold mb-2">Username</label>
          <input 
            v-model="username"
            type="text" 
            id="username" 
            class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" 
            required>
        </div>
        <div class="mb-6">
          <label for="password" class="block text-gray-700 text-sm font-bold mb-2">Password</label>
          <input 
            v-model="password"
            type="password" 
            id="password" 
            class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline" 
            required>
        </div>
        <div class="flex items-center justify-between">
          <button 
            type="submit" 
            class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline w-full">
            <!-- The button text now changes based on the mode -->
            {{ isLogin ? 'Sign In' : 'Create Account' }}
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import { useAuthStore } from '@/stores/auth';

export default {
  name: 'LoginView',
  
  setup() {
    const authStore = useAuthStore();
    return { authStore };
  },

  data() {
    return {
      isLogin: true, 
      username: '',
      password: '',
    };
  },
  
  methods: {
    async handleSubmit() {
      const credentials = {
        username: this.username,
        password: this.password,
      };

      try {
        if (this.isLogin) {
          await this.authStore.login(credentials);
        } else {
          await this.authStore.register(credentials);
        }
      } catch (error) {
        alert("Action failed. Please check the console for details.");
        console.error("Authentication action failed:", error);
      }
    }
  }
}
</script>

<style scoped>
</style>
