from utils import user_input, data

from people_recognizer import PeopleRecognizer

if __name__ == "__main__":
    args = user_input.parse_arguments()
    if not args.filenames:
        filenames = data.get_data_filenames(args.data_dir)
    else:
        filenames = args.filenames.split(",")

    people_recognizer = PeopleRecognizer(args.yolo_config_path)
    people_recognizer.recognize(filenames, args.data_dir, args.results_dir)
