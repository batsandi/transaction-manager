<template>
  <div class="relative border border-gray-300 p-5 m-5 rounded-lg shadow-md">
    <h1 class="text-2xl font-bold mb-4">Details</h1>
    <p class="text-lg">Transaction ID: {{ TransactionId }}</p>

    <button
      class="absolute top-3 right-3
             bg-gray-200 hover:bg-red-500
             text-gray-700 hover:text-white
             font-bold
             rounded-full
             w-8 h-8
             flex items-center justify-center
             transition-colors duration-300 ease-in-out
             focus:outline-none focus:ring-2 focus:ring-red-500 focus:ring-opacity-50"
      @click="goToList()"
      @mouseover="hover = true"
      @mouseleave="hover = false"
    >Close
    </button>
    <p>Details</p>
  </div>
</template>

<script>
import TransactionForm from './TransactionForm.vue';

export default {
    name: 'TransactionDetail',
    data() {
        return {
        hover: false
        };
    },
    computed: {
    TransactionId() {
      return this.$route.params.id;
    }
  },
    methods: {
        goToList() {
            this.$router.push({ name: 'transaction-list'});
        },
    }
}

</script>

<style scoped>
/* Scoped styles for this component */
</style>
