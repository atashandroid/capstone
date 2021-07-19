import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from auth.auth import requires_auth, AuthError
from models import setup_db, Composition, Musician


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.after_request
    def after_request(responce):
        responce.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
        responce.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
        return responce

    @app.route('/compositions', methods=['GET'])
    @requires_auth('get:compositions')
    def get_compositions(payload):
        compositions = Composition.query.all()

        if not compositions:
            abort(404)

        return jsonify({
            'success': True,
            'compositions': [composition.format() for composition in compositions]
        })

    @app.route('/musicians', methods=['GET'])
    @requires_auth('get:musicians')
    def get_musicians(payload):
        musicians = Musician.query.all()

        if not musicians:
            abort(404)

        return jsonify({
            'success': True,
            'musicians': [musician.format() for musician in musicians]
        })

    @app.route('/compositions/create', methods=['POST'])
    @requires_auth('post:compositions')
    def add_new_composition(payload):
        body = request.get_json()

        composition_title = body.get('title')
        composition_release_date = body.get('release_date')

        if composition_title == '' or composition_release_date == '':
            abort(400)

        try:
            composition = Composition(title=composition_title, release_date=composition_release_date)
            composition.insert()

            return jsonify({
                'success': True,
                'created': composition.id
            })

        except:
            abort(422)

    @app.route('/musicians/create', methods=['POST'])
    @requires_auth('post:musician')
    def add_new_musician(payload):
        body = request.get_json()
        musician_name = body.get('name')
        musician_age = body.get('age')
        musician_gender = body.get('gender')

        if musician_name == '' or musician_age == '' or musician_gender == '':
            abort(400)

        try:
            musician = Musician(name=musician_name, age=musician_age, gender=musician_gender)
            musician.insert()

            return jsonify({
                'success': True,
                'created': musician.id
            })
        except:
            abort(422)

    @app.route('/compositions/delete/<int:composition_id>', methods=['DELETE'])
    @requires_auth('delete:compositions')
    def delete_composition(payload, composition_id):

        delete_with_id = Composition.query.filter(Composition.id == composition_id).one_or_none()

        if delete_with_id is None:
            abort(404)

        try:
            delete_with_id.delete()

            return jsonify({
                'success': True,
                'deleted': composition_id
            })
        except:
            abort(422)

    @app.route('/musicians/delete/<int:musician_id>', methods=['DELETE'])
    @requires_auth('delete:musician')
    def delete_musician(payload, musician_id):

        delete_with_id = Musician.query.filter(Musician.id == musician_id).one_or_none()

        if delete_with_id is None:
            abort(404)

        try:
            delete_with_id.delete()

            return jsonify({
                'success': True,
                'deleted': musician_id
            })
        except:
            abort(422)

    @app.route('/compositions/update/<int:composition_id>', methods=['PATCH'])
    @requires_auth('patch:compositions')
    def update_composition(payload, composition_id):
        composition = Composition.query.filter(Composition.id == composition_id).one_or_none()
        body = request.get_json()
        composition_title = body['title']
        composition_release_date = body['release_date']

        if (not composition_title) or (not composition_release_date):
            abort(404)

        try:
            composition.title = composition_title
            composition.release_date = composition_release_date
            composition.update()

            return jsonify({
                'success': True,
                'updated': composition_id
            })
        except:
            abort(422)

    @app.route('/musicians/update/<int:musician_id>', methods=['PATCH'])
    @requires_auth('patch:musician')
    def update_musician(payload, musician_id):

        musician = Musician.query.filter(Musician.id == musician_id).one_or_none()
        body = request.get_json()
        musician_name = body['name']
        musician_age = body['age']
        musician_gender = body['gender']

        if (not musician_name) or (not musician_age) or (not musician_gender):
            abort(404)

        try:
            musician.name = musician_name
            musician.age = musician_age
            musician.gender = musician_gender

            musician.update()

            return jsonify({
                'success': True,
                'updated': musician_id
            })
        except:
            abort(422)

    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify({
            'success': False,
            'error': 500,
            'message': 'internal server error'
        }), 500

    @app.errorhandler(404)
    def resource_not_found(error):
        return jsonify({
            'success': False,
            'error': 404,
            'message': 'resource not found'
        }), 404

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            'success': False,
            'error': 422,
            'message': 'unprocessable'
        }), 422

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            'success': False,
            'error': 400,
            'message': 'bad request'
        }), 400

    @app.errorhandler(AuthError)
    def auth_error(e):
        return jsonify({
            'success': False,
            'error': e.status_code,
            'message': e.error['description']
        }), e.status_code

    return app


app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
