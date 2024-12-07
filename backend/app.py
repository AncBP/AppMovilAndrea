from flask import Flask
from flask_restful import Api
from models import db
from routes import RegistrarUsuario,Usuario, Login, ListarProductos
from config import DATABASE_URI
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

CORS(app)
db.init_app(app)
api = Api(app)

# Rutas
api.add_resource(RegistrarUsuario, '/usuarios')
api.add_resource(Usuario, '/usuarios/<int:id>')
api.add_resource(Login, '/login')
api.add_resource(ListarProductos, '/productos')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  
    app.run(debug=True)