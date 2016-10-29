from flask import Flask,Blueprint,render_template,abort,redirect,url_for,request,session,jsonify
import os
from werkzeug import secure_filename
from functools import wraps
from jinja2 import TemplateNotFound
from Models.Model import db,Cursos,Unidades,Periodos,Disciplinas
from Models.Model import Areas,Professores,Turmas,Alunos,Faculdades,Modulos


aluno = Blueprint('aluno',__name__,template_folder='templates')

def force_auth():
	if not 'aluno-id' in session:
		abort(401)

aluno.before_request(force_auth)


@aluno.route("/aluno/")
def index():
	try:
		aluno = Alunos.query.filter(Alunos.id==session['aluno-id']).first()
		faculdade = db.session.query(Faculdades,Unidades,Turmas,Cursos).join(Unidades).join(Turmas).join(Cursos)
		return render_template("aluno/index.html",aluno=aluno,faculdade=faculdade)
	except TemplateNotFound:
		abort(404)

@aluno.route("/aluno/perfil/")
def perfil():
    try:		
        aluno = Alunos.query.filter(Alunos.id==session['aluno-id']).first()
        return "perfil do aluno"
    except TemplateNotFound:
        abort(404)

@aluno.route("/aluno/grupos/")
def aluno_grupos():
    try:		
        aluno = Alunos.query.filter(Alunos.id==session['aluno-id']).first()
        return render_template("aluno/grupos.html",aluno=aluno)
    except TemplateNotFound:
        abort(404)

@aluno.route("/aluno/grupos/<idgrupo>/")
def vergrupos(idgrupo):
    try:		
        aluno = Alunos.query.filter(Alunos.id==session['aluno-id']).first()
        return render_template("aluno/vergrupos.html",aluno=aluno)
    except TemplateNotFound:
        abort(404)

@aluno.route("/aluno/notas/")
def aluno_notas():
    try:		
        aluno = Alunos.query.filter(Alunos.id==session['aluno-id']).first()
        return render_template("aluno/notas.html",aluno=aluno)
    except TemplateNotFound:
        abort(404)		


@aluno.route("/aluno/trabalhos/")
def aluno_trabalhos():
    try:		
        aluno = Alunos.query.filter(Alunos.id==session['aluno-id']).first()
        return render_template("aluno/trabalhos.html",aluno=aluno)
    except TemplateNotFound:
        abort(404)			

@aluno.route("/aluno/historico/")
def aluno_historico():
    try:		
        aluno = Alunos.query.filter(Alunos.id==session['aluno-id']).first()
        return render_template("aluno/historico.html",aluno=aluno)
    except TemplateNotFound:
        abort(404)		

@aluno.route("/aluno/grade/")
def aluno_grade():
    try:		
        aluno = Alunos.query.filter(Alunos.id==session['aluno-id']).first()
        return render_template("aluno/grade.html",aluno=aluno)
    except TemplateNotFound:
        abort(404)						

@aluno.route("/aluno/forum/")
def aluno_forum():
    try:	
        aluno = Alunos.query.filter(Alunos.id==session['aluno-id']).first()	
        return render_template("aluno/forum.html",aluno=aluno)
    except TemplateNotFound:
        abort(404)	

@aluno.route("/aluno/forum/<idforum>/")
def verforum(idgrupo):
    try:		
        aluno = Alunos.query.filter(Alunos.id==session['aluno-id']).first()
        return render_template("aluno/verforum.html",aluno=aluno)
    except TemplateNotFound:
        abort(404)			

@aluno.route("/aluno/curso/<int:cursoid>/")
def aluno_curso(cursoid):
    try:		
        aluno = Alunos.query.filter(Alunos.id==session['aluno-id']).first()
        curso = db.session.query(Cursos).filter_by(id=cursoid)
        print curso
        return render_template("aluno/curso.html",curso=curso,aluno=aluno)
    except TemplateNotFound:
        abort(404)

@aluno.route("/aluno/perfil/foto/",methods=["POST"])
def aluno_upload():
    try:		
        foto = request.files['foto-perfil']
        foto.save(os.path.join("/srv/unisocial/static/imagens/alunos/",(str(session['aluno-id'])+".jpg")))
        return jsonify({"status":0,"message":"Foto alterada com sucesso!"})
    except Exception as e:
        return jsonify({"status":1,"message":"Falhou ao fazer o upload! %s"%e})
