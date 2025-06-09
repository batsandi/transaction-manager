import { defineConfig } from 'vite'
import { fileURLToPath, URL } from 'node:url'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
  server: {
    // This is the line that allows Vite to be accessible from outside the container
    host: true,

    // This is the port your Vite server will run on
    port: 5173,

    // This is needed for file changes to be detected inside a Docker container
    watch: {
      usePolling: true
    }
  }
})