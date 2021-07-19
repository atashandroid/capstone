import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from models import setup_db, Musician, Composition
from app import create_app
from models import db

ASSISTANT = ('eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlkzbUQ0c19Tc3M5VGZXUHdReFgxMCJ9.eyJpc3MiOiJodHRwczovL2F0YXNoLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MGY0MzQwNDYxMGE3NjAwNjllYzM3N2MiLCJhdWQiOiJjYXN0aW5nIiwiaWF0IjoxNjI2NzAzMzAzLCJleHAiOjE2MjY3ODk3MDMsImF6cCI6IkZKTUVGaERCTHRzOEZaSXN3ejZOU3VIUGVyYzdEaFJ1Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6Y29tcG9zaXRpb25zIiwiZ2V0Om11c2ljaWFucyJdfQ.JaEejIx3LW6ILLqqNg9LHPT4OgNccUK0gKnUhhRTP-oaSjS2yBKwyLSQCPkzxfX8bcjERigmpQXvNObdnov42dDJCt-tcYxiUX--PdkLsVTFWRbpWtfqYSg9O78DPQqeoNx17g7vx3j8VLELN-tigjUVKEooqcINCZRsSL0gdiOCg_Vx2gaQnNj04h1wXXGjZ2hgb4Gp_8UQ3QTwbCdUvXpy8Ox1mWGo8wxPZ16X2SJ4R07GyuiDMSDW5ufS2IPWXqIGTEqIXUvFL6SvIG35cFUy-NLQB-8pq568sOf0dS004zWWkeMfb4-9ZCAdnCCOzC3xhOez9_xoGQ53nQfDLg')
DIRECTOR = ('eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlkzbUQ0c19Tc3M5VGZXUHdReFgxMCJ9.eyJpc3MiOiJodHRwczovL2F0YXNoLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MGY0NDk2MjhjYjIxMjAwNjk3MmM5N2MiLCJhdWQiOiJjYXN0aW5nIiwiaWF0IjoxNjI2NzAzMzg4LCJleHAiOjE2MjY3ODk3ODgsImF6cCI6IkZKTUVGaERCTHRzOEZaSXN3ejZOU3VIUGVyYzdEaFJ1Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6Y29tcG9zaXRpb25zIiwiZGVsZXRlOm11c2ljaWFuIiwiZ2V0OmNvbXBvc2l0aW9ucyIsImdldDptdXNpY2lhbnMiLCJwYXRjaDpjb21wb3NpdGlvbnMiLCJwYXRjaDptdXNpY2lhbiIsInBvc3Q6Y29tcG9zaXRpb25zIiwicG9zdDptdXNpY2lhbiJdfQ.n_5tjI3Pyy8out3BuD9qKFr6NrEkdvhglWZlRkJoH7SZZHUNcVx1Uqmhmf1G_Da9XZwdGQSj1bADrNDPxjaRCo4H61-pkITxL8veDvsWDSgGYbFWFoPiRpUMTHGuLYs01tiGL0hbZZ7Ujc46UlXedPeNH-rwXFU7VGCA-p9eIqIMYZm3JDdOxZ8mg1XB469xdPJZOtYYPXR-1gS00NZ_Bnb7tKeBZS34t3PNikW602TLy38bH66XaQmwrMZNed5cGR_uRZ0pU4dmj7f3gZZdub6ylQPpKcxMAcuKb8l7aCgfMoFFcbr5JMCZZ234L--OPoAdFuFKRksPkOGPTTCVWA')

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
