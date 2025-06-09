import { defineStore } from 'pinia';
import apiService from '@/services/apiService';
import router from '@/router';

// We get the token from localStorage to persist login across page reloads
const storedToken = localStorage.getItem('token');

export const useAuthStore = defineStore('auth', {
  // The initial state
  state: () => ({
    token: storedToken || null,
    user: null,
    error: null,
    loading: false,
  }),

  // Computed properties derived from the state
  getters: {
    isLoggedIn: (state) => !!state.token,
  },

  // Methods that can be called to change the state
  actions: {
    async register(credentials) {
      this.loading = true;
      this.error = null;
      try {
        await apiService.post('/users/', credentials);
        // After successful registration, automatically log them in
        await this.login(credentials);
      } catch (error) {
        this.error = error.response?.data?.detail || 'Registration failed.';
        this.loading = false;
        // Re-throw the error so the component knows the registration failed
        throw error;
      }
    },

    async login(credentials) {
      this.loading = true;
      this.error = null;
      try {
        const params = new URLSearchParams();
        params.append('username', credentials.username);
        params.append('password', credentials.password);

        const response = await apiService.post('/login/access-token', params);
        
        this.token = response.data.access_token;
        
        // Store the token in localStorage to keep the user logged in
        localStorage.setItem('token', this.token);

        // Set the auth header for all future requests
        apiService.defaults.headers.common['Authorization'] = `Bearer ${this.token}`;
        
        router.push({ name: 'transaction-list' });
      } catch (error) {
        this.error = error.response?.data?.detail || 'Login failed.';
        // Re-throw the error so the component knows the login failed
        throw error;
      } finally {
        this.loading = false;
      }
    },

    logout() {
      // Clear all authentication state
      this.token = null;
      this.user = null;
      localStorage.removeItem('token');
      delete apiService.defaults.headers.common['Authorization'];
      router.push('/');
    },
  },
});
