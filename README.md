# Waiter Robot
## introduction
A robot used to deliver food from resturant kitchen to tables Autonomously.This robot is my take on reverse engineering the  "Mozo" robot by Marses, Link: https://www.marses.systems/hospitality/
This robot uses ROS's navigation stack to move around in it's environment and calculate the best route around static and dynamic obstacles. 
![](https://github.com/Tariq96/Waiter_Robot/blob/master/pictures/GIF-201006_133905.gif)
## Operation Flow

## mapping
The robot is used for the first time to create a map of the restaurant in order to use it later for navigation around obstacles Autonomously. using the Slam algorithm along with odometry sensors such as encoders , IMU and lidar , a map is created and saved for later use.

mapping commands :
```
roslaunch waiter_bot restaurant.launch
roslaunch waiter_bot slam.launch
rosrun waiter_bot pub.py
```

![](https://github.com/Tariq96/Waiter_Robot/blob/master/pictures/GIF-201006_134455.gif)

## passing orders 
commands to the robot are bassed through a simple GUI ment to show on a screen in the kitchen or the robot, it's used to point the robot to it's next target position in it's environment. This part assumes that the restaurant table position is fixed in order to navigate around the restaurant relaying only on lidat and odometry sensors. dynamic table positions in therestaurant will require a layer of computer vision software in order to loalize the variable table positions. [adding cameras and table localization stack is targeted in the next update to allow dynamic restaurant layout]
for now the table positiong in the restaurant is shown in the picture. 
![](https://github.com/Tariq96/Waiter_Robot/blob/master/pictures/20201006_151235.png)

To use the Gui run the gui.py mode in a new terminal:
```
rosrun waiterbot gui.py
```
![](https://github.com/Tariq96/Waiter_Robot/blob/master/pictures/GIF-201006_135716.gif)

## frame structure
The robot frame is built around the main chassis all robot parts are refrenced to the main frame.
![](https://github.com/Tariq96/Waiter_Robot/blob/master/pictures/robot_frames.png)

## topics structure
![](https://github.com/Tariq96/Waiter_Robot/blob/master/pictures/rosgraph.png)


## installing / running simulation

1- install ros
2- install gazebo
3- git clone my rebo
```
inside your catkin workspace type in a terminal :
git clone "https://github.com/Tariq96/Waiter_Robot.git"
```
4- compile all the project files
```
catkin_make
```


![](https://github.com/Tariq96/Waiter_Robot/blob/master/pictures/GIF-201006_135319.gif)


## refrences 
