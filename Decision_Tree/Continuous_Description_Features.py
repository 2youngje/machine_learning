import numpy as np

spring = [2100,4740,4900]
summer = [3000,5800,6200]
autumn = [2910,2880,2820]
winter = [800,826,900]

season = np.var(spring)+np.var(summer)+np.var(autumn)+np.var(winter)

tru = [900,4740,4900,5800,6200,2820]
fals = [800,826,2100,3000,2910,2880]

boolean = np.var(tru)+np.var(fals)

print(season/4)
print(boolean/2)