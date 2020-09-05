import tensorflow as tf
import numpy as np 
# Info 로그를 필터링하려면 1, Warning 로그는 2, Error 로그는 3
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import random

random.seed(777)
learning_rate=0.001
batch_size=100
training_epochs=15
nb_classes=10

mnist=tf.keras.datasets.mnist

(x_train, y_train), (x_test2, y_test) = tf.keras.datasets.mnist.load_data()

# normalizing data
#x_train, x_test = x_train / 255.0, x_test / 255.0

x_train= x_train.reshape(x_train.shape[0],784)
x_test=x_test2.reshape(x_test2.shape[0],784)

y_train=tf.keras.utils.to_categorical(y_train,nb_classes)
y_test=tf.keras.utils.to_categorical(y_test,nb_classes)


#Glorot normal initializer, also called Xavier normal initializer. 
tf.model=tf.keras.Sequential()
tf.model.add(tf.keras.layers.Dense(input_dim=784, units=256,kernel_initializer='glorot_normal', activation='relu'))
tf.model.add(tf.keras.layers.Dense(units=512,kernel_initializer='glorot_normal',activation='relu'))
tf.model.add(tf.keras.layers.Dense(units=512,kernel_initializer='glorot_normal',activation='relu'))
tf.model.add(tf.keras.layers.Dense(units=512,kernel_initializer='glorot_normal',activation='relu'))
tf.model.add(tf.keras.layers.Dense(units=nb_classes,kernel_initializer='glorot_normal',activation='softmax'))
tf.model.compile(loss='categorical_crossentropy', optimizer=tf.keras.optimizers.Adam(lr=learning_rate), metrics=['accuracy'])
tf.model.summary()

tf.model.fit(x_train,y_train,batch_size=batch_size, epochs=training_epochs)

y_predicted=tf.model.predict(x_test)
for x in range(0,10):
    random_index=random.randint(0,x_test.shape[0]-1)
    print("index: ", random_index, "actual y: ", np.argmax(y_test[random_index]),
        "predicted y : ", np.argmax(y_predicted[random_index]))



evaluation=tf.model.evaluate(x_test,y_test)
print('loss : ', evaluation[0])
print('accuracy', evaluation[1])
