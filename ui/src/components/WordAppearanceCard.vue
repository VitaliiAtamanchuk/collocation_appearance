<template>
  <div>
    <v-card light raised class='ma-3'>
      <v-card-title primary-title>
        <div class="headline">
          <span class='font-italic font-weight-medium'>{{word}}</span> - 
          <a class='body-1' target='_blank' :href="value['link']"><v-icon>open_in_new</v-icon></a>
        </div>
      </v-card-title>

      <v-card-actions>
        <v-spacer />
        <v-slide-y-transition>
          <v-dialog v-model="show" persistent max-width='700'>
            <v-btn slot='activator' flat small color="green darken-1" dark>Open appearances {{value['appearance'].length}}</v-btn>
            <v-card>
              <v-card-title class="headline">Appearances - {{word}}</v-card-title>
              <v-card-text>
                <v-list
                  subheader
                  two-line
                  v-for="(appearance, index) in value['appearance']"
                  :key='index'
                >
                  <v-list-tile @click="">
                    <!-- <v-list-tile-action>
                      <v-checkbox v-model="notifications"></v-checkbox>
                    </v-list-tile-action> -->
                    <v-list-tile-content>
                      <v-list-tile-title>
                        <a 
                          :href='get_youtube_time_url(appearance["webpage_url"], appearance["start"])' 
                          target='_blank'>
                          {{appearance['title']}}</a>
                      </v-list-tile-title>
                      <v-list-tile-sub-title>
                        {{appearance['start'] | formatTime}}-{{appearance['end'] | formatTime}}
                      </v-list-tile-sub-title>
                    </v-list-tile-content>
                  </v-list-tile>
                </v-list>
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
      show: false,
    }
  },
  methods: {
    get_youtube_time_url(url, startTime) {      
      startTime = startTime.split('.')[0]
      let [hours, mins, secs] = startTime.split(':')
      let time = parseInt(secs) + parseInt(mins)*60 + parseInt(hours)*3600
      let videoId = url.split('?v=')[1]
      let retval = `https://youtu.be/${videoId}?t=${time}`
      return retval
    }
  }
}
</script>