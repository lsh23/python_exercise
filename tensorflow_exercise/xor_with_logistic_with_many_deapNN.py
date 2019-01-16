import tensorflow as tf
import numpy as np

x_data = np.array([[0,0],[0,1],[1,0],[1,1]], dtype=np.float32)
y_data = np.array([[0],[1],[1],[0]])

X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)

# W = tf.Variable(tf.random_normal([2,1]), name = "weight")
# b = tf.Variable(tf.random_normal([1]), name ="bias")

W1 = tf.Variable(tf.random_normal([2,5],-1.0, 1.0), name = "weight1")
W2 = tf.Variable(tf.random_normal([5,5],-1.0, 1.0), name = "weight2")
W3 = tf.Variable(tf.random_normal([5,5],-1.0, 1.0), name = "weight3")
W4 = tf.Variable(tf.random_normal([5,5],-1.0, 1.0), name = "weight4")
W5 = tf.Variable(tf.random_normal([5,5],-1.0, 1.0), name = "weight5")
W6 = tf.Variable(tf.random_normal([5,5],-1.0, 1.0), name = "weight6")
W7 = tf.Variable(tf.random_normal([5,5],-1.0, 1.0), name = "weight7")
W8 = tf.Variable(tf.random_normal([5,5],-1.0, 1.0), name = "weight8")
W9 = tf.Variable(tf.random_normal([5,5],-1.0, 1.0), name = "weight9")
W10 = tf.Variable(tf.random_normal([5,5],-1.0, 1.0), name = "weight10")

W11 = tf.Variable(tf.random_normal([5,1],-1.0, 1.0), name = "weight11")

b1 = tf.Variable(tf.random_normal([5]), name ="bias1")
b2 = tf.Variable(tf.random_normal([5]), name ="bias2")
b3 = tf.Variable(tf.random_normal([5]), name ="bias3")
b4 = tf.Variable(tf.random_normal([5]), name ="bias4")
b5 = tf.Variable(tf.random_normal([5]), name ="bias5")
b6 = tf.Variable(tf.random_normal([5]), name ="bias6")
b7 = tf.Variable(tf.random_normal([5]), name ="bias7")
b8 = tf.Variable(tf.random_normal([5]), name ="bias8")
b9 = tf.Variable(tf.random_normal([5]), name ="bias9")
b10 = tf.Variable(tf.random_normal([5]), name ="bias10")
b11 = tf.Variable(tf.random_normal([1]), name ="bias11")

L1 = tf.sigmoid(tf.matmul(X,W1)+ b1)
L2 = tf.sigmoid(tf.matmul(L1,W2)+ b2)
L3 = tf.sigmoid(tf.matmul(L2,W3)+ b3)
L4 = tf.sigmoid(tf.matmul(L3,W4)+ b4)
L5 = tf.sigmoid(tf.matmul(L4,W5)+ b5)
L6 = tf.sigmoid(tf.matmul(L5,W6)+ b6)
L7 = tf.sigmoid(tf.matmul(L6,W7)+ b7)
L8 = tf.sigmoid(tf.matmul(L7,W8)+ b8)
L9 = tf.sigmoid(tf.matmul(L8,W9)+ b9)
L10 = tf.sigmoid(tf.matmul(L9,W10)+ b10)

hypothesis = tf.sigmoid(tf.matmul(L10,W11) +b11)

cost = -tf.reduce_mean(Y*tf.log(hypothesis) + (1-Y) * tf.log(1-hypothesis))
train = tf.train.GradientDescentOptimizer(learning_rate = 0.1).minimize(cost)

predicted = tf.cast(hypothesis > 0.5 , dtype=tf.float32)
accuracy = tf.reduce_mean(tf.cast(tf.equal(predicted,Y), dtype=tf.float32))

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for step in range(10001):
        sess.run(train, feed_dict={X:x_data, Y: y_data})
        if step % 100 == 0:
            print(step, sess.run(cost, feed_dict={X: x_data, Y : y_data}), sess.run([W1,W2]))

    h , c , a = sess.run([hypothesis, predicted , accuracy], feed_dict={X : x_data , Y : y_data})
    print("\nHypothesis: " , h , "\nCorrect : ", c , "\nAccuracy: ", a)
