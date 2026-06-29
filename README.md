# Neural Network From Scratch Using Python and NumPy

## Project Overview

This project implements a fully connected feedforward neural network from scratch using only Python and NumPy. The objective of this project was to gain a fundamental understanding of how neural networks learn through forward propagation, backpropagation, and stochastic gradient descent, without relying on high-level deep learning frameworks.

The network was trained on the MNIST handwritten digit dataset and achieves strong classification performance using a simple architecture consisting of an input layer, one hidden layer, and an output layer.

---

## Objectives

* Understand the mathematical foundations of neural networks
* Implement forward propagation from scratch
* Implement the backpropagation algorithm manually
* Apply mini-batch stochastic gradient descent (SGD)
* Train and evaluate a neural network on the MNIST dataset
* Gain practical experience with the core concepts underlying modern deep learning systems

---

## Features

* Fully connected feedforward neural network
* Random initialization of weights and biases
* Sigmoid activation function
* Manual implementation of backpropagation
* Mini-batch stochastic gradient descent
* MNIST handwritten digit classification
* Performance evaluation on test data
* Implemented entirely using Python and NumPy

---

## Project Structure

```text
.
├── network.py          # Neural network implementation
├── mnist_loader.py     # MNIST data loading and preprocessing
├── README.md
├── requirements.txt
└── fig/                # Project figures and illustrations
```

---

## Neural Network Architecture

The implemented neural network follows the architecture:

```text
Input Layer (784 neurons)
            ↓
Hidden Layer (30 neurons)
            ↓
Output Layer (10 neurons)
```

Where:

* 784 neurons correspond to the 28×28 pixel values of an MNIST image
* 30 neurons form the hidden layer
* 10 output neurons represent the digits 0–9

---

## Learning Algorithm

The model learns using:

### Forward Propagation

Computes activations layer by layer through the network.

### Cost Function

Calculates prediction error between actual and expected outputs.

### Backpropagation

Computes gradients of the cost function with respect to network parameters.

### Stochastic Gradient Descent (SGD)

Updates weights and biases using mini-batches to minimize prediction error.

---

## Technologies Used

* Python 3
* NumPy

---

## Dataset

The network is trained using the MNIST handwritten digit dataset, consisting of:

* 60,000 training images
* 10,000 test images
* Grayscale images of size 28×28 pixels

---

## Results

The neural network successfully learns to classify handwritten digits and demonstrates how gradient-based optimization enables neural networks to improve their predictions over multiple training epochs.

Example training output:

```text
Epoch 0: 9124 / 10000
Epoch 1: 9298 / 10000
...
Epoch 29: 9550 / 10000
```

---

## Key Concepts Explored

* Artificial Neural Networks
* Feedforward Networks
* Activation Functions
* Gradient Descent
* Stochastic Gradient Descent
* Backpropagation
* Cost Functions
* Weight Optimization
* Supervised Learning
* Deep Learning Fundamentals

---

## Motivation

This project was developed as a hands-on implementation to understand the mathematical and computational foundations of deep learning. Rather than relying on high-level libraries such as TensorFlow or PyTorch, the entire learning process was implemented manually to gain a deeper understanding of how neural networks function internally.

---

## Future Improvements

* Implement ReLU activation functions
* Add Cross-Entropy Loss
* Implement Adam optimization
* Build deeper neural network architectures
* Reimplement the model using PyTorch
* Extend the project toward transformer architectures and modern generative AI systems

```
```
