""" Parameters of the machine performs the numerical and simulation eperiments

Author: Nguyen Minh Hai
Date: 16:56 GMT+10, June 06, 2022.
"""

import platform

# The following script descript the folder/file paths for reading/recording/updating
# intances and numerical/simulation results.
# These paths are depent on particular machine and operation.
renting_ubuntu_server_use = False # This parameter is set True if the numerical/simulation
                               # experiments are tackled on the Ubuntu server that I
                               # I rent in April 2022, otherwises it is set to False.
UET_714_desktop_use = False # This parameter is set True if the numerical/simulation
                         # experiments are tackled on the Windows desktop in 714 room,
                         # E3 building of University of Engineering and Technology
                         # in 144 Xuan Thuy, Hanoi, Vietnam.

machine_code = "MYASUS01" # Code of machine that tackles the numerical/simulation experiments,
                         # default is ASUS TUF Gaming with Windows 10 OS.
dataSet_code = "MNISTt10k" # Data set code, default is the MNISTt10k
deep_learning_architechture_code = "FedLearn3LayersSGD" # Architechture of deep learning network,
                                                     # default is the 3 layers SGD.

if renting_ubuntu_server_use == True:
    train_data_path = '/Projects/Data/DifferentialPrivacy-DistributedLearning-MEC-Energy/infimnist/'
    test_data_path = '/Projects/Data/DifferentialPrivacy-DistributedLearning-MEC-Energy/handwritting/'
    result_folder_path = "/Projects/DifferentialPrivacy-DistributedLearning-MEC-Energy/python-source/results/detail-result/"
elif UET_714_desktop_use == True:
    train_data_path = 'C:\hainm\Data-for-Data-Science\data\infimnist\\'
    test_data_path = 'C:\hainm\Data-for-Data-Science\handwritting\\'
    result_folder_path = "C:\hainm\Projects\DifferentialPrivacy-DistributedLearning-MEC-Energy\python-source\\results\detail-result\\"
elif platform.system() == "Linux":
    # For my Ubuntu 20 operation system (dated on June 06, 2022).
    machine_code = "MYASUS02"
    train_data_path = "/media/nmhai/DATA/Data-for-Data-Science/data/infimnist/"
    test_data_path = "/media/nmhai/DATA/Data-for-Data-Science/handwritting/"
    result_folder_path = "/media/nmhai/DATA/Projects/DifferentialPrivacy-DistributedLearning-MEC-Energy/python-source/results/detail-result/"
    feasible_solutions_record_folder_path = "D:\Projects\DifferentialPrivacy-DistributedLearning-MEC-Energy\python-source\\results\\"
elif platform.system() == "Windows":
    # For my Windows operation system (dated on June 06, 2022).
    train_data_path = 'D:\Data-for-Data-Science\data\infimnist\\'
    test_data_path = 'D:\Data-for-Data-Science\handwritting\\'
    result_folder_path = "D:\Projects\DifferentialPrivacy-DistributedLearning-MEC-Energy\python-source\\results\detail-result\\"