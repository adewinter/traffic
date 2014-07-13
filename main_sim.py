"""
Do a simple run
"""

from traffic.car import Car
import numpy as np
from numpy.linalg import norm
from pylab import figure, plot, show, xlabel, ylabel, title, legend, zeros, subplot, get_current_fig_manager

ticks = 300

def do_command_line_run():
    """
    Just a test run
    """
    first_car = Car(velocity=np.array([0, 0.1]), acceleration=np.array([0, 5]))
    print 'Mycar %s' % first_car
    data = np.zeros((ticks, 6))
    for i in range(ticks/2):
        data[i] = first_car.update()

    print 'Interim val:\t%s' % first_car
    print 'Car state: %s' % first_car.state
    print '\n\n'


    first_car.acceleration = np.array([0, -5])
    first_car.turn('EAST')
    print 'Car accel = %s now' % first_car.acceleration
    for i in range(ticks/2, (ticks/2)+100):
        data[i] = first_car.update()

    print 'Interim val:\t%s' % first_car

    first_car.turn('SOUTH')

    print 'Car accel = %s now' % first_car.acceleration
    for i in range((ticks/2)+100, ticks):
        data[i] = first_car.update()

    print 'Final val:\t%s' % first_car




    time = np.linspace(0, (0.01*(ticks-1)), num=ticks)


    norm_vel = zeros(ticks)
    for k, i in enumerate(data[:, [2, 3]]):
        norm_vel[k] = norm(i)

    print data[0]
    figure(0)
    # plot(data[:, 0], data[:, 1], '.', label='Position')
    # plot(time, norm_vel, '.r', label="Normalized vel")
    subplot(211)
    plot(time, data[:, 2], label='V_x')
    plot(time, data[:, 3], label='V_y')
    plot(time, data[:, 4], label='a_x')
    plot(time, data[:, 5], label='a_y')
    xlabel('time(s)')
    ylabel('stuff')
    title('Car test velocity and acceleration')
    
    legend()

    subplot(212)
    plot(data[:, 0], data[:, 1], '.', label='Position')
    title("Position")

    fm = get_current_fig_manager()
    fm.full_screen_toggle()
    show()

    
if __name__ == '__main__':
    do_command_line_run()
