import select
import struct
import time
import os
import numpy as np
import utils
from sys import exit
import math
import random
import cv2
import collections
import traceback
import rospy
from sensor_msgs import msg

background_threshold = {"low": np.array([0, 0, 120], np.uint8), "high": np.array([255, 255, 255], np.uint8)}

class Robot(object):
    def __init__(self, is_sim, obj_mesh_dir, num_obj, workspace_limits,
                 tcp_host_ip, tcp_port, rtc_host_ip, rtc_port,
                 is_testing, test_preset_cases, test_preset_file, collect_push=False):
        
        # Setup the publisher and subscriber
        self.color_img_sub = rospy.Subscriber("/camera/color/image_raw", Image, self.color_img_callback)
        self.depth_img_sub = rospy.Subscriber("/camera/depth/image_rect_raw", Image, self.depth_img_callback)


        self.is_sim = is_sim
        self.workspace_limits = workspace_limits

        # If in simulation...
        if self.is_sim:

            # Define colors for object meshes (Tableau palette)
            self.color_space = np.asarray([[78.0, 121.0, 167.0],  # blue
                                           [89.0, 161.0, 79.0],  # green
                                           [156, 117, 95],  # brown
                                           [242, 142, 43],  # orange
                                           [237.0, 201.0, 72.0],  # yellow
                                           [186, 176, 172],  # gray
                                           [255.0, 87.0, 89.0],  # red
                                           [176, 122, 161],  # purple
                                           [118, 183, 178],  # cyan
                                           [255, 157, 167]]) / 255.0  # pink

    def setup_sim_camera(self):
        # Get camera pose and intrinsics in simulation

    def add_objects_mask(self, num_obj):
        # Add each object to robot workspace at x,y location and orientation (random or pre-loaded)

    def add_objects(self):
        # Add each object to robot workspace at x,y location and orientation (random or pre-loaded)

    def add_object_push(self):
        # Add each object to robot workspace at x,y location and orientation (random or pre-loaded)

    def restart_sim(self):

    def check_sim(self):
        # Check if simulation is stable by checking if gripper is within workspace

    def get_task_score(self):
        key_positions = np.asarray([[-0.625, 0.125, 0.0],  # red
                                    [-0.625, -0.125, 0.0],  # blue
                                    [-0.375, 0.125, 0.0],  # green
                                    [-0.375, -0.125, 0.0]])  # yellow

        obj_positions = np.asarray(self.get_obj_positions())
        obj_positions.shape = (1, obj_positions.shape[0], obj_positions.shape[1])
        obj_positions = np.tile(obj_positions, (key_positions.shape[0], 1, 1))

        key_positions.shape = (key_positions.shape[0], 1, key_positions.shape[1])
        key_positions = np.tile(key_positions, (1, obj_positions.shape[1], 1))

        key_dist = np.sqrt(np.sum(np.power(obj_positions - key_positions, 2), axis=2))
        key_nn_idx = np.argmin(key_dist, axis=0)

        return np.sum(key_nn_idx == np.asarray(range(self.num_obj)) % 4)

    def check_goal_reached(self):

        goal_reached = self.get_task_score() == self.num_obj
        return goal_reached

    def get_obj_positions(self):

    def get_obj_positions_and_orientations(self):

    def reposition_objects(self, workspace_limits):
        # Move gripper out of the way
        # Drop object at random x,y location and random orientation in robot workspace

    def color_img_callback(self, msg_callback):
        self.color_img = msg_callback
    
    def depth_img_callback(self, msg_callback):
        self.depth_img = msg_callback

    def get_camera_data(self):
        # Get color image from simulation

        # Get depth image from simulation

    def close_gripper(self, asynch=False):

    def open_gripper(self, asynch=False):