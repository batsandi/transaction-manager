import { defineStore } from 'pinia';
import apiService from '@/services/apiService';

export const useTransactionStore = defineStore('transactions', {
  // --- STATE ---
  state: () => ({
    transactions: [],
    loading: false,
    error: null,
  }),

  // --- ACTIONS ---
  actions: {
    // Fetches all transactions from the backend
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
        await apiService.post('/transactions/', transactionData);
        await this.fetchTransactions();
      } catch (err) {
        console.error('Failed to create transaction:', err);
        // Re-throw the error so the component knows it failed
        throw err;
      }
    },
  },
});
