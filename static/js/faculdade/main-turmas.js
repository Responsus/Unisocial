$(document).ready(function(){
	function carregar_alunos_turma(turmaid,callback){
		$("#turma-clicada-id").val(turmaid);
        var faculdade_id = $("#faculdade-id").val();
		$.ajax({
				url: "/api/faculdade/"+faculdade_id+"/turmas/"+turmaid+"/",
				type: "GET",			
			})
			.done(function(data){
				$(".lista-alunos").html("");
				for(i=0;i<data.turmas[0].alunos.length;i++){
					$(".lista-alunos").append(
						"<div class='item'><div class='right floated content'><div class='ui red tiny button'>Remover</div></div><img class='ui avatar image' src='/static/imagens/alunos/"+data.turmas[0].alunos[i].id+".jpg'><div class='content'>"+data.turmas[0].alunos[i].nome+"</div></div>"

					);
				}
					$("#turma-id").html("Turma: "+data.turmas[0].id);
					$("#periodo-nome").html("Periodo: "+data.turmas[0].periodo);
					$("#curso-nome").html("Curso: "+data.turmas[0].curso);
					$("#unidade-nome").html("Unidade: "+data.turmas[0].unidade);
					$("#data-inicio").html("Data de Inicio: "+data.turmas[0].data_inicio);
					$("#data-fim").html("Data de Fim: "+data.turmas[0].data_fim);
					$("#modulo").html("Modulo: "+data.turmas[0].modulo.nome);
					$("#modulo-id").val(data.turmas[0].modulo.id);
					callback();
			})
			.fail(function(data){
				console.log(data);
			})
	}


	function carregar_alunos_por_nome(palavra){
        var faculdade_id = $("#faculdade-id").val();
		$.ajax({
				url: "/api/faculdade/"+faculdade_id+"/alunos/",
				type: "GET",			
			})
			.done(function(data){				
				$(".novos-alunos").html("");
				for(i=0;i<data.alunos.length;i++){					
					if (data.alunos[i].nome.toLowerCase().indexOf(palavra) >= 0){							
							$(".novos-alunos").append("<div class='item'><div class='right floated content'><div class='ui green tiny button incluir-aluno' id='"+data.alunos[i].id+"'>Adicionar</div></div><img class='ui avatar image' src='/static/imagens/alunos/"+data.alunos[i].id+".jpg'><div class='content'>"+data.alunos[i].nome+" - RG "+data.alunos[i].rg+"</div></div>");
					   }	
				}		
				$(".incluir-aluno").each(function(){
						turmaid = $("#turma-clicada-id").val();
						$(this).click(function(){
                            var faculdade_id = $("#faculdade-id").val();
							$.ajax({
								url: "/api/faculdade/"+faculdade_id+"/turmas/"+turmaid+"/aluno/"+$(this).attr('id')+"/",
								type: "POST",			
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
					alert(data);
				})	
	
	}

	$(".btn-excluir-turma").each(function(){
		
		$(this).click(function(){
			console.log($(this));
            var faculdade_id = $("#faculdade-id").val();
			$.ajax({
				url: "/api/faculdade/"+faculdade_id+"/turmas/"+$(this).attr('id')+"/",
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


	$(".coupled.modal").modal({
		allowMultiple: true
	});

    $('.second.modal').modal('attach events',".first.modal .add-aluno-turma");
	$('.thirt.modal').modal('attach events',".first.modal .alterar-grade-button");

	$(".btn-editar-turma").each(function(){
		var id = $(this).attr("id");
		$(this).click(function(){
    		$("#turma-curso-id").val($(this).attr("curso"));
			carregar_alunos_turma(id,$('.first.modal').modal('show'));			
		});

	})

	$(".nome-aluno-buscar").keyup(function(){
		console.log($(this).val());
		carregar_alunos_por_nome($(this).val());
	});
	
	$(".alterar-grade-button").each(function(){
		$(this).click(function(){
            var faculdade_id = $("#faculdade-id").val();
			$.ajax({
				url: "/api/faculdade/"+faculdade_id+"/cursos/"+$("#turma-curso-id").val()+"/",
				type: "GET",			
			})
			.done(function(data){
				$(".tabela-disciplinas").html("");
                var select_box = "<select class='ui fluid dropdown professores-disciplinas'>"+option_select+"</select>";	
                var option_select = "";
                 $.ajax({
				url: "/api/faculdade/"+faculdade_id+"/professores/",
				type: "GET",			
			    })
			    .done(function(data){
		            for(var i=0;i<data.professores.length;i++){
                        $(".professores-disciplinas").append("<option>"+data.professores[i].nome+"</option>");
                     }					
			    })
			    .fail(function(data){
				    alert(data);
			    })

				for(i=0;i < data.cursos[0].disciplinas.length;i++){
					$(".tabela-disciplinas").append(
						"<tr><td>"+data.cursos[0].disciplinas[i].nome+"</td><td><select class='ui dropdown'><option>Segunda Feira</option><option>Terça Feira</option><option>Quarta Feira</option><option>Quinta Feira</option><option>Sexta Feira</option><option>Sábado</option><option>Domingo</option></select></td><td>21:00</td><td>42</td><td>"+select_box+"</td></tr>"
					);
				}
			})
			.fail(function(data){
				alert(data.message);
			})
		});
		
	});

});
