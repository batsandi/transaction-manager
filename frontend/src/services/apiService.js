import axios from 'axios';

const apiService = axios.create({
  baseURL: 'http://localhost:8000/api/v1',
});

export default apiService;