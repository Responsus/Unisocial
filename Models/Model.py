from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy,BaseQuery
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import backref
from sqlalchemy.sql import func
from datetime import datetime
import ConfigParser
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://unisocial:CXZ!@#azxc1@62.151.181.253/unisocial'

db = SQLAlchemy(app)


# Tabelas associativas #
#unidades_areas = db.Table("Unidades_Areas",
#	db.Column("unidade_id",db.Integer,db.ForeignKey("Unidades.id")),
#	db.Column("area_id",db.Integer,db.ForeignKey("Areas.id"))
#	)

#unidades_cursos = db.Table("Unidades_Cursos",
#	db.Column("unidade_id",db.Integer,db.ForeignKey("Unidades.id")),
#	db.Column("curso_id",db.Integer,db.ForeignKey("Cursos.id"))
#	)

#professor_aula = db.Table("Professor_aulas",
#	db.Column("professor_id",db.Integer,db.ForeignKey("Professores.id")),
#	db.Column("aula_id",db.Integer,db.ForeignKey("aulas.id"))
#	)

#professor_area = db.Table("Professor_Areas",
#	db.Column("professor_id",db.Integer,db.ForeignKey("Professores.id")),
#	db.Column("area_id",db.Integer,db.ForeignKey("Areas.id"))
#	)

#grupo_aluno = db.Table("Grupo_Aluno",
#	db.Column("grupo_id",db.Integer,db.ForeignKey("Grupos.id")),
#	db.Column("aluno_id",db.Integer,db.ForeignKey("Alunos.id"))
#	)

#faculdade_professor = db.Table("Faculdade_Professor",
#	db.Column("faculdade_id",db.Integer,db.ForeignKey("Usuarios.id")),
#	db.Column("professor_id",db.Integer,db.ForeignKey("Professores.id"))
#	)
#
#faculdade_area = db.Table("Faculdade_Area",
#	db.Column("faculdade_id",db.Integer,db.ForeignKey("Usuarios.id")),
#	db.Column("area_id",db.Integer,db.ForeignKey("Areas.id"))
#	)
#area_aula = db.Table("Area_aula",
#	db.Column("area_id",db.Integer,db.ForeignKey("Areas.id")),
#	db.Column("aula_id",db.Integer,db.ForeignKey("aulas.id"))
#	)

usuario_aluno = db.Table("usuario_aluno",
	db.Column("usuario_id",db.Integer,db.ForeignKey("usuarios.id")),
	db.Column("aluno_id",db.Integer,db.ForeignKey("alunos.id"))
	)

turma_aluno  = db.Table("turma_aluno",
		db.Column("turma_id",db.Integer,db.ForeignKey("turmas.id")),
		db.Column("aluno_id",db.Integer,db.ForeignKey("alunos.id"))
	)

curso_aula  = db.Table("curso_aula",
		db.Column("curso_id",db.Integer,db.ForeignKey("cursos.id")),
		db.Column("aula_id",db.Integer,db.ForeignKey("aulas.id"))
	)

professor_curso  = db.Table("professor_curso",
		db.Column("professor_id",db.Integer,db.ForeignKey("professores.id")),
		db.Column("curso_id",db.Integer,db.ForeignKey("cursos.id"))
	)

professor_aula  = db.Table("professor_aula",
		db.Column("professor_id",db.Integer,db.ForeignKey("professores.id")),
		db.Column("aula_id",db.Integer,db.ForeignKey("aulas.id"))
	)
#modulo_aula  = db.Table("Modulo_aula",
#		db.Column("modulo_id",db.Integer,db.ForeignKey("Modulos.id")),
#		db.Column("aula_id",db.Integer,db.ForeignKey("aulas.id"))
#	)
# fim #


class Usuarios(db.Model):
    __tablename__ = "usuarios"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True)
    cnpj = db.Column(db.String(120), unique=True)
    senha = db.Column(db.String(120))
    #unidades = db.relationship('Unidades')
    cursos = db.relationship('Cursos')
    #professores = db.relationship("Professores",secondary=faculdade_professor,backref="Usuarios")
    #areas = db.relationship("Areas",secondary=faculdade_area,backref="Usuarios")
    alunos = db.relationship("Alunos",secondary=usuario_aluno,backref="Usuarios")

    def __init__(self,usuario):
        self.nome = usuario.nome
        self.email = usuario.email
        self.senha = usuario.senha
        self.cnpj = usuario.cnpj

