from flask import Flask,Blueprint,jsonify,request,session,abort
from Classes.Usuario import Usuario as UsuarioClass

Usuario = Blueprint('Usuario',__name__)

# def force_auth():
#     if not 'id' in session:
#         abort(401)
#     elif int(session['id']) != int(request.url.split("/")[5]):
#         abort(401)

# Usuario.before_request(force_auth)


@Usuario.route("/api/usuario/",methods=["POST"])
def save():
    try:
        # form params
        usuario = UsuarioClass()
        novo = request.get_json()
        for attr in novo.keys():
            print attr
            # print novo.get(attr)
            setattr(usuario,attr,novo.get(attr))
        response = usuario.save()
        return jsonify(response)
    except Exception as e:
        return jsonify({"status":"1","message":"Nao foi possivel cadastrar o usuario %s"%e})


@Usuario.route("//faculdade/<int:faculdadeid>/Usuario/",methods=["GET"])
def list(faculdadeid):
    try:
        professordao = ProfessorDao()
        json_retorno = {"Usuario":[]}
        for p in professordao.list(faculdadeid):
            json_professor = {}
            json_professor["nome"] = p.nome
            json_professor["Aulas"] = [d.nome for d in p.Aulas ]
            json_retorno["Usuario"].append(json_professor)
        return jsonify(json_retorno)
    except Exception as e:
        return jsonify({"status":"1","message":"Nao foi possivel buscar lista de Usuario %s"%e})
