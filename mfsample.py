#! /usr/bin/python

# This script provides an example of the use of heterodynes (or matched filter)
# to identify the frequency content in a time series.
# (Max Isi - January 2016)

import numpy as np
#import matplotlib.pyplot as plt


# -----------------------------------------------------------------------------
# REAL-VALUED DATA
# -----------------------------------------------------------------------------

# The following are the parameters needed to create fake data with or without
# a signal.

# Time vector
N = 1000 # number of samples
dt = 1  # sampling period in, say, seconds (1/sampling rate)
t0 = 0  # initial time
time = t0 + dt*np.arange(0, N)

# Signal
f = 0.5  # frequency in Hz
w = 2*np.pi*f  # angular frequency in rad/s
phi0 = 0  # initial phase
a = 1.0  # amplitude
signal = a*np.sin(w*time + phi0)

# Noise
snr = 10.0  # signal-to-noise ratio, defined naively as a_s/a_n
noise = (max(signal)/snr)*np.random.randn(N)

# Data
data = signal + noise

# Or you can use a function to create data on the fly:
def fabricate_data(time, f, snr, a=1.0, phi0=0):
  """Return series of fabricated data.
  """
  signal = a*np.sin(w*time + phi0)
  noise = (max(signal)/snr)*np.random.randn(N)
  return signal + noise

# Next we want to define functions to evaluate the overlap between two data
# sets, i.e. how much the two are alike.

def ip(vector1, vector2):
  """Return innner product (overlap) of vector1 and vector2
  """
  return sum(vector1 * vector2)

def norm(vector):
  """Norm of the vector as defined by the above inner product.
  Equivalent to np.linalg.norm
  """
  return np.sqrt(np.abs(ip(vector, vector)))

def mf(f, time, data, phi0=0):
  """Match-filter data corresponding to some time with a sinusoid of frequency
  f (Hz). One can optionally specify the initial phase phi0.
  """
  template = np.sin(2*np.pi*f*time + phi0)
  return ip(template, data)/norm(template)**2

# The mf function is close to what we want in the end: it computes how "much"
# of a certain frequency is present in the data. For example:
print "Real-valued data example 1: %.2e" %  mf(f, time, data)
print "\nReal-valued data example 2: %.2e" %  mf(0.3, time, data)

# You can play with the above to replicate what you had achieved with your own
# code already and to answer "experimentally" many of the questions that I 
# asked you to answer (for your own enlightenment) in our first meeting, like:
# what's the relation between frequency content and the properties of the time
# series? How loud can the noise be before you can't find the signal? What does
# this depend on?


# -----------------------------------------------------------------------------
# COMPLEX-VALUED DATA
# -----------------------------------------------------------------------------

# So far we have used the fact that sinusoids of different frequencies are 
# orthogonal under the inner product defined above over the domain [0,2Pi].
# However, in order to capture all possible signals we need to complete the 
# basis by including cosines as well as sines; equivalently, we could also
# use complex exponentials to span everything. (I'm assuming you're familiar
# with Fourier analysis; if you aren't, please read about it.) What follows is 
# all based on Euler's formula.

# Complex data example:
signal = a*np.exp(1j*2*np.pi*f*time + phi0)
noise = (max(abs(signal))/snr)*(np.random.randn(N)+np.random.randn(N))
data = signal + noise

# Matched filter:
def fabricate_cdata(time, f, snr, a=1.0, phi0=0):
  """Return series of fabricated data.
  """
  signal = a*np.exp(1j*2*np.pi*f*time + phi0)
  noise = (max(abs(signal))/snr)*(np.random.randn(N)+np.random.randn(N))
  return signal + noise

def cip(vector1, vector2):
  """Return innner product (overlap) of vector1 and vector2
  """
  return sum(vector1 * np.conj(vector2))

def cnorm(vector):
  """Norm of the vector as defined by the above inner product.
  Equivalent to np.linalg.norm
  """
  return np.sqrt(np.abs(cip(vector, vector)))

def cmf(f, time, data, phi0=0):
  """Match-filter data corresponding to some time with a sinusoid of frequency
  f (Hz). One can optionally specify the initial phase phi0.
  """
  template = a*np.exp(1j*2*np.pi*f*time + phi0)
  return cip(template, data)/cnorm(template)**2

# Matched filter example:
print "\nComplex-valued data example 1:"
match = cmf(f, time, data)
print "\tMatch: %.2e + i*%.2e" % (match.real, match.imag)
print "\tNorm: %.2e" % abs(match)
print "\tPhase: %.2e" % np.angle(match)

print "\nComplex-valued data example 2:"
match = cmf(0.3, time, data)
print "\tMatch: %.2e + i*%.2e" % (match.real, match.imag)
print "\tNorm: %.2e" % abs(match)
print "\tPhase: %.2e" % np.angle(match)

print "\nComplex-valued data example 3:"
match = cmf(f, time, data, phi0=0.5)
print "\tMatch: %.2e + i*%.2e" % (match.real, match.imag)
print "\tNorm: %.2e" % abs(match)
print "\tPhase: %.2e" % np.angle(match)

# Again, you can use these examples to try out several things. An important
# question is: how would you use a matched filter to determine whether a signal
# of unknown amplitude and phase is hidden in the data? This can be adapted 
# to the case when a signal is known to be located in some small window in
# frequency space (e.g. when we're tracking a known line).