#class Unidades(db.Model):
#	__tablename__ = "Unidades"
#	id = db.Column(db.Integer, primary_key=True)
#	nome = db.Column(db.String(80))
#	endereco = db.Column(db.String(120))
#	turmas = db.relationship("Turmas")
#	faculdade_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'))
#	areas = db.relationship("Areas",secondary=unidades_areas,backref='Unidades')
#	cursos = db.relationship("Cursos",secondary=unidades_cursos,backref="Unidades")
#
#	def __init__(self,unidade):
#		self.nome = unidade.getNome()
#		self.endereco = unidade.getEndereco()
#		self.faculdade_id = unidade.getFaculdade().getId()

class Areas(db.Model):
	__tablename__ = "areas"
	id = db.Column(db.Integer, primary_key=True)
	nome = db.Column(db.String(80))
	usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'))
	#aulas = db.relationship("aulas",secondary=area_aula)
	cursos = db.relationship("Cursos")

	def __init__(self, area):
		self.nome = area.getNome()
		self.faculdade_id = area.getFaculdade().getId()

class Tipos(db.Model):
	__tablename__ = "tipos"
	id = db.Column(db.Integer, primary_key=True)
	nome = db.Column(db.String(80))
	usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'))
	cursos = db.relationship("Cursos")

	def __init__(self, tipos):
		self.nome = tipos.getNome()
		self.faculdade_id = tipos.getFaculdade().getId()


class Cursos(db.Model):
    __tablename__ = "cursos"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80))
    descricao = db.Column(db.String(120))
    aulas = db.relationship("Aulas",secondary=curso_aula,backref="Cursos")
    #	modulos = db.relationship("Modulos",cascade="all, delete-orphan")
    turmas = db.relationship("Turmas")
    #	matrizcurricular = db.relationship("MatrizCurricular")
    area_id = db.Column(db.Integer, db.ForeignKey("areas.id"))
    tipo_id = db.Column(db.Integer, db.ForeignKey("tipos.id"))
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuarios.id"))

    def __init__(self,curso):
        self.nome = curso.nome
        self.descricao = curso.descricao
        self.usuario_id = curso.usuario_id


# class Modulos(db.Model):
#     __tablename__ = "Modulos"
#     id = db.Column(db.Integer, primary_key=True)
#     nome = db.Column(db.String(80))
#     aulas = db.relationship("aulas",cascade="all",secondary=modulo_aula,backref="Modulos")
#     curso_id = db.Column(db.Integer,db.ForeignKey("Cursos.id"))
#     turmas = db.relationship("Turmas")
#
#     def __init__(self,modulo):
#         self.nome = modulo.getNome()


class Aulas(db.Model):
	__tablename__ = "aulas"
	id = db.Column(db.Integer, primary_key=True)
	nome = db.Column(db.String(80))
	descricao = db.Column(db.String(120))
	# trabalhos = db.relationship("Trabalhos")
	#modulo_id = db.Column(db.Integer,db.ForeignKey("Modulos.id"))


	def __init__(self,aula):
		self.nome = aula.nome
		self.descricao = aula.descricao
		#self.modulo_id = aula.getModulo().getId()

#class Grade(db.Model):
#    __tablename__ = "Grade"
#    id = db.Column(db.Integer,primary_key=True)
#    turma_id = db.Column(db.Integer,db.ForeignKey("Turmas.id"))
#    curso_id = db.Column(db.Integer,db.ForeignKey("Cursos.id"))
#    aulas_id = db.Column(db.Integer,db.ForeignKey("aulas.id"))
#    professor_id = db.Column(db.Integer,db.ForeignKey("Professores.id"))
#    dia = db.Column(db.String(50))
#    sala = db.Column(db.String(50))
#
#    def __init__(self,turma,curso,aula,professor=None,dia=None,sala=None):
#        self.turma_id = turma
#        self.curso_id = curso
        # self.aula_id = aulas
        # self.professor_id = professor
        # self.dia = dia
        # self.sala = sala


class Turmas(db.Model):
    __tablename__ = "turmas"
    id = db.Column(db.Integer, primary_key=True)
    limite_alunos = db.Column(db.Integer)
    data_inicio = db.Column(db.Date)
    data_fim = db.Column(db.Date)
    curso_id = db.Column(db.Integer,db.ForeignKey("cursos.id"))
    aluno = db.relationship("Alunos",secondary=turma_aluno,backref="Turmas")

    def __init__(self,turma):
        self.limite_alunos = turma.limite_alunos
        print datetime.strptime(turma.data_inicio,"%d/%m/%Y")
        self.data_inicio = datetime.strptime(turma.data_inicio,"%d/%m/%Y")
        self.data_fim = datetime.strptime(turma.data_fim,"%d/%m/%Y")
        self.curso_id = turma.curso_id

