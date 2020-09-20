import argparse
import os
import random
import shutil


def distribute_frames(in_dir, percent, out_dir_1, out_dir_2):
    files = os.listdir(in_dir)
    total_files = len(files)
    random.shuffle(files)
    dir_1_num = int(percent * total_files)
    for i in range(total_files):
        if i < dir_1_num:
            output_dir = out_dir_1
        else:
            output_dir = out_dir_2
        name = files[i]
        in_path = os.path.join(in_dir, name)
        out_path = os.path.join(output_dir, name)
        shutil.copy(in_path, out_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract a certain frame number from CV2 source")
    parser.add_argument("in_dir", type=str, help="Choose directory.")
    parser.add_argument("percent", type=float, help="Percentage of items to directory 1 (input as decimal).")
    parser.add_argument("out_dir_1", type=str, help="First output directory.")
    parser.add_argument("out_dir_2", type=str, help="Second output directory")
    args = parser.parse_args()
    distribute_frames(args.in_dir, args.percent, args.out_dir_1, args.out_dir_2)
