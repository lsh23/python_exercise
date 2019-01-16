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

with tf.name_scope("layer1") as scope:
    L1 = tf.nn.relu(tf.matmul(X,W1)+ b1)
with tf.name_scope("layer2") as scope:
    L2 = tf.nn.relu(tf.matmul(L1,W2)+ b2)
with tf.name_scope("layer3") as scope:
    L3 = tf.nn.relu(tf.matmul(L2,W3)+ b3)
with tf.name_scope("layer4") as scope:
    L4 = tf.nn.relu(tf.matmul(L3,W4)+ b4)
with tf.name_scope("layer5") as scope:
    L5 = tf.nn.relu(tf.matmul(L4,W5)+ b5)
with tf.name_scope("layer6") as scope:
    L6 = tf.nn.relu(tf.matmul(L5,W6)+ b6)
with tf.name_scope("layer7") as scope:
    L7 = tf.nn.relu(tf.matmul(L6,W7)+ b7)
with tf.name_scope("layer8") as scope:
    L8 = tf.nn.relu(tf.matmul(L7,W8)+ b8)
with tf.name_scope("layer9") as scope:
    L9 = tf.nn.relu(tf.matmul(L8,W9)+ b9)
with tf.name_scope("layer10") as scope:
    L10 = tf.nn.relu(tf.matmul(L9,W10)+ b10)


with tf.name_scope("last") as scope:
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
            print(step, sess.run(cost, feed_dict={X: x_data, Y : y_data}), sess.run([W1,W2,W3,W4,W5,W6,W7,W8,W9,W10,W11]))

    h , c , a = sess.run([hypothesis, predicted , accuracy], feed_dict={X : x_data , Y : y_data})
    print("\nHypothesis: " , h , "\nCorrect : ", c , "\nAccuracy: ", a)
