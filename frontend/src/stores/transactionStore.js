import { defineStore } from 'pinia';
import apiService from '@/services/apiService';

export const useTransactionStore = defineStore('transactions', {
  // State

  state: () => ({
    transactions: [],
    loading: false,
    error: null,
  }),

  // Actions
  actions: {
    async fetchTransactions() {
      this.loading = true;
      this.error = null;
      try {
        const response = await apiService.get('/transactions/');
        this.transactions = response.data;
      } catch (err) {
        this.error = 'Failed to fetch transactions.';
        console.error(err);
      } finally {
        this.loading = false;
      }
    },

    // Creates a new transaction
    async createTransaction(transactionData) {
      try {
        const response = await apiService.post('/transactions/', transactionData);
        // On success, add the new transaction to the start of local array
        this.transactions.unshift(response.data);
      } catch (err) {
        console.error('Failed to create transaction:', err);

        throw err;
      }
    },
  },
});
