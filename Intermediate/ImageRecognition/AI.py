import numpy
from tensorflow.keras import datasets, models
import matplotlib.pyplot as mpl
import cv2 as cv

uInput = str(input('make sure you trained the ai first! and also make sure the image is 32x32\nEnter name of image eg: horse.jpg: '))

(training_image, training_label), (testing_image, testing_label) = datasets.cifar10.load_data()
training_image, testing_image = training_image / 255, testing_image / 255

classSet = ['Plane', 'Car', 'Bird', 'Cat', 'Deer', 'Dog', 'Frog', 'Horse', 'Ship', 'Truck']

training_image = training_image[:20000]
training_label = training_label[:20000]
testing_image = testing_image[:20000]
testing_label = testing_label[:20000]

nn = models.load_model('NeuralNetwork')
image = cv.imread(uInput)
image = cv.cvtColor(image, cv.COLOR_BGR2BRGB)
mpl.imshow(image, cmap=mpl.cm.binary)

predict = nn.predict(numpy.array([image]) / 255)
index = numpy.argmax(predict)
print(f'This image is a {classSet[index]}')
