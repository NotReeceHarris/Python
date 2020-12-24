from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as mpl

(training_image, training_label), (testing_image, testing_label) = datasets.cifar10.load_data()
training_image, testing_image = training_image / 255, testing_image / 255

classSet = ['Plane', 'Car', 'Bird', 'Cat', 'Deer', 'Dog', 'Frog', 'Horse', 'Ship', 'Truck']

for x in range(16):
    mpl.subplot(4, 4, x + 1)
    mpl.xticks([])
    mpl.yticks([])
    mpl.imshow(training_image[x], cmap=mpl.cm.binary)
    mpl.xlabel(classSet[training_label[x][0]])
mpl.show()

training_image = training_image[:20000]
training_label = training_label[:20000]
testing_image = testing_image[:20000]
testing_label = testing_label[:20000]

nn = models.Sequential() # neural network
nn.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))
nn.add(layers.MaxPooling2D((2, 2)))
nn.add(layers.Conv2D(64, (3, 3), activation='relu'))
nn.add(layers.MaxPooling2D((2, 2)))
nn.add(layers.Conv2D(64, (3, 3), activation='relu'))
nn.add(layers.Flatten)
nn.add(layers.Dense(64, activation='relu'))
nn.add(layers.Dense(10, activation='softmax'))

nn.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

nn.fit(training_image, training_label, epochs=100, validation_data=(testing_image, testing_label))

loss, accuracy = nn.evaluate(testing_image, testing_label)
print(f'loss: {loss}\nAccuracy: {accuracy}, 0.98 = 98%')
nn.save('NeuralNetwork')