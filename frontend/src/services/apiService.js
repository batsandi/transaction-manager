import axios from 'axios';
import { useAuthStore } from '@/stores/auth';


const apiService = axios.create({
  baseURL: 'http://localhost:8000/api/v1',
});

// Check localStorage for a token when the app loads
const token = localStorage.getItem('token');
if (token) {
  apiService.defaults.headers.common['Authorization'] = `Bearer ${token}`;
}

apiService.interceptors.response.use(
  (response) => {
    return response;
  },
  (error) => {
    if (error.response && error.response.status === 401) {
      const authStore = useAuthStore();
      console.log('Token expired or invalid. Logging out.');
      authStore.logout();
    }
    // Return the error so the original caller can still handle it if needed
    return Promise.reject(error);
  }
);

export default apiService;
