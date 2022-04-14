from flask import Flask, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

import config

db = SQLAlchemy()
migrate = Migrate()

def create_app() :
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app) 
    migrate.init_app(app, db)

    import views.test_view as test_view
    app.register_blueprint(test_view.bp)
    
    # /는 서버 주소를 의미 -> 127.0.0.1:5000/
    @app.route('/')
    def test_view() :
        return '123123'

    # 사람 - 이름, 나이, 주소
    # 1. 홍길동 20 대전
    # 2. 홍길동 20 대전

    p1 = Person(name='홍길동', age=30, address='대전')
    app.app_context().push() 
    db.session.add(p1)
    db.session.commit()

    return app

class Person(db.Model) :
    no = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    age = db.Column(db.Integer)
    address = db.Column(db.String(50))