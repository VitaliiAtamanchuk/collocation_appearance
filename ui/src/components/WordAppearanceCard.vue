<template>
  <div>
    <v-card light raised class='ma-3'>
      <v-card-title primary-title>
        <div class="headline">
          <span class='font-italic font-weight-medium'>{{word}}</span> -
          <a class='body-2' target='_blank' :href="value['link']"><v-icon>open_in_new</v-icon></a>
        </div>
      </v-card-title>

      <v-card-actions>
        <v-spacer />
        <v-slide-y-transition>
          <v-dialog v-model="show" max-width='700'>
            <v-btn slot='activator' flat small color="green darken-1" dark>Open appearances {{value['appearance'].length}}</v-btn>
            <v-card>
              <v-card-title class="headline">
                <div>
                  Appearances - {{word}} -
                  <a class='body-1' target='_blank' :href="value['link']">
                    <v-icon size='30'>open_in_new</v-icon></a>
                </div>
                <v-layout row>
                  <v-text-field v-model='numOfTabs' class='pr-5' single-line
                    label="Number of tabs" outline />
                  <v-btn @click='openVideos' class='ml-5' large>
                    Open in new tabs<v-icon>open_in_new</v-icon></a></v-btn>
                </v-layout>
              </v-card-title>
              <v-card-text>
                <v-data-table
                        :headers="headers"
                        :items="value['appearance']"
                        item-key="link" 
                        light
                        class="elevation-1"
                        :rows-per-page-items="[5,10,20]"
                    >
                        <template slot="items" slot-scope="props">
                            <td><a 
                                :href="get_youtube_time_url(props.item.webpage_url, props.item.start)"
                                target='_blank'>
                                {{props.item.title}}
                            </a></td>
                            <td>{{ props.item.start | formatTime }} - {{ props.item.end | formatTime }}</td>
                        </template>
                    </v-data-table>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="green darken-1" flat @click.native="show = false">Close</v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>
        </v-slide-y-transition>

      </v-card-actions>
    </v-card>
  </div>
</template>

<script>
export default {
  props: ['value', 'word'],
  data() {
    return {
      headers: [
        {text: 'Link', sortable: false},
        {text: 'Time', sortable: false},
      ],
      show: false,
      numOfTabs: 10,
    }
  },
  methods: {
    get_youtube_time_url(url, startTime) {
      startTime = startTime.split('.')[0]
      let [hours, mins, secs] = startTime.split(':')
      let time = parseInt(secs) + parseInt(mins)*60 + parseInt(hours)*3600 - 2
      let videoId = url.split('?v=')[1]
      let retval = `https://youtu.be/${videoId}?t=${time}`
      return retval
    },
    openVideos() {
      const min = Math.min(this.numOfTabs, this.value['appearance'].length)
      const values = this.value['appearance'].slice(0, min)
      let urls = []
      for (let value of values) {
        urls.push(this.get_youtube_time_url(value['webpage_url'], value['start']))
      }

      for (let url of urls) {
        // Object.assign(document.createElement('a'), { target: '_blank', href: url}).click()
        // window.open(url, 'parent')
        // window.focus()
        // var a = document.createElement("a")
        // a.href = url
        // var evt = document.createEvent("MouseEvents")
        // evt.initMouseEvent("click", true, true, window, 0, 0, 0, 0, 0,
        //   true, false, false, false, 0, null)
        // a.dispatchEvent(evt)
      }
    }
  }
}
</script>
