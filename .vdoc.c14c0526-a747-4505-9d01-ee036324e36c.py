# type: ignore
# flake8: noqa
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
import math
%precision 2
# Setup
floor = 8
section = '203 x 203x 52'
ixp = 1     # Index for primary lx
ixs = 1     # Index for secondary lx
it = 3      # Scenario index

# Automation start here
lp_list = [6000, 8250, 7500]
ls_list = [1500, 3000, 2750, 3750, 1875]
Type_list = ['Edge', 'Perimeter1', 'Perimeter2', 'Internal']
Type = Type_list[it-1]
lxl = lp_list[ixp-1]
s_lx = ls_list[ixs-1]

# Scenario in primary and secondary beams
if Type == 'Edge':
    Typep = 'Perimeter'
    Types = 'Edge'
    BC = 2
elif Type == 'Perimeter1':
    Typep = 'Perimeter'
    Types = 'Internal'
    BC = 3
elif Type == 'Perimeter2':
    Typep = 'Internal'
    Types = 'Edge'
    BC = 5
else:
    Typep = 'Internal'
    Types = 'Internal'
    BC = 4

# Heights for Floor and Roof
if floor == 1:
  H = 6000
else:
  H = 4000

# Dead floor
gt_f = 0.7
gs_f = 3.38
gc_f = 0.5
gste_f = 0.3
gser_f = 1.4

# Impose floor
qpar_f = 1.0
qimp_f = 4.0
qcl = 1.2

# Dead roof
gt_r = 1.0
gs_r = 3.38
gc_r = 0.5
gste_r = 0.2
gser_r = 1.0

# Impose roof
qimp_r = 1.5

# ULS loads
Gtyp_f = gt_f + gs_f + gc_f + gste_f + gser_f
Qtyp_f = qpar_f + qimp_f
wtyp_f = 1.35 * Gtyp_f + 1.5 * Qtyp_f
Gtyp_r = gt_r + gs_r + gc_r + gste_r + gser_r
Qtyp_r = qimp_r
wtyp_r = 1.35 * Gtyp_r + 1.5 * Qtyp_r

# Cladding loads specific to beam types & levels
p_qclad_f = 0.0 if Typep == 'Internal' else 1.5 * qcl * H * 1e-3
s_qclad_f = 0.0 if Types == 'Internal' else 1.5 * qcl * H * 1e-3
# Primary beam Ved
p_ly = 13500 / 2 if Typep == 'Perimeter' else 13500 
SB = 2 if lxl == 8250 else 1
p_lb = lxl
if SB == 1:
    # Floor Calculations
    ptotal_f = 1e-6 * wtyp_f * p_lb * p_ly / 2
    p_Ved_f = ptotal_f / 2 + p_qclad_f * (p_lb * 1e-3) / 2
    
    # Roof Calculations
    ptotal_r = 1e-6 * wtyp_r * p_lb * p_ly / 2
    p_Ved_r = ptotal_r / 2
else:
    # Floor Calculations
    ptotal_f = 1e-6 * wtyp_f * p_lb * p_ly / 3
    p_Ved_f = ptotal_f + p_qclad_f * (lxl * 1e-3) / 2
    # Roof Calculations
    ptotal_r = 1e-6 * wtyp_r * p_lb * p_ly / 3
    p_Ved_r = ptotal_r
# Ssecondary beam Ved
s_ly = 13500
qtyp_applied_f = wtyp_f * s_lx * 1e-3
qtyp_applied_r = wtyp_r * s_lx * 1e-3
if Types == 'Edge':
    qtotal_f = s_qclad_f + qtyp_applied_f
    qtotal_r =  qtyp_applied_r
else:
    qtotal_f = qtyp_applied_f
    qtotal_r = qtyp_applied_r
s_Ved_f = qtotal_f * (s_ly * 1e-3) / 2
s_Ved_r = qtotal_r * (s_ly * 1e-3) / 2
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
import pandas as pd
import math

df_all = pd.read_csv('section_mm.csv')
if df_all.columns[0] == 'Unnamed: 0':
  df_all = df_all.rename(columns = {'Unnamed: 0' : 'Section Profile'})

# Scientific notation formatter
def sci(value):
    exp_num = math.floor(math.log10(abs(value)))
    base = value / (10 ** exp_num)
    return value, base, exp_num

#material
fu= 500.0
fy = 355.0
E = 210000
G = 81000

df = df_all[df_all['Section Profile'] == section]
#section
h = float(df['h (mm)'].iloc[0])
b = float(df['b (mm)'].iloc[0])
tw = float(df['tw (mm)'].iloc[0])
tf = float(df['tf (mm)'].iloc[0])
d = float(df['d (mm)'].iloc[0])
r= float(df['r(mm)'].iloc[0])
A, A1, A2 = sci(float(df['A (mm^2)'].iloc[0]))
Iy, Iy1, Iy2 = sci(float(df['Iy (mm^4)'].iloc[0]))
Iz, Iz1, Iz2 = sci(float(df['Iz (mm^4)'].iloc[0]))
Ry = float(df['Ry (mm)'].iloc[0])
Rz = float(df['Rz (mm)'].iloc[0])
Wey, Wey1, Wey2 = sci(float(df['W_el,y (mm^3)'].iloc[0]))
Wez, Wez1, Wez2 = sci(float(df['W_el,z (mm^3)'].iloc[0]))
Wpy, Wpy1, Wpy2 = sci(float(df['W_pl,y (mm3)'].iloc[0]))
Wpz, Wpz1, Wpz2 = sci(float(df['W_pl,z (mm^3)'].iloc[0]))
Iw, Iw1, Iw2 = sci(float(df['I_w (mm^6)'].iloc[0]))
It, It1, It2 = sci(float(df['I_T (mm^4)'].iloc[0]))

