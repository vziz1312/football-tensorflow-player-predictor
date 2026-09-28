import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

import tensorflow as tf

a = tf.constant([10, 20, 30])
b = tf.constant([1, 2, 3])

addition = a + b
multiplication = a * b

print("Addition:", addition)
print("Multiplication:", multiplication)