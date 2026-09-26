import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

import tensorflow as tf

players = tf.constant([
    [0.72, 0.35, 3.4, 42.1, 6.2],
    [0.41, 0.20, 2.1, 35.7, 4.8],
    [0.85, 0.51, 4.2, 38.4, 7.1]
])

print(players)
print("Shape:", players.shape)