#!/usr/bin/python


class Alunos:
	_id = 0
	_nome = ""
	_email = ""
	_rg = ""
	_cpf = ""
	_celular = ""
	_telefone = ""
	_facebook = ""
	_senha = ""

	def __init__(self,nome="",email="",rg="",cpf="",celular="",telefone="",facebook="",senha=""):
		self._nome = nome
		self._email = email
		self._rg = rg
		self._cpf = cpf
		self._celular = cpf
		self._telefone = telefone
		self._facebook = facebook
		self._senha = senha

	def setId(self,id):
		self._id = id
		return self

	def setNome(self,nome):
		self._nome = nome
		return self

	def setEmail(self,email):
		self._email = email
		return self

	def setRg(self,rg):
		self._rg = rg
		return self

	def setCpf(self,cpf):
		self._cpf = cpf
		return self

	def setCelular(self,celular):
		self._celular = celular
		return self

	def setTelefone(self,telefone):
		self._telefone = telefone
		return self

	def setFacebook(self,facebook):
		self._facebook = facebook
		return self

	def setSenha(self,senha):
		self._senha = senha
		return self
	
	def getId(self):
		return self._id

	def getNome(self):
		return self._nome

	def getEmail(self):
		return self._email

	def getRg(self):
		return self._rg

	def getCpf(self):
		return self._cpf

	def getCelular(self):
		return self._celular

	def getTelefone(self):
		return self._telefone

	def getFacebook(self):
		return self._facebook

	def getSenha(self):
		return self._senha
