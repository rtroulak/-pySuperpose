#rtroulak 09/03 21:43
import math
import numpy as np
import matplotlib.pyplot as plot

#The main oscillator function which gets parameters(frequencies, widths,phases and duration) to sum 2 oscillators, sum these and plot the results
def oscillator_plot(freq_first,freq_second,width_first,width_second,phase_first,phase_second,seconds):
    
    #setting default fs
    fs = 44100
    #convert duration of plot on second depends of fs
    duration = 44100 * seconds
    #initialize array 
    n = np.linspace(0,duration, duration)
  
    #set the gives parameters of the function
    #frequencies
    freq = freq_first
    freq2 = freq_second
    #widths
    A=width_first
    B=width_second
    #phase multiply with pi to get the correct type
    phase = phase_first * math.pi
    phase2 = phase_second * math.pi

    # the sum of 2 oscillators with their values
    oscillators =  A*np.sin(2*math.pi*freq*n/fs + phase) + B*np.sin(2*math.pi*freq2*n/fs + phase2)

    #create the plot of oscillators
    main_plot = plot.subplot()
    main_plot.plot(n/fs, oscillators, label="Sum of Oscillators")
    main_plot.legend(loc='upper right')
    #set the plot labels
    plot.title('Oscillators Plot')
    plot.ylabel('Width')
    plot.xlabel('Time')
    plot.show()


#main inputs for our program, frequencies, widths,phases and duration
freq, width, phase = input("Enter frequency, width and phase of the 1st Oscillator: ").split() 
freq2, width2, phase2 = input("Enter frequency, width and phase of the 2nd Oscillator: ").split() 
duration = input("Enter the duration in seconds: ") 

#Here the typecast to convert input values from string to float or integer
freq = float(freq)
freq2 = float(freq2)
phase = float(phase)
phase2 = float(phase2)
width = float(width)
width2 = float(width2)
duration = int(duration)

#print parameters for debug
print("Oscillators Overview (for ",duration," sec) \n First Oscillator:  \n  frequency = ",freq,"\n  width = ",width,"\n  phase = ",phase)
print(" Second Oscillator:  \n  frequency = ",freq2,"\n  width = ",width2,"\n  phase = ",phase2)

#Call oscillator_plot funtion
oscillator_plot(freq,freq2,width,width2,phase,phase2,duration)
# oscillator_plot(25,27,2,4,15,0,2)
