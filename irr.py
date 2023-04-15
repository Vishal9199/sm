Design two turtles namely "Dogobot" and "Catobot" which can be included within the Turtlesim and both the turtles should run concurrently in a random motion.

You can use the Spawn module for creating another turtle.

Instructions:

Already we have tried creating a TurtleSIM which can move in different shapes and and through teleop key as well 

$ roscore

$ rosrun turtlesim turtlesim_node 

$ rosrun turtlesim turtle_teleop_key 

$ rosrun ros_tut_1 circularmovement.py

Now, You need to define two turtles in a single turtlesim namely:

scp lab21@172.16.10.7:pradeep_ws/src/ros_tutorial1/script/twoturtles.py .

===================================================================================================================================
Today  Exercise will be on Irritated Robot:
If the robot encounters an obstacle at a threshold distance of 0.5, then the robot engage in a twisted motion or circular motion

If no obstacle, the robot moves forward with a nominal speed.

You can make use of Burger as the Turtlebot model

Exercise 2: From the above example, make the irritated robot to a diplomat robot where the robot moves away
from the obstacle and move forward with a nominal speed. 

How to do: Open a terminal

Step 1: $ roscore

Step 2: Open another terminal

$ export TURTLEBOT3_MODEL=burger

$ roslaunch turtlebot3_gazebo turtlebot3_empty_world.launch 

Step 3:

Copy the irritated_robot.py from the following folder 

$ scp lab21@172.16.10.7:irritational_robot.py

move the file to pradeep_ws/src/ros_tutorial1/src/

Go to the above folder and execute the following command.

$ chmod 777 irritational_robot.py

$ rosrun ros_tutorial1 irritational_robot.py 

and check the gazebo platform and add the obstacles and check the status of the robot (Burger)
