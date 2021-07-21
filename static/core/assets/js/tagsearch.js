// Tag Search

$(function(){
    // checkboxのchangeイベントで発火
    $('#js-tagsearch-form input[type="checkbox"]').on("change", function(){
        // ローディングGIF表示
        var h = $(window).height();
        $('#loader-bg ,#loader').height(h).css('display','block');

        // API実行
        var queryData = $('#js-tagsearch-form').serialize();

        response = getUserListApi(queryData);
       
        // リクエスト用のページ数更新
        $('#js-tagsearch-form input[name="page"]').val(response.page);

        // ユーザ・リスト更新
        renderUserList(response.users);
        // タグ・リスト更新
        renderTagList(response.tag_list);

        // ページネーション更新
//        $(".pager").remove();
//        $(".js-paginate-table").paginate({
//            rows: 10,
//        });

        // ローディングGIF非表示
        $('#loader-bg ,#loader').css('display','none');
    });

    // ユーザリストを取得
    function getUserListApi(data) {
        var result = $.ajax({
            url : '/api/tagged_end_users/',
            type : 'GET',
            data : data,
            dataType: 'json',
            async: false
        })
        .done(function(data){
//             console.log("SUCCESS!");
//             console.log(data);
        })
        .fail(function(data){
//             console.log("ERROR!");
//             console.log(data);
        });

        return result.responseJSON;
    };

    // ユーザリストを描画
    function renderUserList(userList) {
        var tbody = $('#js-tagsearch-result');
        tbody.html('');
        var sendbutton = $('#js-tagsearch-buttom-result')
        sendbutton.html('');

        userList.forEach(function(val){
            tbody.append('<input type="hidden" name="suser[]" value=' + val.id + ' />');
            tbody.append(
                $('<tr>')
                    .append('<td>'+val.id+'</td>')
                    .append('<td>'+val.first_name+' '+val.last_name+'</td>')
                    .append('<td><a href="' + val.href_url_detail + '" class="badge badge-info btn-fill btn-wd"><i class="glyphicon glyphicon-pencil" aria-hidden="true"></i>&nbsp;details</a></td>')
                );

            sendbutton.append('<button type="submit" class="btn btn-info btn-fill btn-wd">SEND MESSAGE</button>');
        });
    };

    // タグリストを描画（hidden）
    function renderTagList(tagList) {
        var tag_div = $('#js-tagsearch-tag-list');
        tag_div.html('');
        tagList.forEach(function(val){
            tag_div.append('<input type="hidden" name="tag[]" value=' + val + ' />')
        });
    };
});