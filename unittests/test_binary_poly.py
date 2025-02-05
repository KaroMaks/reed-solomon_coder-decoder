from unittest import TestCase

from polynomials.binary_poly import BinaryPoly


class TestBinaryPoly(TestCase):
    p1 = BinaryPoly([0, 1, 0, 1, 1])
    p2 = BinaryPoly([1, 1, 1, 1, 1, 1])

    def test_get_value(self):
        self.assertEqual(self.p1.get_value(), 11)
        self.assertEqual(self.p2.get_value(), 63)

    def test_get_trimmed(self):
        self.assertEqual(self.p1.get_trimmed(), BinaryPoly([1, 0, 1, 1]))
        self.assertEqual(self.p2.get_trimmed(), BinaryPoly([1, 1, 1, 1, 1, 1]))
        self.assertEqual(len(self.p1.get_trimmed().coefficients), 4)
        self.assertEqual(len(self.p2.get_trimmed().coefficients), 6)

    def test_get_filled(self):
        self.assertEqual(self.p1.get_filled(8), BinaryPoly([0, 0, 0, 0, 1, 0, 1, 1]))
        self.assertEqual(self.p2.get_filled(8), BinaryPoly([0, 0, 1, 1, 1, 1, 1, 1]))
        self.assertEqual(len(self.p1.get_filled(8).coefficients), 8)
        self.assertEqual(len(self.p1.get_filled(125).coefficients), 125)

    def test_get_inverse(self):
        self.assertEqual(self.p1.get_inverse(), BinaryPoly([1, 1, 1, 0, 0]))
        self.assertEqual(self.p2.get_inverse(), BinaryPoly([1, 0, 0, 0, 0, 0]))

    def test_addition(self):
        self.assertEqual(self.p1 + self.p2, BinaryPoly([1, 1, 0, 1, 0, 0]))

    def test_division(self):
        self.assertEqual(self.p1 / self.p2, BinaryPoly([1, 0, 1, 1, 1, 1]))

    def test_multiplication(self):
        self.assertEqual(self.p1 * self.p2, BinaryPoly([1, 1, 0, 0, 1, 1]))

    # chatgpt
    def test_addition_xor(self):
        p3 = BinaryPoly([1, 0, 1])
        p4 = BinaryPoly([1, 1, 0])
        self.assertEqual(p3 + p4, BinaryPoly([0, 1, 1]))

    def test_multiplication_in_galois_field(self):
        p3 = BinaryPoly([1, 0, 1])
        p4 = BinaryPoly([1, 1])
        self.assertEqual(p3 * p4, BinaryPoly([1, 1, 1, 1]))

    def test_division_exact(self):
        p3 = BinaryPoly([1, 0, 1, 1])
        p4 = BinaryPoly([1, 1])
        self.assertEqual(p3 / p4, BinaryPoly([1, 1, 1, 0, 0, 0]))

        p5 = BinaryPoly([1, 0, 1, 1])
        p6 = BinaryPoly([1, 0, 1])
        self.assertEqual(p5 / p6, BinaryPoly([1, 0, 1, 0, 0, 1]))

    def test_division_with_remainder(self):
        p3 = BinaryPoly([1, 0, 1, 1])
        p4 = BinaryPoly([1, 0, 1])
        self.assertEqual(p3 / p4, BinaryPoly([1, 0, 1, 0, 0, 1]))

    def test_edge_cases(self):
        zero_poly = BinaryPoly([0])
        one_poly = BinaryPoly([1])
        self.assertEqual(zero_poly + one_poly, one_poly)
        self.assertEqual(zero_poly * one_poly, zero_poly)
        self.assertEqual(one_poly * one_poly, one_poly)
        self.assertEqual(zero_poly.get_inverse(), None)

    def test_large_polynomial_operations(self):
        large_poly1 = BinaryPoly([1] * 1000)
        large_poly2 = BinaryPoly([1, 0] * 500)
        result_add = large_poly1 + large_poly2
        self.assertEqual(result_add.coefficients.count(1), 500)
        result_mul = large_poly1 * BinaryPoly([1])
        self.assertEqual(result_mul, large_poly1)
