from flask import Flask,Blueprint,jsonify,request,session,abort
from ClassesDao.CursosDao import CursosDao
from ClassesDao.DisciplinasDao import DisciplinasDao
from ClassesDao.TiposDao import TiposDao
from ClassesDao.AreasDao import AreasDao
from ClassesDao.ModulosDao import ModulosDao
from Classes.Cursos import Cursos
from Classes.Modulos import Modulos
from Classes.Disciplinas import Disciplinas

CursosProfessorAPI = Blueprint('Cursos_Professor_API',__name__)

def force_auth():
    if not 'id' in session:
        abort(401)
    elif int(session['id']) != int(request.url.split("/")[5]):
        abort(401)

CursosProfessorAPI.before_request(force_auth)

@CursosProfessorAPI.route("/api/professor/<int:professorid>/cursos/",methods=["GET"])
def list(professorid,areaid):
	try:
		json_cursos = {}
		lista_cursos = []
		cursos = CursosDao()
		for c in cursos.list(areaid):
			curso_dic = {}
			curso_dic['id'] = c.getId()
			curso_dic['nome'] = c.getNome()
			curso_dic['descricao'] = c.getDescricao()
			curso_dic['area'] = c.getArea().getNome()
			lista_cursos.append(curso_dic)

		json_cursos['cursos'] = lista_cursos

		return jsonify(json_cursos)
	except Exception as e:
		return jsonify({"status":0,"message":"Falhou ao buscar cursos %s"%e})

@CursosProfessorAPI.route("/api/professor/<int:professorid>/cursos/<int:cursoid>/",methods=["GET"])
def select(professorid,cursoid):
	try:
		cursos = CursosDao()
		c = cursos.select(cursoid)
		curso_dic = c.__dict__
		lista_disciplinas = []
		for d in c.getDisciplinas():
			json_disciplinas = d.__dict__
			lista_disciplinas.append(json_disciplinas)

		curso_dic["disciplinas"] = lista_disciplinas
		lista_cursos.append(curso_dic)
		json_cursos['cursos'] = lista_cursos

		return jsonify(json_cursos)
	except Exception as e:
		return jsonify({"status":0,"message":"Falhou ao buscar curso %s"%e})


@CursosProfessorAPI.route("/api/professor/<int:professorid>/cursos/",methods=["POST"])
def save(professorid):
	try:
		# form params
		nome = request.form["nome"]
		descricao = request.form["descricao"]
		#------------
		curso = Cursos(nome,descricao,tipo,area)
		cursodao = CursosDao(curso)
		res = cursodao.save()
		return jsonify(res)
	except Exception as e:
		return jsonify({"status":"1","message":"Nao foi possivel cadastrar o curso %s"%e})

@CursosProfessorAPI.route("/api/professor/<int:professorid>/cursos/<int:cursoid>/",methods=["PUT"])
def put(idcurso,methods=["PUT"]):
	try:
		turmas = db.session.query(Turmas,Cursos,Periodos).join(Cursos).join(Periodos).all()
		return render_template("professor/index.html",turmas=turmas)
	except TemplateNotFound:
		abort(404)

@CursosProfessorAPI.route("/api/professor/<int:professorid>/cursos/<int:cursoid>/",methods=["DELETE"])
def delete(professorid,cursoid):
	try:
		curso = Cursos()
		curso.setId(cursoid)
		cursodao = CursosDao(curso)
		res = cursodao.delete()
		return jsonify(res)
	except Exception as e:
		return jsonify({"status":"1","message":"Erro: %s"%e})

@CursosProfessorAPI.route("/api/professor/<int:professorid>/cursos/<int:cursoid>/modulo/<int:moduloid>/disciplinas/",methods=["POST"])
def addDisciplinaModulo(professorid,cursoid,moduloid):
	try:
		discid = request.form["disciplinaid"]
		modulo = Modulos()
		modulo.setId(moduloid)
		modao = ModulosDao(modulo)

		disciplina = Disciplinas()
		disciplina.setId(discid)
		disc_dao = DisciplinasDao()
		res1 = disc_dao.select(discid)

		res = modao.addDisciplina(res1)

		return jsonify(res)
	except Exception as e:
		return jsonify({"status":"1","message":"Erro: %s"%e})

@CursosProfessorAPI.route("/api/professor/<int:professorid>/cursos/<int:cursoid>/modulo/<int:moduloid>/disciplinas/",methods=["GET"])
def listaDisciplinaModulo(professorid,cursoid,moduloid):
	try:
		modulo = Modulos()
		modulo.setId(moduloid)
		modao = ModulosDao(modulo)

		disciplina = Disciplinas()
		disciplina.setId(discid)
		disc_dao = DisciplinasDao()
		res1 = disc_dao.select()

		res = modao.addDisciplina(res1)

		return jsonify(res)
	except Exception as e:
		return jsonify({"status":"1","message":"Erro: %s"%e})
