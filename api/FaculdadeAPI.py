from flask import Flask,Blueprint,jsonify,request,session
from flask.views import MethodView
import sys
from Classes.Faculdade import Faculdade
from Classes.Areas import Areas
from Classes.Alunos import Alunos
from Classes.Tipos import Tipos
from Classes.Unidades import Unidades
from Classes.Disciplinas import Disciplinas
from Classes.Periodos import Periodos
from Classes.Turmas import Turmas
from ClassesDao.FaculdadeDao import FaculdadeDao
from ClassesDao.UnidadeDao import UnidadeDao
from ClassesDao.AreasDao import AreasDao
from ClassesDao.AlunosDao import AlunosDao
from ClassesDao.TiposDao import TiposDao
from ClassesDao.DisciplinasDao import DisciplinasDao
from ClassesDao.PeriodosDao import PeriodosDao
from ClassesDao.TurmasDao import TurmasDao
from ClassesDao.CursosDao import CursosDao
from ClassesDao.ModulosDao import ModulosDao


class PeriodoAPI(MethodView):
	def get(self,faculdadeid,idperiodo):
		if idperiodo is None:
			try:
				json_periodos = {}
				lista_periodos = []
				periodo_dic = {}
				periodos = PeriodosDao()
				for p in periodos.list(faculdadeid):
					periodo_dic['id'] = p.id
					periodo_dic['nome'] = p.nome
					periodo_dic['inicio'] = p.inicio
					periodo_dic['intervalo'] = p.intervalo
					periodo_dic['termino'] = p.termino
					lista_periodos.append(periodo_dic)
					periodo_dic = {}
				json_periodos['periodos'] = lista_periodos

				return jsonify(json_periodos)
			except Exception as e:
				return jsonify({"status":0,"message":"Falhou ao buscar unidades %s"%e})
		else:
			try:
				json_periodos = {}
				lista_periodos = []
				periodo_dic = {}
				periodos = Periodos.query.filter(Periodos.id==idperiodo)
				for p in periodos:
					periodo_dic['id'] = p.id
					periodo_dic['nome'] = p.nome
					periodo_dic['inicio'] = p.inicio
					periodo_dic['intervalo'] = p.intervalo
					periodo_dic['termino'] = p.termino
					lista_periodos.append(periodo_dic)
				json_periodos['periodos'] = lista_periodos

				return jsonify(json_periodos)
			except Exception as e:
				return jsonify({"status":0,"message":"Falhou ao buscar unidades %s"%e})

	def post(self,faculdadeid):
		try:
			nome = request.form["nome"]
			inicio = request.form["inicio"]
			intervalo = request.form["intervalo"]
			termino = request.form["fim"]
			facDao = FaculdadeDao()
			fac = facDao.select(faculdadeid)
			if not isinstance(fac,Faculdade):
				return jsonify(fac)
			periodo = Periodos(nome,inicio,intervalo,termino,fac)
			periododao = PeriodosDao(periodo)
			retorno = periododao.save()
			if retorno['status'] == "1":
				return jsonify(retorno)
			return jsonify({"status":"0","message":"Periodo cadastrado com sucesso"})
		except Exception as e:
			return jsonify({"status":"1","message":"Falhou ao cadastrar periodo %s"%e})

	def put(idperiodo,methods=["PUT"]):
		try:
			turmas = db.session.query(Turmas,Cursos,Periodos).join(Cursos).join(Periodos).all()
			return render_template("faculdade/index.html",turmas=turmas)
		except TemplateNotFound:
			abort(404)

	def delete(self,faculdadeid,periodoid):
		try:
			periodo = Periodos()
			periodo.setId(periodoid)
			periodosdao = PeriodosDao(periodo)
			res = periodosdao.delete()
			return jsonify(res)
		except Exception as e:
			return jsonify({"status":"1","message":"Erro: %s"%e})