# class Grupos(db.Model):
# 	__tablename__ = "Grupos"
# 	id = db.Column(db.Integer, primary_key=True)
# 	nome = db.Column(db.String(80))
# 	quantidade_integrantes = db.Column(db.Integer)
# 	alunos = db.relationship("Alunos",secondary=grupo_aluno,backref="Grupos")
# 	trabalho_id = db.Column(db.Integer,db.ForeignKey("Trabalhos.id"))
#
# 	def __init__(self,nome,quantidade_integrantes,trabalho_id):
# 		self.nome = nome
# 		self.quantidade_integrantes = quantidade_integrantes
# 		self.trabalho_id = trabalho_id

class Alunos(db.Model):
	__tablename__ = "alunos"
	id = db.Column(db.Integer, primary_key=True)
	nome = db.Column(db.String(80))
	email = db.Column(db.String(120), unique=True)
	rg = db.Column(db.String(120), unique=True)
	cpf = db.Column(db.String(120), unique=True)
	celular = db.Column(db.String(20))
	telefone = db.Column(db.String(20))
	facebook = db.Column(db.String(120))
	senha = db.Column(db.String(120))

	def __init__(self,aluno):
		self.nome = aluno.getNome()
		self.email = aluno.getEmail()
		self.rg = aluno.getRg()
		self.cpf = aluno.getCpf()
		self.celular = aluno.getCelular()
		self.telefone = aluno.getTelefone()
		self.facebook = aluno.getFacebook()
		self.senha = aluno.getSenha()

class Professores(db.Model):
    __tablename__ = "professores"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True)
    rg = db.Column(db.String(120), unique=True)
    cpf = db.Column(db.String(120), unique=True)
    facebook = db.Column(db.String(120))
    senha = db.Column(db.String(120))
    # areas = db.relationship("Areas",secondary=professor_area,backref="Professores")
    # aulas = db.relationship("aulas",secondary=professor_aula,backref="Professores")
    # curriculo = db.relationship("Curriculos")
    # trabalhos = db.relationship("Trabalhos")
    cursos = db.relationship("Cursos",secondary=professor_curso,backref="Professores")

    def __init__(self,professor):
        self.nome = professor.nome
        self.email = professor.email

# class Historicos(db.Model):
# 	__tablename__ = "Historicos"
# 	id = db.Column(db.Integer, primary_key=True)
# 	aluno_id = db.Column(db.String(80))
# 	aula_id = db.Column(db.String(120))
# 	nota = db.Column(db.String(120))


# class Periodos(db.Model):
# 	__tablename__ = "Periodos"
# 	id = db.Column(db.Integer, primary_key=True)
# 	nome = db.Column(db.String(80))
# 	inicio = db.Column(db.String(120))
# 	intervalo = db.Column(db.String(120))
# 	termino = db.Column(db.String(120))
# 	faculdade_id = db.Column(db.Integer,db.ForeignKey("Usuarios.id"))
# 	turmas = db.relationship("Turmas")
#
# 	def __init__(self,periodo):
# 		self.nome = periodo.getNome()
# 		self.inicio = periodo.getInicio()
# 		self.intervalo = periodo.getIntervalo()
# 		self.termino = periodo.getTermino()
# 		self.faculdade_id = periodo.getFaculdade().getId()
#
# class Trabalhos(db.Model):
# 	__tablename__ = "Trabalhos"
# 	id = db.Column(db.Integer, primary_key=True)
# 	nome = db.Column(db.String(80))
# 	data_entrega = db.Column(db.String(120))
# 	nota = db.Column(db.Integer)
# 	aula_id = db.Column(db.Integer,db.ForeignKey("aulas.id"))
# 	professor_id = db.Column(db.Integer,db.ForeignKey("Professores.id"))
#
# 	def __init__(self,nome,data_entrega,nota,aula_id,professor_id):
# 		self.nome = nome
# 		self.data_entrega = data_entrega
# 		self.nota = nota
# 		self.aula_id = aula_id
# 		self.professor_id = professor_id
#
#
# class Curriculos(db.Model):
# 	__tablename__ = "Curriculos"
# 	id = db.Column(db.Integer, primary_key=True)
# 	nome = db.Column(db.String(80), unique=True)
# 	inicio = db.Column(db.String(120), unique=True)
# 	intervalo = db.Column(db.String(120), unique=True)
# 	termino = db.Column(db.String(120), unique=True)
# 	professor_id = db.Column(db.Integer,db.ForeignKey("Professores.id"))
#
# class MatrizCurricular(db.Model):
# 	__tablename__ = "MatrizCurricular"
# 	id = db.Column(db.Integer, primary_key=True)
# 	descricao = db.Column(db.String(120))
# 	curso_id = db.Column(db.Integer,db.ForeignKey("Cursos.id"))
