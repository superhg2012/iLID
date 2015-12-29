from network import *
import tensorflow as tf

labels = 2
net = Network("TopCoder",
		      [39, 600, 1],
		      [labels],
		      [ConvolutionLayer(7, 7, 1, 1, 32),
		       PoolingLayer(3, 3, 2, 2),
		       ConvolutionLayer(5, 5, 1, 1, 64),
		       PoolingLayer(3, 3, 2, 2),
		       ConvolutionLayer(3, 3, 2, 2, 64),
		       PoolingLayer(3, 3, 2, 2),
		       ConvolutionLayer(3, 3, 1, 1, 128),
		       PoolingLayer(3, 3, 2, 2),
		       ConvolutionLayer(3, 3, 1, 1, 128),
		       PoolingLayer(3, 3, 2, 2),
		       ConvolutionLayer(3, 3, 1, 1, 256),
		       PoolingLayer(3, 3, 2, 2),
		       FullyConnectedLayer(1024),
		       DropoutLayer(0.5),
		       FullyConnectedLayer(1024),
		       DropoutLayer(0.5),
		       FullyConnectedLayer(labels, activation_function=tf.identity)])