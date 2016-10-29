from flask import Flask,Blueprint,render_template,abort,session
from api.UsuarioAPI import *

UsuarioAPI = Blueprint('UsuarioAPI',__name__,template_folder='templates')


def force_auth():
    if not 'id' in session:
        abort(401)
    elif int(session['id']) != int(request.url.split("/")[5]):
        abort(401)

UsuarioAPI.before_request(force_auth)

area_view = AreaAPI.as_view('areas_api')
UsuarioAPI.add_url_rule('/api/usuario/<int:usuarioid>/areas/',
					defaults={'idarea':None},
					view_func=area_view,
					methods=["GET"]
				)
UsuarioAPI.add_url_rule('/api/usuario/<int:usuarioid>/areas/',
					view_func=area_view,
					methods=["POST"]
				)
UsuarioAPI.add_url_rule('/api/usuario/<int:usuarioid>/areas/<int:areasid>/',
					view_func=area_view,
					methods=["GET","PUT","DELETE"]
				)

tipo_view = TipoAPI.as_view('tipo_api')
UsuarioAPI.add_url_rule('/api/usuario/<int:usuarioid>/tipos/',
					defaults={'idtipo':None},
					view_func=tipo_view,
					methods=["GET"]
				)
UsuarioAPI.add_url_rule('/api/usuario/<int:usuarioid>/tipos/',
					defaults={'idunidade':None},
					view_func=tipo_view,
					methods=["POST"]
				)
UsuarioAPI.add_url_rule('/api/usuario/<int:usuarioid>/tipos/<int:idtipo>',
					view_func=tipo_view,
					methods=["GET","PUT","DELETE"]
				)

periodo_view = PeriodoAPI.as_view('periodo_api')
UsuarioAPI.add_url_rule('/api/usuario/<int:usuarioid>/periodos/',
					defaults={'idperiodo':None},
					view_func=periodo_view,
					methods=["GET"]
				)
UsuarioAPI.add_url_rule('/api/usuario/<int:usuarioid>/periodos/',
					view_func=periodo_view,
					methods=["POST"]
				)
UsuarioAPI.add_url_rule('/api/usuario/<int:usuarioid>/periodos/<int:periodoid>/',
					view_func=periodo_view,
					methods=["GET","PUT","DELETE"]
				)

disciplina_view = DisciplinaAPI.as_view('disciplina_api')
UsuarioAPI.add_url_rule('/api/usuario/<int:usuarioid>/areas/<int:areaid>/disciplinas/',
					defaults={"iddisciplinas":None},
					view_func=disciplina_view,
					methods=["GET"]
				)
UsuarioAPI.add_url_rule('/api/usuario/<int:usuarioid>/disciplinas/',
					view_func=disciplina_view,
					methods=["POST"]
				)
UsuarioAPI.add_url_rule('/api/usuario/<int:usuarioid>/disciplinas/<int:disciplinaid>/',
					view_func=disciplina_view,
					methods=["GET","PUT","DELETE"]
				)

turmas_view = TurmasAPI.as_view('turmas_api')
UsuarioAPI.add_url_rule('/api/usuario/<int:usuarioid>/turmas/',
					defaults={'turmaid':None},
					view_func=turmas_view,
					methods=["GET"]
				)
UsuarioAPI.add_url_rule('/api/usuario/<int:usuarioid>/turmas/',
					view_func=turmas_view,
					defaults={"alunoid":None,"turmaid":None},
					methods=["POST"]
				)
UsuarioAPI.add_url_rule('/api/usuario/<int:usuarioid>/turmas/<int:turmaid>/',
					view_func=turmas_view,
					methods=["GET","PUT","DELETE"]
				)

UsuarioAPI.add_url_rule('/api/usuario/<int:usuarioid>/turmas/<int:turmaid>/aluno/<int:alunoid>/',
					view_func=turmas_view,
					methods=["POST","DELETE"]
				)


alunos_view = AlunosAPI.as_view('alunos_api')
UsuarioAPI.add_url_rule('/api/usuario/<int:usuarioid>/alunos/',
					defaults={'alunoid':None},
					view_func=alunos_view,
					methods=["GET"]
				)
UsuarioAPI.add_url_rule('/api/usuario/<int:usuarioid>/alunos/',
					view_func=alunos_view,
					methods=["POST"]
				)
UsuarioAPI.add_url_rule('/api/usuario/<int:usuarioid>/alunos/<int:alunoid>/',
					view_func=alunos_view,
					methods=["GET","PUT","DELETE"]
				)

modulos_view = ModulosAPI.as_view('modulos_api')
UsuarioAPI.add_url_rule('/api/usuario/<int:usuarioid>/modulos/<int:moduloid>/',
					view_func=modulos_view,
					methods=["GET"]
				)
