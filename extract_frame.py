import cv2
import argparse
import os


def extract_frame(src, frame_number, start_skip, end_skip, output_folder, skip_frames=1):
    frame = 0
    print(output_folder)
    cap = cv2.VideoCapture(src)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    name, extension = os.path.splitext(os.path.basename(src))
    if frame_number != -1:
        while True:
            success, img = cap.read()
            if not success:
                raise ValueError("Failed to read from capture")
            if frame == frame_number:
                cv2.imwrite(os.path.join(output_folder, name + "_frame_" + str(frame) + ".jpg"), img)
                break
            frame += 1
        return
    for i in range(start_skip, total_frames - end_skip, skip_frames):
        while True:
            success, img = cap.read()
            if not success:
                raise ValueError("Failed to read from capture")
            if frame == i:
                cv2.imwrite(os.path.join(output_folder, name + "_frame_" + str(frame) + ".jpg"), img)
                break
            frame += 1
        frame += 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract a certain frame number from CV2 source")
    parser.add_argument("src", type=str, help="Choose capture source.")
    parser.add_argument("frame_num", type=int, help="Frame number to extract, -1 to extract all frames.")
    parser.add_argument("start_skip", type=int, help="Number of frames to skip at the start of the video.")
    parser.add_argument("end_skip", type=int, help="Number of frames to skip at the end of the video.")
    parser.add_argument("skip_frames", type=int, help="Number of frames to skip between the next saved frame.")
    parser.add_argument("output_folder", type=str, help="Output dir.")
    args = parser.parse_args()
    extract_frame(args.src, args.frame_num, args.start_skip, args.end_skip, args.output_folder, args.skip_frames)
