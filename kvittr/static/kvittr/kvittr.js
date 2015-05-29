$(document).ready(function(){
    /*
    * Get crsf in cookie. Possible with jquery.cookie.js. 
    * Send token with ajax in header to verify.
    */ 
	var csrftoken = $.cookie('csrftoken');
    // increasing
    $(".increase").click(function(event){
        event.preventDefault();
        var note_id = $(this).data("noteid");
        var href = "/notes/" + note_id + "/increase_num_likes/"; 
        $.ajax({
            method: "POST",
            url: href,
            headers: { 'X-CSRFToken': $.cookie('csrftoken') }
        })
        .done(function(data){
            var num_likes_updated = data['num_likes_updated'];
            var element_id = "#likes_" + note_id;
            $(element_id).html(num_likes_updated)
        });
    });
    // decreasing
    $(".decrease").click(function(event){
        event.preventDefault();
        var note_id = $(this).data("noteid");
        var href = "/notes/" + note_id + "/decrease_num_likes/"; 
        $.ajax({
            method: "POST",
            url: href,
            headers: { 'X-CSRFToken': $.cookie('csrftoken') }
        })
        .done(function(data){
            var num_likes_updated = data['num_likes_updated'];
            var element_id = "#likes_" + note_id;
            $(element_id).html(num_likes_updated)
        });
    });
});







































