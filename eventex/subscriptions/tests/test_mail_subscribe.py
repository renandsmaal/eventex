from django.test import TestCase
from django.core import mail
from django.shortcuts import resolve_url as r


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Renan Smaal', cpf='12345678910',
                    email='renan@smaal.net', phone='19-99292-9292')
        self.resp = self.client.post(r('subscriptions:new'), data)
        self.email = mail.outbox[0]

    def test_subscriptions_email_subject(self):
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_form(self):
        expect = 'contato@eventex.com.br'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'renan@smaal.net']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Renan Smaal',
            '12345678910',
            'renan@smaal.net',
            '19-99292-9292',
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
