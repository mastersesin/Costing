from flask import Flask
from flask_cors import CORS
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import IntegrityError
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = 'trantrongtyckiuzk4ever!@#!!!@@##!*&%^$$#$'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://dishorder_PS:123456@10.1.1.11:5430/costing'
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'], echo=False)
Base = declarative_base()
from AppFolder.SqlClasses import models

Base.metadata.create_all(engine)
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()
session.commit()
from AppFolder.Views.views import costing

app.register_blueprint(costing)
