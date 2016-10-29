from flask import Flask, render_template,request,session,abort,jsonify,redirect,url_for, current_app
from flask.ext.script import Manager
from flask_mail import Mail,Message
from flask.ext.migrate import Migrate,MigrateCommand
import ConfigParser

#from Blueprints.IdentityRegister import IdentityRegister

# from Blueprints.AlunoViews import aluno
#from Blueprints.UsuarioViews import Usuario as UsuarioView
#from Blueprints.UsuarioAPI import UsuarioAPI
#from Blueprints.professor import professor


from api.Curso import Curso as CursoAPI
from api.Usuario import Usuario as UsuarioAPI
from api.Professor import Professor as ProfessorAPI
from api.Turma import Turma as TurmaAPI

from Models.Model import db
from Classes.Usuario import Usuario
from Classes.Alunos import Alunos
from ClassesDao.UsuarioDao import UsuarioDao
from ClassesDao.AlunosDao import AlunosDao


app = Flask(__name__)
with app.app_context():
    print current_app.name
app.config["DEBUG"] = True

app.config.update(
MAIL_SERVER = "mail.responsus.com.br",
MAIL_USERNAME = "no-reply@responsus.com.br",
MAIL_PASSWORD = "VALFmfEde8",
MAIL_USE_TLS = True,
MAIL_PORT = 587,
)
mail = Mail(app)

#IdentityRegister(app)

#config_parser = ConfigParser.ConfigParser()
#config_parser.read("/srv/unisocial/unisocial.ini")
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///%s'%config_parser.get('database','file').strip('"')

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

app.register_blueprint(UsuarioAPI)
app.register_blueprint(CursoAPI)
app.register_blueprint(ProfessorAPI)
app.register_blueprint(TurmaAPI)

#migrate = Migrate(app,db)

#manager = Manager(app)
#manager.add_command('db',MigrateCommand)

@app.route('/send/email/',methods=["POST"])
def email():
    try:
        mensagem = request.form["mensagem"]
        email = request.form["email"]
        assunto = request.form["assunto"]
        nome = request.form["nome"]
        msg = Message(subject=assunto,sender=email,recipients=["contato@unisocial.com.br"])
        msg.body = mensagem
        mail.send(msg)
        return jsonify({"status":0,"message":"Mensagem enviada com sucesso!"})
    except Exception as e:
        print e
        return jsonify({"status":1,"message":"Falhou ao enviar a mensagem! Tente novamente mais tarde %s"%e})


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login/aluno/')
def login_aluno():
    return render_template("aluno.html")

@app.route('/login/professor/')
def login_professor():
    return render_template("professor.html")

@app.route('/login/Usuario/')
def login_Usuario():
    return render_template("Usuario.html")

@app.route('/dologin/Usuario',methods=["POST","GET"])
def dologin_Usuario():
    try:
        email = request.form['user']
        senha = request.form['pass']

        Usuario = Usuario()
        Usuario.setEmail(email)
        Usuariodao = UsuarioDao(Usuario)
        res = Usuariodao.selectByEmail(email)
        print res
        if type(res) is dict:
            return jsonify(res)
        if res.getSenha() == str(senha):
            session['nome'] = res.getNome()
            session['id'] = res.getId()
            return redirect("/Usuario")
        else:
            return jsonify({"retorno":"Senha nao confere"})
    except Exception as e:
        return jsonify({"erro":"%s"%e})

@app.route("/logout/Usuario",methods=["GET"])
def logout_Usuario():
	try:
		session.pop("id",None)
		session.pop("nome",None)
		return redirect("/login/Usuario")
	except Exception as e:
		return jsonify({"erro":"Falhou ao deslogar %s"%e})

@app.route('/dologin/aluno',methods=["POST","GET"])
def dologin_aluno():
	try:
		email = request.form['user']
		senha = request.form['pass']

		aluno = Alunos()
		aluno.setEmail(email)
		alunosdao = AlunosDao(aluno)
		res = alunosdao.selectByEmail(email)
		if type(res) is dict:
			return jsonify(res)
		if res.getSenha() == str(senha):
			session['nome'] = res.getNome()
			session['aluno-id'] = res.getId()
			return redirect("/aluno")
		else:
			return jsonify({"retorno":"Senha/Email nao confere"})
	except Exception as e:
		return jsonify({"erro":"Aluno nao encontrado %s"%e})

@app.route("/logout/aluno",methods=["GET"])
def logout_aluno():
	try:
		session.pop("aluno-id",None)
		session.pop("nome",None)
		return redirect("/login/aluno")
	except Exception as e:
		return jsonify({"erro":"Falhou ao deslogar %s"%e})

if __name__ == '__main__':
    db.create_all()
    app.run(host="0.0.0.0",port=8080)
    #manager.run()
