from flask import Flask,Blueprint,jsonify,request,session,abort
# from ClassesDao.ModulosDao import ModulosDao
from Classes.Curso import Curso as CursoClass
from Classes.Aula import Aula as AulaClass


Curso = Blueprint('Curso',__name__)

@Curso.route("/api/usuario/<int:usuarioid>/cursos/",methods=["POST"])
def save(usuarioid):
    try:
        novo = request.get_json()
        curso = CursoClass()
        for attr in novo.keys():
            setattr(curso,attr,novo.get(attr))
        curso.usuario_id = usuarioid
        response = curso.save()
        return jsonify(response)
    except Exception as e:
        return jsonify({"status":0,"message":"Falhou ao cadastrar curso %s"%e})

@Curso.route("/api/usuario/<int:usuarioid>/cursos/<int:cursoid>/aulas/",methods=["POST"])
def save_curso_aula(usuarioid,cursoid):
    try:
        novo = request.get_json()
        aula = AulaClass()
        for attr in novo.keys():
            setattr(aula,attr,novo.get(attr))
        aula = aula.save()
        curso = CursoClass()
        curso.id = cursoid
        curso = curso.select()
        response = curso.addAula(aula)
        return jsonify(response)
    except Exception as e:
        return jsonify({"status":0,"message":"Falhou ao buscar curso %s"%e})

@Curso.route("/api/usuario/<int:usuarioid>/cursos/<int:cursoid>/aulas/",methods=["GET"])
def list_curso_aula(usuarioid,cursoid):
    try:
        curso = CursoClass()
        curso.id = cursoid
        curso = curso.select()
        response = curso.listAula()
        return jsonify(response)
    except Exception as e:
        return jsonify({"status":0,"message":"Falhou ao buscar curso %s"%e})
