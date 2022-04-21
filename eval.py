import argparse
from evaluation.eval_utils import LaneEval


def parse_config():
    parser = argparse.ArgumentParser(description='arg parser')
    parser.add_argument('--cfg_file', type=str, default='cfg/eval.json', help='specify the config for evaluation')
    parser.add_argument('--gt_path', type=str, default=None, required=True, help='')
    parser.add_argument('--pred_path', type=str, default=None, required=True, help='')
    args, unknown_args = parser.parse_known_args()
    return args, unknown_args


if __name__ == "__main__":
    args, unknown_args = parse_config()
    le = LaneEval()
    le.lane_evaluation(args.gt_path, args.pred_path, args.cfg_file)
