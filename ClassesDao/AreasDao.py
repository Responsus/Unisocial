
import sys

sys.path.append("/srv/unisocial")
from Models.Model import db,Areas as AreasModel
from Classes.Areas import Areas


class AreasDao:
	
	_area = ''	

	def __init__(self,area=""):
		self._area = area


	def save(self):
		try:
			area =  AreasModel(self._area)
			db.session.add(area)
			db.session.commit()
			print "Area Cadastrada com Sucesso"
			return {"status":"0","message":"Areas cadastrada com sucesso "}
		except Exception as e:
			print "Falhou ao salvar a area ",e
			print "Fazendo rollback ",e
			db.session.rollback()
			return {"status":"1","message":"Falhou ao cadastrar area %s\nFazendo Rollback"%e}

	def select(self,areaid):
		try:
			res = AreasModel.query.filter(AreasModel.id==areaid).first()
			area = Areas()
			area.setId(res.id)
			area.setNome(res.nome)
			return area
		except Exception as e:
			print "Falhou ",e
			return {"status":1,"message":"Falhou ao buscar area %s"%e}

	def delete(self):
		try:
			res =  AreasModel.query.filter(AreasModel.id==self._area.getId()).first()
#			turmas = TurmasModel.query.filter(TurmasModel.periodo_id==self._area.getId()).count()
#			if turmas:
#				return {"status":1,"message":"Existem turmas nesse periodo"}
			db.session.delete(res)
			db.session.commit()
			return {"status":"0","message":"Area removida com sucesso"}
		except Exception as e:
			db.session.rollback()
			print "Falhou ",e
			return {"status":1,"message":"Falhou ao remover area %s"%e}

	def list(self,faculdadeid):
		try:
			areas = AreasModel.query.filter(AreasModel.faculdade_id==faculdadeid)
			return areas
		except Exception as e:
			print "Falhu %s"%e
			return {"status":"1","message":"Falhou ao listar areas %s"%e}

