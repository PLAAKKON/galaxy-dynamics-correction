import numpy as np,csv
from pathlib import Path
P=Path(__file__).parent
Gconv=1.022712165; vc=200*Gconv; rc=.5; a=5.; dt=.002; steps=1500; N=1200
# log base potential, transient rotating quadrupoles (all gone by end)
def run(seed,scenario):
 rng=np.random.default_rng(seed); r=rng.uniform(6,14,N); th=rng.uniform(0,2*np.pi,N)
 x=np.stack([r*np.cos(th),r*np.sin(th)],axis=1)
 v=vc*r/np.sqrt(r*r+rc**2)
 vel=np.stack([-v*np.sin(th),v*np.cos(th)],axis=1)
 initlz=x[:,0]*vel[:,1]-x[:,1]*vel[:,0]
 def acc(t,x):
  rr=(x*x).sum(1); rad=np.sqrt(rr); ax=-vc**2*x/(rr[:,None]+rc**2)
  if scenario=='control': return ax
  pulses=([(0.65,0.23,0.015,25.)] if scenario=='early_short' else
          [(0.65,0.42,0.015,25.)] if scenario=='early_long' else
          [(0.55,0.22,0.015,25.),(1.4,0.22,0.015,19.)])
  for center,width,epsilon,pattern in pulses:
   e=epsilon*np.exp(-0.5*((t-center)/width)**2)
   if e<1e-12:continue
   az=np.arctan2(x[:,1],x[:,0])-pattern*Gconv*t
   f=rr/(rr+a*a)
   ar=-e*vc**2*2*rad*a*a/(rr+a*a)**2*np.cos(2*az)
   at=2*e*vc**2*f/np.maximum(rad,1e-10)*np.sin(2*az)
   ax+=np.column_stack((ar*x[:,0]/rad-at*x[:,1]/rad,ar*x[:,1]/rad+at*x[:,0]/rad))
  return ax
 ac=acc(0,x)
 for i in range(steps):
  vel+=.5*dt*ac;x+=dt*vel;ac=acc((i+1)*dt,x);vel+=.5*dt*ac
 R=np.linalg.norm(x,axis=1);vr=(x*vel).sum(1)/R/Gconv
 vt=(x[:,0]*vel[:,1]-x[:,1]*vel[:,0])/R/Gconv
 lz=x[:,0]*vel[:,1]-x[:,1]*vel[:,0]
 return {'r':R,'vr':vr,'vt':vt,'lz':lz,'dl':(lz-initlz)/initlz*100,'rg':lz/vc,'rg0':initlz/vc}
rows=[];summary=[]
for seed in range(5):
 runs={s:run(seed,s) for s in ['control','early_short','early_long','two_episodes']}
 for name,z in runs.items():
  rgshift=z['rg']-z['rg0']; dl=z['dl'];
  summary.append([seed,name,round(np.mean(np.abs(rgshift)),5),round(np.median(np.abs(rgshift)),5),round(np.mean(np.abs(dl)),5),round(np.mean(dl),5),round(np.mean(np.abs(rgshift)>0.5)*100,3)])
  for low in (6,8,10,12):
   high=low+2; sel=(z['r']>=low)&(z['r']<high); vt=z['vt'][sel]; vr=z['vr'][sel]
   vct=200*(low+1)/np.sqrt((low+1)**2+rc**2)
   proxy=100*((np.mean(vt)/vct)**2-1)
   rows.append([seed,name,low+1,int(sel.sum()),round(float(np.mean(vt)),4),round(float(np.std(vr)),4),round(float(proxy),4)])
with (P/'radat.csv').open('w',newline='') as f:
 w=csv.writer(f);w.writerow(['seed','history','r_kpc','n','mean_vphi_kms','sigma_vr_kms','naive_mass_proxy_pct']);w.writerows(rows)
with (P/'migraatio.csv').open('w',newline='') as f:
 w=csv.writer(f);w.writerow(['seed','history','mean_abs_delta_rg_kpc','median_abs_delta_rg_kpc','mean_abs_delta_Lz_pct','mean_delta_Lz_pct','fraction_shift_over_0p5kpc_pct']);w.writerows(summary)
print('MIGRATION MEAN over seeds:')
for s in ['control','early_short','early_long','two_episodes']:
 data=np.array([q[2:] for q in summary if q[1]==s],float)
 print(s, 'mean abs dRg',round(data[:,0].mean(),3),'delta Lz abs %',round(data[:,2].mean(),3),'shift>0.5 %',round(data[:,4].mean(),2))
print('BIN PROXY DIFFERENCES mean over seeds:')
for s in ['early_short','early_long','two_episodes']:
 for rad in [7,9,11,13]:
  v=np.array([z[6] for z in rows if z[1]==s and z[2]==rad]); b=np.array([z[6] for z in rows if z[1]=='control' and z[2]==rad]);print(s,rad,round(np.mean(v-b),3))
