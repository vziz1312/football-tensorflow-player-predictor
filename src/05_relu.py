import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

import tensorflow as tf

x = tf.constant([-3.0, -1.0, 0.0, 2.0, 5.0])

y = tf.nn.relu(x)

print("Before ReLU:", x)
print("After ReLU:", y)