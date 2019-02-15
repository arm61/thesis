import numpy as np


def gradient_descent(init_x1, init_x2, dfx1, dfx2, alpha, threshold):
    """
    Applied the gradient descent method to a given two-dimensional
    function, the derivatives of which are dfx and dfy.

    Parameters
    ----------
    init_x1: float
        Initial value for x1.
    init_x2: float
        Initial value for x2.
    dfx1: function
        Derivative of function with respect to x1.
    dfx2: function
        Derivative of function with respect to x2.
    alpha: float
        Step-size for gradient descent steps.
    threshold: float
        The gradient at which fitting stops.

    Returns
    -------
    float, array_like
        The history of the parameters being fit. An array of
        shape m, n, where n is the number of iterations and 
        m is the number of parameters.
    """
    history = np.array([])
    i = 1
    x1 = init_x1
    x2 = init_x2
    while (
        np.abs(dfx1(x1, x2)) > threshold
        and np.abs(dfx2(x1, x2)) > threshold
    ):
        history = np.append(history, np.array([x1, x2]))
        history = np.reshape(history, (i, 2))
        x1 = x1 - alpha * dfx1(x1, x2)
        x2 = x2 - alpha * dfx2(x1, x2)
        i += 1
    return history
