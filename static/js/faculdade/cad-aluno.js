$(document).ready(function(){
	

	$("#cadastrar-aluno").click(function(){
		var nome = $("#aluno-nome").val();
		var email = $("#aluno-email").val();
		var rg = $("#aluno-rg").val();
		var cpf = $("#aluno-cpf").val();
		var celular = $("#aluno-celular").val();
		var telefone = $("#aluno-telefone").val();
		var facebook = $("#aluno-facebook").val();
		var senha = $("#aluno-senha").val();

		$.ajax({
			type:"POST",
			url:"/api/faculdade/1/alunos/",
			data:{"nome":nome,"email":email,"rg":rg,"cpf":cpf,"celular":celular,"telefone":telefone,"facebook":facebook,"senha":senha}
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
