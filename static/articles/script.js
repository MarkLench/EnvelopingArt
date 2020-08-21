import vPopup from "./"

var app = new Vue({
  el: '#article_box',
  data: {
    article: [],
    isInfoArticle: false;
  },
  components {
    vPopup
  },
  /*
  created: function() {
    const self = this;
    axios.get('/publications/api/posts/')
    .then(function(response) {
      self.article = response.data
    })
  }, */
  methods: {
    article_data: funtion(slug) {
        this.isInfoArticle: true;
    }
    close_data : funtion() {

    }
  },
})
