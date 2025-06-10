<template>
  <div class="min-h-screen bg-gray-100 p-4 sm:p-6 lg:p-8" >
    <header class="flex justify-between items-center mb-8">
      <img src="/bank_logo.png" alt="bank_Logo" class="h-10 w-auto" />
      <button @click="authStore.logout()" class="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline">
        Logout
      </button>
    </header>

    <main class="grid grid-cols-1 lg:grid-cols-3 gap-8">
      <!-- Left Column: Transaction Form (Stays static) -->
      <div class="lg:col-span-1">
        <TransactionForm />
      </div>

      <!-- Right Column: Dynamic Content via Nested Router -->
      <div class="lg:col-span-2">
        <!-- This router-view will render either the list or the detail component -->
        <router-view />
      </div>
    </main>
  </div>
</template>

<script>
import { useAuthStore } from '@/stores/auth';
import TransactionForm from '@/components/TransactionForm.vue';

export default {
  name: 'DashboardView',
  components: {
    TransactionForm,
  },
  setup() {
    const authStore = useAuthStore();
    return { authStore };
  }
}
</script>
