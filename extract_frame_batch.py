import argparse
import os
from extract_frame import extract_frame


def extract_frame_batch(in_dir, frame_number, start_skip, end_skip, out_dir, skip_frames=1):
    for video in os.listdir(in_dir):
        # This will print every file and folder in in_dir. Note that these aren't absolute (full) paths, but just
        # the name and extension of these files.
        print(f"Processing video {video}")
        vid_path = os.path.join(in_dir, video)
        extract_frame(vid_path, frame_number, start_skip, end_skip, out_dir, skip_frames)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract a certain frame number from CV2 source")
    parser.add_argument("in_dir", type=str, help="Choose capture source.")
    parser.add_argument("frame_num", type=int, help="Frame number to extract, -1 to extract all frames.")
    parser.add_argument("start_skip", type=int, help="Number of frames to skip at the start of the video.")
    parser.add_argument("end_skip", type=int, help="Number of frames to skip at the end of the video.")
    parser.add_argument("skip_frames", type=int, help="Number of frames to skip between the next saved frame.")
    parser.add_argument("out_dir", type=str, help="Output dir.")
    args = parser.parse_args()
    extract_frame_batch(args.in_dir, args.frame_num, args.start_skip, args.end_skip, args.out_dir, args.skip_frames)
