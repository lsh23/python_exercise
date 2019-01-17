import tensorflow as tf
import numpy as np
tf.set_random_seed(777)
csv_data = np.loadtxt('data-01-test-score.csv', delimiter = ',')
#파일 읽기

x_data = csv_data[:, 0:-1]
y_data = csv_data[:, [-1]]
#읽은 파일로 부터 슬라이싱 해서 x,y값 넣기
print(x_data.shape, x_data, len(x_data))
print(y_data.shape, y_data)


X = tf.placeholder(tf.float32, shape=[None, 3])
Y = tf.placeholder(tf.float32, shape=[None, 1])

W = tf.Variable(tf.random_normal([3, 1]), name = 'weight')
b = tf.Variable(tf.random_normal([1]), name = 'bias')

hypothesis = tf.matmul(X, W) + b
# Y = Wx +b

cost = tf.reduce_mean(tf.square(hypothesis - Y))
# 선형 회귀식

optimizer = tf.train.GradientDescentOptimizer(learning_rate=1e-5)
train = optimizer.minimize(cost)
# GradientDescent 방법으로 최소값을 찾는다.

sess = tf.Session()
sess.run(tf.global_variables_initializer())

for step in range(2001):
    cost_val, hy_val, _ = sess.run(
        [cost, hypothesis, train], feed_dict={X: x_data, Y: y_data})
    if step % 10 == 0:
        print(step, "Cost: ", cost_val, "\nPrediction:\n", hy_val)
print("Your score will be ", sess.run(
    hypothesis, feed_dict={X: [[100, 70, 101]]}))

print("Other scores will be ", sess.run(hypothesis,
                                        feed_dict={X: [[60, 70, 110], [90, 100, 80]]}))
