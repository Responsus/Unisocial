$(document).ready(function(){
	$("#cadastrar-areas").click(function(){
		var nomearea = $("#area-nome").val();
        var faculdade_id = $("#faculdade-id").val()
		console.log(nomearea);
		$.ajax({
			type: "POST",
			url:"/api/faculdade/"+faculdade_id+"/areas/",
			data:{"nome":nomearea}
		})		
		.done(function(data){
			alert(data.message);
		})
		.fail(function(data){
			alert(data.message);
		})
		return false;

	});

});
