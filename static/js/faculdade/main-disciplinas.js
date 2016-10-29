$(document).ready(function(){
	$(".btn-excluir-disciplina").each(function(){
		
		$(this).click(function(){
			console.log($(this));
            var faculdade_id = $("#faculdade-id").val();
			$.ajax({
				url: "/api/faculdade/"+faculdade_id+"/disciplinas/"+$(this).attr('id')+"/",
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
