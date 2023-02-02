from django.test import TestCase

# Create your tests here.
from vzla.models import Turismo

class T_Tests(TestCase):
    def test_Turismo(self):
        Turismo_fecha_valido = Turismo.objects.create(
            fecha_limite='2026-1-2')
        self.assertEqual(Turismo.objects.all().count(), 1)
        self.assertIsNotNone(Turismo_fecha_valido.id)