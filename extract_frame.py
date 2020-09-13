import cv2
import argparse
import os


def extract_frame_number(src, frame_number, output_folder, start_skip_input, end_skip_input, skip_frames=0):
    frames_total = int(src.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT))
    frame = 0
    frames_skipped = 0
    end_skip = frames_total - end_skip_input
    print(output_folder)
    cap = cv2.VideoCapture(src)
    while True:
        if frame <= start_skip_input:

        success, img = cap.read()
        if not success:
            break
        if frame_number >= 0 and frame == frame_number:
            cv2.imwrite(os.path.join(output_folder, "frame_" + str(frame) + ".jpg"), img)
            break
        if frame == 0 or (frame_number < 0 and frames_skipped == skip_frames):
            cv2.imwrite(os.path.join(output_folder, "frame_" + str(frame) + ".jpg"), img)
            frames_skipped = 0
        frames_skipped += 1
        frame += 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract a certain frame number from CV2 source")
    parser.add_argument("src", type=str, help="Choose capture source.")
    parser.add_argument("frame_num", type=int, help="Frame number to extract, -1 to extract all frames.")
    parser.add_argument("start_skip_input", type=int, help="Number of frames to skip at the start of the video.")
    parser.add_argument("end_skip_input", type=int, help="Number of frames to skip at the end of the video.")
    parser.add_argument("skip_frames", type=int, help="Number of frames to skip between saved frames.")
    parser.add_argument("output_folder", type=str, help="Output directory.")
    args = parser.parse_args()
    extract_frame_number(args.src, args.frame_num, args.output_folder, args.skip_frames)