class DisciplinaAPI(MethodView):
	def get(self,faculdadeid,areaid,iddisciplinas):
		if iddisciplinas is None:
			try:
				json_disciplinas = {}
				json_disc = {}
				lista_disciplinas = []
				disciplinas_dic = {}
				disciplinasdao = DisciplinasDao()
				d = disciplinasdao.list(areaid)
				for disc in d:
					json_disc["id"] = disc.getId()
					json_disc["nome"] = disc.getNome()
					json_disc["descricao"] = disc.getDescricao()
					lista_disciplinas.append(json_disc)
					json_disc = {}
				json_disciplinas['disciplinas'] = lista_disciplinas
				return jsonify({"disciplinas":json_disciplinas['disciplinas']})
			except Exception as e:
				return jsonify({"status":0,"message":"Falhou ao buscar disciplinas %s"%e})
		else:
			try:
				json_disciplinas = {}
				lista_disciplinas = []
				disciplinas_dic = {}
				disciplinasDao = DisciplinasDao()
				disciplinas = disciplinasDao.select(iddisciplinas)
				disciplinas_dic['id'] = d.id
				disciplinas_dic['nome'] = d.nome
				disciplinas_dic['descricao'] = d.descricao
				lista_disciplinas.append(disciplinas_dic)
				json_disciplinas['disciplinas'] = lista_disciplinas
				return jsonify(json_disciplinas)
			except Exception as e:
				return jsonify({"status":0,"message":"Falhou ao buscar unidades %s"%e})

	def post(self,faculdadeid):
		try:
			nome = request.form["nome"]
			descricao = request.form["descricao"]
			areas = request.form["areas"].split(",")
			areas_lista = []
			areadao = AreasDao()
			for a in areas:
				areas_lista.append(areadao.select(a))
			disciplina = Disciplinas(nome,descricao,areas_lista)
			disciplinadao = DisciplinasDao(disciplina)
			disciplinadao.save()
			return jsonify({"status":"0","message":"Disciplina cadastrada com sucesso"})
		except Exception as e:
			return jsonify({"status":"1","message":"Falhou ao cadastrar Disciplina %s"%e})

	def put(idperiodo,methods=["PUT"]):
		try:
			turmas = db.session.query(Turmas,Cursos,Periodos).join(Cursos).join(Periodos).all()
			return render_template("faculdade/index.html",turmas=turmas)
		except TemplateNotFound:
			abort(404)

	def delete(self,faculdadeid,disciplinaid):
		try:
			disciplina = Disciplinas()
			disciplina.setId(disciplinaid)
			disciplinasdao = DisciplinasDao(disciplina)
			res = disciplinasdao.delete()
			return jsonify(res)
		except Exception as e:
			return jsonify({"status":"1","message":"Erro: %s"%e})

class AreaAPI(MethodView):
	def get(self,faculdadeid,idarea):
		if idarea is None:
			try:
				json_areas = {}
				lista_areas = []
				areas_dic = {}
				areasdao = AreasDao()
				areas = areasdao.list(faculdadeid)
				for a in areas:
					areas_dic['id'] = a.id
					areas_dic['nome'] = a.nome
					lista_areas.append(areas_dic)
					areas_dic = {}
				json_areas['areas'] = lista_areas

				return jsonify(json_areas)
			except Exception as e:
				return jsonify({"status":0,"message":"Falhou ao buscar unidades %s"%e})
		else:
			try:
				json_areas = {}
				lista_areas = []
				areas_dic = {}
				areas = Areas.query.filter(Areas.id==idarea)
				for a in areas:
					areas_dic['id'] = a.id
					areas_dic['nome'] = a.nome
					lista_areas.append(areas_dic)

				json_areas['areas'] = lista_areas
				return jsonify(json_areas)
			except Exception as e:
				return jsonify({"status":0,"message":"Falhou ao buscar unidades %s"%e})

	def post(self,faculdadeid):
		try:
			nome = request.form["nome"]
			facDao = FaculdadeDao()
			fac = facDao.select(faculdadeid)
			if not isinstance(fac,Faculdade):
				return jsonify(fac)
			print fac.getId()
			area = Areas(nome,fac)
			areadao = AreasDao(area)
			retorno = areadao.save()
			if retorno['status'] == "1":
				return jsonify(retorno)
			return jsonify({"status":"0","message":"Area cadastrada com sucesso"})
		except Exception as e:
			return jsonify({"status":"1","message":"Falhou ao cadastrar Area %s"%e})

	def put(idarea,methods=["PUT"]):
		try:
			turmas = db.session.query(Turmas,Cursos,Periodos).join(Cursos).join(Periodos).all()
			return render_template("faculdade/index.html",turmas=turmas)
		except TemplateNotFound:
			abort(404)

	def delete(self,faculdadeid,areasid):
		try:
			area = Areas()
			area.setId(areasid)
			areasdao = AreasDao(area)
			res = areasdao.delete()
			return jsonify(res)
		except Exception as e:
			return jsonify({"status":"1","message":"Erro: %s"%e})

