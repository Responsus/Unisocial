from flask import Flask,Blueprint,jsonify,request,session,abort
from ClassesDao.CursosDao import CursosDao
from ClassesDao.UnidadeDao import UnidadeDao
from ClassesDao.FaculdadeDao import FaculdadeDao
from ClassesDao.AreasDao import AreasDao
from ClassesDao.ModulosDao import ModulosDao
from Classes.Cursos import Cursos
from Classes.Faculdade import Faculdade
from Classes.Unidades import Unidades

UnidadesAPI = Blueprint('Unidades_Api',__name__)

def force_auth():
    if not 'id' in session:
        abort(401)
    elif int(session['id']) != int(request.url.split("/")[5]):
        abort(401)

UnidadesAPI.before_request(force_auth)

@UnidadesAPI.route('/api/faculdade/<int:faculdadeid>/unidades/')
def list_unidades(faculdadeid):
    try:
        json_unidades = {}
        lista_unidades = []
        unidade_dic = {}
        unidadedao = UnidadeDao()
        unidades = unidadedao.list(faculdadeid)
        for u in unidades:
            unidade_dic['id'] = u.id
            unidade_dic['nome'] = u.nome
            unidade_dic['endereco'] = u.endereco
            unidade_dic['faculdade_id'] = u.faculdade_id
            lista_unidades.append(unidade_dic)
            unidade_dic = {}
            json_unidades['unidades'] = lista_unidades	

        return jsonify(json_unidades)
    except Exception as e:
        return jsonify({"status":0,"message":"Falhou ao buscar unidades %s"%e})

@UnidadesAPI.route('/api/faculdade/<int:faculdadeid>/unidades/<int:unidadeid>/')
def get_unidades(faculdadeid,unidadeid):
    try:
        json_unidades = {}
        lista_unidades = []
        unidade_dic = {}
        unidadedao = UnidadeDao()
        unidade = unidadedao.select(unidadeid)
        unidade_dic['id'] = unidade.getId()
        unidade_dic['nome'] = unidade.getNome()
        unidade_dic['endereco'] = unidade.getEndereco()
        unidade_dic['descricao'] = unidade.getDescricao()
        lista_areas = []
        for l in unidade.getAreas():
            dict_areas = {}
            dict_areas['id'] = l.getId()
            dict_areas['nome'] = l.getNome()
            lista_areas.append(dict_areas)
            unidade_dic['areas'] = lista_areas
            lista_cursos = []
        for c in unidade.getCursos():
            dict_cursos = {}
            dict_cursos["id"] = c.getId()
            dict_cursos["nome"] = c.getNome()
            lista_cursos.append(dict_cursos)
        unidade_dic['cursos'] = lista_cursos
        facDao = FaculdadeDao()
        fac = facDao.select(faculdadeid)
        if not isinstance(fac,Faculdade):
            return jsonify(fac)
        unidade_dic['faculdade_id'] = unidade.getFaculdade()
        lista_unidades.append(unidade_dic)
        unidade_dic = {}
        json_unidades['unidades'] = lista_unidades	

        return jsonify(json_unidades)
    except Exception as e:
        return jsonify({"status":0,"message":"Falhou ao buscar unidades %s"%e})

@UnidadesAPI.route('/api/faculdade/<int:faculdadeid>/unidades/',methods=["POST"])
def post_unidades(faculdadeid):
	try:
		nome = request.form['nome']
		endereco = request.form["endereco"]
		descricao = request.form["descricao"]
		areaunidade = request.form['area']
		print areaunidade
		cursounidade = request.form["curso"]
		print cursounidade
		#print nome,endereco,descricao,areaunidade,cursounidade
		facDao = FaculdadeDao()
		fac = facDao.select(faculdadeid)
		if not isinstance(fac,Faculdade):
			return jsonify(fac)
		print fac.getId()
		listareas = []
		areadao = AreasDao()
		for a in areaunidade.split(","):
			area = areadao.select(a)
			listareas.append(area)
			area = ""

		listcursos = []
		cursosdao = CursosDao()
		for c in cursounidade.split(","):
			curso = cursosdao.select(c)
			listcursos.append(curso)
			curso = ""

		unidade = Unidades(nome,endereco,descricao,fac,listareas,listcursos)
		unidadedao = UnidadeDao(unidade)
		unidadedao.save()
		return jsonify({"status":"0","message":"Unidade cadastrada com sucesso"})
	except Exception as e:
		return jsonify({"status":"1","message":"Falhou ao cadastrar Unidade %s"%e})

@UnidadesAPI.route('/api/faculdade/<int:faculdadeid>/unidades/<int:unidadeid>/',methods=["PUT"])
def put_unidades(unidadeid):
	try:
		turmas = db.session.query(Turmas,Cursos,Periodos).join(Cursos).join(Periodos).all()
		return render_template("faculdade/index.html",turmas=turmas)
	except TemplateNotFound:
		abort(404)

@UnidadesAPI.route('/api/faculdade/<int:faculdadeid>/unidades/<int:unidadeid>/cursos/',methods=["POST"])
def add_curso_unidades(faculdadeid,unidadeid):
    try:
        cursoid = request.form['curso']
        unidade = Unidades()
        unidade.setId(unidadeid)
        unidadedao = UnidadeDao(unidade)
        res = unidadedao.incluirCurso(cursoid)
        return jsonify(res)
    except Exception as e:
        return jsonify({"status":1,"message":"Erro! %s"%e})

@UnidadesAPI.route('/api/faculdade/<int:faculdadeid>/unidades/<int:unidadeid>/areas/',methods=["POST"])
def add_areas_unidades(unidadeid):
	try:
		turmas = db.session.query(Turmas,Cursos,Periodos).join(Cursos).join(Periodos).all()
		return render_template("faculdade/index.html",turmas=turmas)
	except TemplateNotFound:
		abort(404)

@UnidadesAPI.route('/api/faculdade/<int:faculdadeid>/unidades/<int:unidadeid>/',methods=["DELETE"])
def delete_unidades(faculdadeid,unidadeid):
	try:
		unidade = Unidades()
		unidade.setId(unidadeid)
		unidadedao = UnidadeDao(unidade)
		res = unidadedao.delete()
		return jsonify(res)
	except Exception as e:
		return jsonify({"status":"1","message":"Erro: %s"%e})
