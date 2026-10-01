import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

import tensorflow as tf

x = tf.constant(2.0)
y_true = tf.constant(10.0)

w = tf.Variable(3.0)

with tf.GradientTape() as tape:
    y_pred = w * x
    loss = tf.square(y_true - y_pred)

gradient = tape.gradient(loss, w)

print("Weight:", w)
print("Prediction:", y_pred)
print("Loss:", loss)
print("Gradient:", gradient)