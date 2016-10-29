
import sys

sys.path.append("/home/alisson/alisson/unisocial")
from Models.Model import db,Cursos as CursosModel, Aulas as AulasModel, Turmas as TurmasModel, Areas as AreasModel
from Classes.Cursos import Cursos as CursosClass
from Classes.Areas import Areas as AreasClass
from Classes.Disciplinas import Disciplinas as DisciplinasClass
from Classes.Modulos import Modulos as ModulosClass


class CursosDao:

	_curso = ''

	def __init__(self,curso=""):
		self._curso = curso

	def save(self):
		try:
			curso =  CursosModel(self._curso)
			db.session.add(curso)
			db.session.commit()
			return {"status":0,"message":"Curso cadastrado com sucesso"}
		except Exception as e:
			print "Falhou ao salvar o curso",e
			print "Fazendo Rollback"
			db.session.rollback()
			return {"status":1,"message":"Falhou ao cadastrar curso %s"%e}

        def select(self,cursoid):
            try:
                res =  CursosModel.query.filter(CursosModel.id==cursoid).first()
                curso = CursosClass()
                res = res.__dict__.pop("_sa_instance",None)
                curso = res.__dict__
                return curso
            except Exception as e:
                print "Falhou ",e
                return {"status":1,"message":"Falhou ao buscar curso %s"%e}

	def delete(self):
		try:
			res =  CursosModel.query.filter(CursosModel.id==self._curso.getId()).first()
			turmas = TurmasModel.query.filter(TurmasModel.curso_id==self._curso.getId()).count()
			if turmas:
				return {"status":"1","message":"Existem %s turmas cadastradas com esse curso"%turmas}
			db.session.delete(res)
			db.session.commit()
			return {"status":"0","message":"Curso removido com sucesso"}
		except Exception as e:
			db.session.rollback()
			print "Falhou ",e
			return {"status":1,"message":"Falhou ao remover curso %s"%e}

	def list(self,areaid):
		try:
			lista_cursos = []
			cursos = db.session.query(CursosModel).filter(CursosModel.area_id==areaid)
			for c in cursos:
				cur = CursosClass()
				cur.setId(c.id)
				cur.setNome(c.nome)
				cur.setDescricao(c.descricao)
				res3 = AreasModel.query.filter(AreasModel.id==areaid).first()
				areaclass = AreasClass()
				areaclass.setNome(res3.nome)
				areaclass.setId(res3.id)
				cur.setArea(areaclass)
				cur.setDisciplinas(c.disciplinas)
				lista_cursos.append(cur)
			print lista_cursos
			return lista_cursos
		except Exception as e:
			print "Falhou %s"%e
			return {"status":"1","message":"Falhou ao listar disciplinas %s"%e}
