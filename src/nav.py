#!/usr/bin/env python
import rospy
import actionlib
from std_msgs.msg import String 
from move_base_msgs.msg import MoveBaseGoal,MoveBaseAction
from geometry_msgs.msg import Twist , Point
from actionlib_msgs.msg import *


locations={"table1":[-0.007822,-9.32,-5.29870652074e-08,2.80965577068e-06,0.999742138278,-0.0227080810323],
            "table2":[0.14730499787,-12.3255622843,8.81403791388e-06,-1.52848839402e-07, 0.999980559148,  0.00623548295902],
            "table3":[0.185506437263,-15.5865713911, -8.79538414965e-07,-9.7263439565e-06,-0.999992314302,0.00392061750175],
            "table4":[-4.04320763788,-13.0186450679, -2.50302255714e-06,1.91464199011e-06,-0.569909437543,-0.821707510608],
            "table5":[-2.82886310449,-7.08014313382, -3.76908086543e-06,4.1789324188e-06,0.741747628717,-0.670679100063],
            "table6":[-2.73949504593,-10.3345636424, 7.01486757359e-06,1.00485723412e-06, 0.704246875672,-0.70995516623],
            "table7":[-2.6554073559,-13.7750087966,  7.85598565088e-06,7.7734500182e-06,0.719465882395,-0.694527784864],
            "kitchen":[-0.155941103796,0.205165675873, 7.44509152398e-06,-7.42886814816e-06,-0.719876366754,0.694102309806]
            }
def GOTO(place):
    coordinates=locations[place]
    x=coordinates[0]
    y=coordinates[1]
    ox=coordinates[2]
    oy=coordinates[3]
    oz=coordinates[4]
    ow=coordinates[5]
    move(x,y,ox,oy,oz,ow)

def move(x,y,ox,oy,oz,ow):
    ac = actionlib.SimpleActionClient("move_base",MoveBaseAction)

    while(not ac.wait_for_server(rospy.Duration.from_sec(5.0))):
        rospy.loginfo("waiting for move base server")
    goal=MoveBaseGoal()

    #frame parameters
    goal.target_pose.header.frame_id="map"
    goal.target_pose.header.stamp = rospy.Time.now()

    #goal

    goal.target_pose.pose.position= Point(x,y,0)
    goal.target_pose.pose.orientation.x=ox
    goal.target_pose.pose.orientation.y=oy
    goal.target_pose.pose.orientation.z=oz
    goal.target_pose.pose.orientation.w=ow

    ac.send_goal(goal)

if __name__ == '__main__':
    rospy.init_node("navigation_node",anonymous=False)
    
    GOTO("kitchen")

    """
    location("table1")
        location("table2")
    location("table3")
    location("table4")
    location("table5")
    location("table6")
    location("table7")
    location("kitchen")
    """

