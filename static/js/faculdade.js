$(document).ready(function(){
	console.log("Carregou o script");
	// aqui vai o id do elemento DOM
	// quando e id comeca com #
	// quando e class comecao com .
	$("#cadastrar-faculdade").click(function(){
		console.log("clicou no botao");
		alert("clicou no botao");
		var nomefaculdade = $("#faculdade.nome").val();
		var cnpjfaculdade = $("#faculdade.cnpj").val();
		var senhafaculdade = $("#faculdade.senha").val();
		$.post("/api/faculdade/",
			{nome:nomefaculdade,cnpj:cnpjfaculdade,senha:senhafaculdade}
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
