$(document).ready(function(){
	$(".btn-excluir-unidade").each(function(){
        var faculdade_id = $("#faculdade-id").val();
		$(this).click(function(){
			console.log($(this));
			$.ajax({
				url: "/api/faculdade/"+faculdade_id+"/unidades/"+$(this).attr('id')+"/",
				type: "DELETE",			
			})
			.done(function(data){
				alert(data.message);
			})
			.fail(function(data){
				alert(data.message);
			})
		});
		
	})


    $(".btn-editar-unidade").each(function(){		
		$(this).click(function(){
            var id = $(this).attr("id");
            var faculdade_id = $("#faculdade-id").val();
            $.ajax({
                url: "/api/faculdade/"+faculdade_id+"/unidades/"+id+"/",
                type: "GET",                
            })
            .done(function(data){
                $("#areas-itens").html("");
                for(i=0;i<data.unidades.length;i++){                    
                    $("#unidade-id").html("ID: "+data.unidades[i].id);
                    $("#unidade-nome").html("Nome: "+data.unidades[i].nome);
                    $("#unidade-endereco").html("Endereço: "+data.unidades[i].endereco);                    
                    for(j=0;j<data.unidades[i].areas.length;j++){
                        $("#areas-itens").append("<a class='item'>"+data.unidades[i].areas[j].nome+"</a>");
                    }
                    $("#cursos-itens").html("");
                    for(k=0;k<data.unidades[i].cursos.length;k++){
                        $("#cursos-itens").append("<a class='item'>"+data.unidades[i].cursos[k].nome+"</a>");
                    }
                }
            })
            .fail(function(data){
                alert("Erro: "+data);
            })
    
            var faculdade_id = $("#faculdade-id").val();
            $.ajax({
                url: "/api/faculdade/"+faculdade_id+"/areas/",
                type: "GET",                
            })
            .done(function(data){
                $("#areas-faculdade-tab").html("");
                for(i=0;i<data.areas.length;i++){                                                            
                        $("#areas-faculdade-tab").append("<a class='item areas-faculdade-click' id='"+data.areas[i].id+"'>"+data.areas[i].nome+"</a>");
                }
                $(".areas-faculdade-click").each(function(){ 
                    $(this).click(function(){
                          var areaid = $(this).attr("id");
                          $(".areas-faculdade-click").removeClass("active");              
                          $(this).addClass("active");
                          var faculdade_id = $("#faculdade-id").val();
                          $.ajax({
                                url: "/api/faculdade/"+faculdade_id+"/areas/"+$(this).attr("id")+"/cursos/",
                                type: "GET",                
                            })
                            .done(function(data){
                                $("#lista-cursos-area").html("");
                                for(i=0;i<data.cursos.length;i++){                    
                                    $("#lista-cursos-area").append("<div class='item'><div class='right floated content'><div class='ui button add-curso-unidade' area='"+areaid+"' id='"+data.cursos[i].id+"'>Adicionar</div></div><div class='content'>"+data.cursos[i].nome+"</div></div>");
                                }
                                $(".add-curso-unidade").each(function(){
                                    $(this).click(function(){
                                        var curso = $(this).attr("id");
                                        var faculdade_id = $("#faculdade-id").val();
                                        $.ajax({
                                                url: "/api/faculdade/"+faculdade_id+"/unidades/"+id+"/cursos/",
                                                type: "POST",     
                                                data:{"curso":curso},           
                                            })
                                            .done(function(data){
                                                alert(data.message);
                                                
                                            })
                                            .fail(function(data){
                                                alert(data.message);
                                            })
                                        });
                                });
                            })
                            .fail(function(data){
                                alert("Erro: "+data);
                            })
                    });
                });
            })
            .fail(function(data){
                alert("Erro: "+data);
            })

			$('.first.modal').modal('show');			
		});

	})

    $(".coupled.modal").modal({
	        allowMultiple: true
        });

        $('.second.modal').modal('attach events',".first.modal .btn-incluir-curso-unidade");

});
