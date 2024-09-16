
1. Software 


1.2 YOLO inputs 

make an app / service which takes in an input from the phone back camera which will act as in input for the YOLO model to take the data as in input ON THE LAPTOP mainly as of now .
we can use the IP WEBCAM for the time being 


1.1 YOLOv8 detection 
https://www.youtube.com/watch?v=zgbPj4lSc58&list=PL1u-h-YIOL0sZJsku-vq7cUGbqDEeDK0a
for pothole and obstacle deteciton initiallty 

INPUT - stream of inputs from the YOLO INPUTS point 
OUTPUT - temp - pressure values for the can msgs 
        Perma - CAN msgs to the Panda [for the lack of a better name as of now] 


1.2 CAN BUS software 

1.2.1 CAN bus sniffing - using cabana for any car / OBD sniffing 
1.2.2 CAN bus msgs - using STM send msgs to the car for the msg input and expect an output as an action 


tech used = STM32 , rust , c , c++ . react , python  

1.4ACTUATOR USGAE [TEMP]

find out optimal pressure values of the actuator and then do the pressure mapping for the actuatoruy to sudo-run the car in the mode we want 


2. HARDWARE 

2.1 Temporary Working 

We need to make an actuator follow the commands which will be given to the can bus but are now being done in the car superficially just for the lack of a better test car 

2.2 Long term soln - we need to make the STM device PCB in the long term which will be 3D printed and be attached to the OBD port 