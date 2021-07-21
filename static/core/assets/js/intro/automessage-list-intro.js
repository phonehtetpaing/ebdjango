<!--Intro JS-->
      function startIntro(){
        var intro = introJs();
          intro.setOptions({
            showProgress: true,
            showBullets: false,
            doneLabel: gettext('intro_done'),
            steps: [
              {
                intro: gettext('intro_auto_message_list_01')
              },
              {
                element: document.querySelector('#step1'),
                intro: gettext('intro_auto_message_list_02')
              },
              {
                element: document.querySelector('#step2'),
                intro: gettext('intro_auto_message_list_03')
              },
              {
                element: document.querySelector('#step3'),
                intro: gettext('intro_auto_message_list_04')
              },
              {
                element: document.querySelector('#step4'),
                intro: gettext('intro_auto_message_list_05')
              },
              {
                element: document.querySelector('#step5'),
                intro: gettext('intro_auto_message_list_06')
              },
              {
                element: document.querySelector('#step6'),
                intro: gettext('intro_message_new')
              },
              {
                element: document.querySelector('#step7'),
                intro: gettext('intro_message_edit')
              },
              {
                element: document.querySelector('#step8'),
                intro: gettext('intro_auto_message_list_09')
              },
              {
                element: document.querySelector('#step9'),
                intro: gettext('intro_auto_message_list_10')
              },
              {
                element: document.querySelector('#step10'),
                intro: gettext('intro_message_delete')
              },
              {
                element: document.querySelector('#help_tour'),
                intro: gettext('intro_remind_button_location')
              },
            ]
          });
          intro.start();
      }