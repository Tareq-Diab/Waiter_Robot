#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist 

import pygame
from pygame.locals import *
from threading import Thread
import time
v=0.5
z=0.9
pygame.init()
screen = pygame.display.set_mode((240, 240))
pygame.display.set_caption('Pygame Keyboard Test')
pygame.mouse.set_visible(1)
message="empty"

def key_listener():
    global message
    pub=rospy.Publisher("cmd_vel",Twist,queue_size=10)
    rospy.init_node("key_listenser_node")

    while not rospy.is_shutdown():
        events = pygame.event.get()
        twist=Twist()
        for event in events:
            if event.type == pygame.KEYDOWN:

                if event.key ==  pygame.K_LEFT:
                    twist.angular.z=z
                    message='left'
                    print(message)
                    pub.publish(twist)
                    
                if event.key == pygame.K_RIGHT:
                    twist.angular.z=-z
                    message='right'
                    print(message)
                    pub.publish(twist)

                if event.key == pygame.K_UP:
                    twist.linear.x=v
                    message='up'
                    print(message)
                    pub.publish(twist)
                                        
                if event.key == pygame.K_DOWN:
                    twist.linear.x=-v
                    message='DOWN'
                    print(message)
                    pub.publish(twist)

                if event.key == pygame.K_w:
                    message='w'
                    print(message)
                    pub.publish(message)
                     

                if event.key == pygame.K_s:
                    message='s'
                    print(message)
                    pub.publish(message)
                     

                if event.key == pygame.K_d:
                    message='d'
                    print(message)
                    pub.publish(message)
                     

                if event.key == pygame.K_a:
                    message='a'
                    print(message)
                    pub.publish(message)
                     


            if event.type == pygame.KEYUP:
                twist.angular.z=0.0
                twist.linear.x=0.0
                message='key-up'
                print(message)
                pub.publish(twist)
            
            
            

if __name__ == "__main__":
    key_listener()