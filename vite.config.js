import { fileURLToPath, URL } from 'url'
import path from 'path'

import { defineConfig } from 'vite'

import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/

export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, 'src')
    }
  },
  server: {
    proxy: {
    '^/api*': {
    target: 'http://localhost:8080/'
    }
    }
    }
})
