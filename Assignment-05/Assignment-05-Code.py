# -*- coding: utf-8 -*-
"""Copy of Com Eng Math 2 - 1/2022 - Assignment 5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NDb72rhwhfxBxk3ruw7P_J5tQy5nvmFe

#  **<<< Only Problem 2 and 3 will be graded >>>**
"""

# Commented out IPython magic to ensure Python compatibility.
import matplotlib.pyplot as plt
import numpy as np
import IPython.display as ipd
# %matplotlib inline
import os
from scipy import signal,fftpack
from skimage.io import imread
import cv2

"""## Problem 1
Evaluate the convolution of the following signals
1. $ \textrm{rect} \left( \frac{t-a}{a} \right) * \delta (t-b)$

2. $\textrm{rect} \left( \frac{t}{a} \right) * \textrm{rect} \left( \frac{t}{a} \right) $

3. $ t[u(t)-u(t-1)]*u(t) $

<!-- 3. $\textrm{rect} \left( \frac{t}{a} \right) * \textrm{sgn}(t) $ -->

## Problem 2
Determine the convolution $y(t) = h(t)*x(t)$ using Graphical Interpretation of the pairs of the signals shown

1. <a href="https://imgbb.com/"><img src="https://i.ibb.co/YDVdjT1/ii-1.jpg" alt="ii-1" border="0"></a>

2. <a href="https://imgbb.com/"><img src="https://i.ibb.co/102mFqd/ii-2.jpg" alt="ii-2" border="0"></a>


---

## [optional]

3. <a href="https://imgbb.com/"><img src="https://i.ibb.co/vDsDW2z/ii-3.jpg" alt="ii-3" border="0"></a>

4. <a href="https://imgbb.com/"><img src="https://i.ibb.co/fdND0Dv/ii-4.jpg" alt="ii-4" border="0"></a>
"""

delta = 0.0001

plt.title('Problem 2.1')
plt.xlabel('Time')
plt.ylabel('x(t)')

def rect(x):
  if -1 <= x <= 1:
    return 1
  else:
    return 0

t = np.arange(-2,2,delta)
np_rect = np.vectorize(rect, otypes=[float])
x_t = np_rect(t)

plt.grid(True, which='both')
plt.axhline(y=0, color='k')
plt.plot(t,x_t)
plt.show()

#------------------------------------------

plt.title('Problem 2.1')
plt.xlabel('Time')
plt.ylabel('h(t)')

def biphasic(x):
  if 0 <= x <= 1:
    return 1
  elif -1 <= x < 0:
    return -1
  else:
    return 0

t = np.arange(-2,2,delta)
np_biphasic = np.vectorize(biphasic, otypes=[float])
h_t = np_biphasic(t)

plt.grid(True, which='both')
plt.axhline(y=0, color='k')
plt.plot(t,h_t)
plt.show()

#------------------------------------------

plt.title('Problem 2.1')
plt.xlabel('Time')
plt.ylabel('y(t)')

t = np.arange(-3.9999,4,delta)
y_t = np.convolve(x_t, h_t)*delta

plt.grid(True, which='both')
plt.axhline(y=0, color='k')
plt.plot(t,y_t)
plt.show()

delta = 0.0001

plt.title('Problem 2.2')
plt.xlabel('Time')
plt.ylabel('x(t)')

def rect(x):
  if -0.5 <= x <= 0.5:
    return 1
  else:
    return 0

t = np.arange(-1,3,delta)
np_rect = np.vectorize(rect, otypes=[float])
x_t = np_rect((t-1)/2)

plt.grid(True, which='both')
plt.axhline(y=0, color='k')
plt.plot(t,x_t)
plt.show()

delta = 0.0001

plt.title('Problem 2.2')
plt.xlabel('Time')
plt.ylabel('x(t)')

def rmp(x):
  if 0 <= x <= 1:
    return x
  else:
    return 0

t = np.arange(-2,2,delta)
np_ramp = np.vectorize(rmp, otypes=[float])
x_t = np_ramp(t)

