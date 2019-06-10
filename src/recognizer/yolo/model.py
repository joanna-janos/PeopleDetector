import cv2


class YOLOModel:
    def __init__(self, path_to_yolo_config):
        yolo_config_path = path_to_yolo_config + 'yolov3.cfg'
        yolo_weights_path = path_to_yolo_config + 'yolov3.weights'
        self.yolo_classes_path = path_to_yolo_config + 'yolov3.txt'
        self.model = cv2.dnn.readNetFromDarknet(yolo_config_path, yolo_weights_path)
        self.model_input_width = 448
        self.model_input_height = 448

    def get_output_layer_names(self):
        """YOLO3 has more than one output layer giving the prediction, it returns all of them

        Returns
        -------
        List[str]
                output layer names
        """
        names = self.model.getLayerNames()
        return [names[unconnected_out_layer[0] - 1] for unconnected_out_layer in self.model.getUnconnectedOutLayers()]

    def get_classes_to_recognize_by_model(self):
        """Get all classes possible to recognize by yolo model.

        Returns
        -------
        List[str]
                classes possible to recognize by yolo model
        """
        classes = []
        with open(self.yolo_classes_path, 'r') as f:
            for line in f:
                classes.append(line.rstrip('\n'))
        return classes

    def get_model(self):
        """Get pretrained yolo model.

        Returns
        -------
        model
                pretrained yolo model
        """
        return self.model

    def get_input_width(self):
        """Get input width of model.

        Returns
        -------
        int
                input width
        """
        return self.model_input_width

    def get_input_height(self):
        """Get input height of model.

        Returns
        -------
        int
                input height
        """
        return self.model_input_height
