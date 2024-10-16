import unittest
import first_row
import measurements
import print_rows
import quadratics
import stitch_swatch_data
import sweater_pattern_data

class test_quadratics(unittest.TestCase):
    def test_calculate_parabola_slope(self):
        self.assertEqual(quadratics.calculate_parabola_slope())