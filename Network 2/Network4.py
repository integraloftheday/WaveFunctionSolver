import numpy
import scipy.special
import matplotlib.pyplot
#matplotlib inline
class neuralNetwork: 
    
    def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate):
        self.inodes= inputnodes 
        self.hnodes= hiddennodes
        self.onodes=outputnodes 
        
        self.wih = numpy.random.normal(0.0, pow(self.hnodes, -0.5),(self.hnodes, self.inodes))
        self.who = numpy.random.normal(0.0, pow(self.onodes, -0.5),(self.onodes,self.hnodes))
        
        self.lr=learningrate
        
        
        # sigmoid function 
        self.activation_function= lambda x: scipy.special.expit(x)
        pass
    
    
    def train(self, inputs_list, targets_list):
        inputs= numpy.array(inputs_list, ndmin=2).T # converts list to 2d array 
        targets= numpy.array(targets_list,ndmin=2).T #converts list to 2d array
        #input to hidden layer 
        hidden_inputs= numpy.dot(self.wih, inputs)
        hidden_outputs=self.activation_function(hidden_inputs) # applies activation function to hidden matrix
        #hidden to output 
        final_input=numpy.dot(self.who, hidden_outputs)
        final_outputs=self.activation_function(final_input)
            
        #Error target-actual
        output_errors= targets - final_outputs
        # hidden errors is output errors split by weight
        hidden_errors= numpy.dot(self.who.T, output_errors)
        # backprogrogration update weights between hidden and output layers 
        self.who += self.lr * numpy.dot((output_errors * final_outputs * (1.0-final_outputs)), numpy.transpose(hidden_outputs))
        self.wih += self.lr * numpy.dot((hidden_errors * hidden_outputs * (1.0-hidden_outputs)), numpy.transpose(inputs))
            
        pass
    
    
    def query(self, inputs_list):
        inputs= numpy.array(inputs_list, ndmin=2).T #converts list to 2d array
        #input to hidden layer 
        #print(inputs.shape)
        hidden_inputs= numpy.dot(self.wih, inputs)
        hidden_outputs=self.activation_function(hidden_inputs) # applies activation function to hidden matrix
        #hidden to output 
        final_input=numpy.dot(self.who, hidden_outputs)
        final_outputs=self.activation_function(final_input)
        return final_outputs
        pass
    pass 

input_nodes=50
hidden_nodes=10000
output_nodes=100
    
learning_rate =0.05
    
n = neuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate) # neural network class instance 
    
#open training data
#open training data
training_data_file = open("2LS.csv",'r')
training_data_list = training_data_file.readlines()
training_data_file.close()

#start training 

for record in training_data_list:
    all_values = record.split(',')
    inputs = (numpy.asfarray(all_values[1:]) /1000 * .99) + .01 
    targets=numpy.zeros(output_nodes)+.01 
    #print(targets.shape)
    targets[int(all_values[0])]=0.99
    n.train(inputs, targets)
    pass 
test_data_file=open("2LST.csv",'r')
test_data_list = test_data_file.readlines()
test_data_file.close()

scorecard = []
for record in test_data_list:
    all_values = record.split(',')
    correct_label = int(all_values[0])
    print(correct_label, "correct label")
    inputs = (numpy.asfarray(all_values[1:]) / 1000 * .99) +.01
    outputs = n.query(inputs)
    label = numpy.argmax(outputs)
    print(label, "network's answer")
    if (label== correct_label):
        scorecard.append(1)
    else: 
        scorecard.append(0)
        pass
# fun test what number do i look the most like and 8 
scorecard_array= numpy.asarray(scorecard)
print ("preformance =",scorecard_array.sum()/ scorecard_array.size)
n.query((numpy.asfarray(all_values[1:])/1000.0 *.99)+.01)
