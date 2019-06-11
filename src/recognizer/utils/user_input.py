import argparse
from pathlib import Path

from .directory import create_not_existing_directory


def parse_arguments():
    """Parse user provided arguments."""

    parser = argparse.ArgumentParser(
        description="People recognizer."
    )

    parser.add_argument(
        "--filenames",
        default="",
        help="Filename of files on which people will be recognized. Names MUST be separated by ',' and without spaces around them. Left blank if you want to recognize people on all images in data directory."
    )

    parser.add_argument(
        "--data_dir",
        default="../../data/",
        help="Relative path from main.py to files given as filenames argument."
    )

    parser.add_argument(
        "--results_dir",
        default="../../results/",
        help="Relative path from main.py to place where results will be stored"
    )

    parser.add_argument(
        "--yolo_config_path",
        default="yolo/config/",
        help="Relative path from main.py to yolo config"
    )

    args = parser.parse_args()
    create_not_existing_directory(args.results_dir)

    p = Path(args.data_dir)
    if not p.is_dir():
        print(f'Directory: {args.data_dir} does not exist. Make sure that you provide correct path. Exiting...')
        exit(0)

    return args