class TipoAPI(MethodView):
	def get(self,faculdadeid,idtipo):
		if idtipo is None:
			try:
				json_tipos = {}
				lista_tipos = []
				tipos_dic = {}
				tiposdao = TiposDao()
				tipos = tiposdao.list(faculdadeid)
				for t in tipos:
					tipos_dic['id'] = t.id
					tipos_dic['nome'] = t.nome
					lista_tipos.append(tipos_dic)
					tipos_dic = {}
				json_tipos['tipos'] = lista_tipos

				return jsonify(json_tipos)
			except Exception as e:
				return jsonify({"status":0,"message":"Falhou ao buscar tipos de curso %s"%e})
		else:
			try:
				json_areas = {}
				lista_areas = []
				areas_dic = {}
				areas = Areas.query.filter(Areas.id==idarea)
				for a in areas:
					areas_dic['id'] = a.id
					areas_dic['nome'] = a.nome
					lista_areas.append(areas_dic)

				json_areas['areas'] = lista_areas
				return jsonify(json_areas)
			except Exception as e:
				return jsonify({"status":0,"message":"Falhou ao buscar unidades %s"%e})

	def post(self,faculdadeid):
		try:
			nome = request.form["nome"]
			facDao = FaculdadeDao()
			fac = facDao.select(faculdadeid)
			if not isinstance(fac,Faculdade):
				return jsonify(fac)
			print fac.getId()
			tipo = Tipos(nome,fac)
			tiposdao = TiposDao(tipo)
			tiposdao.save()
			return jsonify({"status":"0","message":"Tipo de Curso cadastrada com sucesso"})
		except Exception as e:
			return jsonify({"status":"1","message":"Falhou ao cadastrar tipo de curso %s"%e})

	def put(idarea):
		try:
			turmas = db.session.query(Turmas,Cursos,Periodos).join(Cursos).join(Periodos).all()
			return render_template("faculdade/index.html",turmas=turmas)
		except TemplateNotFound:
			abort(404)




#@faculdade_api.route("/api/faculdade/<faculdadeid>/professores")
#@faculdade_api.route("/api/faculdade/<faculdadeid>/professores/")
#def listProfessores(methods=["GET"]):
#	try:
#		json_professores = {}
#		lista_professores = []
#		professores_dic = {}
#		professores = Professores.query.all()
#		for p in professores:
#			professores_dic['id'] = p.id
#			professores_dic['nome'] = p.nome
#			lista_professores.append(professores_dic)
#
#		json_professores['professores'] = lista_professores
#		return jsonify(json_professores)
#	except Exception as e:
#		return jsonify({"status":0,"message":"Falhou ao buscar unidades %s"%e})

#@faculdade_api.route("/api/faculdade/<faculdadeid>/professores/<idprofessor>")
#@faculdade_api.route("/api/faculdade/<faculdadeid>/professores/<idprofessor>/")
#def getProfessores(idprofessor,methods=["GET"]):
#	try:
#		json_professores = {}
#		lista_professores = []
#		professores_dic = {}
#		professores = Professores.query.filter(Professores.id==idprofessor)
#		for p in professores:
#			professores_dic['id'] = p.id
#			professores_dic['nome'] = p.nome
#			lista_professores.append(professores_dic)
#
#		json_professores['professores'] = lista_professores
#		return jsonify(json_professores)
#	except Exception as e:
#		return jsonify({"status":0,"message":"Falhou ao buscar unidades %s"%e})

