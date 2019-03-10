from django.test import TestCase
from django.test import Client

from django.contrib.auth.models import User
from music.models import Album


class AuthTestCase(TestCase):

    def setUp(self):
        self.client = Client()

    def test_registration(self):
        response = self.client.post('/register/', {'username': 'john', 'password': 'smith', 'email': 'john@mail.com'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(User.objects.filter(username='john').exists())

    def test_login(self):
        self.client.post('/register/', {'username': 'john', 'password': 'smith', 'email': 'john@mail.com'})

        response = self.client.post('/login_user/', {'username': 'john', 'password': 'smith'})
        self.assertEqual(response.status_code, 200)


class AlbumTestCase(TestCase):

    def setUp(self):
        self.client.post('/register/', {'username': 'john', 'password': 'smith', 'email': 'john@mail.com'})
        self.client.post('/login_user/', {'username': 'john', 'password': 'smith'})

    def test_create_album(self):
        response = self.client.post('/create_album/', {'artist': 'Artist', 'album_title': 'Album Title', 'genre': 'pop'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Album.objects.filter(album_title='Album Title').exists())

        user = User.objects.get(username='john')
        album = Album.objects.get(album_title='Album Title')

        self.assertEqual(user.pk, album.user.pk)

    def test_get_album(self):
        self.client.post('/create_album/', {'artist': 'Artist', 'album_title': 'Album Title', 'genre': 'pop'})

        album = Album.objects.get(album_title='Album Title')

        response = self.client.get('/{}/'.format(album.pk))
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/random/')
        self.assertEqual(response.status_code, 404)
