<template>
  <va-navbar color="primary" class="mb-2">
    <template #left>
      <va-navbar-item>E Libroteka</va-navbar-item>
    </template>
    <template #center>
      <va-navbar-item><router-link to="/">Home</router-link></va-navbar-item>
      <va-navbar-item><router-link to="/about">About</router-link></va-navbar-item>
    </template>
    <template #right>
      <va-navbar-item
        ><va-button color="success" gradient class="mr-4"
          ><router-link to="/register-book">Register</router-link></va-button
        ></va-navbar-item
      >
    </template>
  </va-navbar>
  <router-view />
  <h2>Hola mundo</h2>
</template>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
