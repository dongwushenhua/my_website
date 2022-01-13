import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)
export default new Vuex.Store({
    state: { icon: "无", id: "无", username: "无", signature: "无", sex: "无", contact: "无" },
    mutations: {
        getNewIcon(state, newIcon) {
            state.icon = newIcon;
            console.log(icon)
        },
        getNewUsername(state, newUsername) {
            state.username = newUsername
        },
        getNewSignature(state, newSignature) {
            state.signature = newSignature
        },
        getNewSex(state, newSex) {
            state.sex = newSex
        },
        getNewSignature(state, newContact) {
            state.contact = newContact
        }
    },
    actions: {}
})