import cv2
import numpy as np

# Load YOLO
net = cv2.dnn.readNet("D:\\ObjectDetection\\yolov3.weights", "D:\\ObjectDetection\\yolov3.cfg")# path to the weights and cfg file
layer_names = net.getLayerNames()#get the names of the layers
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]#get the output layers

# Load image
image = cv2.imread("D:\\ObjectDetection\\RubbishPhoto\\rubbishOnSand.jpeg")#path to the image
height, width, channels = image.shape#get the image details

# Preprocess image
blob = cv2.dnn.blobFromImage(image, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
net.setInput(blob)#set the input of the network
outs = net.forward(output_layers)#get the output of the network

# Process detections
for out in outs:
    for detection in out:
        scores = detection[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]
        if confidence > 0.5:#if the confidence is greater than 0.5, then we consider it as a valid detection!
            # Object detected
            center_x = int(detection[0] * width)
            center_y = int(detection[1] * height)
            w = int(detection[2] * width)
            h = int(detection[3] * height)

            # Draw bounding box around the object -> show that we detected the object!
            cv2.rectangle(image, (center_x - w // 2, center_y - h // 2), (center_x + w // 2, center_y + h // 2), (255, 0, 0), 2)

# Display the result
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()