from django.test import TestCase
from .models import Alvo

class AlvoModelTest(TestCase):
    def setUp(self):
        Alvo.objects.create(
            nome="Alvo 1",
            latitude=10.0,
            longitude=20.0,
            data_expiracao="2024-12-31"
        )

    def test_alvo_creation(self):
        alvo = Alvo.objects.get(nome="Alvo 1")
        self.assertEqual(alvo.nome, "Alvo 1")
