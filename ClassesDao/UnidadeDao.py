import sys
sys.path.append("/srv/unisocial")
from Models.Model import db,Unidades as UnidadesModel, Areas as AreasModel, Cursos as CursosModel
from Classes.Unidades import Unidades as UnidadeClass
from Classes.Areas import Areas as AreasClass
from Classes.Cursos import Cursos as CursosClass

class UnidadeDao:
    _unidade = ''

    def __init__(self,unidade=""):
     self._unidade = unidade

    def save(self):
        try:
            unidade = UnidadesModel(self._unidade)
            db.session.add(unidade)
            for a in self._unidade.getAreas():
                area = AreasModel.query.filter(AreasModel.id==a.getId()).first()
                unidade.areas.append(area)
                area = ""
            for c in self._unidade.getCursos():
                curso = CursosModel.query.filter(CursosModel.id==c.getId()).first()
                unidade.cursos.append(curso)
                curso = ""
                db.session.commit()
            print "Unidade cadastrada com sucesso"
            return {"status":"0","message":"Unidade Cadastrada com sucesso "}
        except Exception as e:
            print "Falhou ao cadastrar unidade ",e
            db,session.rollback()
            return {"status":"1","message":"Falhou ao cadastrar unidade %s"%e}

    def incluirCurso(self,cursoid):
        try:
            curso = db.session.query(CursosModel,AreasModel).join(AreasModel).filter(CursosModel.id==cursoid).first()

            unidade = UnidadesModel.query.filter(UnidadesModel.id==self._unidade.getId()).first()
            unidade.areas.append(curso.Areas)
            unidade.cursos.append(curso.Cursos)
            db.session.commit()
            return {"status":"0","message":"Curso Adicionado a Unidade com Sucesso"}
        except Exception as e:
            print "Falhou ao cadastrar unidade ",e
            db,session.rollback()
            return {"status":"1","message":"Falhou ao adicionar curso a unidade %s"%e}

    def select(self,unidadeid):
        try:
            res =  UnidadesModel.query.filter(UnidadesModel.id==unidadeid).first()
            unidade = UnidadeClass()
            unidade.setId(res.id)
            unidade.setNome(res.nome)
            unidade.setEndereco(res.endereco)
            unidade.setTurmas(res.turmas)
            unidade.setFaculdade(res.faculdade_id)
            listareas = []
            for a in res.areas:
                areaclass = AreasClass()
                areaclass.setId(a.id)
                areaclass.setNome(a.nome)
                listareas.append(areaclass)
                unidade.setAreas(listareas)			
                listcursos = []
            for c in res.cursos:
                cursoclass = CursosClass()
                cursoclass.setId(c.id)
                cursoclass.setNome(c.nome)
                cursoclass.setDescricao(c.descricao)
                listcursos.append(cursoclass)

            unidade.setCursos(listcursos)
            print res.cursos
            return unidade
        except Exception as e:
            print "Falhou ",e
            return {"status":1,"message":"Falhou ao buscar unidade %s"%e}

	def delete(self):
		try:
			res =  UnidadesModel.query.filter(UnidadesModel.id==self._unidade.getId()).first()
			print res
			db.session.delete(res)
			db.session.commit()
			return {"status":"0","message":"Unidade removida com sucesso"}
		except Exception as e:
			db.session.rollback()
			print "Falhou ",e
			return {"status":1,"message":"Falhou ao remover unidade %s"%e}

    def list(self,faculdadeid):
        try:
            unidades = UnidadesModel.query.filter(UnidadesModel.faculdade_id==faculdadeid)
            return unidades
        except Exception as e:
            print "Falhu %s"%e
            return {"status":"1","message":"Falhou ao listar UnidadesModel %s"%e}
