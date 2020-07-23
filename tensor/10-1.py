import tensorflow as tf
import numpy as np 
# Info 로그를 필터링하려면 1, Warning 로그는 2, Error 로그는 3
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import datetime

learning_rate=0.001
batch_size=100
training_epochs=15
nb_classes=10

mnist=tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()

# normalizing data
x_train, x_test = x_train / 255.0, x_test / 255.0

#change data shape
#print(x_train.shape)
#print(x_train.shape[0])

x_train=x_train.reshape(x_train.shape[0],x_train.shape[1]*x_train.shape[2])
x_test=x_test.reshape(10000, x_test.shape[1] * x_test.shape[2])
#print(x_test.shape)

y_train=tf.keras.utils.to_categorical(y_train,10)
y_test=tf.keras.utils.to_categorical(y_test,10)

#print('y_train : ',y_train[0])
#print('y_test : ',y_test[0])
#print(y_train)

tf.model=tf.keras.Sequential()
tf.model.add(tf.keras.layers.Dense(units=10, input_dim=784, activation='softmax'))
tf.model.compile(loss='categorical_crossentropy', optimizer=tf.optimizers.Adam(0.001),metrics=['accuracy'])
tf.model.summary()

history=tf.model.fit(x_train, y_train, batch_size=batch_size, epochs=training_epochs)

predictions=tf.model.predict(x_test)
print('Prediction: \n', predictions)
#x_train
score=tf.model.evaluate(x_test,y_test)

print('Accuracy: ',score[1])
print(score)
