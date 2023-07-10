import db
from sqlalchemy import Column, Integer, String

# Creacion de la clase
class Registro(db.Base):
 __tablename__ = "registro"# Nombre de la base de datos
 id = Column(Integer, primary_key=True) # Indentificador unico para cada registro con True al primary_key
 nombre= Column(String(200), nullable=False)# en el nombre, email y ciudad  he puesto un maximo de 200 caracteres de texto
 email= Column(String(200))
 telefono= Column(Integer)# Tipo de dato entero
 ciudad=Column(String(200))
 def __init__(self,nombre,email,telefono,ciudad): # creacion del contructor con sus atributos
    self.nombre=nombre
    self.email=email
    self.telefono=telefono
    self.ciudad=ciudad

 def __repr__(self): # Metodo repr
    return "Registro {}: {} {} {} ({})({})".format(self.id, self.nombre,self.email, self.telefono,self.ciudad)

 def __str__(self):# Metodo str de impresion
    return "Registro {}: {} {} {} ({})({})".format(self.id, self.nombre, self.email, self.telefono,self.ciudad)


