from LCRplots import LCRplots 
from scipy.integrate import odeint
import numpy as np
import unittest 
import mock

def func(initial,t):
	return 5

class savefigTestCase(unittest.TestCase):
    
    def test_odeint_working(self):
    	t = np.linspace(0.0,5,50)
    	initial = 0
    	ans = odeint(func,initial,t)
    	self.assertAlmostEqual(ans[-1],25)