import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from models import setup_db, Musician, Composition
from app import create_app
from models import db
import datetime


class CompositionTestCase(unittest.TestCase):

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "music_test"
        self.database_path = "postgresql://{}:{}@{}/{}".format(
            'postgres', '12345', 'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        pass

    def test_get_compositions(self):
        res = self.client().get('/compositions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_fail_compositions(self):
        res = self.client().get('/compositionsss')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_get_musicians(self):
        res = self.client().get('/musicians')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_fail_musicians(self):
        res = self.client().get('/musiciansss')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_create_composition(self):
        composition = {
            'title': 'Music for wedding',
            'release_date': '2021-09-06'
        }
        res = self.client().post('/compositions/create', data=json.dumps(composition),
                                 headers={'Content-Type': 'application/json'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_fail_create_composition(self):
        composition = {
            'title': '',
            'release_date': ''
        }
        res = self.client().post('/compositions/create', data=json.dumps(composition),
                                 headers={'Content-Type': 'application/json'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'bad request')

    def test_create_musician(self):
        musician = {
            'name': 'Peter Peterson',
            'age': '36',
            'gender': 'M'
        }
        res = self.client().post('/musicians/create', data=json.dumps(musician),
                                 headers={'Content-Type': 'application/json'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_fail_create_musician(self):
        musician = {
            'name': 'Peter Peterson',
            'age': '',
            'gender': 'M'
        }
        res = self.client().post('/musicians/create', data=json.dumps(musician),
                                 headers={'Content-Type': 'application/json'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'bad request')

    def test_delete_composition(self):
        composition = Composition(title='Test title', release_date='2021-06-09')
        composition.insert()

        res = self.client().delete(f'/compositions/delete/{composition.id}')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], composition.id)

    def test_fail_delete_composition(self):
        res = self.client().delete('/compositions/delete/10000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    def test_delete_musician(self):
        musician = Musician(name='Test name', age=22, gender='M')
        musician.insert()

        res = self.client().delete(f'/musicians/delete/{musician.id}')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], musician.id)

    def test_fail_delete_musician(self):
        res = self.client().delete('/musicians/delete/10000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    def test_patch_composition(self):
        composition = {
            'title': 'Music for wedding',
            'release_date': '2021-09-06'
        }
        res = self.client().patch('/compositions/update/2', data=json.dumps(composition),
                                  headers={'Content-Type': 'application/json'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_fail_patch_composition(self):
        composition = {
            'title': 'Music for wedding',
            'release_date': '2021-06-09'
        }
        res = self.client().patch('/compositions/update/20000', data=json.dumps(composition),
                                  headers={'Content-Type': 'application/json'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')

    def test_patch_musician(self):
        musician = {
            'name': 'Peter Peterson',
            'age': '36',
            'gender': 'M'
        }
        res = self.client().patch('/musicians/update/2', data=json.dumps(musician),
                                  headers={'Content-Type': 'application/json'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_fail_patch_musician(self):
        musician = {
            'name': 'Peter Peterson',
            'age': '36',
            'gender': 'M'
        }
        res = self.client().patch('/musicians/update/20000', data=json.dumps(musician),
                                  headers={'Content-Type': 'application/json'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
