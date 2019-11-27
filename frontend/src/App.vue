<template>
  <v-app id="app">
     <v-navigation-drawer app fixed permanent clipped>
      <v-toolbar></v-toolbar>
      <v-toolbar flat>
        <v-list
        dense
        nav
      >
        <v-list-item
          v-for="item in items"
          :key="item.title"
          link
          :to="{name: item.title}"
        >
          <v-list-item-content>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
      </v-toolbar>
    </v-navigation-drawer>

    <v-app-bar app class="elevation-1" clipped-left dark>
      <span>My Analysis App</span>
    </v-app-bar>

    <v-content>
      <v-container fluid bg grid-list-md text-xs-center>
        <v-layout row wrap align-cente justify-center align-center>
          <v-flex>
            <router-view></router-view>
          </v-flex>
        </v-layout>
      </v-container>
    </v-content>
  
  <v-footer app dark>
    <v-col
      class="text-center"
      cols="12"
    >
      {{ 2019 }} — <strong>Lorenzo Peppoloni</strong>
    </v-col>
  </v-footer>
  </v-app>
</template>

<script>
export default {
  name: 'App',

  components: {
  },

  data: () => ({
    items: [
      { title: 'Analysis', href: '/'},
      { title: 'Report', href: '/v1/report'},
        ],
  }),
};
</script>
