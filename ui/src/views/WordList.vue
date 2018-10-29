<template>
    <v-container fluid>
        <v-slide-y-transition mode="out-in">
            <v-layout column align-center fill-height>
                <h1 class='text-xs-center my-4'>Word list</h1>
                <v-card light class='pa-3'>
                <v-btn
                    absolute
                    top
                    color="accent"
                    :disabled='!selected.length'
                    right
                    @click='word_appearance()'
                    >
                    Word appearance for selected words
                </v-btn>
                <v-card-title>
                    <v-layout row wrap>
                        <v-flex xs12>
                            <div class='title pl-5'>
                            <span v-if='isRandActive'>Rand List</span>
                            <span v-else>Overall Word List</span>
                            </div>
                            <v-layout row wrap>
                            <v-btn color='primary' @click='get_words()'>
                                Word List</v-btn>
                            <v-btn color='primary' class='pr-4' @click='get_rand_words()'>
                                Rand Word List
                                <v-badge color="cyan" class='px-1 mr-1' right>
                                    <span slot="badge">{{randWordsAmount}}</span>
                                </v-badge>
                            </v-btn>
                            <v-spacer />
                            <v-flex xs4 align-right>
                            <v-text-field
                                label="Rand words amount"
                                single-line
                                v-model='randWordsAmount'
                                outline
                            ></v-text-field>
                            </v-flex>
                            </v-layout>
                        </v-flex>
                        <v-flex xs12>
                            <v-text-field
                            v-model="search"
                            append-icon="search"
                            label="Search"
                            single-line
                            hide-details
                            ></v-text-field>
                    </v-flex>
                    </v-layout>

                    </v-card-title>
                    <v-data-table
                        :headers="headers"
                        :items="filteredWords"
                        :search="search"
                        :loading="loading"
                        v-model="selected"
                        item-key="link"
                        select-all
                        class="elevation-1"
                        :rows-per-page-items="[5,10,20]"
                    >
                        <v-progress-linear slot="progress" color="blue" indeterminate />
                        <template slot="items" slot-scope="props">
                            <td>
                            <v-checkbox
                                v-model="props.selected"
                                primary
                                hide-details
                            ></v-checkbox>
                            </td>
                            <td>{{ props.item.word }}</td>
                            <td><a :href="props.item.link" target='_blank'>
                                oxf3000
                            </a></td>
                            <td>{{ props.item.appearance_num }}</td>
                            <td>
                              <v-btn small color="red lighten-2" @click='mark_learned(props.item)'>
                                Learned<v-icon>save</v-icon>
                              </v-btn>
                            </td>
                        </template>
                        <v-alert slot="no-results" :value="true" color="error" icon="warning">
                            Your search for "{{ search }}" found no results.
                        </v-alert>
                    </v-data-table>
                </v-card>
            </v-layout>
        </v-slide-y-transition>
    </v-container>
</template>

<script>
import { mapMutations } from 'vuex'

export default {
    data() {
        return {
            loading: false,
            search: '',
            isRandActive: false,
            words: [],
            selected: [],
            randWordsAmount: 5,
            headers: [
                {text: 'Word', value: 'word'},
                {text: 'Link', value: 'link', sortable: false},
                {text: 'Appearance num', value: 'appearance_num'},
            ],
        }
    },
    created() {
        this.get_words()
        // this.get_rand_words()
    },
    computed: {
        filteredWords() {
            return this.words.filter((i) => {
                return i.includes(this.search)
            })
        }
    },
    methods: {
        ...mapMutations([
           'selectWords' ,
        ]),
        mark_learned(item) {
          // this.post('http://localhost:8000/mark_learned', {}).then(response => {
          //
          // })
        },
        word_appearance() {
          this.selectWords(this.selected)
          this.$router.push('display_word_app')
        },
        get_rand_words() {
            this.isRandActive = true
            this.loading = true
            const word_num = this.randWordsAmount
            this.$http.get('http://localhost:8000/rand_words',
            {params: {'word_num': word_num}}).then(response => {
                console.log(response)
                this.words = response.body;
            }, response => {
                // error callback
                console.log(response)
            }).then(() => {
                this.loading = false
            })
        },
        get_words() {
            this.isRandActive = false
            this.loading = true
            this.$http.get('http://localhost:8000/word_list').then(response => {
                console.log(response)
                this.words = response.body;
            }, response => {
                // error callback
                console.log(response)
            }).then(() => {
                this.loading = false
            })
        },
    }
}
</script>
