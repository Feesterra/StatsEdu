from collections import Counter
import unittest

import StatsEdu.stat_functions as stat


class TestSupertool(unittest.TestCase):

    def test_data_check_positive(self):
        self.assertIsNone(stat._data_check([1, 6, 7, 6, 9, 9, 5, 6]))

    def test_data_check_negative_1(self):
        with self.assertRaises(Exception) as raised_exception:
            stat._data_check([1, 0.1, 'abcd', 44.2, -7])
            self.assertEqual('Items in data_massive must be numbers', raised_exception.exception.args[0])

    def test_data_check_negative_2(self):
        with self.assertRaises(Exception) as raised_exception:
            stat._data_check(48)
            self.assertEqual('data_massive must be list', raised_exception.exception.args[0])

    def test_mean_positive(self):
        self.assertEqual(3.0, stat.mean([1, 2, 3, 4, 5]))

    def test_mean_negative(self):
        self.assertNotEqual(22, stat.mean([0.265, 340, -847.124]))

    def test_mode_positive_1(self):
        self.assertEqual([6], stat.mode([1,6,7,6,9,9,5,6]))

    def test_mode_positive_2(self):
        self.assertListEqual([4, 6], stat.mode([4, 6, 4, 6, 9, 9, 5, 6, 3, 4]))

    def test_mode_negative(self):
        self.assertNotEqual(7, stat.mode([1,6,7,6,9,9,5,6]))

    def test_quantile_negative(self):
        with self.assertRaises(Exception) as raised_exception:
            stat.quantile([1, 0.1, 8, 44.2, -7], p='sdf')
            self.assertEqual('Order of the quantile should be number.', raised_exception.exception.args[0])

    def test_quantile_positive(self):
        self.assertEqual(3, stat.quantile([1, 10, 3, 4], 0.25))

    def test_range_positive(self):
        self.assertEqual(8, stat.data_range([1, 6, 7, 6, 9, 9, 5, 6]))

    def test_range_negative(self):
        self.assertNotEqual(7, stat.mode([1, 6, 7, 6, 9, 9.9, 5, 6]))

    def test_box_plot_negative(self):
        with self.assertRaises(Exception):
            stat.box_plot([[1, 0.1, 8, 44.2, -7], [4,5,8,'fgt',5]])

    def test_variance_positive(self):
        self.assertEqual(9, stat.variance([1, 3, 4.4, 5,10]))

    def test_variance_negative(self):
        self.assertNotEqual(88, stat.variance([1, 3, 7, 4.4, 5, 10]))

    def test_standard_deviation_positive(self):
        self.assertEqual(3.0, stat.std([1, 3, 4.4, 5, 10]))

    def test_standard_deviation_negative(self):
        self.assertNotEqual(10, stat.std([1, 3, 4.4, 5, 10]))

    def test_covarience_positive(self):
        self.assertEqual(-1.68, stat.covariance([1, 2, 4, 8, 6], [5, 7, 4, 2, 9]))

    def test_covarience_negative(self):
        self.assertNotEqual(-748, stat.covariance([1, 2.02, 4, 5.2, 6], [5, 7, 4, 2.46, 9]))

    def test_corellation_positive(self):
        self.assertEqual(-0.26, stat.correlation([1, 2, 4, 8, 6], [5, 7, 4, 2, 9]))

    def test_corellation_negative(self):
        self.assertNotEqual(-748, stat.correlation([1, 2.02, 4, 5.2, 6], [5, 7, 4, 2.46, 9]))

    def test_make_buckets_positive(self):
        self.assertEqual(Counter({2: 2, 4: 2, 10: 1}), stat._make_buckets([3, 3, 4.4, 5,10], 2))

    def test_make_buckets_negative(self):
        with self.assertRaises(Exception) as raised_exception:
            stat._make_buckets('bucket_size should be integer.', raised_exception.exception.args[0])

    def test_pplot_negative(self):
        with self.assertRaises(Exception):
            stat.pplot([[1,'fttf',4,5], [1,2,8,3]])

if __name__ == '__main__':
    unittest.main()
