$(document).ready(function(){

	function add_disciplina_modulo(curso_id){
		$(".add-disciplina-modulo").each(function(){
			$(this).click(function(){
				var moduloid = $(this).attr("id");
				$.ajax({
					url: "/api/faculdade/1/cursos/"+curso_id+"/",
					type: "GET",			
				})
				.done(function(data){
					$(".lista-todas-disciplinas").html("");
					for(i=0;i<data.cursos[0].disciplinas.length;i++){					
							$(".lista-todas-disciplinas").append("<div class='item'><div class='right floated content'><div class='ui green tiny button disciplina-modulo'  id='"+data.cursos[0].disciplinas[i].id+"'>Adicionar</div></div><div class='content'>"+data.cursos[0].disciplinas[i].nome+"</div></div>");
					}	
					
					$(".disciplina-modulo").each(function(){
						$(this).click(function(){
							var id_disciplina = $(this).attr("id");
							$.ajax({
								url: "/api/faculdade/1/cursos/"+curso_id+"/modulo/"+moduloid+"/disciplinas/",
								type: "POST",
								data: {"disciplinaid":id_disciplina}
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
					alert(data.message);
				})
			});
		
		});
	}

	function modal_curso(cursoid, callback){
		$.ajax({
				url: "/api/faculdade/1/cursos/"+cursoid+"/",
				type: "GET",			
			})
			.done(function(data){
				for(i=0;i<data.cursos.length;i++){
					$(".nome-curso").html(data.cursos[i].id+" - "+data.cursos[i].nome);
					$(".area-curso").html("Area: "+data.cursos[i].area);
					$(".tipo-curso").html("Tipo: "+data.cursos[i].tipo);
					$(".modulos-curso").html("Modulos: "+data.cursos[i].modulos.length);
					$(".lista-modulos").html("");
					for(j=0;j<data.cursos[i].modulos.length;j++){		
						var	disciplis = "";
						for(k=0;k<data.cursos[i].modulos[j].disciplinas.length;k++){
							disciplis += "<div class='menu'><a id='"+data.cursos[i].modulos[j].disciplinas[k].id+"' class='item remover-disciplina-modulo' >"+data.cursos[i].modulos[j].disciplinas[k].nome+"</a></div>";
						}
									
						$(".lista-modulos").append(
							"<div class='column'><div class='ui vertical menu'><div class='item'><div class='header' id='turma-id'>Modulo: "+data.cursos[i].modulos[j].nome+"</div>"+disciplis+"<div class='menu'><a id='"+data.cursos[i].modulos[j].id+"' class='item add-disciplina-modulo'><i class='plus green icon'></i>Adicionar Disciplina</a></div></div></div></div>"
						);
					}

				}
			$('.second.modal').modal('attach events',".first.modal .add-disciplina-modulo");
				add_disciplina_modulo(cursoid);
				//callback;
			})
			.fail(function(data){
				alert(data.message);
			})
	}

	$(".btn-excluir-curso").each(function(){
		
		$(this).click(function(){
			console.log($(this));
			$.ajax({
				url: "/api/faculdade/1/cursos/"+$(this).attr('id')+"/",
				type: "DELETE",			
			})
			.done(function(data){
				alert(data.message);
			})
			.fail(function(data){
				alert(data.message);
			})
		});
		
	});


	$(".coupled.modal").modal({
			allowMultiple: true
		});

		//$('.thirt.modal').modal('attach events',".first.modal .add-disciplina-modulo");

		$(".btn-editar-curso").each(function(){
			var id = $(this).attr("id");
			$(this).click(function(){
				modal_curso(id,$('.first.modal').modal('show'));				
			});

		})		


});
