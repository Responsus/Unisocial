#!/usr/bin/python

from Models.Model import db,Cursos as CursosModel

class Curso:
    id = 0
    nome = ''
    descricao = ''
    usuario_id = 0

    def __init__(self,nome="",descricao="",usuario_id=0):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.usuario_id = usuario_id

    def save(self):
        try:
            curso =  CursosModel(self)
            db.session.add(curso)
            db.session.commit()
            return {"status":0,"message":"Curso cadastrado com sucesso"}
        except Exception as e:
            print "Falhou ao salvar o curso",e
            print "Fazendo Rollback"
            db.session.rollback()
            return {"status":1,"message":"Falhou ao cadastrar curso %s"%e}


    def addAula(self,aula):
        try:
            curso =  CursosModel.query.filter(CursosModel.id==self.id).first()
            curso.aulas.append(aula)
            db.session.add(curso)
            db.session.commit()
            return {"status":0,"message":"Aula adicionada ao curso com sucesso"}
        except Exception as e:
            print "Falhou ao salvar o curso",e
            print "Fazendo Rollback"
            db.session.rollback()
            return {"status":1,"message":"Falhou ao adicionar aula ao curso %s"%e}

    def listAula(self):
        try:
            curso =  CursosModel.query.filter(CursosModel.id==self.id).first()
            aulas = [ a.__dict__ for a in curso.aulas ]
            for a in aulas:
                a.pop("_sa_instance_state",None)
            curso.__dict__.pop("_sa_instance_state",None)
            curso.__dict__.pop("tipo_id",None)
            curso.__dict__.pop("area_id",None)
            curso.__dict__["aulas"] = aulas
            return curso.__dict__
        except Exception as e:
            print "Falhou ao salvar o curso",e
            print "Fazendo Rollback"
            db.session.rollback()
            return {"status":1,"message":"Falhou ao adicionar aula ao curso %s"%e}

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

    def select(self):
        try:
            curso = db.session.query(CursosModel).filter(CursosModel.id==self.id).first()
            curso.__dict__.pop("_sa_instance_instate",None)
            for k in curso.__dict__.keys():
                setattr(self,k,curso.__dict__.get(k))
            return self
        except Exception as e:
            print "Falhou %s"%e
            return {"status":"1","message":"Falhou ao listar disciplinas %s"%e}

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
