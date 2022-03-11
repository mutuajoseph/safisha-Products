<template>
   <div id="dashboard">
      <v-navigation-drawer
      v-model="drawer"
      app
      clipped
    >
   
    <v-list>
      <v-list-item link v-for="item in not_items" :key="item.title" router :to="item.route">
        <v-list-item-icon>
          <v-icon style="Color:item.color" >{{item.action}}</v-icon>
        </v-list-item-icon>

        <v-list-item-title style="font-size: .8rem;">{{item.title}}</v-list-item-title>
      </v-list-item>
      <v-divider></v-divider>
       <v-list-item link v-for="item in items" :key="item.title" router :to="item.route">
        <v-list-item-icon>
          <v-icon  style="text-decoration: none;">{{item.action}}</v-icon>
        </v-list-item-icon>

        <v-list-item-title style="text-decoration: none; font-size: .8rem;">{{item.title}}</v-list-item-title>
      </v-list-item>
    </v-list>
    </v-navigation-drawer>

    <v-app-bar
      app
      clipped-left
      color="#1d3557"
      dark
      dense
    >
      <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title style="cursor: pointer;" @click="$router.push({path: `/`})">Safisha Products</v-toolbar-title>

    </v-app-bar>
    <v-footer app>
      <span style="font-size: .8rem;">&copy; {{ new Date().getFullYear() }} Designed by Joseph Wambua</span>
    </v-footer>
  </div>
</template>

<script>
export default {
    name:"Navbar",
    data: () => ({
      drawer: true,
      not_items: [
            {
            action: 'home',
            title: 'Dashboard',
            route:  '/'
            },
        ],
      items: [
        {
          action: 'collections_bookmark',
          title: 'Products',
          route: '/products',
          color: "red"
        },
      ]
    }),
    methods: {
      
    }
}
</script>

<style>
</style>