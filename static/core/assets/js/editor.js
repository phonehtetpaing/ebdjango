
$(function(){
    updateImageInput()
    updateFileInput()
    $(".option-bubble").hide(200);
    rangeSlider();

    // resize input fields to grow with input
    autosize($('.expand'));
    toggleTitleEdit();
    filterBlocks();
});

// update image previews
function updateImageInput() {
    $(document).on("change", ".message-img-input", function(){
            var url = $(this).val();
            var current = $(this);
            var img = new Image();

            $(current).siblings(".message-img-thumbnail").empty();
            img.onload = function() {
                $(current).siblings(".message-img-thumbnail").prepend('<img src="'+url+'" />')
            }
            img.onerror = function() {
                $(current).siblings(".message-img-thumbnail").prepend('<i class="fa fa-camera fa-5x text-center" aria-hidden="true"></i><span class=" text-center">No Image Found</span>')
            }
            img.src = url;
        });
}

// update file name previews
function updateFileInput() {
    $(document).on("change", ".message-file-input", function(){
            var url = $(this).val();
            var current = $(this);

            $(current).siblings(".message-file-thumbnail").empty();
            url_parts = url.split("/");
            $(current).siblings(".message-file-thumbnail").prepend('<i class="fa fa-file fa-5x text-center" aria-hidden="true"></i><span class=" text-center">'+ url_parts[url_parts.length - 1] +'</span>')
    });
}

// get data from internal api
function getApiData(path, data) {
        var result = $.ajax({
            url : '/api/'+ path,
            method: "GET",
            data : data,
            dataType: 'json'
        })
        .fail(function(error){
             console.log("ERROR!", error);
        });

        return result;
};

function rangeSlider(){
  var slider = $('.range-slider'),
      range = $('.range-slider__range'),
      value = $('.range-slider__value');

  slider.each(function(){

    value.each(function(){
      var value = $(this).prev().attr('value');
      $(this).html(value + " ms");
    });

    range.on('input', function(){
      $(this).next(value).html(this.value + " ms");
    });
  });
};

// toggles between display and edit element for block title
function toggleTitleEdit() {
    $(".title-edit").hide();

    $(document).on("click", ".bi-title-edit", function(){
        $(".title-display").hide();
        $(".title-edit").show();
    });

    $(document).on("click", ".bi-title-save", function(){
        $(".title-edit").hide();
        var newTitle = "<h3>" + $("input[name=admin_text]").val() + " <a class='bi-title-edit'><i class='fa fa-pencil' aria-hidden='true'></i></a></h3>";
        $(".title-display").html(newTitle);
        $(".title-display").show();
    });
}

function filterBlocks() {
    $(".block-filter").on("keyup", function() {
        var value = $(this).val().toLowerCase();
        $(".block-list a").filter(function() {
          $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
        });
    });
}

