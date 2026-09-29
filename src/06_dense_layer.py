import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

import tensorflow as tf

x = tf.constant([[0.8, 0.4, 3.0]])

layer = tf.keras.layers.Dense(4)

y = layer(x)

print("Input:", x)
print("Output:", y)
print("Output shape:", y.shape)
print("Weights shape:", layer.kernel.shape)
print("Bias shape:", layer.bias.shape)