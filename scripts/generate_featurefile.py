#!/usr/bin/python
# Copyright (C) 2012, Aravinda VK <hallimanearavind@gmail.com>
#                          http://aravindavk.in

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import sys
import fontforge

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print ("USAGE: python generate_featurefile.py <font/sfd file>")
    else:
	sfdname = sys.argv[1]
	featurefilename = sfdname[0:-4] + ".fea"
	print (featurefilename)

        font = fontforge.open(sys.argv[1])
        font.generateFeatureFile(featurefilename)
        font.close()
        print ("[SUCCESS]", featurefilename, "feature file generated")
