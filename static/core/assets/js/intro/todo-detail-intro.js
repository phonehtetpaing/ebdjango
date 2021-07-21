<!--Intro JS-->
      function startIntro(){
        var intro = introJs();
          intro.setOptions({
            showProgress: true,
            showBullets: false,
            doneLabel: gettext('intro_done'),
            steps: [
              {
                intro: gettext('intro_todo_detail_01')
              },
              {
                element: document.querySelector('#step1'),
                intro: gettext('intro_todo_detail__02')
              },
              {
                element: document.querySelector('#step2'),
                intro: gettext('intro_todo_detail__03')
              },
              {
                element: document.querySelector('#step3'),
                intro: gettext('intro_todo_detail__04')
              },
              {
                element: document.querySelector('#step4'),
                intro: gettext('intro_todo_detail__05')
              },
              {
                element: document.querySelector('#help_tour'),
                intro: gettext('intro_remind_button_location')
              },
            ]
          });
          intro.start();
      }