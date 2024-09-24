#no imports , just mock  code for the VC_D 

"""
this is the process diagram which I want to happen based on the class inputs 

this are the params I want tto say are 

pothole confidence from dashcanm - conf_pothole - ranges from 0 - 1
Throotle - T - ranges from -30 to 30
braking - b - ranges from 0 - 1 
steering - st - goes from -900 to 0 to +900

(internal threacshold or approach threashold) assuming the other cars are comming from left and right mirrors are calculated with at least 70% confidence - 0.7 

two values from them are also required which will be conf_lm , conf_rm which range from 0-1 for both cases 

I have 6 cases in total (d is used to show delta or change in an param)

    1. slow and divert --> t = t - dt , b = b + db , st = st+- st taking into account conf_lm (case for + sign ) , conf_rm (case for - sign )
    2. fast and diverrt -->  t = t + dt , b = b - db , st = st+- st taking into account conf_lm (case for + sign ) , conf_rm (case for - sign )
    3. constant and divert -->  t = t  , b = b  , st = st+- st taking into account conf_lm (case for + sign ) , conf_rm (case for - sign )

    4. slow and brace -- t = t - dt , b = b + db , st = st
    5. constant and brace -- t = t -dt , b = b  , st=st 

we want to update the mere values in the given range for the given params with the conf of the YOLOv8 which will let us know the pothole confidence which it predicts from the YOLO model .


    
    
"""

class VehicleControl:
    def __init__(self, conf_pothole, T, b, st, conf_lm, conf_rm):
        self.conf_pothole = conf_pothole  # Pothole confidence from dashcam (0-1)
        self.T = T  # Throttle (-30 to 30)
        self.b = b  # Braking (0-1)
        self.st = st  # Steering (-900 to 900)
        self.conf_lm = conf_lm  # Left mirror confidence (0-1)
        self.conf_rm = conf_rm  # Right mirror confidence (0-1)

    def update_controls(self, dt, db, st_change):
        if self.conf_pothole >= 0.7:  
            if self.conf_lm >= 0.7 and self.conf_rm >= 0.7:
               
                self.T -= dt
                self.b += db
                self.st += st_change * self.conf_lm  
                self.st -= st_change * self.conf_rm  
            elif self.conf_lm < 0.7 and self.conf_rm >= 0.7:
               
                self.T += dt
                self.b -= db
                self.st += st_change * self.conf_lm
                self.st -= st_change * self.conf_rm
            elif self.conf_lm >= 0.7 and self.conf_rm < 0.7:
                
                self.T = self.T
                self.b = self.b
                self.st += st_change * self.conf_lm
                self.st -= st_change * self.conf_rm

        else:
           
            if self.conf_lm >= 0.7:
                
                self.T -= dt
                self.b += db
            elif self.conf_rm >= 0.7:
                
                self.T -= dt

        
        self.T = max(-30, min(30, self.T))  # Throttle limits
        self.b = max(0, min(1, self.b))  # Braking limits
        self.st = max(-900, min(900, self.st))  # Steering limits

        return self.T, self.b, self.st



vehicle_control = VehicleControl(conf_pothole=0.8, T=10, b=0.5, st=0, conf_lm=0.9, conf_rm=0.8)


dt = 5   
db = 0.1 
st_change = 10  
# Update vehicle controls
new_T, new_b, new_st = vehicle_control.update_controls(dt, db, st_change)


print(f"Updated Throttle (T): {new_T}")
print(f"Updated Braking (b): {new_b}")
print(f"Updated Steering (st): {new_st}")
