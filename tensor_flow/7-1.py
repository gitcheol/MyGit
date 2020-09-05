import tensorflow as tf
import numpy as np 
# Info 로그를 필터링하려면 1, Warning 로그는 2, Error 로그는 3
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

x_data = [[1, 2, 1],
          [1, 3, 2],
          [1, 3, 4],
          [1, 5, 5],
          [1, 7, 5],
          [1, 2, 5],
          [1, 6, 6],
          [1, 7, 7]]
y_data = [[0, 0, 1],
          [0, 0, 1],
          [0, 0, 1],
          [0, 1, 0],
          [0, 1, 0],
          [0, 1, 0],
          [1, 0, 0],
          [1, 0, 0]]

# Evaluation our model using this test dataset
x_test = [[2, 1, 1],
          [3, 1, 2],
          [3, 3, 4]]
y_test = [[0, 0, 1],
          [0, 0, 1],
          [0, 0, 1]]


learning_rate=0.1

tf.model = tf.keras.Sequential()

#units==output shape, input_dim == input shape
tf.model.add(tf.keras.layers.Dense(units=3, input_dim=3, activation='sigmoid'))

#sgd=tf.keras.optimizers.SGD(lr=1e-5)
tf.model.compile(loss='categorical_crossentropy',optimizer=tf.keras.optimizers.SGD(lr=learning_rate),metrics=['accuracy'])


#prints summary of the model to the terminal
tf.model.summary()

#ift() executes training
history=tf.model.fit(x_data, y_data, epochs=1000)


#predict() returns predicted value
#y_predict=tf.model.predict(np.array([[1,2]]))
#print(y_predict)
print("Accuracy: ", tf.model.evaluate(x_test,y_test)[1])
