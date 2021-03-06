//function loadScript(url) {
//  var script = document.createElement('script');
//  script.type = 'text/javascript';
//  script.src = url;
//};
//
//loadScript("https://cdn.jsdelivr.net/vue/latest/vue.min.js");
//loadScript("https://cdn.jsdelivr.net/npm/botui/build/botui.js");

var botui = new BotUI('hello-world');

      botui.message.add({
        content: 'Hello World from bot!'
      }).then(function () { // wait till previous message has been shown.

        botui.message.add({
          delay: 1000,
          human: true,
          content: 'Hello World from human!'

        }).then(function () {

            botui.message.add({
              delay: 3000,
              loading: true,
              human: true,
              content: 'Hello, this is delayed message shown after a loading message.'
            });
        });
      });