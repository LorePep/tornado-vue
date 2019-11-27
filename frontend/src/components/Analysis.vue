<template>
    <v-flex xs8  offset-md2>
        <v-select
            :items="files"
            menu-props="auto"
            label="Select"
            hide-details
            prepend-icon="folder_open"
            single-line
            v-on:change="loadTimeseries"
        ></v-select>
          <v-chart :options="polar"/>
     </v-flex>
</template>

<script>
import axios from 'axios'
import 'echarts/lib/chart/line'
import ECharts from 'vue-echarts'

export default {
  components: {
    'v-chart': ECharts
  },
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
  methods: {
    loadTimeseries(file) {
      axios.get('http://localhost:5000/v1/timeseries', {params: { fileName: file } })
      .then(response => {
        return {
        polar: {
          title: {
            text: '极坐标双数值轴'
          },
          legend: {
            data: ['line']
          },
          polar: {
            center: ['50%', '54%']
          },
          tooltip: {
            trigger: 'axis',
            axisPointer: {
              type: 'cross'
            }
          },
          angleAxis: {
            type: 'value',
            startAngle: 0
          },
          radiusAxis: {
            min: 0
          },
          series: [
            {
              coordinateSystem: 'polar',
              name: 'line',
              type: 'line',
              showSymbol: false,
              data: response.data.timeseries
            }
          ],
          animationDuration: 2000
        }
        }
        })
      .catch(error => {
        /*eslint no-console: ["error", { allow: ["error"] }] */
        console.error(error);
      })
    }
  }
}
</script>
