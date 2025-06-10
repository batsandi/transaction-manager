<template>
  <div class="bg-white p-6 rounded-lg shadow-md">
    <h2 class="text-xl font-bold mb-4 text-gray-700">Make a Transfer</h2>
    <form @submit.prevent="handleSubmit">
      <div class="mb-4">
        <label for="beneficiary" class="block text-gray-700 text-sm font-bold mb-2">Beneficiary</label>
        <input 
          v-model="beneficiary"
          type="text" 
          id="beneficiary" 
          class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" 
          required>
      </div>
      <div class="mb-4">
        <label for="amount" class="block text-gray-700 text-sm font-bold mb-2">Amount</label>
        <input 
          v-model.number="amount"
          type="number" 
          step="0.01"
          id="amount" 
          class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" 
          required>
      </div>
      <div class="mb-6">
        <label for="transaction_type" class="block text-gray-700 text-sm font-bold mb-2">Transaction Type</label>
        <input 
          v-model="transaction_type"
          type="text" 
          id="transaction_type" 
          class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline" 
          required>
      </div>
      <button 
        type="submit" 
        class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline w-full">
        Submit Transaction
      </button>
    </form>
  </div>
</template>

<script>
import { useTransactionStore } from '@/stores/transactionStore';

export default {
  name: 'TransactionForm',
  setup() {
    const transactionStore = useTransactionStore();
    return { transactionStore };
  },
  data() {
    return {
      beneficiary: '',
      amount: null,
      transaction_type: ''
    };
  },
  methods: {
    async handleSubmit() {
      const transactionData = {
        beneficiary: this.beneficiary,
        amount: this.amount,
        transaction_type: this.transaction_type,
        // The 'status' will default to 'sent' on the backend
      };

      try {
        await this.transactionStore.createTransaction(transactionData);
        
        this.beneficiary = '';
        this.amount = null;
        this.transaction_type = '';

      } catch (error) {
        alert('Failed to create the transaction.');
      }
    }
  }
}
</script>