ratio = h/b
if ratio > 1.2:
  if tf <= 40:
    ay = 0.21
    az = 0.34
  else:
    ay = 0.34
    az = 0.49
else:
  if tf <= 100:
    ay = 0.34
    az = 0.49
  else:
    ay = 0.70
    az = 0.70
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# Count number of floors above the column
num_floor = 9 - floor
if num_floor == 8:
    nfloor =7.5
else: 
    nfloor = num_floor
# eccentricity
ecc_y = (100 + h/2)
ecc_z = (100 + tw/2)

# Axial load and moment on column
if Type == 'Edge':
  BC =2 
  Ned = nfloor*p_Ved_f + p_Ved_r + nfloor*s_Ved_f + s_Ved_r
  Myed = p_Ved_f*ecc_y*1e-3
  Mzed = s_Ved_f*ecc_z*1e-3
elif Type == 'Perimeter1':
  BC = 3
  Ned = nfloor*p_Ved_f + p_Ved_r + 2*nfloor*s_Ved_f + 2*s_Ved_r
  Myed = (s_Ved_f - s_Ved_f)*ecc_y*1e-3
  Mzed = p_Ved_f*ecc_z*1e-13
elif Type == 'Internal':
  BC = 4
  Ned = 2*nfloor*p_Ved_f + 2*p_Ved_r + 2*nfloor*s_Ved_f + 2*s_Ved_r
  Myed = (p_Ved_f - p_Ved_f)*ecc_y*1e-3
  Mzed = (s_Ved_f - s_Ved_f)*ecc_z*1e-3
elif Type == 'Perimeter2':
  BC = 5
  Ned = nfloor*s_Ved_f + s_Ved_r + 2*nfloor*s_Ved_f + 2*p_Ved_r
  Myed = p_Ved_f*ecc_y*1e-3
  Mzed = (s_Ved_f - s_Ved_f)*ecc_z*1e-13
else:
  raise ValueError(f"Unsupported Type: {Type}")
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
ep = math.sqrt(235/fy)
crf = 9*ep
crw = 28*ep
cw = d
c1 = cw/tw
cf = (b-tw-2*r)/2
c2 = cf/tf
```
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
def buckle (Lcr, I, E, A, fy, a):
  Ncr = (math.pi**2 * E * I) / ((Lcr)**2)*1e-3
  lam = math.sqrt(( A*fy / (Ncr*1e3) ))
  phi = 0.5*(1 + a*(lam - 0.2) + lam**2)
  chi = min(1/(phi + math.sqrt(phi**2 - lam**2)),1)
  return Ncr, lam, phi, chi

Lcr = H
Ncry, lamy, phiy, chiy = buckle(Lcr, Iy, E, A, fy, ay)
Ncrz, lamz, phiz, chiz = buckle(Lcr, Iz, E, A, fy, az)

gamma1 = 1.0
chi = min([chiy,chiz])
Nrd = chi*A*fy*1e-3/gamma1
from IPython.display import Latex
if Nrd > Ned:
    output_axial = 'the section is safe in resisting axial load'
else:
    output_axial = 'the section is not safe in resisting axial load'
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
Mcr = ((math.pi**2 * E * Iz) / Lcr**2) * math.sqrt(Iw/Iz + (G * It * (Lcr)**2)/ (math.pi**2 * E * It))*1e-6
if ratio > 1.2:
    if tf <= 40:
        alt = min(0.12*math.sqrt(Wey/Wez), 0.34)
    else:
        alt = min(0.16*math.sqrt(Wey/Wez), 0.49)
else:
    alt = min(0.16*math.sqrt(Wey/Wez), 0.49)

phi_lt = 0.5*(1 + alt*(min(lamy,lamz) - 0.2) + min(lamy,lamz)**2)
chi_lt = min(1/(phi_lt + math.sqrt(phi_lt**2 - min(lamy,lamz)**2)),1)

Myrk = Wpy*fy*1e-6
Mzrk = Wpz*fy*1e-6
Mbrd = chi_lt*Myrk/gamma1
Mcrdz = Mzrk/gamma1

if Mbrd > Myed and Mcrdz > Mzed:
    output_moment = 'the section is safe in resisting bending'
else:
    output_moment = 'the section is not safe in resisting bending'

int_ratio = Ned/Nrd + Myed/Mbrd + Mzed/Mcrdz
if int_ratio < 1.0:
    output_interaction = 'the result is less than 1, the section is safe in resisting interaction'
else:
    output_interaction = 'the result is greater than 1, the section is not safe in resisting interaction'
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
