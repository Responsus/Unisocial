$(document).ready(function(){
    $("#cadastrar-curso-professor").click(function(){
        var curso_nome = $("#curso-nome").val();

    });

    $("#nova-aula-botao").click(function(){

            $("#aulas-curso-container").append("<div class='card'>  \
                <div class='content aula'> \
                    <div class='header'>Digite o titulo da aula</div> \
                    <div class='description'> \
                        Descreva o conteudo da aula \
                    </div> \
                </div> \
            </div>");
            return false;
    })


})
