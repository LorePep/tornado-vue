<template>
    <v-flex xs8  offset-md2>
        <v-select
            :items="files"
            menu-props="auto"
            label="Select"
            hide-details
            prepend-icon="folder_open"
            single-line
        ></v-select>
     </v-flex>
</template>

<script>
import axios from 'axios'

export default {
  data () {
    return {
      files: [],
    }
  },
  mounted () {
    return axios.get('http://localhost:5000/v1/listfiles')
      .then(response => {
        this.files = response.data.fileList
      })
      .catch(error => {
        /*eslint no-console: ["error", { allow: ["error"] }] */
        console.error(error)
      })
  },
}
</script>
