import cv2
import numpy as np


def get_box_dimensions(result, img_height, img_width):
    """Get dimensions of box for drawing purposes.

    Parameters
    ----------
    result : box
    img_height : height of image
    img_width : width of image

    Returns
    -------
    List[int]
            Box dimensions on image
    """
    width = result[2] * img_width
    height = result[3] * img_height
    left = result[0] * img_width - (width // 2)
    top = result[1] * img_height - (height // 2)
    return [int(left),
            int(top),
            int(width),
            int(height)]


def get_boxes_and_scores_for_people_on_image(model, img, score_threshold=0.5):
    """Get boxes dimensions on image and corresponding score (implicates "How sure is model that on image is a person?)."

    Parameters
    ----------
    model : yolo model
    img : image provided for people recognition
    score_threshold : how sure should be model -  if score is above this value, person is recognized

    Returns
    -------
    Tuple(List[List[int]], List[float])
            Boxes where person is recognized with corresponding score
    """
    boxes = []
    scores = []
    classes_recognized_by_model = model.get_classes_to_recognize_by_model()
    output_layer_names = model.get_output_layer_names()
    for output in model.get_model().forward(output_layer_names):
        for result in output:
            measurements = len(result) - len(classes_recognized_by_model)
            recognized_class_id = np.argmax(result[measurements:])
            score = result[measurements + recognized_class_id]
            if score > score_threshold and classes_recognized_by_model[recognized_class_id] == 'person':
                scores.append(float(score))
                boxes.append(
                    get_box_dimensions(result, img.shape[0], img.shape[1])
                )
    return boxes, scores


def draw_boxes_on_img(img, boxes, scores, score_threshold=0.5):
    """Draw boxes on image where object where recognized.

    Parameters
    ----------
    img : image provided for object recognition
    boxes : boxes dimensions where object are recognized
    scores : scores for people recognition (should be corresponding to boxes)
    score_threshold : how sure should be model -  if score is above this value, person is recognized

    Returns
    -------
    image
            Image with drawn boxes where object were recognized
    """
    for i in cv2.dnn.NMSBoxes(boxes, scores, score_threshold, 0.4):
        box = boxes[i[0]]
        cv2.rectangle(img,
                      (box[0], box[1]),
                      (box[0] + box[2], box[1] + box[3]),
                      (0, 0, 255))
    return img
