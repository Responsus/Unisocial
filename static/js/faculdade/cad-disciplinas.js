$(document).ready(function(){
    var faculdade_id = $("#faculdade-id").val();
	$.ajax({
                url:"/api/faculdade/"+faculdade_id+"/areas",
        })
        .done(function(data){
                for(i = 0; i < data.areas.length; i++){
                        $("#areas-disciplina").append("<option value='"+data.areas[i].id+"'>"+data.areas[i].nome+"</option>");
                }
        })
        .fail(function(data){
                console.log(data);
        })


	$("#cadastrar-disciplina").click(function(){
        var faculdade_id = $("#faculdade-id").val();
		var nome = $("#nome-disciplina").val();
		var descricao = $("#descricao-disciplina").val();
		var areas = $("#areas-disciplina").val();
		var areasstr = "";
		for(a = 0;a < areas.length;a++){
			areasstr += areas[a]+",";
		}
		areasstr = areasstr.substring(0,areasstr.length-1);
		$.ajax({
			type:"POST",
			url: "/api/faculdade/"+faculdade_id+"/disciplinas/",
			data: {"nome":nome,"descricao":descricao,"areas":areasstr}
		})
		.done(function(data){
			alert(data.message);
		})
		.fail(function(data){
			alert(data.message);
		})
	});

});
