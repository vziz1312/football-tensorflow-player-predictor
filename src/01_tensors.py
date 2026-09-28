import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

import tensorflow as tf

player_stats=tf.constant([10,20,30,40])

print("tensor : ", player_stats)
print("shape : ", player_stats.shape)
print("Data type : ", player_stats.dtype)
