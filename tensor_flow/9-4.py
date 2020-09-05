import tensorflow as tf
import numpy as np 
# Info 로그를 필터링하려면 1, Warning 로그는 2, Error 로그는 3
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import datetime

x_data=np.array([[0,0],[0,1],[1,0],[1,1]],dtype=np.float32)
y_data=np.array([[0],[1],[1],[0]],dtype=np.float32)

tf.model=tf.keras.Sequential()
tf.model.add(tf.keras.layers.Dense(units=2,input_dim=2))
tf.model.add(tf.keras.layers.Activation('sigmoid'))
tf.model.add(tf.keras.layers.Dense(units=1,input_dim=2))
tf.model.add(tf.keras.layers.Activation('sigmoid'))
tf.model.compile(loss='binary_crossentropy',optimizer=tf.optimizers.SGD(lr=0.1),metrics=['accuracy'])
tf.model.summary()


#prepare callback
log_dir = os.path.join(".","logs","fit",datetime.datetime.now().strftime("%Y%m%d~%H%M%S"))
tensorboard_callback=tf.keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1)

#add callback param to fit()
history=tf.model.fit(x_data, y_data, epochs=10000, callbacks=[tensorboard_callback])


history=tf.model.fit(x_data, y_data, epochs=10000)

predictions=tf.model.predict(x_data)
print('prediction: \n',predictions)

score=tf.model.evaluate(x_data,y_data)
print('Accuracy: ', score[1])
'''
at the end of the run, open terminal / command window
cd to the source directory
tensorboard --logdir logs/fit
read more on tensorboard: https://www.tensorflow.org/tensorboard/get_started
'''
