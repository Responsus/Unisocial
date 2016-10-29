#!/usr/bin/python
from Models.Model import db, Professores as ProfessoresModel, Cursos as CursosModel

class Professor:
    def __init__(self,nome="",email=""):
        self._id = 0
        self._nome = nome
        self._email = email

    def save(self):
        try:
            professor =  ProfessoresModel(self)
            db.session.add(professor)
            db.session.commit()
            return {"status":0,"message":"Professor Cadastrado com Sucesso"}
        except Exception as e:
            print "Falhou ao salvar o professor",e
            print "Fazendo Rollback"
            db.session.rollback()
            return {"status":1,"message":"Falhou ao Cadastrar Professor %s"%e}

    def select(self):
        try:
            professor = ProfessoresModel.query.filter(ProfessoresModel.id==self.id).first()
            professor.__dict__.pop("_sa_instance_state",None)
            for p in professor.__dict__:
                setattr(self,p,professor.__dict__.get(p))
            return self
        except Exception as e:
            print "Falhou ao retornar professor: %s"%e
            return {"status":1,"message": "Falhou ao retornar professor %s"%e}


    def addCurso(self,curso):
        try:
            professores = ProfessoresModel.query.filter(ProfessoresModel.id==self.id).first()
            curso = CursosModel.query.filter(CursosModel.id==curso.id).first()
            if not curso:
                return {"status":1,"message":"Curso nao encontrado"}
            if not professores:
                return {"status":1,"message":"Professor nao encontrado"}
            professores.cursos.append(curso)
            db.session.add(professores)
            db.session.commit()
            return {"status":0,"message":"Professor mistrando o curso com sucesso"}
        except Exception as e:
            print "Falhou %s"%e
            return {"status":"1","message":"Falhou ao listar professores %s"%e}
