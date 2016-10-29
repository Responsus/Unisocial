
class Unidades:
	_id = 0
	_nome = ''
	_endereco = ''
	_descricao = ''
	_faculdade = ''
	_turmas = ''
	_areas = []
	_cursos = []
	
	def __init__(self,nome="",endereco="",descricao="",faculdade="",areas="",cursos=""):
		self._nome = nome
		self._endereco = endereco
		self._descricao = descricao
		self._faculdade = faculdade
		self._areas = areas
		self._cursos = cursos

	def setId(self,id):
		self._id = id
		return self

	def setNome(self,nome):
		self._nome = nome
		return self

	def setEndereco(self,endereco):
		self._endereco = endereco
		return self
	
	def setDescricao(self,descricao):
		self._descricao = descricao
		return self


	def setFaculdade(self,faculdade):
		self._faculdade = faculdade
		return self

	def setTurmas(self,turmas):
		self._turmas = turmas
		return self

	def setAreas(self,areas):
		self._areas = areas
		return self

	def setCursos(self,cursos):
		self._cursos = cursos
		return self

	def getId(self):
		return self._id

	def getNome(self):
		return self._nome

	def getEndereco(self):
		return self._endereco

	def getDescricao(self):
		return self._descricao

	def getFaculdade(self):
		return self._faculdade

	def getAreas(self):
		return self._areas

	def getCursos(self):
		return self._cursos

