import tensorflow as tf
import numpy as np 
# Info 로그를 필터링하려면 1, Warning 로그는 2, Error 로그는 3
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

x_train= [[1, 2],
          [2, 3],
          [3, 1],
          [4, 3],
          [5, 3],
          [6, 2]]
y_train= [[0],
          [0],
          [0],
          [1],
          [1],
          [1]]


tf.model = tf.keras.Sequential()

#units==output shape, input_dim == input shape
tf.model.add(tf.keras.layers.Dense(units=1, input_dim=2))
tf.model.add(tf.keras.layers.Activation('sigmoid'))#this line can be omitted, as linear activation is default


#sgd=tf.keras.optimizers.SGD(lr=1e-5)
tf.model.compile(loss='binary_crossentropy',optimizer=tf.keras.optimizers.SGD(lr=0.01),metrics=['accuracy'])


#prints summary of the model to the terminal
tf.model.summary()

#ift() executes training
history=tf.model.fit(x_train, y_train, epochs=5000)


#predict() returns predicted value
y_predict=tf.model.predict(np.array([[1,2]]))
print(y_predict)
print("Accuracy: ", history.history['accuracy'][-1])
