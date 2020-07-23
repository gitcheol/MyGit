import tensorflow as tf
import numpy as np 
# Info 로그를 필터링하려면 1, Warning 로그는 2, Error 로그는 3
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

x_data=np.array([[0,0],[0,1],[1,0],[1,1]],dtype=np.float32)
y_data=np.array([[0],[1],[1],[0]],dtype=np.float32)

tf.model=tf.keras.Sequential()
tf.model.add(tf.keras.layers.Dense(units=10,input_dim=2))
tf.model.add(tf.keras.layers.Activation('sigmoid'))
tf.model.add(tf.keras.layers.Dense(units=10,activation='sigmoid'))
tf.model.add(tf.keras.layers.Dense(units=10,activation='sigmoid'))
tf.model.add(tf.keras.layers.Dense(units=10,activation='sigmoid'))
tf.model.add(tf.keras.layers.Dense(units=1,activation='sigmoid'))
tf.model.compile(loss='binary_crossentropy',optimizer=tf.optimizers.SGD(lr=0.1),metrics=['accuracy'])

tf.model.summary()

history=tf.model.fit(x_data, y_data, epochs=10000)

predictions=tf.model.predict(x_data)
print('prediction: \n',predictions)

score=tf.model.evaluate(x_data,y_data)
print('Accuracy: ', score[1])
