
class Modulos:
	_id = 0
	_nome = ''
	_disciplinas = []
	_curso = ""

	def __init__(self,nome=""):
		self._nome = nome
	
	def setId(self,id):
		self._id = id

	def setNome(self,nome):
		self._nome = nome
		return self

	def setDisciplinas(self,disciplinas):
		self._disciplinas = disciplinas
		return self
	
	def setCurso(self,curso):
		self._curso = curso
		return self


	def getId(self):
		return self._id

	def getNome(self):
		return self._nome

	def getDisciplinas(self):
		return self._disciplinas
	
	def getCurso(self):
		return self._curso
	
