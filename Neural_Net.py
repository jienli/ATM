import numpy as np

import Constants as CONSTANT

class NeuralNetwork():

    def __init__(self, structure=[3,1]):
        self.structure = structure
        self.depth = len(structure)  # How many layers in the neural network
        # np.random.seed(5423)
        # print(structure)
        self.synaptic_weights = []
        for layer in range(self.depth - 1):
            # print(self.structure[layer])
            # self.synaptic_weights.append(2 * np.random.random((self.structure[layer], self.structure[layer + 1])) + CONSTANT.BIAS)
            self.synaptic_weights.append([])
        self.randomize_synaptic_weights()
    
    def randomize_synaptic_weights(self):
        for layer in range(self.depth - 1):
            self.synaptic_weights[layer] = 2 * np.random.random((self.structure[layer], self.structure[layer + 1])) + CONSTANT.BIAS
        return 0

    def activation_function(self, x, type, deriv=False):
        if (type == 1): #sigmoid
            if (deriv):
                return x * (1 - x)
            return 1 / (1 + np.exp(-x))

        # Default is Sigmoid
        if (deriv):
            return x * (1 - x)
        return 1 / (1 + np.exp(-x))


    def train(self, training_inputs, training_outputs, training_iterations, num_of_starting_points):
        layer = []
        error = []
        delta = []
        for i in range(self.depth):
            layer.append([])
            error.append([])
            delta.append([])
        
        best_error = np.inf
        best_synaptic_weights = []
        
        for starting_point_i in range(num_of_starting_points):

            when_to_print = 1
            self.randomize_synaptic_weights()

            for iteration in range(training_iterations):
                ################################
                # Layers Calculation (Think)
                ################################
                training_inputs = training_inputs.astype(float)
                layer[0] = training_inputs
                for i in range(1, self.depth):
                    layer[i] = self.activation_function(x=np.dot(layer[i - 1], self.synaptic_weights[i - 1]), type=1)


                ################################
                # Back Propagation
                ################################

                # output = self.think(training_inputs)

                error[self.depth - 1] = training_outputs - layer[self.depth - 1]
                delta[self.depth - 1] = error[self.depth - 1] * self.activation_function(x=layer[self.depth - 1], type=1, deriv=True)
                # adjustments = np.dot(training_inputs.T, error * self.activation_function(x=output, type=1, deriv=True))
                for i in range(self.depth - 2, 0, -1):
                    error[i] = delta[i + 1].dot(self.synaptic_weights[i].T)
                    delta[i] = error[i]*self.activation_function(x=layer[i], type=1, deriv=True)

                #print error change
                if ((iteration+1) % when_to_print == 0):
                    print("After ", when_to_print, "th Iteration, Error:" + str(np.mean(np.abs(error[self.depth - 1]))))
                    when_to_print = when_to_print * 10


                ################################
                # Gradient Descent
                ################################
                # self.synaptic_weights[0] += adjustments
                for i in range(0, self.depth - 1):
                    self.synaptic_weights[i] += layer[i].T.dot(delta[i + 1]) * CONSTANT.DRUNKNESS_INDEX
            
            print()
            if (np.mean(np.abs(error[self.depth - 1])) < best_error):
                best_error = np.mean(np.abs(error[self.depth - 1]))
                best_synaptic_weights = self.synaptic_weights
        
        self.synaptic_weights = best_synaptic_weights



    def think(self, inputs):
        layer = []
        for i in range(self.depth):
            layer.append([])
        inputs = inputs.astype(float)
        layer[0] = inputs
        for i in range(1, self.depth):
            layer[i] = self.activation_function(x=np.dot(layer[i - 1], self.synaptic_weights[i - 1]), type=1)

        # return layer[self.depth - 1]
        return layer

        # inputs = inputs.astype(float)
        # output = self.activation_function(x=np.dot(inputs, self.synaptic_weights[0]), type=1)
        # return output



if __name__ == "__main__":
    np.set_printoptions(suppress=True)
    # neural_network = NeuralNetwork(structure=[7,7,1])

    # print("Random synaptic weights: ")
    # print(neural_network.synaptic_weights)

    # ------------------------Sample Input 1-------------------------------
    # training_inputs = np.array([[0,0,1],
    #                            [1,1,1],
    #                            [1,0,1],
    #                            [0,1,1]])
    #
    # training_outputs = np.array([[0,1,1,0]]).T  # Transpose to 4 by 1 matrix
    #----------------------------------------------------------------------


    # ------------------------Sample Input 2-------------------------------
    # #100 phony data points (not working)
    # training_inputs = np.float32(np.random.rand(2, 100))
    #
    # training_outputs = np.dot([0.1, 0.2], training_inputs) + 0.3
    #----------------------------------------------------------------------

    # ------------------------Sample Input & Output 3-------------------------------
    #####  The artificail pattern if if the last number > 5 then output 1, if not then 0

    neural_network = NeuralNetwork(structure=[7,7,7,1])

    print("Starting synaptic weights(random): ")
    print(neural_network.synaptic_weights)

    training_inputs = np.array([[0,0,1,2,3,1,2],
                               [1,1,1,31,2,3,1],
                               [1,0,1,3,21,3,1],
                               [0,3,1,3,2,14,17],
                               [2,1,1,3,22,4,4],
                               [0,4,1,3,2,5,1],
                               [2,6,1,2,5,1,2]])
    training_outputs = np.array([[0,0,0,1,0,0,0]]).T  # Transpose to 4 by 1 matrix

    neural_network.train(training_inputs, training_outputs, 10000, num_of_starting_points= 10)

    print("Final synaptic wieghts(after training): ")
    print(neural_network.synaptic_weights)

    print("New situation: input data = 0,0,0,0,0,0,10")
    print("Output data: ")
    predictionMatrix = neural_network.think(np.array([0,0,0,0,0,0,10]))
    print(predictionMatrix)
    print("prediction is: ", float(predictionMatrix[len(predictionMatrix) - 1]))
    # ----------------------------------------------------------------------
