from flask import Flask  #Importing Flask module
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy() #defining a database
DB_NAME = 'database.db'

def create_app():
    app = Flask(__name__) #Initializing our app. __name__ just represents name of file
        #Encrypts cookies and session data related to our website
    app.config['SECRET_KEY'] = 'ennuwenne4883985t85j3m9j93jf4inf293jeinf3'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}' #Database is stored in this location
    db.init_app(app)



    from .views import views 
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login' #redirects those who need to login
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

    # Created a flask application and initialized the secret key

def create_database(app):
    with app.app_context():
        db.create_all()
        print('Created Database!')
