from flask import Flask,Blueprint,jsonify,request,session,abort

from Classes.Professor import Professor as ProfessorClass
from Classes.Curso import Curso as CursoClass

Professor = Blueprint('Professor',__name__)

@Professor.route("/api/usuario/<int:usuarioid>/professor/",methods=["POST"])
def save(usuarioid):
    try:
        # form params
        novo = request.get_json()
        professor = ProfessorClass()
        for attr in novo.keys():
            setattr(professor,attr,novo.get(attr))
        response = professor.save()
        return jsonify(response)
    except Exception as e:
        return jsonify({"status":"1","message":"Nao foi possivel cadastrar o professor %s"%e})


@Professor.route("/api/usuario/<int:usuarioid>/professor/<int:professorid>/curso/<int:cursoid>/",methods=["POST"])
def add_professor_curso(usuarioid,professorid,cursoid):
    try:
        professor = ProfessorClass()
        professor.id = professorid
        professor = professor.select()
        curso = CursoClass()
        curso.id = cursoid
        curso = curso.select()
        response = professor.addCurso(curso)
        return jsonify(response)
    except Exception as e:
        return jsonify({"status":"1","message":"Nao foi possivel buscar lista de professores %s"%e})
