from flask import Flask, request, render_template, redirect, session, flash, url_for
import hashlib 
app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'

# Simulação de banco de dados de usuários
users = {
    'usuario1': {
        'email': 'usuario1@example.com',
        'senha': hashlib.sha256('senha123'.encode()).hexdigest()
    }
}

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        senha = hashlib.sha256(request.form['senha'].encode()).hexdigest()

        if usuario in users and users[usuario]['senha'] == senha:
            session['usuario'] = usuario
            flash('Login bem-sucedido', 'success')
            return redirect(url_for('index'))
        else:
            flash('Credenciais inválidas', 'error')

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
