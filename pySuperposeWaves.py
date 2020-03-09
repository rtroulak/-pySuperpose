
import matplotlib.pyplot as plt

from numpy      import sin, linspace, zeros, pi
from docopt     import docopt

def superpose(freq,freq2,width,width2,phase,phase2):
  nwaves  = 2
  npt     = 120
  #add 2*pi to phases
  phase     *= 2*pi
  phase2     *= 2*pi


  freqMin = freq - width/2      # Define min and max frequencies of the first wave
  freqMax = freq + width/2      

  freqMin2 = freq2 - bwidth2/2      # Define min and max frequencies of the second wave
  freqMax2 = freq2 + bwidth2/2

  freqSp  = linspace(freqMin, freqMax, 2)  # Equally spaced frequencies of the first wave
  tmax    = float(npt)/(2.0*freqMax)           # Sample at twice highest freq; Nyquist condition
  t       = linspace(0, tmax, num=npt)

  freqSp2  = linspace(freqMin2, freqMax2, 2) # Equally spaced frequencies  of the second wave
  tmax2    = float(npt)/(2.0*freqMax2)           # Sample at twice highest freq; Nyquist condition
  t2       = linspace(0, tmax2, num=npt)


  sumSine = zeros(npt, dtype=float)   
  #Wave Creation for superpose of two waves
  for freq in freqSp2:
      sumSine += sin(2*pi*freq*t2 + phase)
  for freq in freqSp:
      sumSine += sin(2*pi*freq*t + phase2)

  fig = plt.figure()
  fig.suptitle("Superposed Wave")
  plt.plot(sumSine)
  #plot of superposed wave
  plt.show()


freq, width, phase = input("Enter frequency, width and phase of the 1st wave: ").split() 
freq2, width2, phase2 = input("Enter frequency, width and phase of the 2nd wave: ").split() 
freq = float(freq)
freq2 = float(freq2)
phase = float(phase)
phase2 = float(phase)
width = float(width)
width2 = float(width2)

print("Waves Overview \n First Wave:  \n  frequency = ",freq,"\n  width = ",width,"\n  phase = ",phase)
print(" Second Wave:  \n  frequency = ",freq2,"\n  width = ",width2,"\n  phase = ",phase2)

# Call of funtion for superpose
# superpose(140,120,240,220,2.8286,3.682403)
superpose(freq,freq2,width,width2,phase,phase2)