plt.grid(True, which='both')
plt.axhline(y=0, color='k')
plt.plot(t,x_t)
plt.show()

#------------------------------------------

plt.title('Problem 2.2')
plt.xlabel('Time')
plt.ylabel('h(t)')

def rect(x):
  if -1 <= x <= 1:
    return 1
  else:
    return 0

t = np.arange(-2,2,delta)
np_rect = np.vectorize(rect, otypes=[float])
h_t = np_rect(t)

plt.grid(True, which='both')
plt.axhline(y=0, color='k')
plt.plot(t,h_t)
plt.show()

#------------------------------------------

plt.title('Problem 2.2')
plt.xlabel('Time')
plt.ylabel('y(t)')

t = np.arange(-3.9999,4,delta)
y_t = np.convolve(x_t, h_t)*delta

plt.grid(True, which='both')
plt.axhline(y=0, color='k')
plt.plot(t,y_t)
plt.show()

"""## Problem 3
Find the convolution $y[n] = h[n]*x[n]$ of the following signals
1.
$x[n] = \begin{cases} -1 , -5 \leq n \leq -1 \\ 1 , 0 \leq n \leq 4 \end{cases} h[n]=2u[n]$

2.
$x[n] = \left( \frac{1}{2} \right)^n u[n],\, h[n] = \delta[n] +\delta[n-1] +  \left( \frac{1}{3} \right)^n u[n]$
---
## [optional]
3.
$x[n] = u[n],\, h[n] = 1 \; ; 0 \leq n \leq 9 $

4.
$x[n] = \left( \frac{1}{3} \right)^n u[n],\, h[n] = \delta[n] + \left( \frac{1}{2} \right)^n u[n]$


"""

plt.title('Problem 3.1')
plt.xlabel('Time')
plt.ylabel('x(t)')

t = np.arange(-8,8)
x_t = np.array([0, 0, 0, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 0, 0, 0])

plt.grid(True, which='both')
plt.axhline(y=0, color='k')
plt.stem(t,x_t)
plt.show()

#------------------------------------------

plt.title('Problem 3.1')
plt.xlabel('Time')
plt.ylabel('h(t)')

t = np.arange(-1,20)
h_t = 2*np.heaviside(t,1)

plt.grid(True, which='both')
plt.axhline(y=0, color='k')
plt.stem(t,h_t, linefmt='b-', markerfmt='bo', basefmt='r-')
plt.show()

#------------------------------------------

plt.title('Problem 3.1')
plt.xlabel('Time')
plt.ylabel('y(t)')

t = np.arange(-9,9)
y_t = np.convolve(h_t, x_t)[:18]

plt.grid(True, which='both')
plt.axhline(y=0, color='k')
plt.stem(t,y_t)
plt.show()

plt.title('Problem 3.2')
plt.xlabel('Time')
plt.ylabel('x(t)')

t = np.arange(-1,7)
x_t = (0.5**t)*np.heaviside(t,1)

plt.grid(True, which='both')
plt.axhline(y=0, color='k')
plt.stem(t,x_t, linefmt='b-', markerfmt='bo', basefmt='r-')
plt.show()

#------------------------------------------

plt.title('Problem 3.2')
plt.xlabel('Time')
plt.ylabel('h(t)')

def pulse(x):
  if 0 == x:
    return 1
  else:
    return 0

t = np.arange(-1,7)
np_pulse = np.vectorize(pulse, otypes=[float])
h_t = np_pulse(t) + np_pulse(t-1) + ((1/3)**t)*np.heaviside(t,1)

plt.grid(True, which='both')
plt.axhline(y=0, color='k')
plt.stem(t,h_t, linefmt='b-', markerfmt='bo', basefmt='r-')
plt.show()

#------------------------------------------

plt.title('Problem 3.2')
plt.xlabel('Time')
plt.ylabel('y(t)')

t = np.arange(-2,13)
y_t = np.convolve(x_t, h_t)

