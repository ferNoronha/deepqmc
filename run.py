from Combined import *

def fit(batch_size=2056,steps=15,epochs=4,R1=1.5,R2=-1.5,losses=["variance","energy","symmetry"]):

for i in range(10):
    fit(steps=1000,epochs=32,losses=["variance"])
    fit(steps=1000,epochs=32,losses=["energy"])
    fit(steps=1000,epochs=32,losses=["variance,energy"])
    fit(steps=1000,epochs=32)
