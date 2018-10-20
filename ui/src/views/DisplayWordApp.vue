<template>
    <v-container fluid>
        <v-slide-y-transition mode="out-in">
            <v-layout column align-center fill-height>
                <v-dialog
                    v-model="loading"
                    persistent
                    width="300"
                >
                    <v-card class='pa-4' color="primary" dark>
                    <v-card-text>
                        Please stand by
                        <v-progress-linear
                        indeterminate
                        color="white"
                        class="mb-0"
                        ></v-progress-linear>
                    </v-card-text>
                    </v-card>
                </v-dialog>
                <div>
                    <h1 class='text-xs-center my-4'>
                        Word appearance
                        <v-btn flat icon color="green" @click='get_word_appearances()'>
                            <v-icon>cached</v-icon>
                        </v-btn>
                    </h1>
                    <words-appearance-list :wordsAppearances='wordsAppearances' />
                </div>
            </v-layout>
        </v-slide-y-transition>
    </v-container>
</template>

<script>
    import WordsAppearanceList from '@/components/WordsAppearanceList.vue'

    export default {
        components: {
            'words-appearance-list': WordsAppearanceList,
        },
        data() {
            return {
                loading: true,
                wordsAppearances: [],
            }
        },
        created() {
            this.get_word_appearances()
        },
        methods: {
            get_word_appearances() {
                this.loading = true
                const words = this.$store.state.selectedWords
                this.$http.post('http://localhost:8000/word_appearance', {words}).then(response => {
                    console.log(response)
                    this.wordsAppearances = response.body;
                }, response => {
                    // error callback
                    console.log(response)
                }).then(() => {
                    this.loading = false
                })
            }
        },
        computed: {
            selectedWords() {
                return this.$store.state.selectedWords
            }
        }
    }
</script>