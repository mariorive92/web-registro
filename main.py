from flask import Flask,render_template,request,url_for,redirect,flash
import db
from models import Registro





app = Flask(__name__) # la app se encuentra en el  servidor web de Flask

# Aqui he creado una ruta al entrar a la web para hacer un login antes de entrar directamente al registro
@app.route('/')
def hola_mundo():
   return  render_template("login.html")
# Aqui doy yo el usuario y la clave de entrada, para que pueda yo dar accceso a las personas
database={'Registro':'123'}
# En esta parte del codigo de abajo hago un condicional para que coincidan el usuario y el password en los campos indicados
@app.route('/', methods=['POST','GET'])
def login():
   name1=request.form['username']
   pwd=request.form['password']
   if name1 not in database:
       return render_template('login.html', info='Usuario Invalido')
   else:
       if database[name1]!=pwd:
           return render_template('login.html', info='Contraseña Invalida')
       else:
           # En el else he puesto que si se introducen los terminos correctos accedas directamente al index.html de registros
           return render_template('index.html', name=name1)

# la linea de codigo de abajo esta relacionada con la pestaña que aparece de registro creado cunado introduces  los campos asi como cuando eliminas el registro
app.secret_key='mysecretkey'

#creacion de la ruta principal para realizar el registro
@app.route('/home')
def home():
    todos_los_registro = db.session.query(Registro).all() # Consultar y almacenar informacion en la base de datos
    return render_template("index.html", lista_de_registro= todos_los_registro) # Aqui carge el render_template que va con el index.html y la lista de registros que luego manipularemos con Flask


# Ruta para crear registros
@app.route('/crear-registro', methods=['POST'])
def crear():
      #Los registros vienen de la clase registro , abajo vienen los campos asignados o lo que vendria a ser los atributos de la clase
     registro = Registro(nombre=request.form['nombre_registro'], email=request.form['email'], telefono=request.form['telefono'], ciudad=request.form['ciudad']) # id no es necesario asignarlo manualmente, porque la primary key se genera automáticamente
     db.session.add(registro) # Aññadir registro
     db.session.commit()# Guradar registro
     flash('Contacto creado.')#Nombre asignado a la pestaña que aparece cuando se crea el registro
     return redirect(url_for('home'))# poner url_for("homa") hace que no se nos cambie la ruta se quede en home y no me de error

# Ruta para eliminar registros
@app.route('/eliminar-registro/<id>')
def eliminar(id):
    registro = db.session.query(Registro).filter_by(id=int(id)).delete() # Busca y elimina informacion deseada en la base de datos
    db.session.commit()# Guarda los cambios
    flash('Contacto Eliminado.')# Esto es lo mismo explicado anteriormente pero ahora aparece al eliminar el registro
    return  redirect(url_for('home'))


# Creacion de la ruta registro-hecho, aqui no tiene mucho sentido ya que en cuanto escribes la informacion y le das a guardar ya estaria pero lo he querido dejar
@app.route('/registro-hecho/<id>')
def hecho(id):
    registro = db.session.query(Registro).filter_by(id=int(id)).first() # seleciona internamente el registro marcado
    db.session.commit()
    return redirect(url_for('home'))



if __name__ == '__main__':
    db.Base.metadata.create_all(db.engine) # Creacion del modelo de datos
    app.run(debug=True)  # Debug a True para cada vez que modifique el codigo se cambie automaticamente


