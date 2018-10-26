<template>
  <v-layout row wrap>
    <v-flex xs12 sm6 md3 xl2 v-for="(value, word, index) in wordsAppearances" :key='index'>
      <word-appearance-card :value='value' :word='word' />
    </v-flex>
  </v-layout>
</template>

<script>
import WordAppearanceCard from './WordAppearanceCard.vue'

export default {
  props: ['wordsAppearances'],
  components: {
    'word-appearance-card': WordAppearanceCard,
  },
}
</script>
