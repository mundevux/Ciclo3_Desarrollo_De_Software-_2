import os
from flask import Flask, render_template, flash, redirect, url_for
from form import Forminicio

app = Flask(__name__)   # crearuna aplicacion en Flask
app.secret_key = os.urandom(24)  # generar token
@app.route('/')
@app.route('/index')
def index():
  return render_template('index.html',titulo='Formulario')
  
@app.route('/login', methods=['GET', 'POST'] )
def login():
  form = Forminicio()
  if(form.validate_on_submit()):
    flash('Inicio de sesion solicitado por el usuario: {}'.format(form.nombre.data)) 
    return redirect(url_for('gracias'))
  return render_template('iniciar_sesion.html', titulo='Iniciar Sesión', form=form)

@app.route('/gracias')
def gracias():
    return render_template('gracias.html',titulo='Gracias')