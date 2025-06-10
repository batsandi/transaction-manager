<template>
  <div class="bg-white p-6 rounded-lg shadow-md">
    <div class="flex justify-between items-center mb-4">
      <h2 class="text-xl font-bold text-gray-700">Recent Transactions</h2>
    </div>

    <div v-if="loading" class="text-center text-gray-500 py-4">
      Loading transactions...
    </div>

    <div v-else-if="error" class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded" role="alert">
      <p><strong>Error:</strong> {{ error }}</p>
    </div>

    <div v-else-if="transactions.length === 0" class="text-center text-gray-500 py-4">
      You have no transactions yet.
    </div>

    <div v-else class="overflow-x-auto">
      <table class="min-w-full divide-y divide-gray-200">
        <thead class="bg-gray-50">
          <tr>
            <th @click="sortBy('id')" scope="col" class="cursor-pointer px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">#</th>
            <th @click="sortBy('status')" scope="col" class="cursor-pointer px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Status</th>
            <th @click="sortBy('date')" scope="col" class="cursor-pointer px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Date</th>
            <th @click="sortBy('beneficiary')" scope="col" class="cursor-pointer px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Beneficiary</th>
            <th @click="sortBy('amount')" scope="col" class="cursor-pointer px-6 py-3 text-right text-xs font-medium text-gray-500 uppercase tracking-wider">Amount</th>
            <th @click="sortBy('amount')" scope="col" class="cursor-pointer px-6 py-3 text-right text-xs font-medium text-gray-500 uppercase tracking-wider">Type</th>

          </tr>
        </thead>
        <tbody class="bg-white divide-y divide-gray-200">
          <!-- We now loop over the 'transactions' computed property -->
          <tr 
            v-for="transaction in sortedTransactions"
            :key="transaction.id"
            @click="goToDetails(transaction.id)"
            class="cursor-pointer hover:bg-gray-50 transition-colors duration-150">
            <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
              {{ transaction.id }}
            </td>
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
            <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-700 text-right">
              {{ transaction.transaction_type }}
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import { useTransactionStore } from '@/stores/transactionStore';
import { mapState, mapActions } from 'pinia';

export default {
  name: 'TransactionList',
  data() {
    return {
      sortKey: 'id',
      sortOrder: -1,
    };
  },
  computed: {
    ...mapState(useTransactionStore, ['transactions', 'loading', 'error']),
      sortedTransactions() {
      const transactionsCopy = [...this.transactions];
      
      transactionsCopy.sort((a, b) => {
        const aValue = a[this.sortKey];
        const bValue = b[this.sortKey];

        if (aValue < bValue) {
          return -1 * this.sortOrder;
        }
        if (aValue > bValue) {
          return 1 * this.sortOrder;
        }
        return 0;
      });
      
      return transactionsCopy;
    }
  },
  methods: {
    ...mapActions(useTransactionStore, ['fetchTransactions']),

    formatDate(dateString) {
      const options = { year: 'numeric', month: 'long', day: 'numeric' };
      return new Date(dateString).toLocaleDateString(undefined, options);
    },
    formatCurrency(value) {
      return new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' }).format(value);
    },
    goToDetails(transactionId) {
      this.$router.push({ name: 'transaction-detail', params: { id: transactionId } });
    },
    sortBy(key) {
      if (this.sortKey === key) {
        this.sortOrder = this.sortOrder * -1;
      } else {
        this.sortKey = key;
        this.sortOrder = 1;
      }
    },

    statusClass(status) {
      const classes = {
        sent: 'bg-red-100 text-red-800',
        received: 'bg-yellow-100 text-yellow-800',
        paid: 'bg-green-100 text-green-800',
      };
      const lowerCaseStatus = status ? status.toLowerCase() : '';
      return classes[lowerCaseStatus] || 'bg-gray-100 text-gray-800';
    }
  },
  mounted() {
    this.fetchTransactions();
  }
}
</script>
