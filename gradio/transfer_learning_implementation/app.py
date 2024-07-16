import gradio as gr
import numpy as np
import tensorflow as tf
import requests
import cv2

inception_net = tf.keras.applications.InceptionV3()
mobile_net = tf.keras.applications.MobileNetV2()

response = requests.get("https://git.io/JJkYN")
labels = response.text.split("\n")

def classify_image_with_mobile_net(im):
    im = cv2.resize(im, (224, 224))
    arr = np.array(im).reshape((-1, 224, 224, 3))
    arr = tf.keras.applications.mobilenet.preprocess_input(arr)
    prediction = mobile_net.predict(arr).flatten()
    return {labels[i]: float(prediction[i]) for i in range(1000)}

def classify_image_with_inception_net(im):
    im = cv2.resize(im, (299, 299))
    arr = np.array(im).reshape((-1, 299, 299, 3))
    arr = tf.keras.applications.inception_v3.preprocess_input(arr)
    prediction = inception_net.predict(arr).flatten()
    return {labels[i]: float(prediction[i]) for i in range(1000)}

def classify_image_with_both(im):
    mobile_net_result = classify_image_with_mobile_net(im)
    inception_net_result = classify_image_with_inception_net(im)
    return mobile_net_result, inception_net_result

image = gr.Image(type="numpy", label="Input Image")
label_mobile_net = gr.Label(num_top_classes=3, label="MobileNet Predictions")
label_inception_net = gr.Label(num_top_classes=3, label="InceptionNet Predictions")

examples = [
    ["bird.jpg"],
    ["cat.jpg"],
    ["fox.jpg"],
    ["lion.jpg"],
    ["monkey.jpg"]
]

gr.Interface(
    fn=classify_image_with_both,
    inputs=image,
    outputs=[label_mobile_net, label_inception_net],
    title="MobileNet vs. InceptionNet",
    description="Compare MobileNetV2 and InceptionNetV3 models performance in terms of accuracy.",
    examples=examples
).launch()