$(function(){
    // jQuery UI
    $('#apis').sortable({
		update: function(event, ui) {
		    child_no_refresh();
		    dataIdRefresh();
		}
	});
    $(".carousel_columns").sortable({
		update: function(event, ui) {
		    carousel_child_no_refresh(ui.item);
		}
	});

    // Carouse columns Toggle
    $(document).on("click", ".columns-toggle", function(){
        if ($(this).hasClass("ti-angle-down")) {
            $(this).removeClass("ti-angle-down");
            $(this).addClass("ti-angle-up");
            $(this).siblings(".carousel_columns").hide(200);
        } else if($(this).hasClass("ti-angle-up")) {
            $(this).removeClass("ti-angle-up");
            $(this).addClass("ti-angle-down");
            $(this).siblings(".carousel_columns").show(200);
        }
    });

    // Quick Reply Options Toggle
    $(document).on("click", ".api-child", function(e){
        // Hide all open options
        $(".option-bubble").not($(this).find(".option-bubble")).hide(200);
    })

    $(document).on("click", ".quick-reply", function(e){
        // Hide all open options
        $(".option-bubble").not(this.children).hide(200);
        $(this).children(".option-bubble").show(200);
    })

    // Api Child 要素追加
    $(".add-textsend").on("click", function(){ addTextMessage.bind($(this))(); });
    $(".add-imgsend").on("click", function(){ addImageMessage.bind($(this))(); });
    $(".add-filesend").on("click", function(){ addFileMessage.bind($(this))(); });
    $(".add-carouselsend").on("click", function(){ addCarouselMessage.bind($(this))(); });
    $(".add-quickreplysend").on("click", function(){ addQuickReplyMessage.bind($(this))(); });
    $(".add-waitsend").on("click", function(){ addWaitMessage.bind($(this))(); });
    $(".add-tagsend").on("click", function(){ addTagMessage.bind($(this))(); });
    $(".add-inputsend").on("click", function(){ addInputMessage.bind($(this))(); });
    $(".add-formsend").on("click", function(){ addFormMessage.bind($(this))(); });
    $(".add-goto").on("click", function(){ addGoToMessage.bind($(this))(); });
    $(document).on("click", ".add-form-child", function(){ addFormChild.bind($(this))(); });
    $(document).on("click", ".add-quickreply-child", function(){ addQuickReplyChild.bind($(this))(); });
    $(document).on("click", ".add-carousel-child", function(){ addCarouselMessageColumn.bind($(this))(); });

    $(document).on("click", ".ti-close", function(){
        if(!confirm(gettext('dia-erase-confirm'))){
            return false;
        } else {
            $(this).closest(".api-child").remove();
            child_no_refresh();
        }
    });
});

function addTextMessage(){
        var api_child_num = $(".api-child").length;

        var html = '<div class="row api-child" data-id="'+(api_child_num+1)+'">';
        html += '<div class="col-md-12">';
        html += '<div class="message-bubble">';
        html += '<div class="form-group">';
        html += '<div class="widgets"><ul><li><span class="widget-icon"><i class="ti-close"></i></li><li</span><span class="widget-icon"><i class="ti-close"></i></span></li></ul></div>';
        html += '<textarea rows="5" class="form-control input-child border-input bubble-input bubble-border-blue expand" style="height: auto" placeholder=" " name="TextSendMessage_0_'+(api_child_num+1)+'" maxlength="2000" required></textarea>';
        html += '<small class="form-text text-muted">Max 2000 characters.</small>';
        html += '</div>';
        html += '</div>';
        html += '</div>';
        html += '</div>';

        $("#apis").append(html);
        $("#apis").sortable('refresh');
        child_no_refresh();
}

function addImageMessage(){
        var api_child_num = $(".api-child").length;

        var html = '<div class="row api-child" data-id="'+(api_child_num+1)+'"> ';
        html += '<div class="col-md-12">';
        html += '<div class="message-bubble">';
        html += '<div class="form-group">';
        html += '<label><i class="ti-menu"></i>&nbsp;</label><i class="ti-close"></i>';

        html += '<div class="message-img-thumbnail vertical-align"><i class="fa fa-camera fa-5x text-center" aria-hidden="true"></i><span class=" text-center">No Image Found</span></div>';

        html += '<input type="text" class="message-img-input form-control border-input input-child" placeholder="https://example.com/original.jpg" name="ImageSendMessage_original_content_url_0_'+(api_child_num+1)+'" value="" maxlength="1000" required>';
        html += '<small class="form-text text-muted">Max 1000 characters.</small>';
        html += '</div>';
        html += '</div>';
        html += '</div>';
        html += '</div>';

        $("#apis").append(html);
        $("#apis").sortable('refresh');
        child_no_refresh();
    }

