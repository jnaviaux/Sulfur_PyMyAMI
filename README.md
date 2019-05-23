# Sulfur_PyMyAMI
Code Modified from Hain et al (2015) to calculate seawater equilibrium constants under conditions of variable [Sulfur]
MyAMI Specific Ion Interaction Model (Version 1.0):

MyAMI is Python code to calculate thermodynamic pK's and conditional pK's

Author: Mathis P. Hain -- m.p.hain@soton.ac.uk
Modified by John D. Naviaux --jnaviaux@caltech.edu

Reference:
Hain, M.P., Sigman, D.M., Higgins, J.A., and Haug, G.H. (2015) The effects of secular calcium and magnesium concentration changes on the thermodynamics of seawater acid/base chemistry: Implications for Eocene and Cretaceous ocean carbon chemistry and buffering, Global Biogeochemical Cycles, 29, doi:10.1002/2014GB004986

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
REQUIREMENTS: (1) you need Python (2.7.5 verified); (2) you need the standard Python modules ?NumPy? and ?SciPy?;
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

HOW TO:
Call Python code from MATLAB to calculate conditional and thermodynamic equilibrium constants at a given [Ca2+], [Mg2+], [Sulfur], temperature and salinity.

(1) open Matlab
(2) navigate to folder that contains [JN_PyMyAMI.m]
(3) >>PITZERpath = '~/path/to/folder/of/MyAMI/code/JN_Pitzer.py';
(4) >>T = 25;
(5) >>S = 35;
(6) >>Ca = 0.0102821 * S/35;
(7) >>Mg = 0.0528171* S/35;
(8) >>xST= 0.0282352* S/35; %This is the concentration of sulfur
(9) >>B = xB*S / 1.80655 * 0.0000219;   
(10) >>[K] = JN_PyMyAMI(PITZERpath,num2str(T),num2str(S),num2str(Ca),num2str(Mg));

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

HOW TO: Calculate the change in Calcite or Aragonite Saturation for a given seawater composition [Ca2+],[Mg2+],[Sulfur]

(1) open Matlab
(2) open Omega_Calculator_CO2SYS_PyMyAMI.m
(3) Change [Ca2+],[Mg2+],[Sulfur] to desired values by changing xCa, xMg, xST, respectively. Note that xCa, xMg, and xST vary are the fraction of concentration with respect to modern values.
(4) Input Alk, pH, and/or DIC of the seawater, along with any other desired parameters (phosphate, silicate, pressure, temperature, etc)
(5) Hit run!
