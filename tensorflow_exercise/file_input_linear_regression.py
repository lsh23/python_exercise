import tensorflow as tf
import numpy as np
tf.set_random_seed(777)
csv_data = np.loadtxt('Admission_Predict.csv', delimiter = ',')
