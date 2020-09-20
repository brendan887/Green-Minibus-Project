import re
import argparse
import os


def rename_batch(dir):
    for video in os.listdir(dir):
        # This will print every file and folder in in_dir. Note that these aren't absolute (full) paths, but just
        # the name and extension of these files.
        name, extension = os.path.splitext(video)
        pattern = 'vlc-record-(.+)-.+'
        match = re.search(pattern, name)
        match_name = match.group(1)
        old_name = os.path.join(dir, video)
        new_name = os.path.join(dir, match_name + extension)
        os.rename(old_name, new_name)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("dir", type=str, help="Choose folder")
    args = parser.parse_args()
    rename_batch(args.dir)
