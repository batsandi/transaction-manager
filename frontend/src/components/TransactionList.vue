<template>
  <div class="bg-white p-6 rounded-lg shadow-md">
    <div class="flex justify-between items-center mb-4">
      <h2 class="text-xl font-bold text-gray-700">Recent Transactions</h2>

    </div>

    <!-- Loading State -->
    <div v-if="loading" class="text-center text-gray-500 py-4">
      Loading transactions...
    </div>

    <!-- Error State -->
    <div v-else-if="error" class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded" role="alert">
      <p><strong>Error:</strong> {{ error }}</p>
    </div>

    <!-- Empty State -->
    <div v-else-if="transactions.length === 0" class="text-center text-gray-500 py-4">
      You have no transactions yet.
    </div>

    <!-- Data Table -->
    <div v-else class="overflow-x-auto">
      <table class="min-w-full divide-y divide-gray-200">
        <thead class="bg-gray-50">
          <tr>
            <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Status</th>
            <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Date</th>
            <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Beneficiary</th>
            <th scope="col" class="px-6 py-3 text-right text-xs font-medium text-gray-500 uppercase tracking-wider">Amount</th>
          </tr>
        </thead>
        <tbody class="bg-white divide-y divide-gray-200">
          <tr v-for="transaction in transactions" :key="transaction.id">
            <td class="px-6 py-4 whitespace-nowrap">
              <span 
                :class="statusClass(transaction.status)"
                class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full">
                {{ transaction.status }}
              </span>
            </td>
            <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
              {{ formatDate(transaction.date) }}
            </td>
            <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">
              {{ transaction.beneficiary }}
            </td>
            <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-700 text-right">
              {{ formatCurrency(transaction.amount) }}
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import apiService from '@/services/apiService';

export default {
  name: 'TransactionList',
  data() {
    return {
      transactions: [],
      loading: false,
      error: null,
    };
  },
  methods: {
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
    formatDate(dateString) {
      const options = { year: 'numeric', month: 'long', day: 'numeric' };
      return new Date(dateString).toLocaleDateString(undefined, options);
    },
    formatCurrency(value) {
      return new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' }).format(value);
    },
    statusClass(status) {
      const classes = {
        sent: 'bg-red-100 text-red-800',
        received: 'bg-yellow-100 text-yellow-800',
        paid: 'bg-green-100 text-green-800',
      };
      return classes[status.toLowerCase()] || 'bg-gray-100 text-gray-800';
    }
  },
  mounted() {
    this.fetchTransactions();
  }
}
</script>
