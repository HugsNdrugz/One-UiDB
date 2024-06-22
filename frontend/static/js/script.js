import Vue from 'vue';
import anime from 'animejs';

const app = new Vue({
  el: '#app',
  data: {
    apps: [
      { name: 'SMS', icon: 'message' },
      { name: 'Contacts', icon: 'account_box' },
      { name: 'Calendar', icon: 'date_range' },
      // Add more apps here
    ],
  },
  mounted() {
    this.animateAppIcons();
  },
  methods: {
    urlForAppDetails(appName) {
      return `app/${appName}`; // Construct dynamic URLs
    },
    animateAppIcons() {
      const appCards = document.querySelectorAll('.app-card');

      appCards.forEach((card) => {
        anime({
          targets: card,
          opacity: [0, 1],
          translateY: [-20, 0],
          duration: 800,
          easing: 'easeInOutCubic',
        });
      });
    },
  },
});