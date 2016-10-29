
import sys

sys.path.append("/srv/unisocial")
from Models.Model import db,Modulos as ModulosModel
from Models.Model import db,Disciplinas as DisciplinasModel
from Classes.Areas import Areas
from Classes.Modulos import Modulos as ModulosClass
from Classes.Disciplinas import Disciplinas as DisciplinasClass


class ModulosDao:

    _modulo = ''	

    def __init__(self,modulo=""):
        self._modulo = modulo	

    def select(self,moduloid):
        try:
            res = ModulosModel.query.filter(ModulosModel.id==int(moduloid)).first()
            modulo = ModulosClass()
            modulo.setId(res.id)
            modulo.setNome(res.nome)
            lista_disciplinas = []
            for d in res.disciplinas:
                disciplinas = DisciplinasClass()
                disciplinas.setId(d.id)
                disciplinas.setNome(d.nome)
                lista_disciplinas.append(disciplinas)
            modulo.setDisciplinas(lista_disciplinas)
            return modulo
        except Exception as e:
            print "Falhou ",e
            return {"status":1,"message":"Falhou ao buscar modulo %s"%e}

    def addDisciplina(self,disciplina):
        try:
            res =  ModulosModel.query.filter(ModulosModel.id==self._modulo.getId()).first()
            res1 = DisciplinasModel.query.filter(DisciplinasModel.id==disciplina.getId()).first()
            res.disciplinas.append(res1)
            #db.session.save(res)
            db.session.commit()
            return {"status":"0","message":"Disciplina adicionada com sucesso"}
        except Exception as e:
            db.session.rollback()
            print "Falhou ",e
            return {"status":1,"message":"Falhou ao adicionar disciplina %s"%e}

	def list(self,faculdadeid):
		try:
			areas = AreasModel.query.filter(AreasModel.faculdade_id==faculdadeid)
			return areas
		except Exception as e:
			print "Falhu %s"%e
			return {"status":"1","message":"Falhou ao listar areas %s"%e}

