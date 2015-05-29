$(document).ready(function(){
    /*
    * Get crsf in cookie. Possible with jquery.cookie.js. 
    * Send token with ajax in header to verify.
    */ 
	var csrftoken = $.cookie('csrftoken');
    // increasing
    $(".class_increase_button").click(function(event){
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
            var element_id = "#id_increase_" + note_id;
            $(element_id).html(num_likes_updated)
        });
    });
    // decreasing
    $(".class_decrease_button").click(function(event){
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
            var element_id = "#id_increase_" + note_id;
            $(element_id).html(num_likes_updated)
        });
    });
});







































