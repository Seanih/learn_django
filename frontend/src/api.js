import axios from 'axios';
import { ACCESS_TOKEN } from './constants';

// create api object to use for interceptor
const api = axios.create({
	// base url defined in .env file
	baseURL: import.meta.env.VITE_API_URL,
});

// add access token to request header if found in local storage
api.interceptors.request.use(
	config => {
		const token = localStorage.getItem(ACCESS_TOKEN);
		if (token) {
			config.headers.Authorization = `Bearer ${token}`;
		}
		return config;
	},
	error => {
		return Promise.reject(error);
	}
);

export default api;
