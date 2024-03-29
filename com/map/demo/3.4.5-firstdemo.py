# -*- coding: utf-8 -*-
"""
Created on Tue May  7 14:25:09 2019

@author: NJD
"""

import tensorflow as tf

from numpy.random import RandomState

batch_size=8

w1=tf.Variable(tf.random_normal([2,3],stddev=1,seed=1))
w2=tf.Variable(tf.random_normal([3,1],stddev=1,seed=1))

x=tf.placeholder(tf.float32,shape=(None,2),name='x-input')
y_=tf.placeholder(tf.float32,shape=(None,1),name='y-input')

#定义神经网络前向传播过程
a=tf.matmul(x,w1)
y=tf.matmul(a,w2)

#定义损失函数和反向传播的算法
cross_entropy =-tf.reduce_mean(y_ * tf.log(tf.clip_by_value(y,1e-10,1.0)))
train_step=tf.train.AdamOptimizer(0.001).minimize(cross_entropy)

#通过随机数生成一个模拟数据集
rdm=RandomState(1)
data_size=128
X=rdm.rand(data_size,2)
Y=[[int(x1+x2<1)] for (x1,x2) in X]

#创建一个会话来运行TensorFlow程序
with tf.Session() as sess:
    init_op=tf.initialize_all_variables()
    sess.run(init_op)
    print (w2)
    print (w1)

#设定训练的轮数
    STEPS=5000
    for i in range(STEPS):
    #每次选取Batch_size个样本进行训练
        start = (i*batch_size) % data_size
        end = min(start+batch_size,data_size)
    
    #通过选取的样本训练神经网络并更新参数
        sess.run(train_step,feed_dict={x:X[start:end],y_:Y[start:end]})
        if i %1000==0:
        #每隔一段时间计算在所有数据上的交叉熵并输出
            total_cross_entropy=sess.run(cross_entropy,feed_dict={x:X,y_:Y})
            print ("After %d training steps,cross entropy on all data is %g" % (i,total_cross_entropy))

print (w1)
print (w2)
print (rdm)

