

class Tipos:
	_id = 0
	_nome = ''
	_faculdade = ''

	def __init__(self,nome='',faculdade=''):
		self._nome = nome
		self._faculdade = faculdade

	def setNome(self,nome):
		self._nome = nome
		return self

	def setId(self,id):
		self._id = id
		return self

	def setFaculdade(self,faculdade):
		self._faculdade = faculdade
		return self

	def getId(self):
		return self._id

	def getNome(self):
		return self._nome

	def getFaculdade(self):
		return self._faculdade
