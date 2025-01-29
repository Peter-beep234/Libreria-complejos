import libreria_complejos as lc
import unittest


class TestStringMethods(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(lc.sum_complex((3,5),(-2,6.8)), (1,11.8))
        self.assertEqual(lc.sum_complex((1, 9), (-2, -5.5)), (-1, 3.5))

    def test_resta(self):
        self.assertEqual(lc.rest_complex(((3,5),(-2,8)), (1,11.8)))
        self.assertEqual(lc.rest_complex((1, 9), (-2, -5)), (-1, 3.5))

    def test_multi(self):
        self.assertEqual(lc.mult_complex((3,5),(-2,7)), (-41,11))
        self.assertEqual(lc.mult_complex((1, 9), (-2, -5.5)), (47.5, -23.5))

    def test_div(self):
        self.assertEqual(lc.div_complex((3,5),(-2,6)), (0.6,-0.7))
        self.assertEqual(lc.div_complex((4, 10), (2, 5)), (2,0))

    def test_mod(self):
        self.assertEqual(lc.mod_complex((3,4)), (5))
        self.assertEqual(lc.mod_complex((8, 6)), (10))

    def test_conj(self):
        self.assertEqual(lc.conj_complex((3,4)), (3,-4))
        self.assertEqual(lc.conj_complex((8, -6)), (8,6))

    def test_c_a_p(self):
        self.assertEqual(lc.cartesiano_a_polar_complex((3,4)), (5, 0.9272952180016122))
        self.assertEqual(lc.cartesiano_a_polar_complex((8, -6)), (10,-0.6435011087932844))

    def test_p_a_c(self):
        self.assertEqual(lc.polar_a_cartesiano_complex((3,4)), (-1.960930862590836,-2.2704074859237844))
        self.assertEqual(lc.polar_a_cartesiano_complex((8, -6)), (7.681362293202928, 2.235323985591407))

    def test_fase(self):
        self.assertEqual(lc.fase_complex((3,4)), (0.9272952180016122))
        self.assertEqual(lc.fase_complex((8, -6)), (-0.6435011087932844))


if __name__ == '__main__':
    unittest.main()