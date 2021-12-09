import numpy as np

def import_time(file):
    """
    INPUT: path to TD type file (str)
    
    OUTPUT: time domain np array
    # 0: time
    # 1: x-axis [muT]
    # 2: y-axis
    # 3: z-axis
    # 4: magn
    """
    time_domain = np.genfromtxt(file, delimiter='\t', skip_header=True)
    time_domain = time_domain[:,:-4]
    
    return time_domain

def import_spec(file):
    """
    INPUT: path to SPEC type file (str)
    
    OUTPUT: spec domain np array
    # 0: frequency [Hz]
    # 1: x-axis [muT]
    # 2: y-axis
    # 3: z-axis
    # 4: magn
    """
    spec_domain = np.genfromtxt(file, delimiter='\t', skip_header=True)
    return spec_domain