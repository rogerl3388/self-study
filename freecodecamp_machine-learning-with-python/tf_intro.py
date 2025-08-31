import tensorflow as tf
# print(tf.__version__)

# scalar tensor creation (rank 0)
string = tf.Variable("string", tf.string)
number = tf.Variable(235, tf.int16)

# ranked tensors
rank1_t = tf.Variable(["cool"], tf.string)
rank2_t = tf.Variable([['test1','test2'],['swag','bank']], tf.string)

# testing some stuff out
print(tf.rank(rank1_t))
print(tf.rank(number))
print(rank2_t.shape)

# trying shape changes
one_t = tf.ones([3,2,4])
one_t2 = tf.reshape(one_t,[-1,2,12])
print(one_t2)

