<template>
  <v-app>
    <v-toolbar fixed app dark clipped-left color="primary" class="elevation-2">
          <v-toolbar-title>My Analysis Site</v-toolbar-title>
    </v-toolbar>

    <v-navigation-drawer  class="drawer-style" id="style-1">
      <v-divider></v-divider>

      <v-list dense>
        <v-list-item
          v-for="item in items"
          :key="item.title"
        >
          <v-list-item-content>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
      
  <v-container fluid>
    <router-view></router-view>
  </v-container>
  
  <v-footer padless>
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
          { title: 'Analysis'},
          { title: 'Second Page'},
        ],
  }),
};
</script>
