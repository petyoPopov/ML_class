import numpy as np
from sklearn.svm import LinearSVC


### Functions for you to fill in ###

def one_vs_rest_svm(train_x, train_y, test_x):
    """
    Trains a linear SVM for binary classifciation

    Args:
        train_x - (n, d) NumPy array (n datapoints each with d features)
        train_y - (n, ) NumPy array containing the labels (0 or 1) for each training data point
        test_x - (m, d) NumPy array (m datapoints each with d features)
    Returns:
        pred_test_y - (m,) NumPy array containing the labels (0 or 1) for each test data point
    """
    
    #C - penalty parameter
    #random_state=1 sets the seed for the random num generator
    lin_clf = LinearSVC(random_state=0 , C=0.1)
    lin_clf.fit(train_x,train_y)
    test_y_predict = lin_clf.predict(test_x)
        
    try:
        return test_y_predict
    except:
        raise NotImplementedError


def multi_class_svm(train_x, train_y, test_x):
    """
    Trains a linear SVM for multiclass classifciation using a one-vs-rest strategy

    Args:
        train_x - (n, d) NumPy array (n datapoints each with d features)
        train_y - (n, ) NumPy array containing the labels (int) for each training data point
        test_x - (m, d) NumPy array (m datapoints each with d features)
    Returns:
        pred_test_y - (m,) NumPy array containing the labels (int) for each test data point
    """
    lin_clf = LinearSVC(random_state=0 , C=0.1)
    lin_clf.fit(train_x,train_y)
    test_y_predict = lin_clf.predict(test_x)
        
    try:
        return test_y_predict
    except:
        raise NotImplementedError


def compute_test_error_svm(test_y, pred_test_y):
    t_error = 1 - np.mean(test_y == pred_test_y)
    try:
        return t_error
    except:
        raise NotImplementedError
