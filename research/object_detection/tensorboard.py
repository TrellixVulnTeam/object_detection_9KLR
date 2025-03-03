import tensorflow as tf
from tensorflow.python.platform import gfile

with tf.Session() as sess:
    model_filename =r'./LOGDIR/frozen_inference_graph.pb'
    with gfile.FastGFile(model_filename, 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        g_in = tf.import_graph_def(graph_def)

    LOGDIR='LOGDIR'
    train_writer = tf.summary.FileWriter(LOGDIR)
    train_writer.add_graph(sess.graph)