#!/usr/bin/python

from Models.Model import db,Usuarios as UsuarioModel

class Usuario:
    id = 0
    nome = ""
    email = ""
    cnpj = ""
    senha = ""

    def __init__(self,nome='',email='',cnpj='',senha=''):
        self.nome = nome
        self.email = email
        self.cnpj = cnpj
        self.senha = senha

    def save(self):
        try:
            usuario =  UsuarioModel(self)
            db.session.add(usuario)
            db.session.commit()
            print "Usuario cadastrado com sucesso!"
            return {"status":"0","message":"Usuario cadastrado com sucesso!"}
        except Exception as e:
            print "Falhou ao salvar a Usuario ",e
            print "Fazendo rollback ",e
            db.session.rollback()
            return {"status":"1","message":"Falhou ao cadastrar Usuario %s\nFazendo Rollback"%e}

    def select(self,Usuarioid):
        try:
            res = Usuarios.query.filter(Usuarios.id==Usuarioid)
            for r in res:
                if r is None:
                    break
                print r
                fac = Usuario()
                fac.setId(r.id)
                fac.setNome(r.nome)
                fac.setCnpj(r.cnpj)
                fac.setSenha(r.senha)
                return fac
            else:
                return {"status":1,"message":"Usuario nao encontrada"}
        except Exception as e:
            print "Falhou ",e
            return {"status":1,"message":"Falhou ao buscar Usuario %s"%e}

    def selectByEmail(self,email):
        try:
            res = Usuarios.query.filter(Usuarios.email==email)
            for r in res:
                print r
                if r is None:
                    break
                print r
                fac = Usuario()
                fac.setId(r.id)
                fac.setNome(r.nome)
                fac.setCnpj(r.cnpj)
                fac.setSenha(r.senha)
                return fac
            else:
                return {"status":1,"message":"Usuario nao encontrada"}
        except Exception as e:
            print "Falhou ",e
            return {"status":1,"message":"Falhou ao buscar Usuario %s"%e}
