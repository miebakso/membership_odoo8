$(document).ready(function() {
	
	$("#active_tab").click(function(){
		var state = $(this).data("state");
		$("#activated").empty();
	    $.ajax({
	        url: "mypurchases/"+state,
	        type: "GET",
	        dataType: 'html',
	        traditional: true,
	        success: function(response){
				$("#activated").html(response);
	        },
	        error: function(data){
	            $("#activated").append('<h1>Tidak mempunyai voucher</h1>');
	        }
	    });
	});
	$("#used_tab").click(function(){
	   var state = $(this).data("state");
		$("#activated").empty();
	    $.ajax({
	        url: "mypurchases/"+state,
	        type: "GET",
	        dataType: 'html',
	        traditional: true,
	        success: function(response){
				$("#activated").html(response);
	        },
	        error: function(data){
	            $("#activated").append('<h1>Tidak mempunyai voucher</h1>');
	        }
	    });
	});
	$("#expired_tab").click(function(){
	   var state = $(this).data("state");
		$("#activated").empty();
	    $.ajax({
	        url: "mypurchases/"+state,
	        type: "GET",
	        dataType: 'html',
	        traditional: true,
	        success: function(response){
				$("#activated").html(response);
	        },
	        error: function(data){
	            $("#activated").append('<h1>Tidak mempunyai voucher</h1>');
	        }
	    });
	});
	$(".see_details").click(function(){
		var obj = $(this);
		var state = obj.data("state");
	    $.ajax({
	        url: "vouchers/"+parseInt(state),
	        type: "GET",
	        dataType: 'html',
	        traditional: true,
	        success: function(response){
	        	$('.description').hide();
	        	$(".see_details").show();
	        	obj.hide();
				obj.parent().parent().parent().parent().parent().append(response);
				$(".btn_collapse").click(function(){
					alert('asdf');
			    	$('.description').hide();
			    	$(".see_details").show();
				});        
	        },
	        error: function(data){
	            $("#list_of_vouchers").append('<h1>Tidak mempunyai voucher</h1>');
	        }
	    });
	});
});

