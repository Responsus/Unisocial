$(document).ready(function(){
    var faculdade_id = $("#faculdade-id").val();
	$.ajax({
		url:"/api/faculdade/"+faculdade_id+"/unidades",
	})
	.done(function(data){
		for(i = 0; i < data.unidades.length; i++){
			$("#unidade").append("<option value='"+data.unidades[i].id+"'>"+data.unidades[i].nome+"</option>");
		}
	})
	.fail(function(data){
		console.log(data);
	})

    $.ajax({
		url:"/api/faculdade/"+faculdade_id+"/periodos",
	})
	.done(function(data){
		for(i = 0; i < data.periodos.length; i++){
			$("#periodo").append("<option value='"+data.periodos[i].id+"'>"+data.periodos[i].nome+"</option>");
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
			$("#curso").html("");
            $("#curso").append("<option value=''>Selecione um Curso</option>");
			for(i = 0; i < data.cursos.length; i++){
				$("#curso").append("<option value='"+data.cursos[i].id+"'>"+data.cursos[i].nome+"</option>");
			}
		})
		.fail(function(data){
			console.log(data);
		})
	}

    function getModulos(cursoid,faculdade_id){
		$.ajax({
			url:"/api/faculdade/"+faculdade_id+"/cursos/"+cursoid+"/",
		})
		.done(function(data){
			$("#modulo").html("");
			for(i = 0; i < data.cursos.length; i++){
                for(j = 0; j < data.cursos[i].modulos.length;j++){
                    $("#modulo").append("<option value='"+data.cursos[i].modulos[j].id+"'>"+data.cursos[i].modulos[j].nome+"</option>");
                }
			}
		})
		.fail(function(data){
			console.log(data);
		})
	}

	function getUnidadeAreas(unidade,faculdade_id){
		$.ajax({
			url:"/api/faculdade/"+faculdade_id+"/unidades/"+unidade+"/",
		})
		.done(function(data){
			$("#area").html("");
            $("#area").append("<option value=''>Selecione uma Area</option>");
			for(i = 0; i < data.unidades[0].areas.length; i++){
				$("#area").append("<option value='"+data.unidades[0].areas[i].id+"'>"+data.unidades[0].areas[i].nome+"</option>");
			}
		})
		.fail(function(data){
			console.log(data);
		})
	}
	
	$("#unidade").change(function(){
        var faculdade_id = $("#faculdade-id").val();
		var unidade = $(this).val();
		getUnidadeAreas(unidade,faculdade_id);		
	});

	$("#area").change(function(){
        var faculdade_id = $("#faculdade-id").val();
		var areas = $(this).val();
		getCursos(areas,faculdade_id);		
	});

    $("#curso").change(function(){
        var faculdade_id = $("#faculdade-id").val();
		var curso = $(this).val();
        console.log("Buscando Modulos");
		getModulos(curso,faculdade_id);		
	});

	$("#cadastrar-turmas").click(function(){
		var unidade = $("#unidade").val();
		var area = $("#area").val();
		var curso = $("#curso").val();
		var periodo = $("#periodo").val();
		var qtdalunos = $("#qtdalunos").val();
		var datainicio = $("#data-inicio").val();
		var datafim = $("#data-fim").val();
        var faculdade_id = $("#faculdade-id").val();
        var modulo = $("#modulo").val();
		console.log(unidade,area,curso,periodo,qtdalunos,datainicio,datafim);
		$.ajax({
			url:"/api/faculdade/"+faculdade_id+"/turmas/",
			type: "POST",
			data:{"unidade":unidade,"area":area,"curso":curso,
					"periodo":periodo,"qtdalunos":qtdalunos,"modulo":modulo,
					"datainicio":datainicio,"datafim":datafim}
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
