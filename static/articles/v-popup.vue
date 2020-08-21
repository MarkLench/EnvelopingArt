<template>
<div class="content_container">
    <div class="close_content_container" v-on:click="close_data()"></div>
    <div class="content_display">
        <div class="text_container">
            <h3>Title</h3><slog></slot>
            <h6>Thesis</h6>
            <p>BODY</p>
         </div>
    </div>
</div>
</template>

<script>
    {
    name: "popup",
    props: {},
    data() {
        return {}
    },
    computed: {}
    }
</script>
<style>
    .content_container {
        .content_container {
          position: fixed;
          display: flex;
          align-items: center;
          justify-content: center;
          width: 100%;
          height: 100%;
          background-color: rgba(0, 0, 0, 0.2);
          z-index: 11;
        }
        .close_content_container {
          position: fixed;
          width: 42px;
          height: 42px;
          background-color: black;
          z-index: 12;
          top: 5px;
          right: 5px;
        }
        .content_display {
          height: 90%;
          width: 960px;
          background-color: white;
          border-radius: 25px;
          overflow: auto;

          -webkit-transition: 0.8s;
          -moz-transition: 0.8s;
          -o-transition: 0.8s;
          transition: 0.8s;
        }
        @media only screen and (max-width: 980px) {
          .content_display {
            width: 90%;}
        }
        .text_container {
            margin: 0 30px;
            padding: 25px 0;
        }
        /* хром, сафари */
        .content_display::-webkit-scrollbar { width: 0; }

        /* ie 10+ */
        .content_display { -ms-overflow-style: none; }
    }
</style>