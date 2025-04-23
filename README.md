# OR Gate Perceptron 🔌🧠

This project implements a simple **Perceptron** model to learn the behavior of the **OR logic gate** using Python and NumPy. It demonstrates the basics of binary classification using one of the simplest types of artificial neural networks.

---

## 🧪 Dataset

We use the standard truth table for the OR gate:

| Input 1 | Input 2 | Output |
|---------|---------|--------|
|    0    |    0    |   0    |
|    0    |    1    |   1    |
|    1    |    0    |   1    |
|    1    |    1    |   1    |

---

## 🔧 Model

The model is a **single-layer Perceptron** trained using:

- Learning rate: 0.1  
- Number of iterations: 3  
- Activation function: Step function

During training, weights and bias are updated according to the Perceptron learning rule.

---

## 📈 Output

After training, the model correctly predicts the output for each input:

pre: [0 1 1 1]


This confirms that the Perceptron has successfully learned the OR logic.

---




