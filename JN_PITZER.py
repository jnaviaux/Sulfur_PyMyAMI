# MyAMI Specific Ion Interaction Model (Version 1.0):
# This is a Python script to calculate thermodynamic pK's and conditional pK's
# Author: Mathis P. Hain -- m.p.hain@soton.ac.uk
#
# Reference:
# Hain, M.P., Sigman, D.M., Higgins, J.A., and Haug, G.H. (2015) The effects of secular calcium and magnesium concentration changes on the thermodynamics of seawater acid/base chemistry: Implications for Eocene and Cretaceous ocean carbon chemistry and buffering, Global Biogeochemical Cycles, 29, doi:10.1002/2014GB004986
#
# For general context on the calculations see Millero, 2007 (Chemical Reviews) and Millero and Pierrot, 1998 (Aquatic Geochemistry)

# NOTE: in Python log is natural-logarithm & log10 is log-base-10

# THIS FILE CONTAINS THE PYTHON/MATLAB INTERFACE
# THERE IS A "MyPY.m" FILE TO CALL THE PITZER MODEL

# header information needed to run
import math
import numpy
import sys
import JN_pKs

Tc = float(sys.argv[1])
Sal = float(sys.argv[2])
XmCa = float(sys.argv[3])
XmMg = float(sys.argv[4])
xST = float(sys.argv[5]) #JN added xST 2-28-19 for amount of SO4

mMg = 0.0528171 # Mg Millero et al., 2008; Dickson OA-guide
mCa = 0.0102821 # Ca Millero et al., 2008; Dickson OA-guide
mST = 0.0282352*Sal/35 # SO4 Millero et al., 2008; Dickson OA-guide #JN added

OUT = numpy.zeros([29]) #JN changed from 29->33 to include extras at end

Kall = JN_pKs.calculate_Ks(Tc,Sal, XmCa, XmMg, xST)
#Note: numbering for python vectors starts at 0 (vs Matlab which starts at 1)
#This code first gets the outputs for modern SW (second row of Kall)
# then for the inputted fraction of Ca and Mg (third row of Kall)
# then it recalculates the entire thing for modern SW again and takes from the second
# row of Kall. The first row of Kall is for freshwater values I believe

OUT[0] = XmCa
OUT[1] = XmMg
OUT[2] = Tc
OUT[3] = Sal

# empirical (i.e., modern)
OUT[4] = Kall[1,1]
OUT[5] = Kall[2,1]
OUT[6] = Kall[3,1]
OUT[7] = Kall[4,1]
OUT[8] = Kall[5,1]
OUT[9] = Kall[6,1]
OUT[10] = Kall[7,1]
OUT[11] = Kall[8,1]

# MyAMI XmCa and XmMg
OUT[12] = Kall[1,2]
OUT[13] = Kall[2,2]
OUT[14] = Kall[3,2]
OUT[15] = Kall[4,2]
OUT[16] = Kall[5,2]
OUT[17] = Kall[6,2]
OUT[18] = Kall[7,2]
OUT[19] = Kall[8,2]
## JN added
# need to get conditional constants here, otherwise they 
# will be recalculated for modern Ca & Mg
#OUT[29] = Kall[9,0] #K_MgCO3
#OUT[30] = Kall[9,1] #K_CaCO3
#OUT[31] = Kall[9,2] #K_MgOH
#OUT[32] = 9999999 #needs a final number at end for code to properly step through everything

# MyAMI modern Ca and Mg
Kall = JN_pKs.calculate_Ks(Tc,Sal, mCa, mMg, mST)
OUT[20] = Kall[1,2]
OUT[21] = Kall[2,2]
OUT[22] = Kall[3,2]
OUT[23] = Kall[4,2]
OUT[24] = Kall[5,2]
OUT[25] = Kall[6,2]
OUT[26] = Kall[7,2]
OUT[27] = Kall[8,2]

OUT[28] = XmCa/mCa

#JN added extra outputs to get other K values
#OUT[29] = Kall[9,1]

#OUT[30] = XmCa/mCa #need to have a final value to read or the code wont work




print OUT
                  

