# Automatic_door_opening_with_hardware_implementation
Home security systems secure valuables by blocking entry points and allowing only authorized people to enter the secured area. Numerous studies show homes without security systems, when compared to those with professionally monitored systems, are up to three times more likely to be burglarized because burglars are opportunistic by nature and are on the hunt for easy targets. The objective of this project is to use a deep learning model for face recognition and deploy it for securing doors. 

# Our Hardware Set-up details:
- Hardware Requierement
1. Jetson Nano
2. SBEC
3. Servo Motor
4. Motor Driver
5. 4 Jumper Wires
6. 1 Camera

<p align="center">
  <img src="img_%26_demo/hardware.jpg" width="550" title="hover text">
</p>
<br>
- My Hardware Connection
<p align="center">
  <img src="img_%26_demo/my_hardware_setup.jpg" width="550" title="hover text">
</p>
<br>

## How to use it
- First Set up complete hardware as above

- Install all dependencies
```
pip install -r requiremtnt.txt
```
- In order to add person in database
```
python train_and_collect_images.py
```
- to check door opening system

```
python final_file.py
```



## Sample Video
- **Servo Motor Rotation through Jetson GPIO pins**
<br>
![only_servo_motor_rotation_demo](https://github.com/pankajrajput0312/Automatic_door_Opening_with_Hardware_implementation/blob/main/img_%26_demo/only_servo_motor_rotation_demo.gif )
<br>

- **Face Recognition with Door opening Demo**
<br>
 ![alt text][gif]
 
 [gif]: https://github.com/pankajrajput0312/Automatic_door_Opening_with_Hardware_implementation/blob/main/img_%26_demo/face_recognition_and_servo_rotation_demo.gif "GIF"
 <br>
- **Admin receive notification with detail of person entering in the house.**
- **Visitor receive Welcome message when he enters into house.**
<p align="center" style="align: inline-block; border: 5px solid black;">
  <img src="img_%26_demo/notification_received_by_admin.jpeg" width="350" title="hover text">
  <img src="img_%26_demo/visitor_notification.jpeg" width="350" title="hover text">
</p>


