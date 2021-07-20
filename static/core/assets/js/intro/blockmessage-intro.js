 <!--Intro JS-->
      function startIntro(){
        var intro = introJs();
          intro.setOptions({
            showProgress: true,
            showBullets: false,
            doneLabel: "I got it!",
            steps: [
              {
                intro: gettext('intro_block_message_01')
              },
              {
                element: document.querySelector('#step1'),
                intro: gettext('intro_block_message_02')
              },
              {
                element: document.querySelector('#step2'),
                intro: gettext('intro_step_message')
              },
              {
                element: document.querySelector('#step3'),
                intro: gettext('intro_text_message')
              },
              {
                element: document.querySelector('#step4'),
                intro: gettext('intro_image_message')
              },
              {
                element: document.querySelector('#step5'),
                intro: gettext('intro_carousel_message')
              },
              {
                element: document.querySelector('#step6'),
                intro: gettext('intro_quickreply_message')
              },
              {
                element: document.querySelector('#step7'),
                intro: gettext('intro_wait_message')
              },
              {
                element: document.querySelector('#step8'),
                intro: gettext('intro_file_message')
              },
              {
                element: document.querySelector('#step9'),
                intro: gettext('intro_tag_message')
              },
              {
                element: document.querySelector('#step10'),
                intro: gettext('intro_input_message')
              },
              {
                element: document.querySelector('#step11'),
                intro: gettext('intro_form_message')
              },
              {
                element: document.querySelector('#step12'),
                intro: gettext('intro_block_message_03')
              },
              {
                element: document.querySelector('#step13'),
                intro: gettext('intro_block_message_04')
              },
              {
                element: document.querySelector('#help_tour'),
                intro: gettext('intro_remind_button_location')
              },
            ]
          });
          intro.start();
      }