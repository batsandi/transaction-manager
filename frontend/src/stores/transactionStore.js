import { defineStore } from 'pinia';
import apiService from '@/services/apiService';

export const useTransactionStore = defineStore('transactions', {
  state: () => ({
    transactions: [],
    transactionDetail: null,
    loading: false,
    error: null,
  }),

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

    // New action to fetch a single transaction
    async fetchTransactionDetail(id) {
      this.loading = true;
      this.error = null;
      try {
        const response = await apiService.get(`/transactions/${id}`);
        this.transactionDetail = response.data;
      } catch (err) {
        this.error = 'Failed to fetch transaction details.';
        console.error(err);
      } finally {
        this.loading = false;
      }
    },

    async createTransaction(transactionData) {
      try {
        await apiService.post('/transactions/', transactionData);
        // Re-fetch the list to ensure it's up-to-date
        await this.fetchTransactions();
      } catch (err) {
        console.error('Failed to create transaction:', err);
        throw err;
      }
    },

    async updateTransactionStatus(id, newStatus) {
      try {
        const response = await apiService.put(`/transactions/${id}`, { status: newStatus });
        const updatedTransaction = response.data;

        this.transactionDetail = updatedTransaction;

        const index = this.transactions.findIndex(t => t.id === id);
        if (index !== -1) {
          this.transactions[index] = updatedTransaction;
        }

      } catch (err) {
        console.error('Failed to update status:', err);
        throw err;
      }
    },
  },
});
