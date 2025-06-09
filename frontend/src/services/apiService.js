import axios from 'axios';

const apiService = axios.create({
  baseURL: 'http://localhost:8000/api/v1',
});

// Check localStorage for a token when the app loads
const token = localStorage.getItem('token');
if (token) {
  apiService.defaults.headers.common['Authorization'] = `Bearer ${token}`;
}

export default apiService;