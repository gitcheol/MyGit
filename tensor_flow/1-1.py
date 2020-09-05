import tensorflow as tf
import numpy as np 
# Info 로그를 필터링하려면 1, Warning 로그는 2, Error 로그는 3
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

node1=tf.constant(3.0,tf.float32)
node2=tf.constant(3.0,tf.float32)

out_a=node1+node2
print(out_a)

