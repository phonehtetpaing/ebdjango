// Flowchart

$(function(){
    var chart_cnt = 0;
    var data = [];
    var chartdata = {
        operators : {}
    };
    var carousel_template_columns = [];
    var image_carousel_template_columns = [];

    // Create Event
    $(document).on("click", ".create", function(){
        var api = $(this).data("api");

        if( api == "TextSendMessage" ) {
            flowchart_operator_create("TextSendMessage", "テキスト", 1);
            var text = $(this).parent("form").children(".text").val();
            // DATA
            var apidata = {
                api : api,
                text : text,
                operator_id : operator_id
            };
            data.push(apidata);
        } else if( api = "CarouselTemplate" ) {
            var alt_text = $(this).parent("form").children(".alt_text").val();
            // DATA
            var apidata = {
                api : api,
                alt_text : alt_text,
                template : carousel_template_columns
            };
            data.push(apidata);
        }

        chart_cnt++;
    });

    // Add Event
    $(document).on("click", ".add", function(){
        var api = $(this).data("api");

        if( api == "CarouselTemplate" ) {
            var thumbnail_image_url = $(this).parent("form").children(".thumbnail_image_url").val();
            var title = $(this).parent("form").children(".title").val();
            var text = $(this).parent("form").children(".text").val();

            var actions = {
                PostbackTemplateAction : {
                    label : $(this).parent("form").children(".pta-label").val(),
                    text : $(this).parent("form").children(".pta-text").val(),
                    data : $(this).parent("form").children(".data").val()
                },
                MessageTemplateAction : {
                    label : $(this).parent("form").children(".mta-label").val(),
                    text : $(this).parent("form").children(".mta-text").val(),
                },
                URITemplateAction : {
                    label : $(this).parent("form").children(".uta-label").val(),
                    text : $(this).parent("form").children(".uri").val(),
                },
            }

            var column = {
                thumbnail_image_url : thumbnail_image_url,
                title : title,
                text : text,
                actions : actions
            }

            carousel_template_columns.push(column);

        } else if( api = "CarouselTemplate" ) {
        }
    });

    $(document).on("click", ".send", function(){
        sendJson(data);
    });

    // JSON送信
    function sendJson(data) {
        $.ajax({
            url : '/api/flow',
            type : 'POST',
            data : JSON.stringify(data)
        })
        .done(function(data){
            // TODO:正常終了時の処理を追加
        })
        .fail(function(data){
            // TODO:エラー時の処理を追加
        });
    };

    // フローチャート

    var $flowchart = $('#flowchart');
    $flowchart.flowchart({
      data: data
    });

    var flowchart_operator_create = function(label, title, outputs_num=1) {

        var operatorId = label + chart_cnt;
        var operatorData = {
            top: 20 + (100 * chart_cnt),
            left: 20,
            properties: {
                title: title,
                inputs: {
                    input_1: {
                        label: '前',
                    },
                },
                outputs : {

                }
            }
        }
        for(var i = 0; i<outputs_num; i++){
            operatorData["properties"]["outputs"]["output_" + i] = {
                label: '次',
            }
        }

        $flowchart.flowchart('createOperator', operatorId, operatorData);
    };

    var flowchart_operator_create_after = function(operatorId, operatorData, fullElement) {
        console.log(operatorId);
        console.log(operatorData);
        console.log(fullElement);
        return true;
    };



    $flowchart.siblings('.delete_selected_button').click(function() {
        $flowchart.flowchart('deleteSelected');
    });

    var $flowchart = $('#flowchart');
    $flowchart.flowchart({
      data: data,
      onOperatorCreate : flowchart_operator_create_after
    });

    // Controll Button Container Fixed

    $('div.main-panel').scroll(function(){
        if ($(this).scrollTop() >= 105) {
            $('.controll-container').addClass("fixed");
        } else {
            $('.controll-container').removeClass("fixed");
        }
    });

    // jQuery UI
    function refleshsortable() {
    }
    $('#apis').sortable({
		update: function(event, ui) {
		    child_no_refresh();
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
            $(this).parent().siblings(".carousel_columns").hide(200);
        } else if($(this).hasClass("ti-angle-up")) {
            $(this).removeClass("ti-angle-up");
            $(this).addClass("ti-angle-down");
            $(this).parent().siblings(".carousel_columns").show(200);
        }
    });

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

    // Api Child 要素追加
    $(".add-textsend").on("click", function(){
        var api_child_num = $(".api-child").length;

        var html = '<div class="row api-child">';
        html += '<div class="col-md-12">';
        html += '<div class="card">';
        html += '<div class="form-group">';
        html += '<label><i class="ti-menu"></i>&nbsp;'+ gettext('lbl_api_text_message') +'</label><i class="ti-close"></i>';
        html += '<textarea rows="5" class="form-control border-input input-child" style="height: auto" placeholder=" " name="TextSendMessage_0_'+(api_child_num+1)+'" maxlength="2000" required></textarea>';
        html += '<small class="form-text text-muted">Max 2000 characters.</small>';
        html += '</div>';
        html += '</div>';
        html += '</div>';
        html += '</div>';

        $("#apis").append(html);
        $("#apis").sortable('refresh');
        child_no_refresh();
    });

    $(".add-imgsend").on("click", function(){
        var api_child_num = $(".api-child").length;

        var html = '<div class="row api-child">';
        html += '<div class="col-md-4">';
        html += '<div class="card">';
        html += '<div class="form-group">';
        html += '<label><i class="ti-menu"></i>&nbsp;'+ gettext('lbl_api_image_message') +'</label><i class="ti-close"></i>';

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
    });

    $(".add-carouselsend").on("click", function(){
        var api_child_num = $(".api-child").length;

        var html = '<div class="row api-child">';
        html += '<div class="col-md-12">';
        html += '<div class="card">';
        html += '<div class="form-group">';
        html += '<label><i class="ti-menu"></i>&nbsp;'+ gettext('lbl_api_carousel_message') +'&nbsp;<i class="columns-toggle ti-angle-down"></i></label><i class="ti-close"></i>';
        html += '<input type="text" class="form-control border-input input-child" placeholder="https://example.com/original.jpg" name="CarouselTemplate_alt_text_0_'+(api_child_num+1)+'" value="" hidden>';
        html += '<div class="carousel_columns">';
        html += '</div>';

        html += '<div class="carousel_columns_control text-right">';
        html += '<button type="button" class="btn btn-info btn-fill btn-wd add-carousel-child"><i class="ti-plus"></i>&nbsp;'+ gettext('api_add_carousel_col') +'</button>';
        html += '</div>';

        html += '</div>';
        html += '</div>';
        html += '</div>';
        html += '</div>';

        $("#apis").append(html);
        $("#apis").sortable('refresh');
        child_no_refresh();
    });

    $(document).on("click", ".add-carousel-child", function(){
        var api_child_num = $(this).parent().siblings(".carousel_columns").children(".card").length;
        var sibling_input_child_name = $(this).parent().siblings(".input-child").attr("name");

        var name_split = sibling_input_child_name.split('_');
        var column_id = name_split[name_split.length - 1];

        // prevent more than 10 columns on carousel (LINE limitation)
        if (api_child_num >= 10)
            return false

        var html = '<div class="card api-child"><input type="hidden" name="CarouselTemplate_column_'+column_id+'_'+(api_child_num+1)+'">';
        html += '<div class="content">';

        html += '<div class="row"><i class="ti-close"></i>';
        html += '<div class="col-md-12">';
        html += '<div class="form-group">';
        html += '<label><i class="ti-menu"></i>&nbsp;'+ gettext("lbl_thumbnail") +'</label>';

        html += '<div class="message-img-thumbnail vertical-align"><div class="row"><div class="row col-md-12 text-center"><i class="fa fa-camera fa-5x" aria-hidden="true"></i></div><div class="row col-md-12 text-center">No Image Found</div></div></div>';

        html += '<input type="text" class="message-img-input form-control border-input" placeholder=" " name="column_thumbnail_image_url_'+column_id+'" value="" maxlength="1000" required>';
        html += '<small class="form-text text-muted">Max 1000 characters.</small>';
        html += '</div>';
        html += '</div>';
        html += '</div>';

        html += '<div class="row">';
        html += '<div class="col-md-12">';
        html += '<div class="form-group">';
        html += '<label>'+ gettext("lbl_title") +'</label>';
        html += '<input type="text" class="form-control border-input" placeholder="" name="column_title_'+column_id+'" value="" maxlength="40" required>';
        html += '<small class="form-text text-muted">Max 60 characters.</small>';
        html += '</div>';
        html += '</div>';
        html += '</div>';

        html += '<div class="row">';
        html += '<div class="col-md-12">';
        html += '<div class="form-group">';
        html += '<label>'+ gettext("lbl_text") +'</label>';
        html += '<input type="text" class="form-control border-input" placeholder="" name="column_text_'+column_id+'" value="" maxlength="60" required>';
        html += '<small class="form-text text-muted">Max 60 characters.</small>';
        html += '</div>';
        html += '</div>';
        html += '</div>';

        html += '<div class="row">';
        html += '<div class="col-md-12">';
        html += '<div class="form-group">';
        html += '<label>'+ gettext("lbl_action_url") +'</label>';
        html += '<input type="url" class="form-control border-input" placeholder=" " name="column_action_json_'+column_id+'" value="" maxlength="1000" required>';
        html += '<small class="form-text text-muted">Max 1000 characters.</small>';
        html += '</div>';
        html += '</div>';
        html += '</div>';

        html += '</div></div>';

        $(this).parent().siblings(".carousel_columns").append(html);
        $("#apis").sortable('refresh');
        child_no_refresh();
    });

    $(document).on("click", ".ti-close", function(){
        if(!confirm(gettext('dia-erase-confirm'))){
            return false;
        } else {
            $(this).closest(".api-child").remove();
            child_no_refresh();
        }
    });

    // update image previews
    $(function(){
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
    });
});