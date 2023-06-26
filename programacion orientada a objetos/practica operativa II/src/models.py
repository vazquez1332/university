from __main__ import app
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy(app)

class Preceptor(db.Model):
    __tablename__ = "preceptor"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    apellido = db.Column(db.String(80), nullable=False)
    correo = db.Column(db.String(80), unique=True, nullable=False)
    clave = db.Column(db.String(80), nullable=True)
    cursos = db.relationship("Curso", backref="preceptor", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Preceptor {self.id}: {self.nombre} {self.apellido}>"

class Curso(db.Model):
    __tablename__ = 'curso'
    id = db.Column(db.Integer, primary_key=True)
    anio = db.Column(db.Integer, nullable=False)
    division = db.Column(db.Integer, nullable=False)
    idpreceptor = db.Column(db.Integer, db.ForeignKey('preceptor.id'), nullable=False)
    estudiantes = db.relationship('Estudiante', backref='curso', cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Curso {self.id}: {self.anio} - {self.division}>"

class Estudiante(db.Model):
    __tablename__ = 'estudiante'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    apellido = db.Column(db.String(80), nullable=False)
    dni = db.Column(db.String(80), nullable=False)
    idcurso = db.Column(db.Integer, db.ForeignKey('curso.id'), nullable=False)
    idpadre = db.Column(db.Integer, db.ForeignKey('padre.id'))
    asistencias = db.relationship('Asistencia', backref='estudiante', cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Estudiante {self.id}: {self.nombre} {self.apellido}>"

class Asistencia(db.Model):
    __tablename__ = 'asistencia'
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    codigoclase = db.Column(db.Integer, nullable=False)
    asistio = db.Column(db.String(1), nullable=False)
    justificacion = db.Column(db.String(80), nullable=True)
    idestudiante = db.Column(db.Integer, db.ForeignKey('estudiante.id'), nullable=False)

    def __repr__(self):
        return f"<Asistencia {self.id}: {self.fecha} - {self.codigoclase} - {self.asistio} - {self.justificacion} - {self.idestudiante}>"

class Padre(db.Model):
    __tablename__ = 'padre'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    apellido = db.Column(db.String(80), nullable=False)
    correo = db.Column(db.String(80), unique=True, nullable=False)
    clave = db.Column(db.String(80), nullable=True)
    estudiantes = db.relationship('Estudiante', backref='padre', cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Padre {self.id}: {self.nombre} {self.apellido}>"

with app.app_context():
    db.create_all()