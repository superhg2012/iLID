from network import *
import tensorflow as tf

labels = 2
net = Network("Berlin2",
                      [39, 600, 1],
                      [labels],
                      [ConvolutionLayer(6, 6, 1, 1, 12),
                       LocalResponseNormalizationLayer(),
                       PoolingLayer(2, 2, 2, 2),
                       ConvolutionLayer(6, 6, 1, 1, 12),
                       LocalResponseNormalizationLayer(),
                       PoolingLayer(2, 2, 2, 2),
                       ConvolutionLayer(6, 6, 1, 1, 12),
                       LocalResponseNormalizationLayer(),
                       PoolingLayer(2, 2, 2, 2),
                       FullyConnectedLayer(2048),
                       FullyConnectedLayer(1024),
                       FullyConnectedLayer(labels, activation_function=tf.identity)])