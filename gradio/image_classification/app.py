import gradio as gr
import numpy as np
import tensorflow as tf
import requests
import keras
import cv2

inception_net = keras.applications.InceptionV3()

response = requests.get("https://git.io/JJkYN")
labels = response.text.split("\n")

def classify_image(input):
    input = cv2.resize(input,(299,299))
    input = input.reshape((-1,299,299,3))
    input = keras.applications.inception_v3.preprocess_input(input)
    prediction = inception_net.predict(input).flatten()
    return {labels[i]:float(prediction[i]) for i in range(1000)}

image = gr.Image()
label = gr.Label(num_top_classes=3)

gr.Interface(fn=classify_image,
             inputs=image,
             outputs=label,
             examples=["bird.jpg", "cat.jpg"]).launch()