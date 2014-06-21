"""
Core module for class Car and Car Controller
"""
import numpy as np
from numpy.linalg import norm
from pylab import figure, plot, show, xlabel, ylabel, title, legend, zeros
class Car(object):
    """
    Car object. Does self updating of state, position, velocity.
    """
    def __init__(self, position=None, velocity=None, acceleration=None):
        if not position:
            position = np.array([0, 0], 'float')
        self.position = position
        if velocity == None:
            velocity = np.array([0, 0], 'float')
        self.velocity = velocity
        if acceleration == None:
            acceleration = 0 #make acceleration a constant
        self.acceleration = acceleration

    def update(self, delta_t=10):
        """
        Updates state and pos, vel vectors
        """
        state = self.state
        if state == 'STOP':
            self.acceleration = 0
            self.velocity = np.array([0, 0], 'float')
            return #no point in running more calculations for this cycle.
        
        delta_t = delta_t/1000.0 #from Milliseconds to Seconds
        delta_v = self.acceleration * delta_t
        self.velocity += delta_v
        delta_p = self.velocity * delta_t
        self.position += delta_p
        ret = np.append(self.position, self.velocity)
        ret = np.append(ret, self.acceleration)
        return ret


    def __unicode__(self):
        return "Car: %s, %s, %s" % (self.position, \
                                     self.velocity, \
                                     self.acceleration)
    
    def __str__(self):
        return self.__unicode__()
    
    @property
    def state(self):
        """
        Gets the state of the Car object. 
        Possible values are: 
            'STOP' (car stopped), 
            'SLOWDOW' (car is velocity decreasing),
            'CRUISE' (car at constant velocity) and 
            'SPEEDUP' (car velocity increasing)
        """
        m_vel = norm(self.velocity)
        if m_vel <= 0 and self.acceleration <= 0: #we never 
                                                  #want a car to go backwards
            return 'STOP'        
        
        if self.acceleration < 0:
            return 'SLOWDOWN'
        
        if self.acceleration == 0:
            return 'CRUISE'  
        
        if self.acceleration > 0:
            return 'SPEEDUP'

    def turn(self, direction):
        """
        Turn the car in one of the cardinal directions.
        `direction` values can be one of:
        'NORTH',
        'SOUTH',
        'EAST' or
        'WEST'
        """
        vel_mag = norm(self.velocity)
        direction_map = {
            'NORTH': np.array([0, 1], 'float'),
            'SOUTH': np.array([0, -1], 'float'),
            'EAST' : np.array([1, 0], 'float'),
            'WEST' : np.array([-1, 0], 'float')
        }
        direction_vector = None
        if direction not in direction_map:
            direction_vector = direction # assume it's a 
                                         # 2d vector that was passed in
        else:
            direction_vector = direction_map[direction]

        self.velocity = direction_vector * vel_mag

        return self.velocity

def do_command_line_run():
    """
    Just a test run
    """
    first_car = Car(velocity=np.array([0, 0.1]), acceleration=5)
    print 'Mycar %s' % first_car
    data = np.zeros((200, 5))
    for i in range(100):
        pritn = first_car.update()
        if i == 99:
            print pritn
        data[i] = pritn

    print 'Interim val:\t%s' % first_car
    print 'Car state: %s' % first_car.state
    print '\n\n'
    first_car.acceleration = -1
    print 'Car accel = -1 now'
    first_car.turn('SOUTH')
    print 'Car direction = SOUTH now'
    for i in range(100, 200):
        pritn = first_car.update()
        if i == 100:
            print pritn
        data[i] = pritn

    print 'Final val:\t%s' % first_car
    time = np.linspace(0, (0.01*199), num=200)


    norm_vel = zeros(200)
    for k, i in data[:, [2,3]]:
        norm_vel[k] = norm(i)

    print data[0]
    figure()
    # plot(data[:, 0], data[:, 1], '.', label='Position')
    plot(time, norm_vel, '.r', label="Normalized vel")
    plot(time, data[:, 2], label='U')
    plot(time, data[:, 3], label='V')
    plot(time, data[:, 4], label='a')
    xlabel('time(s)')
    ylabel('stuff')
    title('Car test velocity')
    
    legend()
    show()

    
if __name__ == '__main__':
    do_command_line_run()
