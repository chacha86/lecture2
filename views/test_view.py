from flask import Blueprint
from app import db
from app import Person 
# 라우팅 해주는 객체
bp = Blueprint('test', __name__, url_prefix="")

# /는 서버 주소를 의미 -> 127.0.0.1:5000/hello
@bp.route('/hello')
def hello() :
    return "hello"

@bp.route('/bye')
def bye() :
    return "bye"

@bp.route('/introduce')
def introduce() :
    return "my name is cha"

@bp.route('print_person')
def print_person() :
    result = db.session.query(Person).all() 
    string = ""
    for p in result :
        string += "{}사는 {}살 {}입니다.       ".format(p.address, p.age, p.name) 
    #p1 = db.session.query(Person).first() 
    # return "{}사는 {}살 {}입니다.".format(p1.address, p1.age, p1.name) 
    return string 