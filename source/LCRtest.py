from LCRplots import LCRplots 
import unittest 
import mock

class savefigTestCase(unittest.TestCase):
    
    @mock.patch(LCRplots.os)
    @mock.patch(LCRplots.matplotlib.pyplot)
    def is_savefig_working(self, plt, lcrplots_os):
        
        
