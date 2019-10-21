<h1 align="center"><b><i>People recognizer</i></b></h1>
<p align=center>
    <a><img alt="YOLOv3 model" src="https://img.shields.io/badge/model-YOLOv3-blue"></a>
    <a><img alt="Penn Fudan Database dataset" src="https://img.shields.io/badge/dataset-Penn Fudan Database-blue"></a>
    <a><img alt="Supported img extensions" src="https://img.shields.io/badge/Supported input extensions-png, jpg-blue"></a> <br>
    <a><img alt="Python" src="https://img.shields.io/badge/python-3.7-blue.svg"></a>
    <a><img alt="OpenCV" src="https://img.shields.io/badge/OpenCV-3.4.2-blue.svg"></a>
</p>

<p align=center>
    <a><img alt="Python" src="data/FudanPed00027.png"></a>
    <a><img alt="Python" src="results/FudanPed00027.png"></a>
    <br>
    <i>Image on the left side was an input to recognizer. <br>
    On the right side is result with boxes indicating detected people.</i>
</p>

<h2> ⚙️ Model</h2>

For detection I used pretrained **YOLOv3 model**. It has been trained on COCO dataset with 80 possible classes. In my case, after detecting an object I check if label matches person class as I need only this one.  <br>
More information about YOLOv3 can be found [here](https://pjreddie.com/darknet/yolo/).


<h2> :hammer: Input preprocessing</h2>

Image width and height are scaled to fit dimensions of model input.
Then image is transformed to BLOB<sup>1</sup>.

<h2> :page_facing_up: Dataset</h2>

As a dataset I chose [Penn-Fudan Database for Pedestrian Detection and Segmentation](https://www.cis.upenn.edu/~jshi/ped_html/). \
<cite>"This is an image database containing images that are used for pedestrian detection [...]. The images are taken from scenes around campus and urban street. [...] Each image will have at least one pedestrian in it. [...] All labeled pedestrians are straight up."</cite>

<h2> :interrobang: How does it work?</h2>

You can recognize people on some choosen images or all in selected directory.

1. Prepare data directory with images (only .png and .jpg extensions are supported). \
 Default directory is called `data` and is in the same level as `src` directory.
2. Prepare config for YOLOv3 model (configuration file, model weights and classes to be recognized). \
Default directory is called `config` and is under `yolo` directory.
3. Go to `recognizer` directory and run `python main.py` (there are 4 possible arguments to set: data path, results path, model config path and which files should be pass to recognizer).

If you need any help, run `python main.py --help`

<h2> :sparkles: Results </h2>

1. Recognizer can draw boxes for more than one person on image. Person can stay in shadow or even be turned. For an example input-output you can look at images at the beginning of this README.

2. Sometimes recognizer marks two people as one detected object. <br>

<p align=center>
    <a><img alt="Python" src="data/FudanPed00014.png" width="49%" height="50%"></a>
    <a><img alt="Python" src="results/FudanPed00014.png" width="49%" height="50%"></a>
    <br>
    <i>Input on the left, output on the right side.</i>
</p>

<br><br>


<sup>1</sup> BLOB - Binary Large OBject - <cite>"A Blob is a group of connected pixels in an image that share some common property."</cite>
