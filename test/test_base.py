# *********************************************************************************************
# Copyright (C) 2017 Joel Becker,  Jillian Anderson, Steve McColl and Dr. John McLevey
#
# This file is part of the tidyextractors package developed for Dr John McLevey's Networks Lab
# at the University of Waterloo. For more information, see
# http://tidyextractors.readthedocs.io/en/latest/
#
# tidyextractors is free software: you can redistribute it and/or modify it under the terms of
# the GNU General Public License as published by the Free Software Foundation, either version 3
# of the License, or (at your option) any later version.
#
# tidyextractors is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
# without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with tidyextractors.
# If not, see <http://www.gnu.org/licenses/>.
# *********************************************************************************************

import unittest
import pandas as pd
import tidyextractors as tx


class TestBaseExtractor(unittest.TestCase):

    def setUp(self):
        self.basex = tx.BaseExtractor('')

    def test_construction(self):
        self.assertEqual(isinstance(self.basex, tx.BaseExtractor), True)

    def test_raw(self):
        self.assertEqual(isinstance(self.basex.raw(), pd.DataFrame), True)


if __name__ == '__main__':
    unittest.main()