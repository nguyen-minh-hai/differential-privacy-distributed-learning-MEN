""" Parameters of deep learning network

Describe the parameters relating the deep learning process.

Author: Nguyen Minh Hai
Date: 14:56 GMT+10, June 06, 2022.
"""

max_epochs_nb = 2500 # The maximal running epochs.
batch_size = 16 # Batch size of data per each epoch.
inversed_current_batch_size = 1. / batch_size
max_unimproved_consecutive_epochs_nb = 2500 # If after this unimproved test accuracy consecutive
                                        # epochs, the leaning process will cease. If maxEpochsNb
                                        # = maxUnimprovedConsecutiveEpochsNb, the learning will
                                        # run for maxEpochsNb epochs.

optimizer_function_name = 'momentum' # The learn function name.

convergence_error_accuracy = 0.0001 # The learning will stop if the gradients are below this value.
l_rate = 0.001 # Learning rate.
beta = .9 # This parameter serves the Adam learning rate adjusting.
decrease_l_rate = 1.005 # This parameter is the decreasing ratio of learning rate
                      # each time the learning process gets improved.
acc_window = 10 # This parameter describes the number of epochs between two consecutive
               # times of adjusting the learning rate.
ratio_variance_of_acc_2_series_decreasing_l_rate = 0.86 #

federated_learning = True # True if the federated is applying, i.e., more than 1 mobile device,
                         # False if the learning is performed in the base station.

nb_of_1st_layer_nodes = 784 # The number of first learning layer nodes.
nb_of_2nd_layer_nodes = 60 # The number of second learning layer nodes.
nb_of_3rd_layer_nodes = 10 # The number of third learning layer nodes.
dimension_nb = 785 * 60 + 61 * 10 # The number of learning parameters.
                                 # Default is the number of network with 3 layers,
                                 # where the hidden consisting of 60 nodes,
                                 # of Digitial recognization MNIST task.