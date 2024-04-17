from scipy.cluster.hierarchy import dendrogram
import numpy as np
from process_cube.dat import read_dat_file, Header
from matplotlib import pyplot as plt
import sys
sys.setrecursionlimit(1000000) 


header = Header.read_header("self_test_rad.hdr")
img = read_dat_file("self_test_rad.img", header).astype(np.float64)
mine = np.fromfile("hierarchy").reshape(-1,4)
print("1")
plt.figure()
print("2")
dendrogram(mine)
print("3")
plt.show()
