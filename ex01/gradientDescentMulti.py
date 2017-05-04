import numpy as np
import computeCostMulti as ccm

def gradientDescentMulti(X, y, theta, alpha, num_iters):
#GRADIENTDESCENTMULTI Performs gradient descent to learn theta
#   theta = GRADIENTDESCENTMULTI(x, y, theta, alpha, num_iters) updates theta by
#   taking num_iters gradient steps with learning rate alpha

# Initialize some useful values
    m = len(y) # number of training examples
    J_history = np.zeros((num_iters, 1))
    
    for iter in range(num_iters):
    # ====================== YOUR CODE HERE ======================
    # Instructions: Perform a single gradient step on the parameter vector
    #               theta. 
    #
    # Hint: While debugging, it can be useful to print out the values
    #       of the cost function (computeCostMulti) and gradient here.
        S = (np.dot(X, theta).transpose() - y)
        for j in range(X.shape[1]):  
            theta[j] = theta[j] - (alpha / m) * np.sum(S * X[:, j])
    # ============================================================
    # Save the cost J in every iteration    
        J_history[iter] = ccm.computeCostMulti(X, y, theta)
        
    return theta, J_history