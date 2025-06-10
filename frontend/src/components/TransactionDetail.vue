<template>
  <div v-if="loading" class="text-center p-5">Loading...</div>
  <div v-else-if="error" class="text-center p-5 text-red-500">{{ error }}</div>
  <div v-else-if="transactionDetail" class="relative border border-gray-300 p-5 m-5 rounded-lg shadow-md">
    <h1 class="text-2xl font-bold mb-4">Details for Transaction #{{ transactionDetail.id }}</h1>
    
    <p class="text-lg">Beneficiary: {{ transactionDetail.beneficiary }}</p>
    <p class="text-lg">Amount: {{ transactionDetail.amount }}</p>

    <button
      class="absolute top-3 right-3 bg-gray-200 hover:bg-red-500 text-gray-700 hover:text-white font-bold rounded-full w-8 h-8 flex items-center justify-center transition-colors duration-300 ease-in-out focus:outline-none focus:ring-2 focus:ring-red-500 focus:ring-opacity-50"
      @click="goToList()"
    >
      X
    </button>

    <div class="mt-6 mb-4 flex items-center space-x-2">
      <label for="transaction-status" class="text-md font-medium text-gray-700">Status:</label>
      <select
        id="transaction-status"
        v-model="selectedStatus"
        @change="handleStatusChange"
        class="block w-auto px-3 py-1 text-base text-gray-800 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 sm:text-sm"
      >
        <option v-for="status in statuses" :key="status" :value="status">
          {{ status }}
        </option>
      </select>
    </div>
  </div>
</template>

<script>
import { useTransactionStore } from '@/stores/transactionStore';
import { mapState, mapActions } from 'pinia';

export default {
  name: 'TransactionDetail',
  props: {
    id: {
      type: [String, Number],
      required: true,
    }
  },
  data() {
    return {
      selectedStatus: '',
      statuses: ['sent', 'received', 'paid']
    };
  },
  computed: {
    // Map the state from the store to local computed properties
    ...mapState(useTransactionStore, ['transactionDetail', 'loading', 'error'])
  },
  watch: {
    // Watch the transactionDetail object from the store
    transactionDetail: {
      handler(newDetail) {
        // When it changes, update the local selectedStatus for the dropdown
        if (newDetail && newDetail.status) {
          this.selectedStatus = newDetail.status;
        }
      },
      immediate: true // Run this watcher immediately when the component loads
    }
  },
  methods: {
    // Map the actions from the store to local methods
    ...mapActions(useTransactionStore, ['fetchTransactionDetail', 'updateTransactionStatus']),
    
    goToList() {
      this.$router.push({ name: 'transaction-list' });
    },
    
    async handleStatusChange() {
      try {
        // Call the store action to update the status
        await this.updateTransactionStatus(this.id, this.selectedStatus);
        // The store now handles all state updates automatically.
      } catch (error) {
        console.error('Error updating status:', error);
        alert('Failed to update status.');
      }
    }
  },
  mounted() {
    // When the component mounts, call the store action to fetch its data
    this.fetchTransactionDetail(this.id);
  }
}
</script>
