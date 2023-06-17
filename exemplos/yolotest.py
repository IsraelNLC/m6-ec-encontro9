from roboflow import Roboflow
rf = Roboflow(api_key="81lbF5HnsWKEGsEq3A12")
project = rf.workspace().project("face-detection-mik1i")
model = project.version(18).model

# infer on a local image
# print(model.predict("./received/siu1686775681.6702244.png", confidence=40, overlap=30).json())

# visualize your prediction
model.predict("./received/siu1686775681.6702244.png", confidence=40, overlap=30).save("prediction.jpg")

# infer on an image hosted elsewhere
# print(model.predict("URL_OF_YOUR_IMAGE", hosted=True, confidence=40, overlap=30).json())