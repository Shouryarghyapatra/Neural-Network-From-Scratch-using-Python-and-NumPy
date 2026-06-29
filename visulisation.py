import matplotlib.pyplot as plt
import mnist_loader

training_data, _, _ = mnist_loader.load_data()

image = training_data[0][0].reshape(28,28)

plt.imshow(image, cmap='gray')
plt.show()
