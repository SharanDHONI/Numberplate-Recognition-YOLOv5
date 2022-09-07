# Numberplate-Recognition-YOLOv5

Collected around 2000 images of Vehicles and Annotated the Vehicles and their Numberplates using the LabelIMG.
Trained the images using the YOLOv5L and this public repo consists of the samples of the data of which I tested the model.

The next step would be to crop the numberplates alone and extract the text out of them. This can be made with libraries like Easy OCR or PyTesseract 
Once text is extracted, we can compare that with the list of numberplates that are allowed inside a particular place

We can also compress the NMS to a minimum threshold and therby reducing the clutter during the runtime! 

## You can find more images / Outputs in the "Results" Directory

In the below image, you can see that the model was able to identify the type of vehicle as well as the Numberplate.
![red](https://user-images.githubusercontent.com/20862520/147906666-4aa7f3c0-abc7-4bde-a773-404685f390f7.jpg)
![red](https://user-images.githubusercontent.com/20862520/147911514-262d3cca-8f0c-4a6e-981b-344904a2739b.jpg)


Here, the Numberplate alone has been cropped seperately and will be passed to a function that can extract text out of the image. Eg, pyTesseract, TesserOCR etc.



Below are some more examples !


![share](https://user-images.githubusercontent.com/20862520/149266907-0d5cc005-4ee5-4103-b003-91c6fd01db02.jpg)
![share](https://user-images.githubusercontent.com/20862520/149266920-741c5569-29b9-496c-9f4a-5c3760da6930.jpg)
![share](https://user-images.githubusercontent.com/20862520/149266934-486f56ce-fe9c-4f8b-b556-40276a2d2a92.jpg)










