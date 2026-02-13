"""
Modelo de la base de datos
table: tareas
"""

# from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone, timedelta

from extensions import db
import random
import string
import secrets

# Crear la instalcia a la base de datos
# db = data base

# db = SQLAlchemy()


class Usuario(db.Model):
    """
    Model de Usuario
    representa a la tabla usuarios
    """

    __tablename__ = "usuarios"

    # columnas
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    # verificar el usuario
    verificado = db.Column(db.Boolean, default=False)
    codigo_verificacion = db.Column(db.String(6))
    codigo_expiracion = db.Column(db.DateTime)

    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    # relacion entre usuario y tareas
    tareas = db.relationship("Tarea", backref="usuario", lazy=True)

    def to_dict(self, incluir_tareas=False):
        data = {
            "id": self.id,
            "nombre": self.nombre,
            "email": self.email,
            "verificado": self.verificado,
            "created_at": self.created_at.isoformat(),
        }
        if incluir_tareas:
            data["tareas"] = [tarea.to_dict() for tarea in self.tareas]
            data["total_tarea"] = len(self.tareas)
        return data
    
    def generar_codigo_verificacion(self):
        """
        genera un codigo de verificacion de 6 caracteres
        """
        self.codigo_verificacion = secrets.token_hex(3).upper()
        # self.codigo_verificacion = ''.join(random.choice(string.digits, k=6))
        # vamos a definir un tiempo de expiracion 15 minutos
        # self.codigo_expiracion = datetime.now(timezone.utc) + timedelta(minutes=10)
        self.codigo_expiracion = datetime.utcnow() + timedelta(minutes=15)
        return self.codigo_verificacion
    
    def verificar_codigo(self, codigo):
        """Verifica si el codigo es correcto y no ha expirado"""
        # if self.codigo_verificacion == codigo and datetime.now(timezone.utc) < self.codigo_expiracion:
        #     self.verificado = True
        #     self.codigo_verificacion = None
        #     self.codigo_expiracion = None
        #     return True
        # return False
        if not self.codigo_verificacion or not self.codigo_expiracion:
            return False

        if datetime.utcnow() > self.codigo_expiracion:
        # if datetime.now(timezone.utc) > self.codigo_expiracion:
            return False

        return codigo == self.codigo_verificacion


class Tarea(db.Model):
    """
    Modelo de Tarea
    representa a la tabla tareas
    """

    __tablename__ = "tareas"

    # atributos de la tabla (columnas)
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(200), nullable=False)
    descripcion = db.Column(db.Text)
    categoria = db.Column(db.String(100))
    completado = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    # created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    # cuando creemos o actualicemo una tarea sera necesario incluir el campo (columano) user_id
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuarios.id"), nullable=False)

    def to_dict(self, incluir_usuario=False):
        """
        Convertir el objeto a un diccionario JSON
        """
        data = {
            "id": self.id,
            "titulo": self.titulo,
            "descripcion": self.descripcion,
            "categoria": self.categoria,
            "completado": self.completado,
            "usuario_id": self.usuario_id,
            "created_at": self.created_at.isoformat(),
        }
        if incluir_usuario:
            data["usuario"] = {
                "id": self.usuario.id,
                "nombre": self.usuario.nombre,
                "email": self.usuario.email,
            }
        return data
