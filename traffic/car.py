"""
Core module for class Car and Car Controller
"""
import numpy as np
from numpy.linalg import norm
from traffic.vecops import is_opposite, is_same_direction
class Car(object):
    """
    Car object. Does self updating of state, position, velocity.
    """
    def __init__(self, position=np.array([0, 0], 'float'), \
                    velocity=np.array([0, 0], 'float'), \
                    acceleration=np.array([0, 0], 'float')):
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration

    def update(self, delta_t=10):
        """
        Updates state and pos, vel vectors
        """
        state = self.state
        if state == 'STOP':
            self.acceleration = np.array([0, 0], 'float')
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
        m_acc = norm(self.acceleration)
        if m_vel <= 0 and self.acceleration <= 0: #we never go backwards
            return 'STOP'
        
        if self.is_decelerating():
            return 'SLOWDOWN'
        
        if m_acc == 0:
            return 'CRUISE'
        
        if self.is_accelerating():
            return 'SPEEDUP'

        raise Exception("Bad state in Car! IS_ACCCEL: %s, \
                                        IS_DECEL:%s, \
                                        STATE:%s" % (self.is_accelerating(), \
                                                    self.is_decelerating(), \
                                                    self))

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
        acc_mag = norm(self.acceleration)
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
        self.acceleration = direction_vector * acc_mag

        return (self.velocity, self.acceleration)


    def is_decelerating(self):
        """
        Returns true when acceleration vector is pointing in antiparalell 
        direction of velocity vector
        """
        return is_opposite(self.velocity, self.acceleration)

    def is_accelerating(self):
        """
        Returns true when acceleration vector is pointing in paralell 
        direction of velocity vector, and acceleration is positive.
        """
        m_acc = norm(self.acceleration)
        return m_acc > 0 and is_same_direction(self.velocity, self.acceleration)

