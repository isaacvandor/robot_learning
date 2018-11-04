#!/usr/bin/env python

from __future__ import print_function
from geometry_msgs.msg import PointStamped, PointStamped
from std_msgs.msg import Header, String
from neato_node.msg import Bump
from sensor_msgs.msg import LaserScan
from visualization_msgs.msg import Marker
from geometry_msgs.msg import Twist
import tty
import select
import sys
import termios
import datetime
import rospy

class Commands(object):
    """This node is to test the neato interface and get it moving"""

    def __init__(self):
        rospy.init_node("Drive")
        self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        rospy.Subscriber('/bump', Bump, self.process_bump)
        rospy.Subscriber('/command_words', String, self.get_command)
        self.command = ''
        print(self.command)

    def process_bump(self, m):
        directions = self.make_twist(0,0)
        self.pub.publish(directions)
        pass
        #print(m.leftFront)

    def make_twist(self, x, theta):
        """
        Takes x and angular velocity and creates the appropriate twist
        to publish to the cmd_vel topic.
        """
        sendy = Twist()
        sendy.linear.x = x
        sendy.linear.y = 0
        sendy.linear.z = 0
        sendy.angular.x = 0
        sendy.angular.y = 0
        sendy.angular.z = theta
        return sendy

    def move_dist(self, distance):
        """
        Takes a distance in meters and moves it forward. Works under the
        timing that 0.5 cmd_vel = 1 ft/s.
        """
        speed = 0.5
        m2ft = 0.3048
        dist_ft = distance/m2ft
        sec = dist_ft

        message = self.make_twist(0.5, 0)
        self.pub.publish(message)

        start = datetime.now()
        if datetime.now()-start > sec:
            stop_msg = make_twist(0,0)
            self.pub.publish(stop_msg)



    def get_command(self, m):
        self.command = m.data
        print(self.command)
            
    def run(self):
        while not rospy.is_shutdown():
            print(self.command == "bird")
            if self.command == "yes" or self.command == 'up':
                move = [1,0]
            elif self.command == 'no' or self.command == 'down':
                move = [-1,0]
            elif self.command == 'stop' or self.command == 'off':
                move = [0,0]
            elif self.command == 'left':
                move = [0,1]
            elif self.command == 'right':
                move = [0,-1]
            else:
                move = [0, 0]

            # print(move)
            lin_vel = 1
            ang_vel = 1

            x_vel = move[0]*lin_vel
            theta_vel = move[1]*ang_vel

            directions = self.make_twist(x_vel,theta_vel)

            self.pub.publish(directions)

if __name__ == '__main__':
    settings = termios.tcgetattr(sys.stdin)
    node = Commands()
node.run()