function addFileMessage(){
        var api_child_num = $(".api-child").length;

        var html = '<div class="row api-child" data-id="'+(api_child_num+1)+'">';
        html += '<div class="col-md-12">';
        html += '<div class="message-bubble">';
        html += '<div class="form-group">';
        html += '<label><i class="ti-menu"></i>&nbsp;</label><i class="ti-close"></i>';

        html += '<div class="message-file-thumbnail vertical-align"><i class="fa fa-file fa-5x" aria-hidden="true"></i><span class=" text-center">No File Found</span></div>';

        html += '<input type="text" class="message-file-input form-control border-input input-child" placeholder="https://example.com/original.jpg" name="FileSendMessage_'+(api_child_num+1)+'" value="" maxlength="1000" required>';
        html += '<small class="form-text text-muted">Max 1000 characters.</small>';
        html += '</div>';
        html += '</div>';
        html += '</div>';
        html += '</div>';

        $("#apis").append(html);
        $("#apis").sortable('refresh');
        child_no_refresh();
    }

function addCarouselMessage(){
        var api_child_num = $(".api-child").length;

        var html = '<div class="row api-child" data-id="'+(api_child_num+1)+'">';
        html += '<div class="col-md-12">';
        html += '<div class="message-bubble col-md-12">';
        html += '<div class="form-group">';
        html += '<label><i class="ti-menu"></i>&nbsp;&nbsp;<i class="columns-toggle ti-angle-down"></i></label><i class="ti-close"></i>';
        html += '<input type="text" class="form-control border-input input-child" placeholder="https://example.com/original.jpg" name="CarouselTemplate_alt_text_0_'+(api_child_num+1)+'" value="" hidden>';
        html += '<div class="carousel_columns scrolling-wrapper">';
        html += '</div>';

        html += '<div class="carousel_columns_control text-right">';
        html += '<button type="button" class="btn btn-info btn-fill btn-wd add-carousel-child"><i class="ti-plus"></i></button>';
        html += '</div>';

        html += '</div>';
        html += '</div>';
        html += '</div>';
        html += '</div>';

        $("#apis").append(html);
        $("#apis").sortable('refresh');
        child_no_refresh();
    }

function addCarouselMessageColumn(){
        var api_child_num = $(this).parent().siblings(".carousel_columns").children(".card").length;
        var sibling_input_child_name = $(this).parent().siblings(".input-child").attr("name");

        var name_split = sibling_input_child_name.split('_');
        var column_id = name_split[name_split.length - 1];

        // prevent more than 10 columns on carousel (LINE limitation)
        if (api_child_num >= 10)
            return false

        var html = '<div class="message-bubble bubble-white bubble-border-blue api-child col-md-12 item"><input type="hidden" name="CarouselTemplate_column_'+column_id+'_'+(api_child_num+1)+'">';
        html += '<i class="ti-close"></i><label>&nbsp;'+ gettext("lbl_thumbnail") +'</label>';
        html += '<div class="content">';
        html += '<div class="form-group">';

        html += '<div class="message-img-thumbnail vertical-align"><div class="row"><div class="row col-md-12 text-center"><i class="fa fa-camera fa-5x" aria-hidden="true"></i></div><div class="row col-md-12 text-center">No Image Found</div></div></div>';

        html += '<input type="text" class="message-img-input form-control border-input" placeholder=" " name="column_thumbnail_image_url_'+column_id+'" value="" maxlength="1000" required>';
        html += '<small class="form-text text-muted">Max 1000 characters.</small>';
        html += '</div>';
        html += '</div>';

        html += '<div class="form-group">';
        html += '<label>'+ gettext("lbl_title") +'</label>';
        html += '<input type="text" class="form-control border-input" placeholder="" name="column_title_'+column_id+'" value="" maxlength="40" required>';
        html += '<small class="form-text text-muted">Max 60 characters.</small>';
        html += '</div>';

        html += '<div class="form-group">';
        html += '<label>'+ gettext("lbl_text") +'</label>';
        html += '<input type="text" class="form-control border-input" placeholder="" name="column_text_'+column_id+'" value="" maxlength="60" required>';
        html += '<small class="form-text text-muted">Max 60 characters.</small>';
        html += '</div>';

        html += '<div class="form-group">';
        html += '<label>'+ gettext("lbl_action_url") +'</label>';
        html += '<input type="url" class="form-control border-input" placeholder=" " name="column_action_json_'+column_id+'" value="" maxlength="1000" required>';
        html += '<small class="form-text text-muted">Max 1000 characters.</small>';
        html += '</div>';

        html += '</div></div>';

        $(this).parent().siblings(".carousel_columns").append(html);
        $("#apis").sortable('refresh');
        child_no_refresh();
    }

