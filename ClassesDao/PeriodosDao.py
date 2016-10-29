
import sys

sys.path.append("/srv/unisocial")
from Models.Model import db,Periodos as PeriodosModel,Turmas as TurmasModel
from Classes.Periodos import Periodos


class PeriodosDao:
	
	_periodo = ''	

	def __init__(self,periodo=""):
		self._periodo = periodo


	def save(self):
		try:
			periodo =  PeriodosModel(self._periodo)
			db.session.add(periodo)
			db.session.commit()
			print "Periodo Cadastrada com Sucesso"
			return {"status":"0","message":"Periodos cadastrada com sucesso "}
		except Exception as e:
			print "Falhou ao salvar a periodo ",e
			print "Fazendo rollback ",e
			db.session.rollback()
			return {"status":"1","message":"Falhou ao cadastrar periodo %s\nFazendo Rollback"%e}

	def select(self,periodoid):
		try:
			res = PeriodosModel.query.filter(PeriodosModel.id==periodoid).first()
			periodo = Periodos()
			periodo.setId(res.id)
			periodo.setNome(res.nome)
			periodo.setInicio(res.inicio)
			periodo.setIntervalo(res.intervalo)
			periodo.setTermino(res.termino)
			return periodo
		except Exception as e:
			print "Falhou ",e
			return {"status":1,"message":"Falhou ao buscar periodo %s"%e}

	def delete(self):
		try:
			res =  PeriodosModel.query.filter(PeriodosModel.id==self._periodo.getId()).first()
			turmas = TurmasModel.query.filter(TurmasModel.periodo_id==self._periodo.getId()).count()
			if turmas:
				return {"status":1,"message":"Existem %s turmas nesse periodo"%turmas}
			db.session.delete(res)
			db.session.commit()
			return {"status":"0","message":"Periodo removido com sucesso"}
		except Exception as e:
			db.session.rollback()
			print "Falhou ",e
			return {"status":1,"message":"Falhou ao remover periodo %s"%e}

	def list(self,faculdadeid):
		try:
			periodos = PeriodosModel.query.filter(PeriodosModel.faculdade_id==faculdadeid)
			return periodos
		except Exception as e:
			print "Falhu %s"%e
			return {"status":"1","message":"Falhou ao listar periodos %s"%e}

