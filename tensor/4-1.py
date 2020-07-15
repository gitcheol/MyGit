import tensorflow as tf
import numpy as np 
# Info 로그를 필터링하려면 1, Warning 로그는 2, Error 로그는 3
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

x_train= [[73., 80., 75.],
          [93., 88., 93.],
          [89., 91., 90.],
          [96., 98., 100.],
          [73., 66., 70.]]
y_train = [[152.],
          [185.],
          [180.],
          [196.],
          [142.]]



tf.model = tf.keras.Sequential()

#units==output shape, input_dim == input shape
tf.model.add(tf.keras.layers.Dense(units=1, input_dim=3))
tf.model.add(tf.keras.layers.Activation('linear'))#this line can be omitted, as linear activation is default


sgd=tf.keras.optimizers.SGD(lr=1e-5)
tf.model.compile(loss='mse',optimizer=sgd)


#prints summary of the model to the terminal
tf.model.summary()

#ift() executes training
history=tf.model.fit(x_train, y_train, epochs=100)


#predict() returns predicted value
y_predict=tf.model.predict(np.array([[73.,80.,75.]]))
print(y_predict)

