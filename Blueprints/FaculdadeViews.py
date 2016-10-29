from flask import Flask,Blueprint,render_template,abort,session
from sqlalchemy.sql import func
from Models.Model import db,Cursos,Unidades,Periodos,Disciplinas,Areas,Professores,Turmas,Alunos,Faculdades
from jinja2 import TemplateNotFound


faculdade = Blueprint('faculdade',__name__,template_folder='templates')


def force_auth():
	if not 'id' in session:
		abort(401)
	else:
		pass

faculdade.before_request(force_auth)

@faculdade.route("/faculdade/")
def index():
    try:
        turmas = db.session.query(Faculdades,Unidades,Turmas,Cursos,Periodos).join(Unidades).join(Turmas).join(Cursos).order_by(Turmas.id.desc()).group_by(Turmas.id,Faculdades.id,Unidades.id,Cursos.id,Periodos.id).filter(Faculdades.id==session['id'])
        faculdade = Faculdades.query.filter(Faculdades.id==session['id']).first()
        return render_template("faculdade/index.html",turmas=turmas,faculdade=faculdade)
    except TemplateNotFound:
        abort(404)


@faculdade.route("/faculdade/perfil/")
def perfil():
	try:
		return "perfil do faculdade"
	except TemplateNotFound:
		abort(404)

@faculdade.route("/faculdade/cursos/")
def cursos():
    try:
        cursos = db.session.query(Faculdades,Cursos,Areas).join(Areas).join(Cursos).filter(Faculdades.id==session['id'])
        faculdade = Faculdades.query.filter(Faculdades.id==session['id']).first()
        return render_template("faculdade/cursos.html",cursos=cursos,faculdade=faculdade)
    except TemplateNotFound:
        abort(404)

@faculdade.route("/faculdade/cursos/novo/")
def novo_curso():
    try:
        faculdade = Faculdades.query.filter(Faculdades.id==session['id']).first()
        return render_template("faculdade/novo_curso.html",faculdade=faculdade)
    except TemplateNotFound:
        abort(404)

@faculdade.route("/faculdade/disciplinas/")
def disciplinas():
    try:
        disciplinas = db.session.query(Faculdades,Areas,Disciplinas).join(Areas).join((Disciplinas,Areas.disciplinas)).group_by(Disciplinas.id,Faculdades.id,Areas.id).filter(Faculdades.id==session['id'])
	print "Faculdade logada: ",session["id"]
        faculdade = Faculdades.query.filter(Faculdades.id==session['id']).first()
        return render_template("faculdade/disciplinas.html",disciplinas=disciplinas,faculdade=faculdade)
    except TemplateNotFound:
        abort(404)

@faculdade.route("/faculdade/disciplinas/novo/")
def nova_disciplina():
    try:
        faculdade = Faculdades.query.filter(Faculdades.id==session['id']).first()
        return render_template("faculdade/nova_disciplina.html",faculdade=faculdade)
    except TemplateNotFound:
        abort(404)

@faculdade.route("/faculdade/professores/")
def professores():
    try:
        professores = Professores.query.all()
        faculdade = Faculdades.query.filter(Faculdades.id==session['id']).first()
        return render_template("faculdade/professores.html",professores=professores,faculdade=faculdade)
    except TemplateNotFound:
        abort(404)

@faculdade.route("/faculdade/professores/novo/")
def novo_professores():
    try:
        disciplinas = db.session.query(Faculdades,Areas,Disciplinas).join(Areas) \
                      .join((Disciplinas,Areas.disciplinas)).group_by(Disciplinas.id) \
                      .filter(Faculdades.id==session['id'])
        areas = db.session.query(Faculdades,Areas).join(Areas).filter(Faculdades.id==session['id'])
        faculdade = Faculdades.query.filter(Faculdades.id==session['id']).first()
        return render_template("faculdade/novo_professor.html",
                                areas=areas,
                                disciplinas=disciplinas,
                                faculdade=faculdade
                              )
    except TemplateNotFound:
        abort(404)