function addQuickReplyMessage() {
        var api_child_num = $(".api-child").length;

            var selection = getApiData('message/block/list/')
            .done(function(api_response){
                var html = "     <div class='row api-child' data-id='"+(api_child_num+1)+"'>";
                html +="          <div class='col-md-12'>";
                html +="            <div class='message-bubble'>";
                html +="                <div class='form-group'>";
                html +="                    <label><i class='ti-menu'></i></label>"
                html +="                    <textarea rows='5' class='form-control input-child border-input bubble-input bubble-border-blue expand' placeholder=' ' name='QuickReplySendMessage_question_"+(api_child_num+1)+"' maxlength='160' required=''></textarea>"
                html +="                    <div class='vertical-align form-group'>"
                html +="                        <i class='ti-close'></i>"
                html +="                        <div class='quick-replies'>"
                html +="                            <div class='quick-reply anchor' data-quickreply-child-id='0'>"
                html +="                                <input type='text' class='input-child bubble-input ' maxlength='20' value='' placeholder='Enter Reply Text' name='QuickReplySendMessage_title_"+(api_child_num+1)+"'>"
                html +="                                <div class='option-bubble bubble-white'>"
                html +="                                    <div class='bubble-content'>"

                html +="                                <select class='input-child' name='QuickReplySendMessage_action_goto_"+(api_child_num)+"'>"
                html +='                                    <optgroup label="'+gettext('option_label_system')+'">'
                html +="                                        <option value='none' selected>"+ gettext("option_continue") +"</option>"
                html +="                                        <option value='__event_GET_STARTED'>"+ gettext("option_event_registration") +"</option>";
                html +="                                    </optgroup>"

                html +='                                    <optgroup label="'+gettext('option_label_blocks')+'">'
                for (var i = 0; i < api_response.data.length; i++) {
                    var block = api_response.data[i];
                    html +="                                    <option value='"+ block.id +"'>"+ block.name +"</option>";
                }
                html +="                                    </optgroup>"
                html +="                                </select>"

                html +="                                    </div>"
                html +="                                </div>"
                html +="                            </div>"
                html +="                        </div>"
                html +="                        <button type='button' class='add-quickreply-child message-bubble bubble-dashed'>+ "+ gettext("lbl_add_quickreply") +"</button>"
                html +="                    </div>"
                html +="                </div>"
                html +="            </div>"
                html +="          </div>"
                html +="      </div>";

                $("#apis").append(html);
                $("#apis").sortable('refresh');
                child_no_refresh();
                $(".option-bubble").hide(0);
            });
    }

function addQuickReplyChild() {
    var parent_name = $(this).parent().siblings(".input-child").attr("name").split('_')
    var api_child_num = Number(parent_name[parent_name.length - 1]);
    var sibling_input_child_name = $(this).siblings(".quick-replies").children(".quick-reply").last().attr("data-quickreply-child-id");

    var name_split = sibling_input_child_name.split('_');
    var reply_id = Number(name_split[name_split.length - 1]);

    // prevent more than 4 replies (LINE limitation)
    if (reply_id >= 4)
        return false

    var reply_container = $(this).siblings(".quick-replies")
    var selection = getApiData('message/block/list/')
    selection.done(function(api_response) {
        var html = "<div class='quick-reply anchor' data-quickreply-child-id="+(reply_id+1)+">"
        html +="                       <input type='text' class='input-child bubble-input' maxlength='20' value='' placeholder='Enter Reply Text' name='QuickReplySendMessage_title_"+(api_child_num)+"'>"
        html +="                       <div class='option-bubble bubble-white'>"
        html +="                           <div class='bubble-content'>"

        html +="                                <select class='input-child' name='QuickReplySendMessage_action_goto_"+(api_child_num)+"'>"
        html +='                                    <optgroup label="'+gettext('option_label_system')+'">'
        html +="                                        <option value='none' selected>"+ gettext("option_continue") +"</option>"
        html +="                                        <option value='__event_GET_STARTED'>"+ gettext("option_event_registration") +"</option>";
        html +="                                    </optgroup>"

        html +='                                    <optgroup label="'+gettext('option_label_blocks')+'">'
        for (var i = 0; i < api_response.data.length; i++) {
            var block = api_response.data[i];
            html +="                                    <option value='"+ block.id +"'>"+ block.name +"</option>";
        }
        html +="                                    </optgroup>"
        html +="                                </select>"

        html +="                           </div>"
        html +="                       </div>"
        html +="                   </div>";

        reply_container.append(html);
        $("#apis").sortable('refresh');
        child_no_refresh();
        $(".option-bubble").hide(0);
    })
}

