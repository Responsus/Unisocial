
class Periodos:
	_id = 0
	_nome = ''
	_inicio = ''
	_intervalo = ''
	_termino = ''
	_faculdade = 0

	def __init__(self,nome="",inicio="",intervalo="",termino="",faculdade=""):
		self._nome = nome
		self._inicio = inicio
		self._intervalo = intervalo
		self._termino = termino
		self._faculdade = faculdade
	
	def setId(self,id):
		self._id = id

	def setNome(self,nome):
		self._nome = nome
		return self

	def setInicio(self,inicio):
		self._inicio = inicio
		return self
	
	def setIntervalo(self,intervalo):
		self._intervalo = intervalo
		return self

	def setTermino(self,termino):
		self._termino = termino
		return self

	def getId(self):
		return self._id

	def getNome(self):
		return self._nome

	def getInicio(self):
		return self._inicio
	
	def getIntervalo(self):
		return self._intervalo

	def getTermino(self):
		return self._termino

	def getFaculdade(self):
		return self._faculdade
