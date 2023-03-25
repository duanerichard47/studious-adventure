#!/usr/bin/env python3

from flask import Flask, make_response, request, jsonify
from flask_migrate import Migrate

from models import db, Hero, HeroPower, Power

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return 'Home Page'

@app.route('/heroes', methods=['GET'])
def heroes():
  
      
    if request.method == 'GET':
        heroes = []
        for hero in Hero.query.all():
            hero_dict = hero.to_dict()
            heroes.append(hero_dict)

        response = make_response(
            jsonify(heroes),
            200
        )

        return response
  

@app.route('/heroes/<int:id>', methods=['GET'])
def hero_by_id(id):
      hero = Hero.query.filter(Hero.id == id).first()
      if heroes == None:
        response_body = {
            "error": "Hero not found"
        }
        response = make_response(jsonify(response_body), 404)

        return response
      
      elif request.method == 'GET':
            hero_dict = hero.to_dict()

            response = make_response(
                jsonify(hero_dict),
                200
            )

            return response
  

@app.route('/powers', methods=['GET'])
def powers():
     
    
    if request.method == 'GET':
        powers = []
        for power in Power.query.all():
            power_dict = power.to_dict()
            powers.append(power_dict)

        response = make_response(
            jsonify(powers),
            200
        )

        return response
    

@app.route('/powers/<int:id>', methods=['GET', 'PATCH'])
def power_by_id(id):
    power = Power.query.filter(Power.id == id).first()
    if powers == None:
        response_body = {
            "error": "Hero not found"
        }
        response = make_response(jsonify(response_body), 404)

        return response

    elif request.method == 'GET':
            power_dict = power.to_dict()

            response = make_response(
                jsonify(power_dict),
                200
            )

            return response

    elif request.method == 'PATCH':
            

            for attr in request.json:
                setattr(power, attr, request.json.get(attr))

            db.session.add(power)
            db.session.commit()

            power_dict = power.to_dict()

            response = make_response(
                jsonify(power_dict),
                200
            )

            return response 


@app.route('/hero_powers', methods=['GET', 'POST'])
def hero_powers():
    if request.method == 'GET':
        hero_powers = []
        for hero_power in HeroPower.query.all():
            hero_power_dict = hero_power.to_dict()
            hero_powers.append(hero_power_dict)

        response = make_response(
            jsonify(hero_powers),
            200
        )

        return response
    
    
    elif request.method == 'POST':
            new_hero_power = HeroPower(
            strength=request.json.get("strength"),
            hero_id=request.json.get("hero_id"),
            power_id=request.json.get("power_id"),   
                                )
                                
            db.session.add(new_hero_power)
            db.session.commit()

            hero_power_dict = new_hero_power.to_dict()

            response = make_response(
            jsonify(hero_power_dict), 201
                                
            )
            return response                                                                            
    


if __name__ == '__main__':
    app.run(port=5555, debug=True)