function addWaitMessage() {
        var api_child_num = $(".api-child").length;

            var html = "     <div class='row api-child' data-id='"+(api_child_num+1)+"'>";
                html +="          <div class='col-md-12'>"
                html +="              <label><i class='ti-menu'></i></label>"
                html +="              <div class='vertical-align form-group'>"
                html +="                  <i class='ti-close'></i>"
                html +="                   <div class='bubble-input bubble-white range-slider anchor' data-api-child-id="+(api_child_num+1)+">"
                html +="                        "+ gettext('api_wait_description')
                html +="                        <input class='range-slider__range' type='range' value='100' min='0' max='500' name='WaitSendMessage_"+(api_child_num)+"'>"
                html +="                        <span class='range-slider__value'>0</span>"
                html +="                    </div>"
                html +="              </div>"
                html +="          </div>"
                html +="      </div>";

        $("#apis").append(html);
        $("#apis").sortable('refresh');
        child_no_refresh();
        rangeSlider();
    }

function addTagMessage(){
        var api_child_num = Number($(".api-child").length);

        var html = '<div class="row api-child" data-id="'+(api_child_num+1)+'">';
        html += '<div class="col-md-12">';
        html += '<div class="message-bubble">';
        html += '<div class="form-group">';
        html += '<label><i class="ti-menu"></i>&nbsp;</label><i class="ti-close"></i>';

        html += '<div class="message-img-thumbnail text-center"><i class="fa fa-user-plus fa-4x" aria-hidden="true"></i><i class="fa fa-tags fa-4x" aria-hidden="true"></i></div>';

        html += '<div class="form-inline horizontal-align bubble-white">';
        html += '<select class="input-child mb-2 mr-sm-2 mb-sm-0" name="TagSendMessage_'+(api_child_num)+'">';
        html += '<option value="add">'+gettext('option_add')+'</option>';
        html += '<option value="add">'+gettext('option_remove')+'</option>';
        html += '</select>';
        html += '<input type="text" class="form-control border-input input-child" placeholder="some tag name" name="TagSendMessage_'+(api_child_num)+'" maxlength="1000" required>';
        html += '</div>';
        html += '<small class="form-text text-muted">Max 1000 characters.</small>';
        html += '</div>';
        html += '</div>';
        html += '</div>';
        html += '</div>';

        $("#apis").append(html);
        $("#apis").sortable('refresh');
        child_no_refresh();
    }

        function addInputMessage(){
        var api_child_num = Number($(".api-child").length);

        var html = '<div class="row api-child" data-id="'+(api_child_num+1)+'">';
        html += '<div class="col-md-12">';
        html += '<div class="message-bubble">';
        html += '<div class="form-group">';
        html += '<label><i class="ti-menu"></i>&nbsp;</label><i class="ti-close"></i>';

        html += '<div class="message-img-thumbnail text-center"><i class="fa fa-keyboard-o fa-4x" aria-hidden="true"></i></div>';

        html += '<div class="form-inline horizontal-align bubble-white">';
        html += '<input type="text" class="form-control border-input" placeholder="'+gettext('placeholder_todo_question')+'" name="InputSendMessage_'+(api_child_num)+'" value="" maxlength="1000" required>';
        html += '<select name="InputSendMessage_'+(api_child_num)+'">';
        html += '<option value="email">'+gettext('option_email')+'</option>';
        html += '<option value="tel1">'+gettext('option_tel')+'</option>';
        html += '<option value="address1">'+gettext('option_address')+'</option>';
        html += '<option value="first_name">'+gettext('option_first_name')+'</option>';
        html += '<option value="last_name">'+gettext('option_last_name')+'</option>';
        html += '</select>';

        html += '</div>';

        html += '</div>';
        html += '</div>';
        html += '</div>';
        html += '</div>';

        $("#apis").append(html);
        $("#apis").sortable('refresh');
        child_no_refresh();
    }

        function addFormMessage(){
        var api_child_num = Number($(".api-child").length);

        var html = '<div class="row api-child" data-id="'+(api_child_num+1)+'">';
        html += '<div class="col-md-12">';
        html += '<div class="message-bubble">';
        html += '<div class="form-group">';
        html += '<label><i class="ti-menu"></i>&nbsp;</label><i class="ti-close"></i>';

        html += '<div class="message-img-thumbnail text-center"><i class="fa fa-keyboard-o fa-4x" aria-hidden="true"></i></div>';

        html += '<div class="form-group bubble-white p-4">';

        html += '<div class="col-md-12">';

        html += '<div class="row form-group">';
        html += '<input type="text" class="form-control border-input input-child" placeholder="'+gettext('placeholder_form_title')+'" name="FormSendMessage_'+(api_child_num)+'" value="" maxlength="1000" required>';
        html += '<input type="text" class="form-control border-input input-child" placeholder="'+gettext('placeholder_form_memo')+'" name="FormSendMessage_'+(api_child_num)+'" value="" maxlength="1000" required>';
        html += '</div>';

        html += '<div class="row form-group">';
        html += '<select class="input-child form-check-label form-inline" name=name="FormSendMessage_'+(api_child_num)+'">';

        html += '<option value="todo"> '+ gettext('lbl_form_todo_option') +'</option>';

        html += '</select>';
        html += '</div>';

        html += '<div class="form-questions">';

        html += '<div class="row form-question" data-form-child-id="0">';
        html += '<input type="text" class="form-control col-md-3 border-input input-child" placeholder="'+gettext('placeholder_form_attribute')+'" name="FormSendMessage_'+(api_child_num)+'" value="" maxlength="1000" required>';
        html += '<input type="text" class="form-control col-md-9 border-input input-child" placeholder="'+gettext('placeholder_form_question')+'" name="FormSendMessage_'+(api_child_num)+'" value="" maxlength="1000" required>';
        html += '</div>';

        html += '</div>';

        html += '<div class="row offset-md-4 p-4">';
        html +="                        <button type='button' class='add-form-child message-bubble bubble-dashed'>+ "+ gettext("lbl_add_form_question") +"</button>"
        html += '</div>';

        html += '</div>';

        html += '</div>';
        html += '</div>';
        html += '</div>';
        html += '</div>';

        $("#apis").append(html);
        $("#apis").sortable('refresh');
        child_no_refresh();
    }

    function addFormChild() {
    var parent_name = $(this).parent().siblings(".form-questions").children(".form-question").first().children().first().attr("name").split('_')
    var api_child_num = Number(parent_name[parent_name.length - 1]);
    var sibling_input_child_name = $(this).parent().siblings(".form-questions").children(".form-question").last().attr("data-form-child-id");

    var name_split = sibling_input_child_name.split('_');
    var reply_id = Number(name_split[name_split.length - 1]);

    var question_container = $(this).parent().siblings(".form-questions")
    var selection = getApiData('message/block/list/')
    selection.done(function(api_response) {
        var html = "<div class='row form-question' data-form-child-id="+(reply_id+1)+">"
        html += '<input type="text" class="form-control col-md-3 border-input input-child" placeholder="'+gettext('placeholder_form_attribute')+'" name="FormSendMessage_'+(api_child_num)+'" value="" maxlength="1000" required>';
        html += '<input type="text" class="form-control col-md-9 border-input input-child" placeholder="'+gettext('placeholder_form_question')+'" name="FormSendMessage_'+(api_child_num)+'" value="" maxlength="1000" required>';
        html += '</div>';

        question_container.append(html);
        $("#apis").sortable('refresh');
        child_no_refresh();
    })
}

