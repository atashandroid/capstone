import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from models import setup_db, Musician, Composition
from app import create_app
from models import db

ASSISTANT = ('eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlkzbUQ0c19Tc3M5VGZXUHdReFgxMCJ9.eyJpc3MiOiJodHRwczovL2F0YXNoLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MGY0MzQwNDYxMGE3NjAwNjllYzM3N2MiLCJhdWQiOiJjYXN0aW5nIiwiaWF0IjoxNjI2Njc3ODgzLCJleHAiOjE2MjY2ODUwODMsImF6cCI6IkZKTUVGaERCTHRzOEZaSXN3ejZOU3VIUGVyYzdEaFJ1Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6Y29tcG9zaXRpb25zIiwiZ2V0Om11c2ljaWFucyJdfQ.QJMnxKvhMyVknmKBjRdoGq3sXINjUshsXKHGfgXix5i_Zzr4NX4zU9P-ohIDJM7nU2IxgJ6cRIVRCK2EAYKHvgi2RhES_iMPYGOroAMQYf2E2pawGja2I8tLQcCtMuzDLD8jCAaPSr-AnNc8-g1AraiBpUgDCIaX9KOlFEhqIMouZIWTk1KN09VGFt4oX4EjJGpZqykAnaebVMaizExn80M1JhPpY05IoKGXdKUNXtaDOncjDDZaLKWmSTywg9XMXukta9EXeWEJlECnyc2e4Dwhx2HCvmcPFvKQqbIAG4GMm-4TcXSAGCMWQ-qVD3R5qLDwwKUUhuHp1YuTigehCg')
DIRECTOR = ('eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlkzbUQ0c19Tc3M5VGZXUHdReFgxMCJ9.eyJpc3MiOiJodHRwczovL2F0YXNoLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MGY0NDk2MjhjYjIxMjAwNjk3MmM5N2MiLCJhdWQiOiJjYXN0aW5nIiwiaWF0IjoxNjI2NjkzNTQ4LCJleHAiOjE2MjY3MDA3NDgsImF6cCI6IkZKTUVGaERCTHRzOEZaSXN3ejZOU3VIUGVyYzdEaFJ1Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6Y29tcG9zaXRpb25zIiwiZGVsZXRlOm11c2ljaWFuIiwiZ2V0OmNvbXBvc2l0aW9ucyIsImdldDptdXNpY2lhbnMiLCJwYXRjaDpjb21wb3NpdGlvbnMiLCJwYXRjaDptdXNpY2lhbiIsInBvc3Q6Y29tcG9zaXRpb25zIiwicG9zdDptdXNpY2lhbiJdfQ.C6IA2YTwNgRlSNPEmc54K_z2RoE8BTZrYwRToUg8W2_yLe6vOR2R3aSg_eM28tzmBAx0HuQ8yrApX0lSH3x5CzNzMsJ-M9Hg64Yp_I7PukdCYqrT0evk-scBI1HSGIwjJSZhPFzo8_Bjaxr_vX-RJJMiKf4ZrNot1KcNJP1wmnqGY53C4irHMutp6N_mEGWwgogc0o5_nKqFzDaCmXLRQx9jeyA0GUrG629l3Iddl6DuyKe5p9TLPCPRrDm8F5UxG2ViN_BMkwMIGsAF84mxdDRkLrj4v8pMuCjeUd8nlEBnCFGHodAO7y2JlIGhiKbj7wJrMnR_lWJIQboaLedppA')

class CompositionTestCase(unittest.TestCase):

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        setup_db(self.app)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        pass

    def test_get_compositions(self):
        res = self.client().get('/compositions', headers={'Authorization': f'Bearer {ASSISTANT}'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_fail_compositions(self):
        res = self.client().get('/compositionsss', headers={'Authorization': f'Bearer {ASSISTANT}'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_get_musicians(self):
        res = self.client().get('/musicians', headers={'Authorization': f'Bearer {ASSISTANT}'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_fail_musicians(self):
        res = self.client().get('/musiciansss', headers={'Authorization': f'Bearer {ASSISTANT}'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_create_composition(self):
        composition = {
            'title': 'Music for wedding',
            'release_date': '2021-01-02'
        }
        res = self.client().post('/compositions/create', data=json.dumps(composition),
                                 headers={'Content-Type': 'application/json', 'Authorization': f'Bearer {DIRECTOR}'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_fail_create_composition(self):
        composition = {
            'title': '',
            'release_date': ''
        }
        res = self.client().post('/compositions/create', data=json.dumps(composition),
                                 headers={'Content-Type': 'application/json', 'Authorization': f'Bearer {DIRECTOR}'})
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
                                 headers={'Content-Type': 'application/json', 'Authorization': f'Bearer {DIRECTOR}'})
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
                                 headers={'Content-Type': 'application/json', 'Authorization': f'Bearer {DIRECTOR}'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'bad request')

    def test_delete_composition(self):
        composition = Composition(title='Test title', release_date='2021-06-09')
        composition.insert()

        res = self.client().delete(f'/compositions/delete/{composition.id}',
                                   headers={'Authorization': f'Bearer {DIRECTOR}'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], composition.id)

    def test_fail_delete_composition(self):
        res = self.client().delete('/compositions/delete/10000',
                                   headers={'Authorization': f'Bearer {DIRECTOR}'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    def test_delete_musician(self):
        musician = Musician(name='Test name', age=22, gender='M')
        musician.insert()

        res = self.client().delete(f'/musicians/delete/{musician.id}',
                                   headers={'Authorization': f'Bearer {DIRECTOR}'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], musician.id)

    def test_fail_delete_musician(self):
        res = self.client().delete('/musicians/delete/10000',
                                   headers={'Authorization': f'Bearer {DIRECTOR}'})
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
                                  headers={'Content-Type': 'application/json', 'Authorization': f'Bearer {DIRECTOR}'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_fail_patch_composition(self):
        composition = {
            'title': 'Music for wedding',
            'release_date': '2021-06-09'
        }
        res = self.client().patch('/compositions/update/20000', data=json.dumps(composition),
                                  headers={'Content-Type': 'application/json', 'Authorization': f'Bearer {DIRECTOR}'})
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
                                  headers={'Content-Type': 'application/json', 'Authorization': f'Bearer {DIRECTOR}'})
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
                                  headers={'Content-Type': 'application/json', 'Authorization': f'Bearer {DIRECTOR}'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
