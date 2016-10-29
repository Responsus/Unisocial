$(document).ready(function(){
    var faculdade_id = $("#faculdade-id").val();
	$.ajax({
		url:"/api/faculdade/"+faculdade_id+"/areas",
	})
	.done(function(data){
		for(i = 0; i < data.areas.length; i++){
			$("#area-curso").append("<option value='"+data.areas[i].id+"'>"+data.areas[i].nome+"</option>");
		}
	})
	.fail(function(data){
		console.log(data);
	})

	$.ajax({
		url:"/api/faculdade/"+faculdade_id+"/tipos",
	})
	.done(function(data){
		for(i = 0; i < data.tipos.length; i++){
			$("#tipos-curso").append("<option value='"+data.tipos[i].id+"'>"+data.tipos[i].nome+"</option>");
		}
	})
	.fail(function(data){
		console.log(data);
	})

	$("#area-curso").change(function(){
		$("#disciplinas-curso").html("");
		$("#disciplinas-curso").nextAll("a").remove();
        var faculdade_id = $("#faculdade-id").val();
		$.ajax({
			url:"/api/faculdade/"+faculdade_id+"/areas/"+$(this).val()+"/disciplinas/",
		})
		.done(function(data){
			for(i = 0; i < data.disciplinas.length; i++){
				$("#disciplinas-curso").append("<option value='"+data.disciplinas[i].id+"'>"+data.disciplinas[i].nome+"</option>");
			}
		})
		.fail(function(data){
			console.log(data);
		})
	});

	$("#cadastrar-curso").click(function(){
		var nomecurso = $("#nome-curso").val();
		var descricaocurso = $("#descricao-curso").val();
		var area = $("#area-curso").val();
		var tiposcurso = $("#tipos-curso").val();
		var disciplinascurso = $("#disciplinas-curso").val();
		var qtdmodulos = $("#qtd-modulos").val();
		var strdisciplinas = "";
		for(i=0;i<disciplinascurso.length;i++){
			strdisciplinas += disciplinascurso[i]+",";
		}
		strdisciplinas = strdisciplinas.substring(0,strdisciplinas.length-1);
        var faculdade_id = $("#faculdade-id").val();
		$.ajax({
			type:"POST",
			url:"/api/faculdade/"+faculdade_id+"/cursos/",
			data:{"nome":nomecurso,"descricao":descricaocurso,"area":area,"tipo":tiposcurso,"disciplinas":strdisciplinas,"modulos":qtdmodulos}
		})		
		.done(function(data){
			alert(data.message);
		})
		.fail(function(data){
			alert(data.message);
		})

	});
});
