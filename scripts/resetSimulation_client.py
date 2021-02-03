#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_srvs.srv import Empty



def resetSimutation_client():
    rospy.wait_for_service("/gazebo/reset_simulation")

    try:
        # rospy.ServiceProxy("name of the Service", TypeOfService)
        resetSim_srv = rospy.ServiceProxy("/gazebo/reset_simulation", Empty)

        # resetSim_srv(data)
        response = resetSim_srv()

        return response
    except rospy.ServiceException, e:
        rospy.logerror("Service call failed : "+e)


if __name__ == '__main__':
    resetSimutation_client()
