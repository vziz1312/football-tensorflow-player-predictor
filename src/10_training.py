import os 
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
import tensorflow as tf

x = tf.constant([[1.0], [2.0], [3.0], [4.0]])
y=tf.constant([2.0, 4.0, 6.0, 8.0])
model=tf.keras.Sequential([
    tf.keras.layers.Dense(1)])

model.compile(
    optimizer=tf.keras.optimizers.SGD(learning_rate=0.1),
    loss="mse"
)
history=model.fit(x,y,epochs=100)

print("Weight:", model.layers[0].kernel.numpy())
print("Bias:", model.layers[0].bias.numpy())

prediction = model.predict(tf.constant([[5.0]]), verbose=0)

print("Prediction for 5:", prediction)