$(function(){

$("#contato-unisocial").click(function(){
        var nome = $("#nome").val();
        var email = $("#email").val();
        var msg = $("#mensagem").val() ;
        var assunto = "Quero saber mais sobre o UniSocial! "+nome;
        $("#msg-alert").html("Aguarde enquando o email esta sendo enviado...");
        $.ajax({
            url:"/send/email/",
            type:"post",
            data: {"mensagem":msg,"nome":nome,"email":email,"assunto":assunto}
        })
        .done(function(data){
            $("#msg-alert").html(data.message);
        })
        .fail(function(data){
            alert(data.message);  
        })
        .always(function(){
            //$("#myModal").modal("hide");
        })
        
    })

});