@faculdade.route("/faculdade/turmas/")
def turmas():
    try:
        turmas = db.session.query(Faculdades,Unidades,Turmas,Cursos,Periodos).join(Unidades).join((Turmas,Unidades.turmas)).join(Periodos).join(Cursos).filter(Faculdades.id==session['id'])
        faculdade = Faculdades.query.filter(Faculdades.id==session['id']).first()
        return render_template("faculdade/turmas.html",turmas=turmas,faculdade=faculdade)
    except TemplateNotFound:
        abort(404)

@faculdade.route("/faculdade/turmas/novo/")
def nova_turma():
    try:
        faculdade = Faculdades.query.filter(Faculdades.id==session['id']).first()
        return render_template("faculdade/nova_turma.html",faculdade=faculdade)
    except TemplateNotFound:
        abort(404)

@faculdade.route("/faculdade/areas/")
def areas():
    try:
        areas = db.session.query(Faculdades,Areas).join(Areas).filter(Faculdades.id==session['id'])
        faculdade = Faculdades.query.filter(Faculdades.id==session['id']).first()
        return render_template("faculdade/areas.html",areas=areas,faculdade=faculdade)
    except TemplateNotFound:
        abort(404)

@faculdade.route("/faculdade/unidades/")
def unidades():
    try:
        unidades = db.session.query(Faculdades,Unidades, func.count(Turmas.id)).join(Unidades).outerjoin(Turmas).group_by(Unidades.id,Faculdades.id).filter(Faculdades.id==session['id'])
        faculdade = Faculdades.query.filter(Faculdades.id==session['id']).first()
        return render_template("faculdade/unidades.html",unidades=unidades,faculdade=faculdade)
    except TemplateNotFound:
        abort(404)

@faculdade.route("/faculdade/unidades/novo/")
def nova_unidades():
    try:
        faculdade = Faculdades.query.filter(Faculdades.id==session['id']).first()
        return render_template("faculdade/nova_unidade.html",faculdade=faculdade)
    except TemplateNotFound:
        abort(404)

@faculdade.route("/faculdade/periodos/")
def periodos():
    try:
        periodos = db.session.query(Faculdades,Periodos).join(Periodos).filter(Faculdades.id==session['id'])
        faculdade = Faculdades.query.filter(Faculdades.id==session['id']).first()
        return render_template("faculdade/periodos.html",periodos=periodos,faculdade=faculdade)
    except TemplateNotFound:
        abort(404)

@faculdade.route("/faculdade/periodo/novo/")
def novo_periodo():
    try:
        faculdade = Faculdades.query.filter(Faculdades.id==session['id']).first()
        return render_template("faculdade/novo_periodo.html",faculdade=faculdade)
    except TemplateNotFound:
        abort(404)

@faculdade.route("/faculdade/area/novo/")
def nova_area():
    try:
        faculdade = Faculdades.query.filter(Faculdades.id==session['id']).first()
        return render_template("faculdade/nova_area.html",faculdade=faculdade)
    except TemplateNotFound:
        abort(404)		

@faculdade.route("/faculdade/alertas/")
def alertas():
    try:
        faculdade = Faculdades.query.filter(Faculdades.id==session['id']).first()
        return render_template("faculdade/alertas.html",faculdade=faculdade)
    except TemplateNotFound:
        abort(404)		

@faculdade.route("/faculdade/alertas/novo/")
def novo_alerta():
    try:
        faculdade = Faculdades.query.filter(Faculdades.id==session['id']).first()
        return render_template("faculdade/novo_alerta.html",idfaculdade=session['id'])
    except TemplateNotFound:
        abort(404)

@faculdade.route("/faculdade/cadastro/")
def cadastro():
    try:
        faculdade = Faculdades.query.filter(Faculdades.id==session['id']).first()
        return render_template("faculdade/cadastro.html",faculdade=faculdade)
    except TemplateNotFound:
        abort(404)			
		
