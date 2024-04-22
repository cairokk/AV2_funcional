
#questao utilizada foi a primeira para ser executada quando o login for bem sucessido!

import hashlib
from flask import Flask, request, render_template
import q1_CairoQueiros as main_app
app = Flask(__name__, template_folder='templates_folder')

# Codificar a senha usando SHA-256
codificador = lambda senha: hashlib.sha256(senha.encode()).hexdigest()

users = lambda : {
    "sam2584": "a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3",
    "robs61286": "03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4",
}

bemVindo = lambda: f"bem vindo {request.form['username']}!"
senhaIncorreta = lambda: "senha incorreta!"
usuarioInexistente = lambda: "Usuario nao encontrado!"

senhasIguais = lambda dic: dic[request.form['username']] == codificador(request.form['password'])

# Determinar se a senha é válida ou não
verificarSenha = lambda: bemVindo() if senhasIguais(users()) else senhaIncorreta()

verificaUsuario = lambda: verificarSenha() if request.form['username'] in users() else usuarioInexistente()

reqresp = lambda: (
    (main_app.main(), bemVindo())[1] if senhasIguais(users()) else senhaIncorreta()
) if request.method == 'POST' else render_template('index.html')
app.add_url_rule('/', 'index', reqresp, methods=['GET', 'POST'])#chama a funcao main da questao 1 caso o login seja bem sucessido



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)

