import cv2
import json
import matplotlib.pyplot as plt
import numpy as np
import os
import seaborn as sns


def read_predicted_file(json_path):
    with open(json_path) as f:
        lane_info = json.load(f)
    lanes_pd = lane_info['lanes']
    lanes = list()
    for lane in lanes_pd:
        lanes.append(lane['points'])
    return lanes


def once_line_reader(json_path):
    """
    Input: json_path of 3D lane labels
    Output: lanes_2d, lanes_3d
    """

    def read_img_lane_from_json(json_path):
        with open(json_path) as f:
            lane_info = json.load(f)
        lanes_3d = lane_info['lanes']
        # lanes_3d = interploate_3d_tool(lanes_3d)
        camera_intri = lane_info['calibration']
        camera_intri_transpose = np.array(camera_intri).T.tolist()
        lanes_2d = []
        for lane_spec_3d in lanes_3d:
            lane_spec_3d = np.array(lane_spec_3d, dtype=np.float32)
            points_xyz = lane_spec_3d[:, :3]
            pcl_camera_homo = np.hstack([points_xyz, np.ones(points_xyz.shape[0], dtype=np.float32).reshape((-1, 1))])
            pcl_img = np.dot(pcl_camera_homo, camera_intri_transpose)
            pcl_img = pcl_img / pcl_img[:, [2]]
            lane_2d_spec = pcl_img[:, :2]
            lanes_2d.append(lane_2d_spec.tolist())
        return lanes_2d, lanes_3d

    lanes_2d, lanes_3d = read_img_lane_from_json(json_path)
    return lanes_2d, lanes_3d


def draw_lanes2d_on_img_points(lanes_2d, img_path, save_path):
    image = cv2.imread(img_path)
    for lane_spec in lanes_2d:
        for point in lane_spec:
            try:
                image = cv2.circle(image, (int(point[0]), int(point[1])), radius=3, color=(0, 0, 255), thickness=-1)
            except:
                print('project error:', int(point[0]), int(point[1]))
    cv2.imwrite(save_path, image)


def draw_lanes2d_on_img_line(lanes_2d, img_path, save_path):
    image = cv2.imread(img_path)
    for lane_spec in lanes_2d:
        lane_spec = np.array(lane_spec).astype(np.int32)
        lane_spec = lane_spec.reshape((-1, 1, 2))
        cv2.polylines(image, [lane_spec], False, color=(0, 0, 255), thickness=2)
    cv2.imwrite(save_path, image)


if __name__ == '__main__':
    json_path = "/nfs_system/Muse/ONCE_3DLanes/train/000092/cam01/1616443025299.json"
    img_path = "/nfs_system/Muse/ONCE/train/000092/cam01/1616443025299.json"
    lanes_2d, lanes_3d = once_line_reader(json_path=json_path)
    print(lanes_2d, lanes_3d)
    draw_lanes2d_on_img_line(lanes_2d=lanes_2d, img_path=img_path, save_path='./lanes_2d.jpg')
