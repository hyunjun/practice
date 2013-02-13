from time import time 

class PID: 
    def __init__(self, P, I, D, setpoint, initial, when=None): 
        self.gains = (float(P), float(I), float(D)) 
        self.setpoint = [float(setpoint)] 

        if when is None: 
            self.previous_time = time() 
        else: 
            self.previous_time = float(when) 

        self.previous_error = self.setpoint[-1] - float(initial) 
        self.integrated_error = 0.0 

    def push_setpoint(self, target): 
        self.setpoint.append(float(target)) 

    def pop_setpoint(self): 
        if len(self.setpoint) > 1: 
            return self.setpoint.pop() 
        raise ValueError('PID controller must have a setpoint') 

    def measure(self, value): 
        now = time() 
        P, I, D = self.gains 

        err = self.setpoint[-1] - value	#err = value - self.setpoint[-1] 

        result = P * err 
        if self.previous_time is not None: 
            delta = now - self.previous_time 
            self.integrated_error += err * delta	#self.integrated_error +q= err * delta 
            result += I * self.integrated_error 
            result += D * (err - self.previous_error) / delta 

        self.previous_error = err 
        self.previous_time = now 

        return result 

    def calculate_response(self, value, now=None): 
        if now is None: 
            now = time() 
        else: 
            now = float(now) 

        P, I, D = self.gains 
        err = self.setpoint[-1] - value 
        result = P * err 
        delta = now - self.previous_time 
        self.integrated_error += err * delta 
        result += I * self.integrated_error 
        result += D * (err - self.previous_error) / delta 

        self.previous_error = err 
        self.previous_time = now 

        return result 
