$(function () {
    $('.button-checkbox').each(function () {

        // Settings
        var $widget = $(this),
            $button = $widget.find('button'),
            $checkbox = $widget.find('input:checkbox'),
            color = $button.data('color');

        // Event Handlers
        $button.on('click', function () {
            $checkbox.triggerHandler('change');
            updateDisplay();
        });
        $checkbox.on('change', function () {
            updateDisplay();
        });

        // Actions
        function updateDisplay() {
            var isChecked = $checkbox.is(':checked');

            // Update the button's color
            if (isChecked) {
                $button
                    .addClass('active');
            }
            else {
                $button
                   .removeClass('active')
            }
        }

        // Initialization
        function init() {
            updateDisplay();
        }
        init();
    });
});