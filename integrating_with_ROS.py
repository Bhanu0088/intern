import rospy
from nav_msgs.msg import OccupancyGrid
from std_msgs.msg import Header

def publish_occupancy_grid(occupancy_grid):
    pub = rospy.Publisher('occupancy_grid', OccupancyGrid, queue_size=10)
    rospy.init_node('occupancy_grid_publisher', anonymous=True)
    rate = rospy.Rate(10)  # 10 Hz

    while not rospy.is_shutdown():
        header = Header()
        header.stamp = rospy.Time.now()
        header.frame_id = 'map'
        
        grid_msg = OccupancyGrid()
        grid_msg.header = header
        grid_msg.info.resolution = 0.1  # Example resolution
        grid_msg.info.width = grid_size[0]
        grid_msg.info.height = grid_size[1]
        grid_msg.data = occupancy_grid.flatten().tolist()
        
        pub.publish(grid_msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        publish_occupancy_grid(occupancy_grid)
    except rospy.ROSInterruptException:
        pass
