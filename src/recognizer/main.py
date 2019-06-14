from people_recognizer import PeopleRecognizer
from utils import user_input, data

if __name__ == "__main__":
    args = user_input.parse_arguments()
    if not args.filenames:
        filenames = data.get_filenames(args.data_dir)
    else:
        filenames = [f.strip() for f in args.filenames.split(",")]

    people_recognizer = PeopleRecognizer(args.yolo_config_path)
    people_recognizer.recognize(filenames, args.data_dir, args.results_dir)
