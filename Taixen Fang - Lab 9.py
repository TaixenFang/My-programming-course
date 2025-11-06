import numpy as np
# Function 1: Read values from a file into an array
# This function reads numerical values from a text file and stores them in a NumPy array.
def read_values_from_file(filename):
    with open(filename, 'r') as file:
        values = [float(line.strip()) for line in file]
    return np.array(values)
print(read_values_from_file("values.txt"))

# Function 2: Read Oscillatory Wave Data and Compute Statistics
# This function reads a file containing wave data with length and amplitude values into a NumPy array.
# It also computes the mean and maximum amplitude.
def read_oscillatory_wave_data(filename):
    data = np.loadtxt(filename,delimiter = ',')
    lengths = data[:,0]
    amplitudes = data[:,1]
    mean_amplitude = np.mean(amplitudes)
    max_amplitude = np.max(amplitudes)
    return lengths, data, mean_amplitude, max_amplitude
print(read_oscillatory_wave_data("wave_data.csv"))



# Function 3: Read Standing Wave Data and Compute Wave Speed
# This function reads a file containing standing wave data with length and tension values into a NumPy array.
# It also computes the wave speed using v = sqrt(T/μ), where μ = mass per unit length (assumed to be 1 for simplicity).
def read_standing_wave_data(filename):
    data = np.loadtxt(filename, delimiter = ',')
    lengths = data[:,0]
    tensions = data[:,1]
    wave_speeds = np.sqrt(tensions/lengths)
    return np.array(wave_speeds)
print(read_standing_wave_data("standing_wave.csv"))
