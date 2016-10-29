
import sys

sys.path.append("/home/alisson/alisson/unisocial")
from Models.Model import db,Turmas as TurmasModel, Unidades as UnidadesModel, Periodos as PeriodosModel, Cursos as CursosModel, Alunos as AlunosModel, Modulos as ModulosModel
from Classes.Turmas import Turmas as TurmasClass
from Classes.Unidades import Unidades as UnidadesClass
from Classes.Periodos import Periodos as PeriodosClass
from Classes.Cursos import Cursos as CursosClass
from Classes.Alunos import Alunos as AlunosClass
from Classes.Modulos import Modulos as ModulosClass


class TurmasDao:

    _curso = ''	

    def __init__(self,turma=""):
        self._turma = turma

    def save(self):
        try:
            turma =  TurmasModel(self._turma)
            db.session.add(turma)
            db.session.commit()
            return {"status":0,"message":"Turma salva com sucesso!"}
        except Exception as e:
            print "Falhou ",e
            print "Falhou ao salvar o turma",e
            print "Fazendo Rollback"
            db.session.rollback()
            return {"status":1,"message":"Falhou ao salvar turma %s"%e}

    def select(self,turmaid):
        try:
            lista_turmas = []
            turmas = TurmasModel.query.filter(TurmasModel.id==turmaid).first()

            turma = TurmasClass()
            unidade = UnidadesClass()
            periodo = PeriodosClass()
            curso = CursosClass()
            modulo = ModulosClass()

            u = UnidadesModel.query.filter(UnidadesModel.id==turmas.unidade_id).first()
            unidade.setId(u.id)
            unidade.setNome(u.nome)

            p = PeriodosModel.query.filter(PeriodosModel.id==turmas.periodo_id).first()
            periodo.setId(p.id)
            periodo.setNome(p.nome)

            c = CursosModel.query.filter(CursosModel.id==turmas.curso_id).first()
            curso.setId(c.id)
            curso.setNome(c.nome)

            m = ModulosModel.query.filter(ModulosModel.id==turmas.modulo_id).first()
            modulo.setId(m.id)
            modulo.setNome(m.nome)

            turma.setId(turmas.id)
            turma.setDataInicio(turmas.data_inicio)
            turma.setDataFim(turmas.data_fim)
            turma.setUnidade(unidade)
            turma.setCurso(curso)
            turma.setPeriodo(periodo)
            turma.setModulo(modulo)

            alunos = db.session.query(TurmasModel).join(TurmasModel.aluno).filter(TurmasModel.id==turmas.id)
            lista_alunos = []
            for a in alunos:
	            for i in a.aluno:
		            aluno = AlunosClass()
		            aluno.setId(i.id)
		            aluno.setNome(i.nome)
		            lista_alunos.append(aluno)

            turma.setAlunos(lista_alunos)

            return turma
        except Exception as e:
            print "Falhu %s"%e
            return {"status":"1","message":"Falhou ao listar disciplinas %s"%e}

	def delete(self):
		try:
			turma = TurmasModel.query.filter(TurmasModel.id==self._turma.getId()).first()
			db.session.delete(turma)
			db.session.commit()
			return {"status":"0","message":"Turma removido com sucesso"}
		except Exception as e:
			db.session.rollback()
			print "Falhou ",e
			return {"status":1,"message":"Falhou ao remover turma %s"%e}

    def list(self,faculdadeid):
        try:
            lista_turmas = []
            turmas = TurmasModel.query.all()
            for t in turmas:
                print t.id
                turma = TurmasClass()
                unidade = UnidadesClass()
                periodo = PeriodosClass()
                curso = CursosClass()
                modulo = ModulosClass()

                u = UnidadesModel.query.filter(UnidadesModel.id==t.unidade_id).first()
                unidade.setId(u.id)
                unidade.setNome(u.nome)

                p = PeriodosModel.query.filter(PeriodosModel.id==t.periodo_id).first()
                periodo.setId(p.id)
                periodo.setNome(p.nome)

                c = CursosModel.query.filter(CursosModel.id==t.curso_id).first()
                curso.setId(c.id)
                curso.setNome(c.nome)

                m = ModulosModel.query.filter(ModulosModel.id==t.modulo_id).first()
                modulo.setId(m.id)
                modulo.setNome(m.nome)

                turma.setId(t.id)
                turma.setDataInicio(t.data_inicio)
                turma.setDataFim(t.data_fim)
                turma.setUnidade(unidade)
                turma.setCurso(curso)
                turma.setPeriodo(periodo)
                turma.setModulo(modulo)
                alunos = db.session.query(TurmasModel).join(TurmasModel.aluno).filter(TurmasModel.id==t.id)
                lista_alunos = []
                for a in alunos:
                    for i in a.aluno:
                        aluno = AlunosClass()
                        aluno.setId(i.id)
                        aluno.setNome(i.nome)
                        lista_alunos.append(aluno)

                turma.setAlunos(lista_alunos)

                lista_turmas.append(turma)
            return lista_turmas
        except Exception as e:
            print "Falhou %s"%e
            return {"status":"1","message":"Falhou ao listar disciplinas %s"%e}

	def incluirAluno(self,turma,aluno):
		try:
			t = TurmasModel.query.filter(TurmasModel.id==turma.getId()).first()
			a = AlunosModel.query.filter(AlunosModel.id==aluno.getId()).first()
			t.aluno.append(a)
			db.session.commit()
			return {"status":"0","message":"Aluno incluido com sucesso"}
		except Exception as e:
			print "Falhou %s"%e
			db.session.rollback()
			return {"status":"1","message":"Falhou ao incluir aluno na turma%s"%e}

	def removerAluno(self,turma,aluno):
		try:
			t = TurmasModel.query.filter(TurmasModel.id==turma.getId()).first()
			a = AlunosModel.query.filter(AlunosModel.id==aluno.getId()).first()
			turma.aluno.remove(a)
			db.session.commit()
			return {"status":"0","message":"Aluno removido com sucesso"}
		except Exception as e:
			print "Falhou %s"%e
			db.session.rollback()
			return {"status":"1","message":"Falhou ao remover aluno da turma%s"%e}

		

