import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

import tensorflow as tf

x = tf.constant([0.8, 0.4, 3.0])
w = tf.constant([2.0, 1.5, 0.2])
b = tf.constant(0.5)

weighted_inputs = x * w

y = tf.reduce_sum(weighted_inputs) + b

print("Inputs:", x)
print("Weights:", w)
print("Weighted inputs:", weighted_inputs)
print("Output:", y)