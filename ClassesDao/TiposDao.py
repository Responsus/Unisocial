
import sys

sys.path.append("/srv/unisocial")
from Classes.Tipos import Tipos
from Models.Model import db,Tipos as TiposModel

class TiposDao:
	
	_tipo = ''	

	def __init__(self,tipo=''):
		self._tipo = tipo


	def save(self):
		try:
			tipo =  TiposModel(self._tipo)
			db.session.add(tipo)
			db.session.commit()
			print "Tipo de Curso Cadastrado com Sucesso"
			return {"status":"0","message":"Tipos cadastrada com sucesso "}
		except Exception as e:
			print "Falhou ao salvar a tipo ",e
			print "Fazendo rollback ",e
			db.session.rollback()
			return {"status":"1","message":"Falhou ao cadastrar tipo do curso %s\nFazendo Rollback"%e}

	def select(self,tipoid):
		try:
			res = TiposModel.query.filter(TiposModel.id==tipoid).first()
			tipo = Tipos()
			tipo.setId(res.id)
			tipo.setNome(res.nome)
			return tipo
		except Exception as e:
			print "Falhou ",e
			return {"status":1,"message":"Falhou ao buscar tipos de curso %s"%e}

	def list(self,faculdadeid):
		try:
			tipos = TiposModel.query.filter(TiposModel.faculdade_id==faculdadeid)
			return tipos
		except Exception as e:
			print "Falhou ",e
			return {"status":"1","message":"Falhou ao listar tipos de curso %s"%e}

