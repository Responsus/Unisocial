from flask import Flask,Blueprint,render_template,abort
from jinja2 import TemplateNotFound


professor = Blueprint('professor',__name__,template_folder='templates')
@professor.route('/',defaults={"professor":"index"})
@professor.route("/professor")
@professor.route("/professor/")
def index():
	try:
		return render_template("professor/index.html")
	except TemplateNotFound:
		abort(404)

@professor.route('/',defaults={"professor":"perfil"})
@professor.route("/professor/perfil")
@professor.route("/professor/perfil/")
def perfil(professor):
	try:
		return "perfil do professor"
	except TemplateNotFound:
		abort(404)

@professor.route("/professor/faculdades")
@professor.route("/professor/faculdades/")
def faculdades(professor):
	try:
		return render_template("professor/faculdades.html")
	except TemplateNotFound:
		abort(404)

@professor.route("/<professor>/cadastroP")
@professor.route("/<professor>/cadastroP/")
def cadastroP(professor):
	try:
		return render_template("professor/cadastroP.html")
	except TemplateNotFound:
		abort(404)
@professor.route("/<professor>/notas")
@professor.route("/<professor>/notas/")
def notas(professor):
	try:
		return render_template("professor/notas.html")
	except TemplateNotFound:
		abort(404)

@professor.route("/<professor>/ads")
@professor.route("/<professor>/ads/")
def professor_ads(professor):
	try:
		return render_template("professor/ads.html")
	except TemplateNotFound:
		abort(404)

@professor.route("/<professor>/trabalhos")
@professor.route("/<professor>/trabalhos/")
def trabalhos(professor):
	try:
		return render_template("professor/trabalhos.html")
	except TemplateNotFound:
		abort(404)

@professor.route("/professor/turmas/")
def grade():
	try:
		return render_template("professor/turmas.html")
	except TemplateNotFound:
		abort(404)

@professor.route("/<professor>/alunos")
@professor.route("/<professor>/alunos/")
def alunos(professor):
	try:
		return render_template("professor/alunos.html")
	except TemplateNotFound:
		abort(404)

@professor.route("/professor/cursos/")
def cursos():
	try:
		return render_template("professor/cursos.html")
	except TemplateNotFound:
		abort(404)
