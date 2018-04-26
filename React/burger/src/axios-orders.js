import axios from 'axios';

const instance = axios.create({
    baseURL: 'https://burger-react-2bc8e.firebaseio.com'
})

export default instance;