#@faculdade_api.route("/api/faculdade/<faculdadeid>/professores")
#@faculdade_api.route("/api/faculdade/<faculdadeid>/professores/")
#def insertProfessores(methods=["POST"]):
#	try:
#		turmas = db.session.query(Turmas,Cursos,Periodos).join(Cursos).join(Periodos).all()
#		return render_template("faculdade/index.html",turmas=turmas)
#	except TemplateNotFound:
#		abort(404)

#@faculdade_api.route("/api/faculdade/<faculdadeid>/professores/<idprofessor>")
#@faculdade_api.route("/api/faculdade/<faculdadeid>/professores/<idprofessor>/")
#def updateProfessores(idprofessor,methods=["PUT"]):
#	try:
#		turmas = db.session.query(Turmas,Cursos,Periodos).join(Cursos).join(Periodos).all()
#		return render_template("faculdade/index.html",turmas=turmas)
#	except TemplateNotFound:
#		abort(404)

#@faculdade_api.route("/api/faculdade/<faculdadeid>/turmas")
#@faculdade_api.route("/api/faculdade/<faculdadeid>/turmas/")
class TurmasAPI(MethodView):
    def get(self,faculdadeid,turmaid):
        if turmaid is None:
            try:
                json_turmas = {}
                lista_turmas = []
                turmas = TurmasDao()
                for t in turmas.list(faculdadeid):
                    lista_alunos = []
                    turmas_dic = {}
                    turmas_dic['id'] = t.getId()
                    turmas_dic['data_inicio'] = t.getDataInicio()
                    turmas_dic['data_fim'] = t.getDataFim()
                    turmas_dic['periodo'] = t.getPeriodo().getNome()
                    turmas_dic['unidade'] = t.getUnidade().getNome()
                    turmas_dic['curso'] = t.getCurso().getNome()
                    turmas_dic['modulo'] = t.getModulo().getNome()
                    lista_turmas.append(turmas_dic)
                for a in t.getAlunos():
                    json_aluno = {}
                    json_aluno['id'] = a.getId()
                    json_aluno['nome'] = a.getNome()
                    lista_alunos.append(json_aluno)
                turmas_dic['alunos'] = lista_alunos
                json_turmas['turmas'] = lista_turmas
                return jsonify(json_turmas)
            except Exception as e:
                return jsonify({"status":0,"message":"Falhou ao buscar turmas %s"%e})
        else:
            try:
                json_turmas = {}
                lista_turmas = []
                lista_alunos = []
                turmas = TurmasDao()
                t = turmas.select(turmaid)
                turmas_dic = {}
                turmas_dic['id'] = t.getId()
                turmas_dic['data_inicio'] = t.getDataInicio()
                turmas_dic['data_fim'] = t.getDataFim()
                turmas_dic['periodo'] = t.getPeriodo().getNome()
                turmas_dic['unidade'] = t.getUnidade().getNome()
                turmas_dic['curso'] = t.getCurso().getNome()
                turmas_dic['modulo'] = {"id":t.getModulo().getId(),"nome":t.getModulo().getNome()}
                for a in t.getAlunos():
                    json_aluno = {}
                    json_aluno['id'] = a.getId()
                    json_aluno['nome'] = a.getNome()
                    lista_alunos.append(json_aluno)
                turmas_dic['alunos'] = lista_alunos
                lista_turmas.append(turmas_dic)
                json_turmas['turmas'] = lista_turmas
                return jsonify(json_turmas)
            except Exception as e:
                return jsonify({"status":0,"message":"Falhou ao buscar unidades %s"%e})

    def post(self,faculdadeid,turmaid,alunoid):
        if turmaid is None:
            try:
                unidade = request.form["unidade"]
                datainicio = request.form['datainicio']
                datafim = request.form['datafim']
                area = request.form['area']
                curso = request.form['curso']
                periodo = request.form['periodo']
                qtdalunos = request.form['qtdalunos']
                modulo = request.form['modulo']

                unidadeDao = UnidadeDao()
                unidadeOb = unidadeDao.select(unidade)
                areaDao = AreasDao()
                areaOb = areaDao.select(area)
                cursoDao = CursosDao()
                cursoOb = cursoDao.select(curso)
                periodoDao = PeriodosDao()
                periodoOb = periodoDao.select(periodo)
                moduloDao = ModulosDao()
                moduloObj = moduloDao.select(modulo)
                print moduloObj

                turmas = Turmas(qtdalunos,datainicio,datafim,unidadeOb,periodoOb,areaOb,cursoOb,moduloObj)
                turmasDao = TurmasDao(turmas)
                res = turmasDao.save()
                return jsonify(res)
            except Exception as e:
                return jsonify({"erro":e})
        else:
            try:
                turma = Turmas()
                turma.setId(turmaid)
                aluno = Alunos()
                aluno.setId(alunoid)
                turmadao = TurmasDao()
                res = turmadao.incluirAluno(turma,aluno)
                return jsonify(res)
            except Exception as e:
                return jsonify({"status":1,"message":"Erro: %s"%e})

	def put(self,faculdadeid,idturma):
		try:
			turmas = db.session.query(Turmas,Cursos,Periodos).join(Cursos).join(Periodos).all()
			return render_template("faculdade/index.html",turmas=turmas)
		except TemplateNotFound:
			abort(404)

	def delete(self,faculdadeid,turmaid):
		try:
			turma = Turmas()
			turma.setId(turmaid)
			turmasdao = TurmasDao(turma)
			res = turmasdao.delete()
			return jsonify(res)
		except Exception as e:
			return jsonify({"status":"1","message":"Erro: %s"%e})

