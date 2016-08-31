# generates a multivariate set of data 

import numpy as np

N=1000

cov_A = np.array([[4.0, 0.0], 
                  [0.0, 1.0]])
mean_A = np.array([0,0])
data = np.random.multivariate_normal(mean_A, cov_A, size=N)
np.savetxt('data_A.txt', data)


cov_B = np.array([[4.0, 1.8], 
                  [1.8, 1.0]])
mean_B = np.array([0,0])
data = np.random.multivariate_normal(mean_B, cov_B, size=N)
np.savetxt('data_B.txt', data)


cov_C = np.array([[4.0, 1.8, 0.9], 
                  [1.8, 2.0, 0.9], 
                  [0.9, 0.9, 0.5]])
mean_C = np.array([0,0,0])
data = np.random.multivariate_normal(mean_C, cov_C, size=N)
np.savetxt('data_C.txt', data)
