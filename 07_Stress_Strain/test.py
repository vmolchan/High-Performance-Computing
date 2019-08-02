#!/usr/bin/env python

import numpy as np
import unittest

from assignment7 import convert_to_true_stress_and_strain


class TestSolution(unittest.TestCase):
    
    def test_convert_to_true_stress_and_strain(self):

        strain, stress = convert_to_true_stress_and_strain('data.dat') 

        np.testing.assert_allclose(strain[:10], np.array([ 1.76974413e-06,  2.19162248e-05, -3.19850395e-05, -2.99607468e-05,
            2.42023361e-05, -1.02986180e-05,  1.80243056e-05,  2.69191677e-05,
            7.80963814e-05,  4.51086396e-05]), atol=1e-6)
        np.testing.assert_allclose(strain[-10:], np.array([0.59983723, 0.59999834, 0.60013837, 0.60030186, 0.60047056,
           0.6006305 , 0.60080112, 0.60096908, 0.60115796, 0.60148428]), atol=1e-6)
        np.testing.assert_allclose(stress[:10], np.array([ 310.00135992,  570.65679508,  817.77043635,  945.39539323,
           1192.34923999, 1423.21648246, 1605.57296261, 1851.96319545,
           2099.05379863, 2286.42636236]), atol=1e-6)
        np.testing.assert_allclose(stress[-10:], np.array([112492.77647224, 112254.75315531, 112024.73779468, 111711.26437979,
           111496.03728211, 111091.35149831, 110849.85117293, 110550.18990996,
           110154.87432769, 108773.98868365]), atol=1e-6)


if __name__ == '__main__':
    unittest.main()


