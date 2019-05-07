# Intent Recognizer

### Module for CU GoodBot project

The Intent Recognizer takes scene information as parsed by the Scene Understanding software. The scene information is list of objects identified by `YOLO v3` along with there distance and angle from the center of the camera on the topic `\scene_info`. The intent Recognizer takes that information, human intent via speech and finds the relevant POIs and obstacles, generates explanations and publishes the intent to `\intent` topic for the [Navigation Manager](https://github.com/cu-goodbot/NavigationManager) to utilize.

## Running the Intent Recognizer

To run the Intent Recognizer software, make sure that you have build the package in your catkin workspace, and sourced the workspace, then simply run

```
$ roslaunch intent_recognizer intent_recognizer.launch
```

To see what the module is publishing, run in a new terminal
```
$ rostopic echo /intent
```
