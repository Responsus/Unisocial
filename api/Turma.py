from flask import Flask,Blueprint,jsonify,request,session,abort
# from ClassesDao.ModulosDao import ModulosDao
from Classes.Turma import Turma as TurmaClass
from Classes.Aula import Aula as AulaClass


Turma = Blueprint('Turma',__name__)

@Turma.route("/api/usuario/<int:usuarioid>/turma/",methods=["POST"])
def save(usuarioid):
    try:
        novo = request.get_json()
        turma = TurmaClass()
        for attr in novo.keys():
            setattr(turma,attr,novo.get(attr))
        response = turma.save()
        return jsonify(response)
    except Exception as e:
        return jsonify({"status":0,"message":"Falhou ao cadastrar Turma %s"%e})

@Turma.route("/api/usuario/<int:usuarioid>/Turmas/<int:Turmaid>/aulas/",methods=["POST"])
def save_Turma_aula(usuarioid,Turmaid):
    try:
        novo = request.get_json()
        aula = AulaClass()
        for attr in novo.keys():
            setattr(aula,attr,novo.get(attr))
        aula = aula.save()
        Turma = TurmaClass()
        Turma.id = Turmaid
        Turma = Turma.select()
        response = Turma.addAula(aula)
        return jsonify(response)
    except Exception as e:
        return jsonify({"status":0,"message":"Falhou ao buscar Turma %s"%e})

@Turma.route("/api/usuario/<int:usuarioid>/Turmas/<int:Turmaid>/aulas/",methods=["GET"])
def list_Turma_aula(usuarioid,Turmaid):
    try:
        Turma = TurmaClass()
        Turma.id = Turmaid
        Turma = Turma.select()
        response = Turma.listAula()
        return jsonify(response)
    except Exception as e:
        return jsonify({"status":0,"message":"Falhou ao buscar Turma %s"%e})
