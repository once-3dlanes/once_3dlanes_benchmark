import json
import numpy as np
from scipy.interpolate import interp1d
from read_and_project import once_line_reader


def interpolate_3d_tool(lanes):
    """
    each lane of input lanes must have at least two points
    input: lanes: [lane_num, ]
    """

    def cubic_interpolate(lane_spec):
        lane_spec = np.array(lane_spec)
        x = lane_spec[:, 0]
        y = lane_spec[:, 1]
        z = lane_spec[:, 2]
        z_min, z_max = min(z), max(z)
        zmin, zmax = np.ceil(z_min * 1000) / 1000, np.floor(z_max * 1000) / 1000
        gt_lane_points_camera = []
        # less than four points cannot do cubic spline interpolate, use linear instead
        if len(lane_spec) < 4:
            f_zx = interp1d(z, x, kind='linear', fill_value='extrapolate')
            f_zy = interp1d(z, y, kind='linear', fill_value='extrapolate')
            for z in np.arange(zmin, zmax, np.around((zmax - zmin) / 6, 3)):
                z = np.around(z, 3)
                x_out = np.around(f_zx(z), 3)
                y_out = np.around(f_zy(z), 3)
                gt_lane_points_camera.append([x_out, y_out, z])
        else:
            f_zx = interp1d(z, x, kind='cubic', fill_value='extrapolate')
            f_zy = interp1d(z, y, kind='cubic', fill_value='extrapolate')
            for z in np.arange(zmin, zmin + np.around((zmax - zmin) / 2, 1), 0.2):
                z = np.around(z, 3)
                x_out = np.around(f_zx(z), 3)
                y_out = np.around(f_zy(z), 3)
                gt_lane_points_camera.append([x_out, y_out, z])
            for z in np.arange(zmin + np.around((zmax - zmin) / 2, 1), zmax, 0.5):
                z = np.around(z, 3)
                x_out = np.around(f_zx(z), 3)
                y_out = np.around(f_zy(z), 3)

                gt_lane_points_camera.append([x_out, y_out, z])
        return gt_lane_points_camera

    lanes_inter = []
    for lane_spec in lanes:
        if len(lane_spec) < 2:
            continue
        lane_spec_inter = cubic_interpolate(lane_spec)
        lanes_inter.append(lane_spec_inter)
    return lanes_inter


if __name__ == '__main__':
    json_path = "/nfs_system/Muse/ONCE_3DLanes/train/000092/cam01/1616443025299.json"
    lanes, _ = once_line_reader(json_path)
    print(lanes)
    lane_inter = interpolate_3d_tool(lanes)
    print(lane_inter)
