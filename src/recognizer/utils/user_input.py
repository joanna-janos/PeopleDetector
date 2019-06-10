import argparse
from pathlib import Path

from .directory import create_not_existing_directory


def parse_arguments():
    """Parse user provided arguments."""

    parser = argparse.ArgumentParser(
        description="People recognizer. If you want to recognize people on predefined images left all arguments blank."
    )

    parser.add_argument(
        "--filenames",
        default="",
        help="Filenames of file on which people will be recognized. Names MUST be separated by ','."
    )

    parser.add_argument(
        "--data_dir",
        default="/Users/joannajanos/Documents/informatyka_wmii_uj/semestr2/biometria/PeopleRecognizer/data/",
        help="Absolute path to files given as filenames argument."
    )

    parser.add_argument(
        "--results_dir",
        default="/Users/joannajanos/Documents/informatyka_wmii_uj/semestr2/biometria/PeopleRecognizer/results/",
        help="Absolute path to place where results will be stored"
    )

    parser.add_argument(
        "--yolo_config_path",
        default="/Users/joannajanos/Documents/informatyka_wmii_uj/semestr2/biometria/PeopleRecognizer/src/recognizer/yolo/config/",
        help="Absolute path to yolo config"
    )

    args = parser.parse_args()
    create_not_existing_directory(args.results_dir)

    p = Path(args.data_dir)
    if not p.is_dir():
        print(f'Directory: {args.data_dir} does not exist. Make sure that you provide correct path. Exiting...')
        exit(0)

    return args