class AlunosAPI(MethodView):
	def get(self,faculdadeid,alunoid):
		if alunoid is None:
			try:
				json_alunos = {}
				lista_alunos = []
				alunos_dic = {}
				alunos = AlunosDao()
				for a in alunos.list(1):
					alunos_dic = {}
					alunos_dic['id'] = a.getId()
					alunos_dic['nome'] = a.getNome()
					alunos_dic['email'] = a.getEmail()
					alunos_dic['rg'] = a.getRg()
					alunos_dic['cpf'] = a.getCpf()
					alunos_dic['celular'] = a.getCelular()
					alunos_dic['telefone'] = a.getTelefone()
					alunos_dic['facebook'] = a.getFacebook()
					lista_alunos.append(alunos_dic)

				json_alunos['alunos'] = lista_alunos
				return jsonify(json_alunos)
			except Exception as e:
				return jsonify({"status":0,"message":"Falhou ao buscar Alunos %s"%e})
		else:
			try:
				json_turmas = {}
				lista_turmas = []
				turmas_dic = {}
				turmas = Turmas.query.filter(Turmas.id==idturma)
				for t in turmas:
					turmas_dic['id'] = t.id
					turmas_dic['nome'] = t.nome
					lista_turmas.append(turmas_dic)

				json_turmas['turmas'] = lista_turmas
				return jsonify(json_turmas)
			except Exception as e:
				return jsonify({"status":0,"message":"Falhou ao buscar Aluno %s"%e})

	def post(self,faculdadeid):
		try:

			nome = request.form["nome"]
			email = request.form['email']
			rg = request.form['rg']
			cpf = request.form['cpf']
			celular = request.form['celular']
			telefone = request.form['telefone']
			facebook = request.form['facebook']
			print "senha"
			senha = request.form['senha']
			print "passou aqui"
			aluno = Alunos(nome,email,rg,cpf,celular,telefone,facebook,senha)
			faculdade = Faculdade()
			faculdade.setId(faculdadeid)
			alunoDao = AlunosDao(aluno,faculdade)
			res = alunoDao.save()
			print res
			return jsonify(res)
		except Exception as e:
			return jsonify({"status":1,"message":"Erro: %s"%e})

	def put(self,faculdadeid,idturma):
		try:
			turmas = db.session.query(Turmas,Cursos,Periodos).join(Cursos).join(Periodos).all()
			return render_template("faculdade/index.html",turmas=turmas)
		except TemplateNotFound:
			abort(404)

	def delete(self,faculdadeid,turmaid):
		try:
			turma = Turmas()
			turma.setId(turmaid)
			turmasdao = TurmasDao(turma)
			res = turmasdao.delete()
			return jsonify(res)
		except Exception as e:
			return jsonify({"status":"1","message":"Erro: %s"%e})


