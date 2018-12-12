from django.test import TestCase

from authentication.models import Account
from authentication.serializers import AccountSerializer

class AccountTest(TestCase):
    def setUp(self):
        self.a = Account.objects.create_user('test@test.com', username='test')

    def testEmpty(self):
        with self.assertRaises(TypeError):
            Account.objects.create_user()

    def testInvalidEmailUser(self):
        #insufficient arguments
        with self.assertRaises(ValueError):
            Account.objects.create_user('test@test.com')

        #not an email address
        #with self.assertRaises(ValueError):
        #    Account.objects.create_user('test', username='test')

        #not a valid username
        with self.assertRaises(ValueError):
            Account.objects.create_user('test@test.com', username='')

    def testFields(self):
        self.assertEqual(str(self.a.email), 'test@test.com', 'Emails do not match')
        self.assertEqual(str(self.a.username), 'test', 'Usernames do not match')


    def testDuplicate(self):
        #Account.objects.create_user('test@test.com', username='test')
        #duplicate email and username
        with self.assertRaises(Exception): #<--IntegrityError
            Account.objects.create_user('test@test.com', username='test')
        #duplicate email
        with self.assertRaises(Exception):
            Account.objects.create_user('test@test.com', username='test1')
        #duplicate username
        with self.assertRaises(Exception):
            Account.objects.create_user('test1@test.com', username='test')

    def testLatestCreated(self):
        b = Account.objects.create_user('test2@test.com', username='test2')
        self.assertEqual(Account.objects.latest('created_at'),
                         b,
                         'Latest not updating correctly'
        )

    def testAccountSerializer(self):
        aSerialized = AccountSerializer(self.a)
        self.assertEqual(aSerialized.data.get('email'),
                         self.a.email,
                         "Serialized email doesn't match model email")
        self.assertEqual(aSerialized.data.get('username'),
                         self.a.username,
                         "Serialized username doesn't match model username")
