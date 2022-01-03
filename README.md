# Numberplate-Recognition-YOLOv5

Collected around 2000 images of Vehicles (Imbalanced mix of classes. Cars were more in number) and Annotated the Vehicles and their Numberplates using LabelIMG.
Trained the images using the YOLOv5s (for only 10 epochs because of hardware constraints) and this public repo consists of the samples of the data of which I tested the model.
The Accuracy isn't that great, but the point being, the model has done pretty decently well with the unbalanced mix of data. 

The next step would be to crop the numberplates alone and extract the text out of them. This can be made with libraries like Easy OCR or PyTesseract 
Once text is extracted, we can compare that with the list of numberplates that are allowed inside a particular place