#@faculdade_api.route("/api/faculdade/<faculdadeid>/alertas")
#@faculdade_api.route("/api/faculdade/<faculdadeid>/alertas/")
#def listAlertas(methods=["GET"]):
#	try:
#		json_alertas = {}
#		lista_alertas = []
#		alertas_dic = {}
#
#		return jsonify({"status":"0","message":"tem que fazer"})
#	except Exception as e:
#		return jsonify({"status":0,"message":"Falhou ao buscar unidades %s"%e})

#@faculdade_api.route("/api/faculdade/<faculdadeid>/alertas/<idalertas>")
#@faculdade_api.route("/api/faculdade/<faculdadeid>/alertas/<idalertas>/")
#def getAlertas(idturma,methods=["GET"]):
#	try:
#		json_alertas = {}
#		lista_alertas = []
#		alertas_dic = {}
#
#		return jsonify({"status":"0","message":"tem que fazer"})
#	except Exception as e:
#		return jsonify({"status":0,"message":"Falhou ao buscar unidades %s"%e})

#@faculdade_api.route("/api/faculdade/<faculdadeid>/alertas")
#@faculdade_api.route("/api/faculdade/<faculdadeid>/alertas/")
#def insertAlertas(methods=["POST"]):
#	try:
#		turmas = db.session.query(Turmas,Cursos,Periodos).join(Cursos).join(Periodos).all()
#		return render_template("faculdade/index.html",turmas=turmas)
#	except TemplateNotFound:
#		abort(404)

#@faculdade_api.route("/api/faculdade/<faculdadeid>/alertas/<idalertas>")
#@faculdade_api.route("/api/faculdade/<faculdadeid>/alertas/<idalertas>/")
#def updateAlertas(idalerta,methods=["PUT"]):
#	try:
#		turmas = db.session.query(Turmas,Cursos,Periodos).join(Cursos).join(Periodos).all()
#		return render_template("faculdade/index.html",turmas=turmas)
#	except TemplateNotFound:
#		abort(404)
class ModulosAPI(MethodView):
    def get(self,faculdadeid,moduloid):
        if moduloid is None:
            return jsonify({"status":1,"message":"Voce precisa especificar um modulo"})
        else:
            try:
                modulosDao = ModulosDao()
                moduloObj = modulosDao.select(moduloid)
                json = {"modulos":[]}
                json_modulo = {"id":moduloObj.getId(),"nome":moduloObj.getNome(),"disciplinas":[]}
                for d in moduloObj.getDisciplinas():
                    json_disc = {}
                    json_disc['id'] = d.getId()
                    json_disc['nome'] = d.getNome()
                    json_modulo['disciplinas'].append(json_disc)
                json["modulos"].append(json_modulo)

                return jsonify(json)
            except Exception as e:
                return jsonify(moduloObj)

class FaculdadeAPI(MethodView):
	def post(self):
		try:
			nome = request.form['nome']
			email = request.form['email']
			cnpj = request.form['cnpj']
			senha = request.form['senha']
			faculdade = Faculdade(nome,email,cnpj,senha)
			fd = FaculdadeDao(faculdade)
			res = fd.save()
			return jsonify(res)
		except Exception as e:
			return jsonify(res)
