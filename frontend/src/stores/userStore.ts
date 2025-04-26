import axios from "axios"
import { defineStore } from "pinia"
import { ref } from "vue"

export const useUserStore = defineStore('userStore', () => {
  const user = ref<{
    role: string | any,
    name:string | any,
    email: string | any,
    is_active:boolean | any,
    is_staff: boolean | any,
  } | null>({
    role: '',
    name: '',
    email: '',
    is_active:false,
    is_staff: false,
  })
  const token = ref('')

  const role = ref('')
  const isAuthenticated = ref(false)

  function setUser(data: any) {
    user.value = data
    role.value = data.role
    isAuthenticated.value = true
  }

  function getUserData(){
    return user.value
  }

  function logout() {
    user.value = null 
    role.value = ''
    isAuthenticated.value = false
  }

  async function getUser(){
    try {
      const res = await axios.get('api/profile-view/', {
        withCredentials: true
      })
      setUser(res.data)
    } catch (err){}
  }

  async function updateUser(){
    await getUser()
  }

  function saveUserToken(x: any){
    token.value = x
  }

  function getUserToken(){
    return token.value
  }

  return {
    user,
    role,
    isAuthenticated,
    setUser,
    logout,
    getUserData,
    getUser,
    updateUser,
    getUserToken,
    saveUserToken,
  }
}, {
  persist: true // ✅ this works with setup syntax
})
