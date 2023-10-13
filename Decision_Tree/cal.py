import numpy as np

IG_stream = 0.3060
IV_stream = -(4/7*np.log2(4/7)+3/7*np.log2(3/7))

IG_ratio_stream = IG_stream / IV_stream

print(IG_ratio_stream)

IG_slope = 0.5774
IV_slope = -((5/7)*np.log2(5/7)+2*(1/7)*np.log2(1/7))
IG_ratio_slope = IG_slope / IV_slope
print(IG_ratio_slope)

IG_elevation = 0.8774
IV_elevation = -((2/7)*np.log2(2/7)+(3/7)*np.log2(3/7))
IG_ratio_elevation = IG_elevation / IV_elevation
print(IG_ratio_elevation)