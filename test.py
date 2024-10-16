import unittest
import first_row
import measurements
import print_rows
import quadratics
import stitch_swatch_data
import sweater_pattern_data

class test_quadratics(unittest.TestCase):
    def test_calculate_parabola_slope(self):
        self.assertEqual(quadratics.calculate_parabola_slope(10.5, 7.5), -.2721)
        
    def test_find_x(self):
        self.assertEqual(quadratics.find_x(-.2723, 7.5, 1), 4.8858)
        self.assertEqual(quadratics.find_x(-.2723, 7.5, 6), 4.6942)

    def test_find_width(self):
        expected_values = {
            'row 1': 10.4964,
            'row 2': 9.7716,
            'row 3': 8.9886,
            'row 4': 8.1305,
            'row 5': 7.1704,
            'row 6': 6.0600,
            'row 7': 4.6942,
            'row 8': 2.7102
        }

        actual_values = quadratics.find_width(-.2723, 7.5, 1, 7)

        for row in expected_values:
            self.assertAlmostEqual(actual_values[row], expected_values[row], places=3)
            

if __name__ == '__main__':
    unittest.main()