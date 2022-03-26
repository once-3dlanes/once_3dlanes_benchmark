import json
import matplotlib as mpl
import matplotlib.pyplot as plt
# import mayavi.mlab  # if you need 3d visualization in mayavi
import cv2
import numpy as np
import os
from matplotlib.ticker import FuncFormatter
from mpl_toolkits.mplot3d import Axes3D

from interpolate import interpolate_3d_tool
from read_and_project import once_line_reader

colors = [[1, 0, 0],  # red
          [0, 1, 0],  # green
          [0, 0, 1],  # blue
          [1, 0, 1],  # purple
          [0, 1, 1],  # cyan
          [1, 0.7, 0],  # orange
          [0.45, 0.17, 0.07]]  # crown


def visual_pcl(pointcloud):
    """
    input point cloud shape:[N,3]
    """
    x = pointcloud[:, 0]  # x position of point
    y = pointcloud[:, 1]  # y position of point
    z = pointcloud[:, 2]  # z position of point
    # r = pointcloud[:, 3]  # reflectance value of point
    fig = mayavi.mlab.figure(bgcolor=(0, 0, 0), size=(1920, 1020))
    mayavi.mlab.points3d(x, y, z,
                         # z,  # Values used for Color
                         mode="point",
                         colormap='spectral',  # 'bone', 'copper', 'gnuplot'
                         color=(0, 1, 1),  # Used a fixed (r,g,b) instead
                         figure=fig,
                         scale_factor=1
                         )

    mayavi.mlab.show()


def visual_all_lane_pcl(pointcloud, all_lane_pcl):
    """
    visualize all lane_points in the scene
    input type: pointcloud [N,3]
                all_lane_pcl [lane_num, ]  all_lane_pcl[0] [N,3]
    """
    pointcloud = np.array(pointcloud)
    x = pointcloud[:, 0]  # x position of point
    y = pointcloud[:, 1]  # y position of point
    z = pointcloud[:, 2]  # z position of point
    # degr = np.degrees(np.arctan(z / d))
    col = z
    fig = mayavi.mlab.figure(bgcolor=(0, 0, 0), size=(1920, 1020))
    mayavi.mlab.points3d(x, y, z,
                         col,  # Values used for Color
                         mode="point",
                         colormap='spectral',  # 'bone', 'copper', 'gnuplot'
                         # color=(0, 1, 0),   # Used a fixed (r,g,b) instead
                         figure=fig,
                         )

    for i in range(len(all_lane_pcl)):
        # only the pcl of the lane
        lane_pcl = all_lane_pcl[i]
        lane_pcl = np.array(lane_pcl)
        lane_x = lane_pcl[:, 0]
        lane_y = lane_pcl[:, 1]
        lane_z = lane_pcl[:, 2]

        mayavi.mlab.points3d(lane_x, lane_y, lane_z,
                             mode="point",
                             colormap='spectral',  # 'bone', 'copper', 'gnuplot', 'spectral'
                             color=(1, 1, 0),  # Used a fixed (r,g,b) instead  yellow
                             figure=fig,
                             )
    mayavi.mlab.show()


def draw_lanes3d(all_lane_points, save_path):
    """
    visual all lane points in 3D ax plot, in the final plot, the coordinates have changed to normal coordinates
    input:
    all_lane_points: [lane_num, ]  all_lane_points[0]: [N,3]
    save_path: the dir path of saved image
    """
    mpl.rcParams['legend.fontsize'] = 10
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    all_lane_points = np.array(all_lane_points)
    # all_lane_points = interpolate_3d_tool(all_lane_points)  #with interpolation
    for i in range(len(all_lane_points)):
        lane_points = all_lane_points[i]
        lane_points = np.array(lane_points)
        x = lane_points[:, 0]
        y = lane_points[:, 1]
        z = lane_points[:, 2]
        t = np.arange(1, lane_points.shape[0] + 1)  # simple assumption that data was sampled in regular steps
        fitx = np.polyfit(t, x, 3)                  # polyfit
        fity = np.polyfit(t, y, 2)
        fitz = np.polyfit(t, z, 2)
        lane = []
        for j in t:
            x_out = np.polyval(fitx, j)
            y_out = np.polyval(fity, j)
            z_out = np.polyval(fitz, j)
            lane.append([x_out, y_out, z_out])
        lane = np.array(lane)
        lane_x, lane_y, lane_z = lane[:, 0], lane[:, 1], lane[:, 2]

        color = colors[np.mod(i, len(colors))]

        ax.plot(lane_x, lane_z, -lane_y, color=color, linewidth=3, label='3D Lane %d' % i)  # normal coordinates
        # ax.scatter(lane_x, lane_z, -lane_y, s=1, c=np.array(color).reshape(1, -1))

    def inverse_z(z, position):
        return "{:.3}".format(-z)

    ax.zaxis.set_major_formatter(FuncFormatter(inverse_z))
    ax.legend()
    plt.savefig(os.path.join(save_path, 'lanes_3d.png'))
    # plt.show()


def draw_lanes2d(lanes_2d, img_path, save_path):
    image = cv2.imread(img_path)
    for lane_spec in lanes_2d:
        lane_spec = np.array(lane_spec).astype(np.int32)
        lane_spec = lane_spec.reshape((-1, 1, 2))
        cv2.polylines(image, [lane_spec], False, color=(0, 0, 255), thickness=2)
    cv2.imwrite(save_path, image)


if __name__ == '__main__':
    json_path = '/nfs_system/Muse/ONCE_3D/train_new_v2/000027/1616100824399.json'
    img_path = '/nfs_system/Muse/ONCE_3D/val/000027/1616100824399.jpg'
    lanes_2d, lanes_3d = once_line_reader(json_path)
    draw_lanes3d(lanes_3d, save_path='./output')
    draw_lanes2d(lanes_2d=lanes_2d, img_path=img_path, save_path='./output/lanes2d.png')
