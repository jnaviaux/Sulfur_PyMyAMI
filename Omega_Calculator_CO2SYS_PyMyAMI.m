clc
clear all
close all

%% JN Note 2-28-19
% different Sulfur concentrations now have an effect on CO2SYs, but boron does not

%Set concentrations of species w.r.t. modern values in mol/kg
%     Ca = xCa*0.0102821 * Sal/35;
%     Mg = xMg*0.0528171* Sal/35; 
%     B  = xB*Sal / 1.80655 * 0.0000219;
%     S  = xST.*0.02824*(Sal./35); 

%xCa, xMg, Alk, DIC must all be vectors of the same length!
xB  = 1; %fraction of Boron w.r.t. modern value
xST = 1; %fraction of Sulfur w.r.t. modern value
xCa = [1]; %fraction of Ca w.r.t. modern value 
xMg = [1
 ]; %fraction of Mg w.r.t. modern value

Alk = [2200]; %umol/kg

ph_measured = [7.403];
DIC = [2238.6
]; %umol/kg

Temp= 21; %temperature in C

par1type =    1; % The first parameter ssupplied is of type "1", which is "alkalinity" (3 is pH)
par1     = Alk; % value of the first parameter
par2type =    2; % The first parameter supplied is of type "2", which is "DIC"
par2     = DIC; % value of the second parameter, which is a long vector of different DICs
sal      =   35; % Salinity of the sample
tempin   = Temp; % Temperature at input conditions
presin   =    0; % Pressure    at input conditions, in dbar or m 
tempout  =    0; % Temperature at output conditions - doesn't matter in this example
presout  =    0; % Pressure    at output conditions - doesn't matter in this example
sil      =    0; % Concentration of silicate  in the sample (in umol/kg)
po4      =    .5; % Concentration of phosphate in the sample (in umol/kg)
pHscale  =    1; % pH scale at which the input pH is reported ("1" means "Total Scale")  - doesn't matter in this example
k1k2c    =    14; % Choice of H2CO3 and HCO3- dissociation constants K1 and K2 ("14" means "Mathis refit", "10" is Lueker(2000) refit.)
kso4c    =    4; % Choice of HSO4- dissociation constants KSO4 ("1" means "Dickson", "4" means Mathis)

%%  Do the calculation. See CO2SYS's help for syntax and output format

%for i =1:length(xMg);
for i =1:length(Alk)
A = Sulfur_CO2SYS_PyMyAMI_JN_edits(par1(i),par2(i),par1type,par2type,sal,tempin,tempout,presin,presout,sil,po4,pHscale,k1k2c,kso4c,xB,xST,xCa,xMg);

     Omega(i) = A(:,15);
     OmegaAR(i)=A(:,16);
     k0(i) = A(:,55); %K_henry
     k1(i)= A(:,56);
     k2(i) = A(:,57);
     
     pH(i) = A(:,3);
     %Ca(i) = xCa(i)*0.0102821*sal/35;
     CO2(i) = A(:,8);
     HCO3(i) = A(:,6);
     CO3(i) = A(:,7);
     Balk(i) = A(:,9); %alk from borate
     %logKsp(i) = log10(CO3(i).*Ca./Omega(i)*1e-6);
     HSO4(i)=A(:,33);
     TS(i) = A(:,83); %total amount of SO4 in system
     
end
% format long
% disp([k1, k2, logKsp])
% format bank
disp('Omega Calcite')
disp([Omega]')