import axios from "axios";
export default async function refreshToken() {
    if (window.localStorage.getItem("username") === null) {
        window.localStorage.setItem("username", "user")
    }
    let body = {
        username: window.localStorage.getItem("username"),
        password: process.env.VUE_APP_ANY_USER_PWD
    }
    let url = process.env.VUE_APP_BACK_END_URL + "login/"

    let response = await axios.post(url, body)
    if (response.status == 200) {
        console.log(response.data.refresh)
        console.log(response.data.access)
        window.localStorage.setItem("refresh_token", response.data.refresh)
        window.localStorage.setItem("access_token", response.data.access)
        return true
    }
    return false


}