function addGoToMessage() {
        console.log('debug testing goto adding');
        var api_child_num = $(".api-child").length;

            var selection = getApiData('message/block/list/')
            .done(function(api_response){
                var html = '<div class="row api-child" data-id="'+(api_child_num+1)+'">';
                html += '<div class="col-md-12">';
                html += '<div class="message-bubble">';
                html += '<div class="form-group">';
                html += '<label><i class="ti-menu"></i>&nbsp;</label><i class="ti-close"></i>';

                html += '<div class="message-img-thumbnail text-center"><i class="fa fa-arrow-right fa-4x" aria-hidden="true"></i></div>';
                html += '<div class="form-inline bubble-white">';
                html += '<div class="form-group mx-5">';

                html += '<label for="GoToMessage_'+(api_child_num)+'_block">'+gettext('lbl_goto_block')+'</label>'
                html +="                                <select id='GoToMessage_"+(api_child_num)+"_block' class='input-child ml-3' name='GoToMessage_"+(api_child_num)+"'>"
                html +='                                    <optgroup label="'+gettext('option_label_blocks')+'">'
                for (var i = 0; i < api_response.data.length; i++) {
                    var block = api_response.data[i];
                    html +="                                    <option value='"+ block.id +"'>"+ block.name +"</option>";
                }
                html +="                                    </optgroup>"
                html +="                                </select>"
                html +="                    </div>"

                html += '<div class="form-group mx-5">';
                html += '<label for="GoToMessage_'+(api_child_num)+'_step">'+gettext('lbl_goto_step')+'</label>'
                html +='<input type="number" id="GoToMessage_'+(api_child_num)+'_step" class="form-control ml-3 border-input input-child" placeholder="" name="GoToMessage_'+(api_child_num)+'" value=0 min="0" required>';
                html +="</div>"

                html +="                    </div>"
                html +="                </div>"
                html +="            </div>"
                html +="          </div>"
                html +="      </div>";

                $("#apis").append(html);
                $("#apis").sortable('refresh');
                child_no_refresh();
                $(".option-bubble").hide(0);
            });
    }

