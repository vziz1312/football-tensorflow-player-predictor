import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

import tensorflow as tf

players = tf.constant([
    [0.72, 0.35, 3.4, 42.1, 6.2],
    [0.45, 0.20, 2.1, 55.3, 3.8],
    [0.90, 0.50, 4.2, 30.5, 8.1]
])

print(players)
print("Shape:", players.shape)
print("First player:", players[0])
print("Second player:", players[1])

print("First player's goals:", players[0][0])
print("Second player's shots:", players[1][2])

print("Goals + assists:")
print(players[:, 0] + players[:, 1])