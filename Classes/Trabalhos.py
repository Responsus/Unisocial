

class Trabalhos:
	_id = 0
	_nome = ''
	_data_entrega = 0
	_nota = 0
	_disciplina_id = 0
	_professor_id = 0

	def __init__(self,nome,dataentrega,nota,disciplinaid,professorid):
		self._nome = nome
		self._data_entrega = dataentrega
		self._nota = nota
		self._disciplina_id = disciplinaid
		self._professor_id = professorid

	def getNome(self):
		return self._nome

	def getDataEntrega(self):
		return self._data_entrega

	def getNota(self):
		return self._nota
	
	def getDisciplina(self):
		return self._disciplina_id

	def getProfessor(self):
		return self._professor_id
