# Intent Recognition

### Module for CU GoodBot project


## Running with ROS

To run in ROS framework:

First, soft (sym) link the IntentRecognition directory to your catkin workspace then run 
```
$ catkin_make 
```
to build the package.

To launch the intent recognizer node run
```
$ roslaunch intent_recognizer intent_recognizer.launch
```

To see what the module is publishing, run in a new terminal
```
$ rostopic echo /intent
```
and you should see a serialized version of the data.

