import pylab
import time

pylab.ion() # animation on

# Note the comma after line. This is placed here because 
# plot returns a list of lines that are drawn.
line, = pylab.plot(0,1,'ro',markersize=6) 
pylab.axis([0,1,0,1])

line.set_xdata([1,2,3])  # update the data
line.set_ydata([1,2,3])
pylab.draw() # draw the points again
time.sleep(6)

line1, = pylab.plot([4],[5],'g*',markersize=8) 
pylab.draw() 

for i in range(10):
    line.set_xdata([1,2,3])  # update the data
    line.set_ydata([1,2,3])
    pylab.draw() # draw the points again
    time.sleep(1)

print("done up there")
line2, = pylab.plot(3,2,'b^',markersize=6)     
pylab.draw() 

time.sleep(20)