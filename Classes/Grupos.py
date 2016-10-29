
class Grupos:
	_id = 0
	_nome = ''
	_quantidade_integrantes = 0
	_trabalho_id = 0

	def __init__(self,nome,qtdintegrantes,trabalhoid):
		self._nome = nome
		self._quantidade_integrantes = qtdintegrantes
		self._trabalho_id = trabalhoid

	def getNome(self):
		return self._nome

	def getQuantidadeIntegrantes(self):
		return self._quantidade_integrantes

	def getTrabalhoId(self):
		return self._id
