#!/usr/bin/python

from Models.Model import db,Turmas as TurmasModel

class Turma:

    def __init__(self,limite_alunos=0,data_inicio=0,data_fim=0,curso=0):
        self.limite_alunos = limite_alunos
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.curso_id = curso

    def save(self):
        try:
            turma =  TurmasModel(self)
            db.session.add(turma)
            db.session.commit()
            return {"status":0,"message":"Turma salva com sucesso!"}
        except Exception as e:
            print "Falhou ",e
            print "Falhou ao salvar o turma",e
            print "Fazendo Rollback"
            db.session.rollback()
            return {"status":1,"message":"Falhou ao salvar turma %s"%e}