plt.grid(True, which='both')
plt.axhline(y=0, color='k')
plt.stem(t,y_t, linefmt='b-', markerfmt='bo', basefmt='r-')
plt.show()

"""## Problem 4
Find the convolution $y[n] = h[n]*x[n]$ of the following signals
1.
$x[n] = \left\{ 1,-\frac{1}{2},\frac{1}{4},-\frac{1}{8} ,\frac{1}{16} \right \},\, h[n]=\left\{ 1,-1,1,-1 \right\}$

1.
$x[n] = \left\{ 1,2,3,0,-1, \right \},\, h[n]=\left\{ 2,-1,3,1,-2 \right\}$

1.
$x[n] = \left\{ 3,\frac{1}{2},-\frac{1}{4},1,4 \right \},\, h[n]=\left\{ 2,-1,\frac{1}{2}, -\frac{1}{2} \right\}$

1.
$x[n] = \left\{ -1,\frac{1}{2},\frac{3}{4},-\frac{1}{5},1 \right \},\, h[n]=\left\{ 1,1,1,1,1 \right\}$

## Problem 6

### Problem 6.1 : Convolution - 1D
The following code creates a gaussian pulse and its self convolutions. Study and apply the convolution between signal e and another signal e with noise (e_noise) and write the report to analyze the results.
"""

t = np.linspace(-1, 1, 2 * 100, endpoint=False)
i, q, e = signal.gausspulse(t, fc=5, retquad=True, retenv=True)
plt.plot(t, e, '--',label = 'orignal signal')
plt.legend(loc='upper right')
plt.show()


conv_e = np.convolve(e,e,'same')
plt.plot(t, e, '--',label = 'orignal signal')
plt.plot(t, conv_e, '--',label = 'self conv signal')
plt.legend(loc='upper right')
plt.show()

e_noise = e + np.random.randn(len(e))*2.5
conv_e_noise = np.convolve(e,e_noise,'same')

# TODO : Apply the convolution between signal e and another signal e with noise (e_noise) and check the results

"""### Problem 6.2

From the self convolution below, when increasing the number of self convolution (now is 8), what is noticeable from the final shape resulted from the convolution?

(HINT 01: Central limit theorem)

(HINT 02: What is Probability Density Function (PDF) of $z$ if $z=x+y$ $?$ )
"""

from scipy.stats import uniform

x = np.linspace(-5,5, 1000)
plt.plot(x, uniform.pdf(x),
       'r-', lw=5, alpha=0.6, label='uniform pdf')

plt.show()


x = np.linspace(-15,15, 10000)
pdf_1 = uniform.pdf(x)
pdf_2 = uniform.pdf(x)

for i in range(8):
    pdf_2 = np.convolve(pdf_2,pdf_1, 'same')

pdf_2 = pdf_2/np.max(pdf_2)
plt.plot(x, pdf_2,'r-', lw=5, alpha=0.6, label='conv uniform')

"""## Problem 7
### 2D (image) signal convolution:
The following code show the 2D signal (image f(x,y)) and a kernel (diag_line). Study the convolution of the kernel and the image. Apply with "circuits.png" image and analyze the results.


[link data](https://drive.google.com/file/d/1geQ4L6aUOQUSOCwl2UvDl5dgn_ocLFg1/view?usp=sharing)

## TODO : Apply diag_line to the "circuits.png image" and analyse the results
"""

from google.colab import drive
drive.mount('/content/gdrive/')
!unzip '/content/gdrive/My Drive/data2.zip'

image_path = os.path.join('ComEngMath2_data','hamtaro0.jpg')

diag_line = np.array([[ 2, -1, -1],
                    [-1, 2, -1],
                    [-1, -1, 2]])

ham = cv2.imread(image_path,0)
plt.figure(figsize=(10,10))
plt.imshow(ham, cmap='gray')
plt.show()
grad = signal.convolve2d(ham,diag_line,boundary='symm',mode='same')
plt.figure(figsize=(10,10))
plt.imshow(grad, cmap='gray')
plt.show()

# TODO : Apply diag_line to the "circuits.png image" and analyse the results