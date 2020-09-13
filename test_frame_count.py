import cv2
import argparse
import os
from extract_frame import extract_frame_number


def count_frames(src):
    cap = cv2.VideoCapture(src)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(total_frames)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract a certain frame number from CV2 source")
    parser.add_argument("src", type=str, help="Select video to count frames.")
    args = parser.parse_args()
    extract_frame_number(args.src)

# cd into BrendanEE
# . env/bin/activate
