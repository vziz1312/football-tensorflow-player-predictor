import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

import tensorflow as tf

x = tf.constant(5.0)

w = tf.Variable(2.0)
b = tf.Variable(1.0)

y = w * x + b

print("Input:", x)
print("Weight:", w)
print("Bias:", b)
print("Output:", y)