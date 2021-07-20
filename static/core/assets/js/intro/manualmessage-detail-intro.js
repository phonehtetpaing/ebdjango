 <!--Intro JS-->
      function startIntro(){
        var intro = introJs();
          intro.setOptions({
            showProgress: true,
            showBullets: false,
            doneLabel: "I got it!",
            steps: [
              {
                intro: gettext('intro_manual_message_list_01')
              },
              {
                element: document.querySelector('#step1'),
                intro: gettext('intro_manual_message_detail_02')
              },
              {
                element: document.querySelector('#step2'),
                intro: gettext('intro_manual_message_detail_03')
              },
              {
                element: document.querySelector('#step3'),
                intro: gettext('intro_step_message')
              },
              {
                element: document.querySelector('#step4'),
                intro: gettext('intro_text_message')
              },
              {
                element: document.querySelector('#step5'),
                intro: gettext('intro_image_message')
              },
              {
                element: document.querySelector('#step6'),
                intro: gettext('intro_carousel_message')
              },
              {
                element: document.querySelector('#help_tour'),
                intro: gettext('intro_remind_button_location')
              },
            ]
          });
          intro.start();
      }