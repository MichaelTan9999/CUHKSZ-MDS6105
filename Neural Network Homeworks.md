### s1. What is a threshold / activation function?

In neural networks, an activation function is the function that describes the output behaviour of a neuron. Most network architectures start by computing the weighted sum of the inputs (that is, the sum of the product of each input with the weight associated with that input. This quantity, the total net input is then usually transformed in some way, using what is sometimes called a squashing function. The simplest squashing function is a step function: if the total net input is less than 0 (or more generally, less than some threshold T) then the output of the neuron is 0, otherwise it is 1. A common squashing function is the logistic function.
In summary, the activation function is the result of applying a squashing function to the total net input.

### 2. What is a logit (coming from logistic)?

In statistics, the logit function is the quantile function associated with the standard logistic distribution. It has many uses in data analysis and machine learning, especially in data transformations.

![](https://upload.wikimedia.org/wikipedia/commons/8/88/Logistic-curve.svg)

$f(x)=\frac{L}{1+e^{-k(x-x_0)}}$, where

$x_0$, the $x$ value of the sigmoid's mid point;

$L$, the curve's maximum value;

$k$, the logistic growth rate or steepness of the curve.

### 3. What is hidden layer?

Neurons or units in a feedforward net are usually structured into two or more layers. The input units constitute the input layer. The output units constitute the output layer. Layers in between the input and output layers (that is, layers that consist of hidden units) are termed hidden layers.
In layered nets, each neuron in a given layer is connected by trainable weights to each neuron in the next layer.

### 4. What is a logistic threshold unit (LTU)?

A logistic threshold unit is a simple artificial neuron whose output is its thresholded total net input. That is, an LTU with threshold T calculates the weighted sum of its inputs, and then outputs 0 if this sum is less than T, and 1 if the sum is greater than T. LTU's form the basis of perceptrons.

### 5. What is a contral / bias unit? Why it is important?

In feedforward and some other neural networks, each hidden unit and each output unit is connected via a trainable weight to a unit (the bias unit) that always has an activation level of –1.
This has the effect of giving each hidden or output a trainable threshold, equal to the value of the weight from the bias unit to the unit.

### 6. What is a feed-forward network?

A kind of neural network in which the nodes can be numbered, in such a way that each node has weighted connections only to nodes with higher numbers. Such nets can be trained using the error backpropagation learning algorithm.
In practice, the nodes of most feedforward nets are partitioned into layers - that is, sets of nodes, and the layers may be numbered in such a way that the nodes in each layer are connected only to nodes in the next layer - that is, the layer with the next higher number. Commonly successive layers are totally interconnected - each node in the earlier layer is connected to every node in the next layer.

The first layer has no input connections, so consists of input units and is termed the input layer (yellow nodes in the diagram below).

The last layer has no output connections, so consists of output units and is termed the output layer (maroon nodes in the diagram below).

The layers in between the input and output layers are termed hidden layers, and consist of hidden units (light blue nodes and brown nodes in the diagram below).

![](http://www.cse.unsw.edu.au/~billw/dictionaries/pix/feedforwardnet.png)

When the net is operating, the activations of non-input neurons are computing using each neuron's activation function.

### 7. What is the target / objective function of the network?

A target function, in machine learning, is a method for solving a problem that an AI algorithm parses its training data to find. Once an algorithm finds its target function, that function can be used to predict results (predictive analysis). The function can then be used to find output data related to inputs for real problems where, unlike training sets, outputs are not included.

### 8. What are input and output of the network?

The input of the network is the variables you feed the network. On the other hand, the output of the network is something you get from the network. At the training stage, the input is the data you have labels and the output is the predicated labels, which will be used for comparing with the true labels and adjusting the model. At the testing or application stage, the input is the data you do not have labels and the output is the predicated labels which the model believe the data belong to the label.

### 9. What is gradient descend optimization algorithm?

When an artificial neural network learning algorithm causes the weights of the net to change, it will do so in such a way that the current point on the error surface will descend into a valley of the error surface, in a direction that corresponds to the steepest (downhill) gradient or slope at the current point on the error surface. For this reason, backprop is said to be a gradient descent method, and to perform gradient descent in weight space.

### 10. What is stochastic gradient descend?

Stochastic gradient descent (often abbreviated SGD) is an iterative method for optimizing an objective function with suitable smoothness properties (e.g. differentiable or subdifferentiable). It can be regarded as a stochastic approximation of gradient descent optimization, since it replaces the actual gradient (calculated from the entire data set) by an estimate thereof (calculated from a randomly selected subset of the data). Especially in high-dimensional optimization problems this reduces the computational burden, achieving faster iterations in trade for a lower convergence rate.

### 11. What are the important optimization tricks in deep neural networks, such as drop-out, simlified threshold function, normalization?

#### Data Augmentation

Deep learning models usually need a lot of data to be properly trained. It is often useful to get more data from the existing ones using data augmentation techniques. The main ones are flip, rotation, random crop, color shift, noise addition, information loss, and contrast change.

#### Batch normalization

It is a step of hyperparameter $\gamma,\beta$ that normalizes the batch ${x_i}$. By noting $\mu_B,\sigma_B^2$ the mean and variance of that we want to correct to the batch, it is done as follows:

$x_i\leftarrow\gamma\frac{x_i-\mu_B}{\sqrt{\sigma_B^2+\epsilon}}+\beta$

It is usually done after a fully connected/convolutional layer and before a non-linearity layer and aims at allowing higher learning rates and reducing the strong dependence on initialization.

#### Dropout

Dropout is a technique used in neural networks to prevent overfitting the training data by dropping out neurons with probability $p>0$. It forces the model to avoid relying too much on particular sets of features.

![](https://stanford.edu/~shervine/teaching/cs-230/illustrations/dropout-ltr.png?27ab877c24a915d22e598fb772fcdc96)

#### Adaptive learning rates

Letting the learning rate vary when training a model can reduce the training time and improve the numerical optimal solution. While Adam optimizer is the most commonly used technique, others can also be useful. They are Momentum, RMSprop, etc.

#### Early stopping

This regularization technique stops the training process as soon as the validation loss reaches a plateau or starts to increase.

![](https://stanford.edu/~shervine/teaching/cs-230/illustrations/early-stopping-en.png?a8aacdfe0c39776d86764857222e19dd)

### 12. What is a convolution?

In mathematics (in particular, functional analysis), convolution is a mathematical operation on two functions ($f$ and $g$) that produces a third function ($f\times g$) that expresses how the shape of one is modified by the other. The term convolution refers to both the result function and to the process of computing it. It is defined as the integral of the product of the two functions after one is reversed and shifted. The integral is evaluated for all values of shift, producing the convolution function.

In image processing, a kernel, convolution matrix, or mask is a small matrix used for blurring, sharpening, embossing, edge detection, and more. This is accomplished by doing a convolution between the kernel and an image.