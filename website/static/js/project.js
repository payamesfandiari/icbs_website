/* Project specific Javascript goes here. */
$(function(){
    $('body').smoothScroll({
        delegateSelector: 'ul.navbar-nav a'
    });
    $('#load_timeline').submit(function (e) {
        $.post('/presentation/search/',$(this).serialize(),function(data){
            if(data.error){
                $('#results').html("<div class='alert-box alert radius'>"+data.error.query_n_id[0]+
                    " <a href='#' class='close'>&times;</a></div>");
            }else {
                console.log(data);
                $('#results').html(data.page);
                make_timeline(data.data);
            }

        });
        e.preventDefault();
    });

    function make_timeline(data){
        var json_obj_check = data.check ;
        var json_obj_loan = data.loan ;
        if(json_obj_check != null){
            var timeline_check = new TL.Timeline('timeline-embed-ch',
                json_obj_check,{"scale_factor" : 0.5,});
        }
        if(json_obj_loan != null){
            var timeline_loan = new TL.Timeline('timeline-embed-loan',
                json_obj_loan,{"scale_factor" : 0.5,});
        }
        $('.tl-text').css({
            "direction" : "rtl",
            "text-align" : "right",
        });
    }
    $window = $(window);
    winH = $window.height();
    winH = winH - 150;
    var msgDiv = $('.messages');
    if(msgDiv){
        msgDiv.css('margin-top',winH+'px');
    }



});
$(document).foundation();
