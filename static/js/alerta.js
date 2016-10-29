$(document).ready(function(){
	console.log("Carregou o script");
	$("#cadastrar-alerta").click(function(){
		console.log("clicou no botao");
		alert("clicou no botao");
		var alertanome = $("#alerta.nome").val();
		var alertaconteudo = $("#alerta.conteudo").val();
		var alertainico = $("#alerta.inicio").val();
		var alertafim = $("#alerta.fim").val();
		$.post("/api/faculdade/alertas/",
			{nome:alertanome,conteudo:alertaconteudo,inicio:alertainicio,fim:alertafim}
		)		
		.done(function(data){
			alert(data.message);
		})
		.fail(function(data){
			alert(data.message);
		})
		return false;

	});

});
