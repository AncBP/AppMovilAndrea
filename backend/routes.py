from flask import request
from flask_restful import Resource
from models import db, Usuarios, Productos

class RegistrarUsuario(Resource):
    # Mostrar todos los usuarios
    def get(self):
        usuarios = Usuarios.query.all()  
        return [usuario.to_dict() for usuario in usuarios]  

    # Registrar un nuevo usuario
    def post(self):
        data = request.json
        new_user = Usuarios(nombre=data['nombre'], correo=data['correo'], contrasena=data['contrasena'])
        db.session.add(new_user)
        db.session.commit()
        return {"message": "Usuario registrado exitosamente"}, 201

class Usuario(Resource):
    # Mostrar un usuario por su ID
    def get(self, id):
        user = Usuarios.query.get(id) 
        if user:
            return user.to_dict() 
        return {"message": "Usuario no encontrado"}, 404

class Login(Resource):
    def post(self):
        data = request.json
        user = Usuarios.query.filter_by(correo=data['correo'], contrasena=data['contrasena']).first()
        if user:
            return {"message": "Inicio de sesión exitoso", "usuario": user.to_dict()}, 200
        return {"message": "Credenciales inválidas"}, 401

class ListarProductos(Resource):
    # Obtener todos los productos
    def get(self):
        products = Productos.query.all()  
        return [product.to_dict() for product in products]  
    
    # Agregar un nuevo producto
    def post(self):
        data = request.json
        new_product = Productos(nombre=data['nombre'], descripcion=data['descripcion'], precio=data['precio'])
        db.session.add(new_product)
        db.session.commit()
        return {"message": "Producto agregado con éxito"}, 201
