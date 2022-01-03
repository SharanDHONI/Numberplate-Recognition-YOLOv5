# Numberplate-Recognition-YOLOv5

Collected around 2000 images of Vehicles (Imbalanced mix of classes. Cars were more in number) and Annotated the Vehicles and their Numberplates using LabelIMG.
Trained the images using the YOLOv5s (for only 10 epochs because of hardware constraints) and this public repo consists of the samples of the data of which I tested the model.
The Accuracy isn't that great, but the point being, the model has done pretty decently well with the unbalanced mix of data. 

The next step would be to crop the numberplates alone and extract the text out of them. This can be made with libraries like Easy OCR or PyTesseract 
Once text is extracted, we can compare that with the list of numberplates that are allowed inside a particular place

We can also compress the NMS to a minimum threshold and therby reducing the clutter during the runtime! 


In the below image, you can see that the model was able to identify the type of vehicle as well as the Numberplate.
![red](https://user-images.githubusercontent.com/20862520/147906666-4aa7f3c0-abc7-4bde-a773-404685f390f7.jpg)

Here, the Numberplate alone has been cropped seperately and will be passed to a function that can extract text out of the image. Eg, pyTesseract, TesserOCR etc.
![red](https://user-images.githubusercontent.com/20862520/147911514-262d3cca-8f0c-4a6e-981b-344904a2739b.jpg)







