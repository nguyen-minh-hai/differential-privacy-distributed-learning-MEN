''' Hardware and enviroment parameters of Mobile Egde Network System

This file declares the mobile edge network parameters and the 
functions to generate the simulate parameters of the system.

This file can also be imported as a module and contains the
following functions:

    * generateDistances - returns a list of distances between
    server and the mobile edge devices.
    * generateChannelGain - returns a list of channel gains.
    * computeMaxTransmitTime - returns the maximal transmit time
    between base station and each device following the
    bandwidth, transmit power, and dimension number,constraints.

Author: Nguyen Minh Hai
Date: 15:30 GMT+10, June 05, 2022.
'''

import random
import math

nb_of_devices = 1000 # Denoted as K in paper.

PkMin = [0.0001] * nb_of_devices # The minimal transmit power in W, denoted as P^min_k in paper.
PkMaxdBm = 20 # The maximal transmit power in dBm, denoted as P^max_k in paper.
PkMax = [10 ** (PkMaxdBm / 10) / 1000] * nb_of_devices # The maximal transmit power in W, denoted as P^max_k in paper.
bandwidth = 9e8 # In Hz, denoted as W in paper.
noisePower = 1e-4 # Noise power, used to be 10^-10 W/Hz, denoted as N_0 in paper.
distMin = 2 # The minimum distance between mobile edge devices and the base station, in m, denoted as d_min in paper.
distMax = 200 # The maximal distance between mobile edge devices and the base station, in m, denoted as d_max in paper.
distStd = 1 # the standard distance, in m, denoted as d_0 in paper.
g0 = -40 # In dB, this pararameter appears in the channel gain h's computing formula.
channelGains = [0.0] * nb_of_devices # The channel gain, denoted as h in paper.
maxTransmitTime = 10 ** (-4.3) # Maximal allowed transmit time, denoted as T in paper.

smallValueInComputing = 1e-4 # The minimal positive value in computing.
maxValueComputing = 2**64 - 1 # The maximal integer value in computing.

def generate_distances(nb_of_devices = nb_of_devices):
    """ Generates the distances between base station 
    and mobilde edge devices.

    Parameters
    ----------
    nb_of_devicesParam : int, optional
        Number of mobile edge devices (K) (default is nb_of_devices).
    
    Returns
    -------
    list
        A list of K distances.

    Algorithms
    -----
        Distance generated follows the uniform distribution U(d_min, d_max).
    """

    dist = [0] * nb_of_devices
    for i in range(nb_of_devices):
        dist[i] = random.randint(distMin, distMax)
    return dist


def generate_channel_gain(nb_of_devices = nb_of_devices, distanceDevicesToBS = [0] * nb_of_devices):
    """ Generates the channel gain list 
        of transmit enviroment.

    Parameters
    ---------- 
    nb_of_devicesParam : int, optional
        Number of mobile edge devices (K) (default is nb_of_devices).
    distanceDevicesToBS : list, optional
        List of the distances between the base station (BS) and nb_of_devicesParam
         devices (default is [0, .., 0]).
    
    Returns
    -------
        List of nb_of_devicesParam channel gain coefficients, denoted as h in paper.
    
    Algorithms
    -----
        Channel gain coefficient i-th is generated following the
        exponential distribution with mean miu = 10^(g0/10) *
        (d0 / d_k)^4, where g0 (dB), d0 and d_k are the standard
        distance and distance between BS and device k-th.
    """

    h  = [0.0] * nb_of_devices
    for i in range(nb_of_devices):
        miu_mean = (10 ** (g0/10)) * ((distStd / distanceDevicesToBS[i]) ** 4)
        h[i] = random.expovariate(miu_mean)
    
    return h

def compute_max_transmit_time(dimensionNb, channelGains = channelGains):
    """ Computes the maximal allowed transmit
    time between base station and each device following the
    bandwidth, transmit power, and dimension number,constraints.

    Parameters
    ----------
    channelGains : List 
        A list of channel gain coefficients.
    dimensionNb : Int 
        An integer as the number of dimension of learning parameters
        of the federated learning system.

    Returns
    -------
        Real as the maximal allowed transmit time.
    
    Algorithms
    -----
        This function assumes that the maximal bits per learning parameter 
        is 32 bits. It then computes param weight by: S_n = 32 * d, where d 
        is the number of parameters. The required time of device i-th is
        computed by: TDev_i = S_n / [W * log_2 (1 + PkMax_i * h_i / N0)].
        The final maximal transmit time is: max_i TDev_i.
    """

    Sn = dimensionNb * 32 * math.log(2) # The param weights in natss
    maxTransTime = 0.0
    for i in range(len(channelGains)):
        TDev = Sn / bandwidth / math.log(1 + PkMax[i] * channelGains[i] / noisePower)
        if TDev > maxTransTime:
            maxTransTime = TDev
    return maxTransTime