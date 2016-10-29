$(document).ready(function(){
    var faculdade_id = $("#faculdade-id").val();
	$.ajax({
		url:"/api/faculdade/"+faculdade_id+"/areas",
	})
	.done(function(data){
		for(i = 0; i < data.areas.length; i++){
			$("#areas").append("<option value='"+data.areas[i].id+"'>"+data.areas[i].nome+"</option>");
		}
	})
	.fail(function(data){
		console.log(data);
	})

	function getCursos(areaid,faculdade_id){
		$.ajax({
			url:"/api/faculdade/"+faculdade_id+"/areas/"+areaid+"/cursos/",
		})
		.done(function(data){
			for(i = 0; i < data.cursos.length; i++){
				$("#cursos").append("<option value='"+data.cursos[i].id+"'>"+data.cursos[i].nome+"</option>");
			}
		})
		.fail(function(data){
			console.log(data);
		})
	}

	$("#areas").change(function(){
		var areas = $(this).val();
        var faculdade_id = $("#faculdade-id").val();
		for(a=0;a<areas.length;a++){
			getCursos(areas[a],faculdade_id);		
		}
	});


	$("#cadastrar-unidades").click(function(){
        var faculdade_id = $("#faculdade-id").val();		
		var nomeunidade = $("#nome-unidade").val();
		var enderecounidade = $("#endereco-unidade").val();
		var descricaounidade = $("#descricao-unidade").val();
		var areas = $("#areas").val();
		var cursos = $("#cursos").val();
		var areasstr = "";
		var cursosstr  = "";
		for(a = 0;a < areas.length;a++){
			areasstr += areas[a]+",";
		}
		for(a = 0;a < cursos.length;a++){
			cursosstr += cursos[a]+",";
		}
		areasstr = areasstr.substring(0,areasstr.length-1);
		cursosstr = cursosstr.substring(0,cursosstr.length-1);

		$.ajax({
			url:"/api/faculdade/"+faculdade_id+"/unidades/",
			type: "POST",
			data:{"nome":nomeunidade,
					"endereco":enderecounidade,
					"descricao":descricaounidade,
					"area":areasstr,
					"curso":cursosstr}
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
