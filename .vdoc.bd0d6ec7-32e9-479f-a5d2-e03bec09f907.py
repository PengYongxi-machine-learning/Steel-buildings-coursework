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
L = 54
Hr = 4
Hg = 6
H = 8*Hr + Hg

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
ifactor = 0.7
Gtyp_f = gt_f + gs_f + gc_f + gste_f + gser_f
Qtyp_f = qpar_f + qimp_f
wtyp_f = 1.35 * Gtyp_f + 1.5 * ifactor * Qtyp_f
# Dead roof
gt_r = 1.0
gs_r = 3.38
gc_r = 0.5
gste_r = 0.2
gser_r = 1.0
# Impose roof
qimp_r = 1.5

Gtyp_r = gt_r + gs_r + gc_r + gste_r + gser_r
Qtyp_r = qimp_r

# Wind load
wk = 1.3
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
#
#
#
#
#
#
#
#
#
# wind load per floor
wfactor = 1.5
Wtotal = wfactor*L*H*wk
Fb = wtotal/4
wudl = Fb/H
wr = wudl*Hr*0.5
wf1 = wudl*Hr
wf2 = wudl*Hg

# floor load
A = (60+45)*54/2
Fstorey = 
#
#
#
