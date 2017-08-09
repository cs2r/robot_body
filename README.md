# robot
The system is tested on ubuntu Xenial armhf
Image avalaible on MEGA Cloud https://mega.nz/#!oIFhUZLa decryption Key: !K1EM5aygbKRRNzjF8cbqpAs_myevqVCU3P7QGwaH8RE

this package need : 

                    ROS Kinetic 

                    pyserial
                    
                    enum
                    
                    python-tk
                    
Installation:

  ROS:
  
    install ROS Kinetic http://wiki.ros.org/kinetic/Installation/Ubuntu
        
  
  Python packages:
  
      $ sudo apt-get install python-pip

      $ sudo pip install pyserial

      $ sudo pip install enum

      $ sudo apt-get install python-tk

  now use git clone to download the package:

      $ cd catkin_ws/src

      $ git clone https://github.com/mekhtiche/robot_body.git

      $ cd ..

      $ catkin_make
  
  source the work space
  
      $ sudo nano .bashrc
    
    in the end of the file add "source ~/catkin_ws/devel/setup.bash"
    
    
  To launch the robot:

      $ roslaunch robot_body Robot_start.launch

      $ roslaunch robot_body Robot_start_stat.launch

  To record sign:

      $ roslaunch robot_body Recording.launch

      $ roslaunch robot_body Recording_stat.launch

  
