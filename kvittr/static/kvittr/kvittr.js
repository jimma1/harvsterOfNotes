$(document).ready(function(){
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
});
