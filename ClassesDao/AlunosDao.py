#!/usr/bin/python
import sys
from Classes.Alunos import Alunos as AlunosClass
from Models.Model import db,Alunos  as AlunosModel, Usuarios as UsuarioModel


class AlunosDao:
	_aluno = ''
	_faculdade = ""

	def __init__(self,aluno="",faculdade=""):
		self._aluno = aluno
		self._faculdade = faculdade

	def save(self):
		try:
			aluno = AlunosModel(self._aluno)
			faculdade = UsuarioModel.query.filter(UsuarioModel.id==self._faculdade.getId()).first()
			db.session.add(aluno)
			faculdade.alunos.append(aluno)
			db.session.commit()
			print "Aluno cadastrado com sucesso"
			return {"status":0,"message":"Aluno cadastrado com sucesso!"}
		except Exception as e:
			print "Falhou ao cadastrar aluno ",e
			print "Fazendo rollback"
			db.session.rollback()
			return {"status":1,"message":"Falhou ao cadastrar Aluno %s"%e}

	def select(self,faculdadeid):
		try:
			res = Usuario.query.filter(Usuario.id==faculdadeid)
			for r in res:
				if r is None:
					break
				print r
				fac = Faculdade()
				fac.setId(r.id)
				fac.setNome(r.nome)
				fac.setCnpj(r.cnpj)
				fac.setSenha(r.senha)
				return fac
			else:
				return {"status":1,"message":"Faculdade nao encontrada"}
		except Exception as e:
			print "Falhou ",e
			return {"status":1,"message":"Falhou ao buscar faculdade %s"%e}

	def selectByEmail(self,email):
		try:
			res = AlunosModel.query.filter(AlunosModel.email==email)
			for r in res:
				if r is None:
					break
				print r
				fac = AlunosClass()
				fac.setId(r.id)
				fac.setNome(r.nome)
				fac.setSenha(r.senha)
				return fac
			else:
				return {"status":1,"message":"Faculdade nao encontrada"}
		except Exception as e:
			print "Falhou ",e
			return {"status":1,"message":"Falhou ao buscar faculdade %s"%e}

	def list(self,faculdadeid):
		try:
			listaAlunos = []
			retorno = AlunosModel.query.all()
			for r in retorno:
				aluno = AlunosClass()
				aluno.setId(r.id)
				aluno.setNome(r.nome)
				aluno.setEmail(r.email)
				aluno.setRg(r.rg)
				aluno.setCpf(r.cpf)
				aluno.setCelular(r.celular)
				aluno.setTelefone(r.telefone)
				aluno.setFacebook(r.facebook)
				aluno.setSenha(r.senha)
				listaAlunos.append(aluno)
			return listaAlunos
		except Exception as e:
			print "Falhou ao listar alunos %s"%e
			return {"status":1,"message":"Falhou ao listar alunos %s"%e}

if __name__ == "__main__":
	aluno = Aluno('Alisson',"alisson.machado@4linux",'34255','386064','alisson.demenezes','12345')
	aluno_dao = AlunoDao(aluno)
	aluno_dao.save()
