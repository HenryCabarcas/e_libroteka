import { createApp } from 'vue'
import App from './App.vue'
import './registerServiceWorker'
import router from './router'
import 'material-design-icons-iconfont/dist/material-design-icons.css'
import { VuesticPlugin } from 'vuestic-ui' // <-
import 'vuestic-ui/dist/vuestic-ui.css' // <-
import './index.css'
const app = createApp(App);
app.use(router);
app.use(VuesticPlugin);
app.mount('#app');
