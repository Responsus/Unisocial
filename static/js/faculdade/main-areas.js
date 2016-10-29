$(document).ready(function(){
	$(".btn-excluir-areas").each(function(){

		$(this).click(function(){
            var faculdade_id = $("#faculdade-id").val();
			console.log($(this));
			$.ajax({
				url: "/api/faculdade/"+faculdade_id+"/areas/"+$(this).attr('id')+"/",
				type: "DELETE",			
			})
			.done(function(data){
				alert(data.message);
			})
			.fail(function(data){
				alert(data.message);
			})
		});
		
	})

});
