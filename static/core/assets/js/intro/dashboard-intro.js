<!--Intro JS-->
      function startIntro(){
        var intro = introJs();
          intro.setOptions({
            showProgress: true,
            showBullets: false,
            doneLabel: gettext('intro_done'),
            steps: [
              {
                intro: gettext("intro_dashboard_01")
              },
              {
                intro: gettext('intro_dashboard_02')
              },
              {
                element: document.querySelector('#step1'),
                intro: gettext('intro_dashboard_03')
              },
              {
                element: document.querySelector('#step2'),
                intro: gettext('intro_dashboard_04'),
                position: 'right'
              },
              {
                element: document.querySelector('#step3'),
                intro: gettext('intro_dashboard_05'),
                position: 'left'
              },
              {
                element: document.querySelector('#step4'),
                intro: gettext('intro_dashboard_06')
              },
              {
                element: document.querySelector('#step5'),
                intro: gettext('intro_dashboard_07')
              },
              {
                element: document.querySelector('#help_tour'),
                intro: gettext('intro_remind_button_location')
              },
            ]
          });
          intro.start();
      }