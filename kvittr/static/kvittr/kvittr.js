$(document).ready(function(){
	/*
	* Code from Django to get cookie and be on the safe side of csrf_token
	*/
	// using jQuery
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

	function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
	}
	$.ajaxSetup({
	    beforeSend: function(xhr, settings) {
	        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
	            xhr.setRequestHeader("X-CSRFToken", csrftoken);
	        }
	    }
	});
	// increase number of likes
	$("#increase_num_likes_thumb").click(function(event){
		event.preventDefault();
		$.ajax({
			method: "POST",
			url: $('#num_likes_url').val()
		})
		.done(function(data){
			var num_likes_updated = data['num_likes_updated'];
			$("$num_likes_div").html(num_likes_updated)
		})
	});
});
/*
$(document).ready(function() {

	function vote (noteID) {
		$.ajax({
			type: "POST",
			url: "/vote",
			data: {"note": noteID},
			success: function() {
				// vote only once 
				$("#note-vote-" + noteID).hide();
			},
			headers: {
				'X-CSRFToken': csrftoken;	
			}
		});
		// don't reload page 
		return false;
	}

	$("a.vote").click(function() {
		var noteID = parseInt(this.id.split("-")[2])
		return vote(noteID);
	})

});*/