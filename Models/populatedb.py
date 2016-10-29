#!/usr/bin/python

from Model import *

db.create_all()
# Criando Faculdades
fac = Faculdades("FMU",12312313)
fac1 = Faculdades("Uninove",22312313)
fac2 = Faculdades("Anhanguera",32312313)
db.session.add(fac)
db.session.add(fac1)
db.session.add(fac2)
#-----------------

# Criando Unidades
uni = Unidades("Vila Mariana","Rua Vergueiro, n 2132",1)
uni1 = Unidades("Tatuape","Rua Tuiuti, n 2132",1)
db.session.add(uni)
db.session.add(uni1)
# Adicionando unidade a faculdade
fac.unidades.append(uni)
fac.unidades.append(uni1)
#---------
#Criando Areas
area = Areas("Humanas")
area1 = Areas("Exatas")
area2 = Areas("Tecnologia")
area3 = Areas("Saude")
# Adicionando areas as faculdades
fac.areas.append(area)
fac.areas.append(area1)
fac.areas.append(area2)
fac1.areas.append(area3)
db.session.add(area)
db.session.add(area1)
db.session.add(area2)
db.session.add(area3)
# -----------------
#Criando Cursos
curso1 = Cursos("Ciencia da Computacao","Nenhuma",1)
curso2 = Cursos("Sistemas para Internet","Nenhuma",2)
db.session.add(curso1)
db.session.add(curso2)
curso = Cursos("Analise de Sistemas","Nenhuma",1)
db.session.add(curso)
# Associando curso a diciplina
cur_dir = Curso_Disciplina("Segunda","42")
cur_dir.disciplina = Disciplinas("Sistemas Distribuidos","Nenhuma")
cur_dir1 = Curso_Disciplina("Terca","18")
cur_dir1.disciplina =  Disciplinas("Algoritmos","Nenhuma")
disc2 = Disciplinas("Logica de Programacao","Nenhuma")
cur_dir2 = Curso_Disciplina("Quarta","13")
cur_dir2.disciplina = disc2
disc3 = Disciplinas("Auditoria de Sistemas","Nenhuma")
cur_dir3 = Curso_Disciplina("Quinta","42")
cur_dir3.disciplina = disc3
disc4 = Disciplinas("Redes de Computadores","Nenhuma")
cur_dir4 = Curso_Disciplina("Sexta","9")
cur_dir4.disciplina = disc4
curso.disciplinas.append(cur_dir)
curso.disciplinas.append(cur_dir1)
curso.disciplinas.append(cur_dir2)
curso.disciplinas.append(cur_dir3)
curso.disciplinas.append(cur_dir4)
#------------------
#Criando Periodos
per = Periodos("Matutino","09:00","10:00","12:00")
per1 = Periodos("Vespertino","13:00","15:00","18:00")
per2 = Periodos("Noturno","18:00","20:00","22:00")
db.session.add(per)
db.session.add(per1)
db.session.add(per2)
#--------- Criando Turmas
tur = Turmas(30,"20/02/2015","30/02/2016",1,1,1)
db.session.add(tur)
prof = Professores("Alisson Machado","alisson.copyleft@gmail.com","342557476","38606432822","alisson.demenezes","alisson.jpg","1234")
prof1 = Professores("Rafael Oliveira","rafael.cs@gmail.com","242557476","28606432822","rafael.silva","alisson.jpg","1234")
db.session.add(prof)
db.session.add(prof1)
# -------- Criando Alunos
aluno = Alunos("Alisson Menezes","alisson.copyleft@gmail.com.br","342557476","38606432822","alisson.demenezes","alisson.jpg","1234",1)
aluno1 = Alunos("Michael Douglas","michael.douglas@gmail.com.br","442557476","48606432822","alisson.demenezes","alisson.jpg","1234",1)
aluno2 = Alunos("Alana Menezes","alanamachado2@yahoo.com.br","542557476","58606432822","alisson.demenezes","alisson.jpg","1234",1)
db.session.add(aluno)
db.session.add(aluno1)
db.session.add(aluno2)
# --------- Salvando no banco
db.session.commit()
