$(function() {

	// Submit comment on submit
	$('#comment-form').on('submit', function(event){
	    event.preventDefault();
	    createPost();
	});

	// AJAX for posting
	function createPost() {
	    $.ajax({
	        url : "comment/", // the endpoint
	        type : "POST", // http method
	        data : { comment : $('#comment-text').val() }, // data sent with the post request

	        // handle a successful response
	        success : function(json) {
	            $('#comment-text').val(''); // remove the value from the input
	            loadComments(1, 1);
	        },

	        // handle a non-successful response
	        error : function(xhr,errmsg,err) {
	            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
	                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
	            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
	        }
	    });
	};

    // This function gets cookie with a given name
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    /*
    The functions below will create a header with csrftoken
    */

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    function sameOrigin(url) {
        // test that a given url is a same-origin URL
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                // Send the token to same-origin, relative URLs only.
                // Send the token only if the method warrants CSRF protection
                // Using the CSRFToken value acquired earlier
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });


    /*
    Auto refresh post comments
    */

    function updateComments(json) {
        var div = '';
        var ids = json['comment_ids'];
        var authors = json['comment_authors'];
        var texts = json['comment_texts'];

        for (var i = 0; i < ids.length; i++) {
            div += `<div id="comment-` + ids[i] + `" class="row">
                    <div class="col-xs-3 col-md-3 comment-author"><b>` + authors[i] + `</b></div>
                    <div class="col-xs-9 col-md-9 comment-text">` + texts[i] + `</div>
                </div><hr>`
        }
        $('#comments-list').html(div);
    }

    function loadComments(times, interval){
        var x = 0;
        var intervalID = setInterval(function () {
            $.ajax({
                url : "list-comments/", // the endpoint
                type : "POST", // http method

                // handle a successful response
                success : function(json) {
                    updateComments(json);
                },

                // handle a non-successful response
                error : function(xhr,errmsg,err) {
                    console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
                }
            });

            if (++x === times) {
               window.clearInterval(intervalID);
            }
        }, interval * 1000);
    }

    $(document).ready(function() {
        setTimeout(function() {loadComments(5,5)}, 5000)
        setTimeout(function() {loadComments(5,10)}, 60000);
        setTimeout(function() {loadComments(5,60)}, 60000);
    });
});
