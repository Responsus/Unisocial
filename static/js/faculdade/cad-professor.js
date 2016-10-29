$(function(){
	

	$("#cadastrar-professor").click(function(){
		var nome = $("#professor-nome").val();
		var email = $("#professor-email").val();
		var rg = $("#professor-rg").val();
		var cpf = $("#professor-cpf").val();
		var celular = $("#professor-celular").val();
		var telefone = $("#professor-telefone").val();
		var facebook = $("#professor-facebook").val();
		var senha = $("#professor-senha").val();
		var areas = JSON.stringify($("#professor-areas").val());
		var disciplinas = JSON.stringify($("#professor-disciplinas").val());
		$.ajax({
			type:"POST",
			url:"/api/faculdade/1/professores/",
			data:{"nome":nome,"email":email,"rg":rg,
                  "cpf":cpf,"celular":celular,"telefone":telefone,
                  "facebook":facebook,"senha":senha,"areas":areas,"disciplinas":disciplinas}
                 })		
		.done(function(data){
			console.log(data);
			alert(data.message);
		})
		.fail(function(data){
			alert(data.message);
		})

	});
});
