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
        self.assertAlmostEqual(quadratics.find_x(-.2723, 7.5, 1), 4.8858)
        self.assertAlmostEqual(quadratics.find_x(-.2723, 7.5, 6), 2.347)

    def test_find_width(self):
        expected_values = {
            'row 0': 10.4964,
            'row 1': 9.7716,
            'row 2': 8.9886,
            'row 3': 8.1305,
            'row 4': 7.1704,
            'row 5': 6.0600,
            'row 6': 4.6942,
            'row 7': 2.7102
        }

        actual_values = quadratics.find_width(-.2723, 7.5, 1, 8)

        for row in expected_values:
            self.assertAlmostEqual(actual_values[row], expected_values[row], places=3)
            
    def test_calculate_stitches_per_row(self):
        row_widths = quadratics.find_width(-.2723, 7.5, 1, 8)
        expected_values = {
            'row 0': 10, 
            'row 1': 9, 
            'row 2': 8, 
            'row 3': 8, 
            'row 4': 7, 
            'row 5': 6, 
            'row 6': 4, 
            'row 7': 2
        }

        actual_values = quadratics.calculate_stitches_per_row(row_widths, 1)

        self.assertEqual(actual_values, expected_values)

    def test_calculate_decrease(self):
        input_values = {
            'row 0': 10, 
            'row 1': 9, 
            'row 2': 8, 
            'row 3': 8, 
            'row 4': 7, 
            'row 5': 6, 
            'row 6': 4, 
            'row 7': 2
        }

        expected_values = {
            'row 0 - 1': -1,
            'row 1 - 2': -1,
            'row 2 - 3': -0,
            'row 3 - 4': -1,
            'row 4 - 5': -1,
            'row 5 - 6': -2,
            'row 6 - 7': -2
        }

        actual_values = quadratics.calculate_decrease(input_values)

        for row in expected_values:
         self.assertEqual(actual_values, expected_values)

# class test_print_rows(unittest.TestCase):
#     def test_calculate_total_stitch_together(self):
#         expected_values = {
#             'front_decrease': 5,
#             'back_decrease': 6
#         }

#         actual_values = print_rows.calculate_total_stitch_together(11)

#         for row in expected_values:
#             self.assertEqual(actual_values, expected_values)

if __name__ == '__main__':
    unittest.main()