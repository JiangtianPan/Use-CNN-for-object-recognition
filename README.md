# Use-CNN-for-objection-recognition
Use CNN for objection recognition, this is the final project of Computer Vision course
1.	Introduction
Task: 		By using image processing approach combining with Principal Component Analysis and Convolutional Neural Network, we can train a model to recognize objects shown in images.
Environment: 	Python 3.6
Dataset: 	PascalVOC Dataset[1]
Library: 	tensorflow[2], keras[3]
Files: xml_read.py – used to read xml files from ‘annotations’
load_dataset.py – used to load data with function in xml_read.py and save them as training and test sets.
CNN_model.py – build the CNN model and transform the sets in load_dataset.py into array that can be used in CNN.
final_project.py – integrate all files and run CNN model, recording the history to ‘save.txt’ and show the relevant results.
Notice: Training and test images are under the folder ‘./test’shown in xml_read.py.

2.	Main Procedure
1.	Dataset Loading 
The PascalVOC dataset is combined with the image dataset and the information of each image is in those xml document. Hence, we need to write a program to read information from xml document. 

2.	Image Processing
Firstly, we segment all objects of images, for example, if there are two objects in one image, we segment them and put them as two images into the Training set. We can segment them based on the shape information of each image. Hence, we can obtain the bounding box of each object in the images. The consequence are like this:
Then, we need to reshape all the segmented objects into same size. Thus, we can guarantee the input matrix of each image has the same dimension. There are two approaches to reshape them. One is to scale a pair of parallel sides the same as the other pair and obtain a square image. The other approach is to fill black pixel into it and we can also obtain a square image. In our project, we choose the second one because the second approach can guarantee the original character of objects. 
Besides that, we need to scale the square images into 64*64 pixels. Hence, the input of all the training images are the same dimension.  

3.	Principal Component Analysis
1.	After that we choose to use PCA approach to obtain the principle component of the features in each image. Each image matrix which is obtained from step 2.3 is transferred into one column (a 4096*1 matrix). Then, all the matrix of images in one label can be arranged into one 4096*N matrix, in which N stands for the number of images in that label set.  
2.	We can obtain the sample mean value of each column of the matrix and then let all values in that column minus the sample mean value. Hence, we can obtain a new matrix of each label set.
3.	Then we can obtain the sample covariance matrix, eigenvalue and eigenvector by using functions “Covariance = cov(.)” and “[Eigenvalue, eigenvector] = eig(.)”
4.	We sort the eigenvectors according to their eigenvalues from large to small. Then, choose the largest k rows to form a new matrix P, in which, the number of k is the dimension we choose to reduce from the original sample matrix. Then, we can obtain the dimension-reduced matrix by using matrix P to multiply the matrix which is obtained from each row of the sample character matrix subtracting the sample mean value. After obtaining the dimension-reduced matrix, we can normalize it to set it into [0,1].  
5.	Finally, we can restore the 4096*N matrix back to N image matrix and each matrix contains 64*64 pixels, which is the feature we obtained from this label set.

4.	Training-Testing Data Separation
In this process, we choose the Training set as 3000 images, as a percentage of 0.8. And the rest 0.2 are set as Test set. Besides that, images in both the Training set and the Test set are all labeled. All the label information is read from the xml documents.

5.	CNN Construction
Here, we construct a Convolutional Neural Network to train a model to recognize objections. The structure of our Convolutional Neural Network model is shown below:
Here, our Convolutional Neural Network contains 3 convolutional layers, 3 maxpooling layers, 2 dense layers, 1 flatten layer and 2 dropout layer. In the construction of  Convolutional Neural Network, one convolutional layer is always followed by a maxpooling layer or a sigmoid function layer. And the dense layers are always set after a flatten layer.
Convolutional Layer: By using the convolutional operation, the image features can be enhanced, and noises can be reduced as well.
Maxpooling Layer: The output of Maxpooling cell is the max number of sampled window.
Dense Layer: Dense Layer is a fully connected layer and always be used after Flatten Layer.
Flatten Layer: This layer is set to skip some connections in the network for avoiding the loss of useful information and inhibiting the creation of extra noise. Hence, this layer can used to increase the generalization and avoid the overfitting. 
Dropout Layer: The function of this layer is to drop out some weights in the network. Similarly, it can also be used to avoid the overfitting. Meanwhile, it can also reduce the amount of calculation. 

6.	Data Training
We divide the data to three part:
Training data:
1.	Read all xml files in ‘annotations’ folder and find all ‘object’ element.
			Choice 1
a.	Cut the image in ‘JPEGImage’ folder with the same filename of xml file with the ‘bndbox’ element under ‘object ’ element. Note: RGB image recommend, gray-scale image is less precise in test.
b.	Every ‘object’ has a ‘name’ as a label and an Image as a training datum
c.	Transfer all images as training data X_train and all labels as training label Y_train.
		Choice 2
a.	Use the whole image instead of the segmentation, saved as X_train.
b.	Every ‘object’ has many ‘name’s as labels of the images. Saved the label list as Y_train.
Validation set: 
Fraction of the training data to be used as validation data. The model will set apart this fraction of the training data, will not train on it, and will evaluate the loss and any model metrics on this data at the end of each epoch. The validation data is selected from the last samples in the x and y data provided, before shuffling. We generally choose it as 0.1.
Test data: 
1.	Read images from ‘JPEGImage’ folder (This time no segmentation, although we take it as an comparison experiment)
2.	Many images have multi-labels, so Y_test is a list of list. The np.to_categorical cannot be applied here. We write a ‘my_to_categorical’ instead (in CNN_model).
3.	Whole images are saved as X_test (also 3 channels)
	
7, 	Model Evaluation
Finally, we use the function to evaluate our model. The parameters that that can reflect out model are accurate rate, loss rate and the average classification rate. And the result of it can be seen as the next part.
