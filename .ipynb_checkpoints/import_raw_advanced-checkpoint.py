import numpy as np

def data_import(measurement):
    """
    INPUT: path to file without TD SPEC ending
    
    OUTPUT: time domain np array
    # 0: time
    # 1: x-axis [muT]
    # 2: y-axis
    # 3: z-axis
    # 4: magn
    """
    time_domain = np.genfromtxt(measurement + "_TD.csv", delimiter='\t', skip_header=True)
    time_domain = time_domain[:,:-4]
    
    spec_domain = np.genfromtxt(measurement + "_SPEC.csv", delimiter='\t', skip_header=True)
    
    return time_domain, spec_domain