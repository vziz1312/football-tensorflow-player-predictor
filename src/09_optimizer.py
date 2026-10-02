import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

import tensorflow as tf

x = tf.constant(2.0)
y_true = tf.constant(10.0)

w = tf.Variable(3.0)

optimizer = tf.keras.optimizers.SGD(learning_rate=0.1)

with tf.GradientTape() as tape:
    y_pred = w * x
    loss = tf.square(y_true - y_pred)

gradient = tape.gradient(loss, w)

optimizer.apply_gradients([(gradient, w)])
new_y_pred=w*x
new_loss=tf.square(y_true - new_y_pred)

print("Updated weight:", w)
print("New prediction:", new_y_pred)
print("New loss:", new_loss)