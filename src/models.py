from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    name = db.Column(db.String(250), nullable=False)
    address1 = db.Column(db.String(250), nullable=False) 
    favoritos = db.relationship('Favoritos', backref='owner') 

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "name": self.name,
            "address1": self.address1
            # do not serialize the password, its a security breach
        }
    

class Personajes(db.Model):
    # __tablename__ = 'characters'
    id = db.Column(db.Integer, primary_key=True)
    favoritos = db.relationship('Favoritos', backref='personajes')
    name = db.Column(db.String(250), nullable=False)
    clasificacion = db.Column(db.String(250), nullable=False)
    lenguaje = db.Column(db.String(250), nullable=False)
    def serialize(self):
        return{
            "id": self.id,
            "favoritos": self.favoritos,
            "name": self.name,
            "clasificacion": self.clasificacion,
            "lenguaje": self.lenguaje
        }

class Planets(db.Model):
    # __tablename__ = 'planetas'
    id = db.Column(db.Integer, primary_key=True)
    favoritos = db.relationship('Favoritos', backref='planets')
    name = db.Column(db.String(250), nullable=False)
    gravity = db.Column(db.String(250), nullable=False)
    def serialize(self):
        return{
            "id": self.id,
            "favoritos": self.favoritos,
            "name": self.name,
            "gravity": self.gravity
        }

class Favoritos(db.Model):
    # __tablename__ = 'favoritos'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    url = db.Column(db.String(250))
    personaje_id = db.Column(db.Integer, db.ForeignKey('personajes.id'), nullable=True)
    planet_id = db.Column(db.Integer, db.ForeignKey('planets.id'), nullable=True)
    def serialize(self):
        return{
            "id": self.id,
            "user_id": self.user_id,
            "personaje_id": self.personaje_id,
            "planet_id": self.planet_id
        }