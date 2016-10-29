#!/usr/bin/python

from Models.Model import db,Aulas as AulasModel

class Aula:
    _id = 0
    nome = ''
    descricao = ''

    def __init__(self,nome="",descricao=""):
        self.nome = nome
        self.descricao = descricao

    def save(self):
        try:
            aula = AulasModel(self)
            db.session.add(aula)
            db.session.commit()
            return aula
        except Exception as e:
            print "Falhou ao cadastrar aula ",e
            db.session.rollback()
            return {"status":"1","message":"Falhou ao cadastrar aula %s"%e}

    def select(self,aulaid):
        try:
            lista_Aulas = []
            disc = AulasModel.query.filter(AulasModel.id==aulaid).first()
            discclass = AulasClass()
            discclass.setId(disc.id)
            discclass.setNome(disc.nome)
            discclass.setDescricao(disc.descricao)
            return discclass
        except Exception as e:
            print "Nao foi possivel retornar a aula ",e

    def delete(self):
        try:
            res =  AulasModel.query.filter(AulasModel.id==self._aula.getId()).first()
            db.session.delete(res)
            db.session.commit()
            return {"status":"0","message":"aula removida com sucesso"}
        except Exception as e:
            db.session.rollback()
            print "Falhou ",e
            return {"status":1,"message":"Falhou ao remover aula %s"%e}

    def list(self,areaid):
        try:
            lista_Aulas = []
            Aulas = db.session.query(AreasModel).join(AreasModel.Aulas).filter(AreasModel.id==areaid)
            for d in Aulas:
                for i in d.Aulas:
                    disc = AulasClass()
                    disc.setId(i.id)
                    disc.setNome(i.nome)
                    disc.setDescricao(i.nome)
                    lista_Aulas.append(disc)
            return lista_Aulas
        except Exception as e:
            print "Falhu %s"%e
            return {"status":"1","message":"Falhou ao listar Aulas %s"%e}
