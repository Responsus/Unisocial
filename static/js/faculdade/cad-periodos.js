$(document).ready(function(){
	$("#cadastrar-periodo").click(function(){
        var faculdade_id = $("#faculdade-id").val();
		var nomeperiodo = $("#periodo-nome").val();
		var inicioperiodo = $("#periodo-inicio").val();
		var intervaloperiodo = $("#periodo-intervalo").val();
		var fimperiodo = $ ("#periodo-fim").val();
		console.log(nomeperiodo,inicioperiodo,intervaloperiodo,fimperiodo);
		$.ajax({
			type:"POST",
			url:"/api/faculdade/"+faculdade_id+"/periodos/",
			data: {"nome":nomeperiodo,"inicio":inicioperiodo,"intervalo":intervaloperiodo,"fim":fimperiodo}
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
