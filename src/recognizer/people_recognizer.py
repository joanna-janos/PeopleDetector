import cv2
from utils import box

from yolo.model import YOLOModel


class PeopleRecognizer:
    """People recognizer for images"""

    def __init__(self, path_to_yolo_config):
        self.yolo = YOLOModel(path_to_yolo_config)
        self.yolo_model = self.yolo.get_model()
        self.input_width = self.yolo.get_input_width()
        self.input_height = self.yolo.get_input_height()

    def recognize(
            self, filenames, path_to_data, path_to_results
    ):
        """Recognize people on images.

        Parameters
        ----------
        filenames : filenames for people recognition
        path_to_data : path to data directory
        path_to_results : path to result directory
        """

        for filename in filenames:
            img = cv2.imread(path_to_data + filename)
            resized_img = cv2.resize(img, (self.yolo.get_input_width(), self.yolo.get_input_height()))
            blob = cv2.dnn.blobFromImage(resized_img, 1 / 255,
                                         (self.yolo.get_input_width(), self.yolo.get_input_height()),
                                         [0, 0, 0], 1, crop=False)
            self.yolo_model.setInput(blob)
            boxes, scores = box.get_boxes_and_scores_for_people_on_image(self.yolo, img)
            img_with_boxes_and_scores = box.draw_boxes_on_img(img, boxes, scores)
            cv2.imwrite(path_to_results + filename, img_with_boxes_and_scores)
