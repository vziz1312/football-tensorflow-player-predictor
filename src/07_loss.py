import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

import tensorflow as tf

y_true = tf.constant(10.0)
y_pred = tf.constant(9.0)

loss = tf.square(y_true - y_pred)

print("True value:", y_true)
print("Predicted value:", y_pred)
print("Loss:", loss)