function dataIdRefresh() {
    var api_childs = $(".api-child");
    $.each(api_childs,function(i,child) {
        var data_id = i + 1;
        $(this).attr("data-id", data_id);
        var input_childs = $(this).find(".input-child");
            $.each(input_childs,function(j,input_child){
                var name = $(this).attr("name");
                var name_split = name.split('_');
                name_split[name_split.length - 1] = data_id;
                name_join = name_split.join("_");
                $(this).attr("name", name_join);
        });
    });
}

// Api Childの順番リフレッシュ
function child_no_refresh(){
        var api_childs = $(".api-child");
        $.each(api_childs,function(i,child){
            var input_childs = $(this).find(".input-child");
            $.each(input_childs,function(j,input_child){
                var name = $(this).attr("name");
                var name_split = name.split('_');
                name_split[name_split.length - 1] = i + 1;
                name_join = name_split.join("_");
                $(this).attr("name", name_join);
            });
        });
        autosize($('.expand'));
        dataIdRefresh();
    }

// Carousel Childの順番リフレッシュ
function carousel_child_no_refresh(carousel_child){
        var carousel_childs = carousel_child.parents(".carousel_columns").children();
        $.each(carousel_childs,function(i,child){
            var name = $(this).children("input:first").attr("name");
            var name_split = name.split('_');
            name_split[name_split.length - 1] = i + 1;
            name_join = name_split.join("_");

            $(this).children("input:first").attr("name", name_join);
        });
    }


