$(document).ready(function(){
    /*
    * Get crsf in cookie. Possible with jquery.cookie.js. 
    * Send token with ajax in header to verify.
    * First part of code works on detailnote.html
    */ 
	var csrftoken = $.cookie('csrftoken');
	// increase number of likes
 	$("#increase_num_likes_thumb").click(function(event){
 		event.preventDefault();
 		$.ajax({
 			method: "POST",
 			url: $('#num_likes_url').val(),
 			headers: { 'X-CSRFToken': $.cookie('csrftoken') }
 		})
 		.done(function(data){
 			var num_likes_updated = data['num_likes_updated'];
 			$("#num_likes_div").html(num_likes_updated)
 		})
 	});
    // descreasing likes    
    $("#decrease_num_likes_thumb").click(function(event){
        event.preventDefault();
        $.ajax({
            method: "POST",
            url: $('#decrease_num_likes_url').val(),
            headers: { 'X-CSRFToken': $.cookie('csrftoken') }
        })
        .done(function(data){
            var num_likes_updated = data['num_likes_updated'];
            $("#num_likes_div").html(num_likes_updated)
        })
    });

    /*
    * Increasing likes on index.html
    */
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

});







































