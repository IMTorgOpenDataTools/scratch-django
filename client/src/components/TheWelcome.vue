<template>
  Press to get the users from the data:  
  <button @click="getUser()">Users</button>
  <div v-for="user in users" :key="user.uuid">
    {{ user.name }}
  </div>
</template>

<script>
export default {
  name: 'TheWelcome',
  data() {
    return {
      users: []
    }
  },
  methods: {
    getUser(){
      fetch('http://localhost:8000/api/users/?format=json', {
          headers: { 'Content-type': 'application/json' },
        }).then(res => res.json()).then((response) => {
          this.users = response.results
        }).catch((error) => {
          console.log('Looks like there was a problem: \n', error);
        })
      return true
    }
  }
}


</script>

