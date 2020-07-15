/*
var app = new Vue({
  el: '#start_content',
  data: {
    comments: [],
    likes: 0,
    dislikes: 0
  },
  created: function() {
    const self = this;
    axios.get('/publications/api/posts/')
    .then(function(response) {
      self.comments = response.data
    })
  },
})
