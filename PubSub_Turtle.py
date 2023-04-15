13th Jan 2023 - Robotic Operating System (ROS)
ROS1 - Noetic 

OS: Ubuntu 20.04 

some of the commands are 
rosrun, roscore, rosnode, roslaunch, rqt_graph, rosgraph, etc. 

Username: lab21
Password: fine 

Prerequisites:
1. Ubuntu OS (basic commands)
2. PATH Setting information 
3. basic knowledge of Unix and Linux Family.
4. Programming knowledge (C++ and Python)

Examples or exercises
0. Basic ROS exercise
1. Publisher, Subscriber
2. Turtlesim 
3. TurtleBot 
4. Gazebo
etc.

My Machine IP address is 172.16.10.7

$ scp lab21@172.16.10.7:first.py .

To begin with, open a terminal and run the follolwing command 

$ roscore

Open another Terminal and run the first.py using 
$ python3 first.py

ROS has a build system called catkin which supports
* easier deployment 
* cross compilation
etc.

some commands related to catkin is 
$ catkin_make 
$ catkin_init_workspace 
$ catkin_create_pkg


Step 1:
Create a folder in the /home/lab21 directory using the command 

$ mkdir -p pradeep_ws/src
$ cd pradeep_ws/

$ catkin_make
after the above command, two folder namely build/ and devel/ might have created. 

Now we need to set the PATH for this file 
devel/setup.bash 

One method is to use , source command when opening a new terminal every time, the command is 

$ source /home/lab21/pradeep_ws/devel/setup.bash

Second method is include the command in the /home/lab21/.bashrc file, so that command will run without any issues when a new terminal is opened.
after the second step, logout and login back to get the command working and activated else run the command 
$ source .bashrc

Step 2 : 
Go to pradeep_ws/src folder and create a catkin package using the following command 

$ cd pradeep_ws/src

$ catkin_create_pkg ros_tutorial1 rospy std_msgs
$ cd ..

$ catkin_make
(this time, the make will include the ros_tutorial1 also in to the devel and build libraries)

Step3 - We will be creating two files namely 
1. publihser.py
2. subscriber.py

Create the above files in the folder 
pradeep_ws/src/ros_tutorial1/script

And give full permission to run 

$ chmod 777 *.py 

Step 4 - running the publisher and subscriber, we need to open two windows one for pub and another for sub.

In Terminal 1 
Go to 
$ cd pradeep_ws/
$ source ./devel/setup.bash 

$ rosrun ros_tutorial1 pub.py

in Terminal 2 
Go to 
$ cd pradeep_ws/
$ source ./devel/setup.bash 
$ rosrun ros_tutorial1 subs.py

You can see the output of I took ROS Knowledge by the Subscriber and "ROS Knowledge" by the publisher.

$ rqt_graph 
will open the graph of all the nodes running under the ROS.

turtlesim 

Step 1: 
Always start the roscore 
$ roscore

Step 2:
Open a Terminal
To open turtlesim, give the following command.
$ rosrun turtlesim turtlesim_node

Open another Terminal
$ rosrun turtlesim turtle_teleop_key

Copy the file from my machine

$ scp lab21@172.16.10.7:circular_movement.py .
password: fine 

Copy the above python file to the folder where you already created (example: pradeep_ws/src/ros_tutorial1/script/)

Open first Terminal and run the command 
$ rosrun turtlesim turtlesim_node

Open Second Terminal, go to your workspace
$ cd pradeep_ws/ 
$ source ./devel/setup.bash
$ rosrun ros_tutorial1 circular_movement.py
