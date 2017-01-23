# Krzysztof Joachimiak 2017
# sciquence: Time series & sequences in Python
#
# Functions for sequence processing
# Author: Krzysztof Joachimiak
#
# License: MIT

import numpy as np
from itertools import groupby

############## Getting sequences ##############

def seq(array):
    '''

    Cut input array into sequences consisting of the same elements

    Parameters
    ----------
    array: ndarray
        Numpy array

    Returns
    -------
    seq_list: list of ndarray
        List of sequences

    Examples
    --------
    >>> from sciquence import sequences as sq
    >>> import numpy as np
    >>> x = np.array([1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0])
    >>> print sq.seq(x)
    [array([1, 1, 1, 1, 1, 1]), array([0, 0, 0, 0, 0, 0]), array([1, 1, 1, 1, 1]), array([0, 0, 0, 0])]

    '''

    return [np.array(list(group)) for elem, group in groupby(array)]


def specseq(array, element):
    '''

    Return sequences consisting of specific tag

    Parameters
    ----------
    array: ndarray
        Numpy array
    element: object
        Element

    Returns
    -------
    seq_list: list of ndarray
        List of sequences consisting of specific tag

    Examples
    --------
    >>> from sciquence import sequences as sq
    >>> import numpy as np
    >>> x = np.array([1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 44, 44, 44, 44, 44, 1, 1, 0, 0, 0, 0])
    >>> print sq.specseq(x, 44)
    [array([44, 44, 44, 44, 44])]

    '''
    return [np.array(list(group)) for elem, group in groupby(array) if elem == element]



def nseq(array):
    '''

    Returns sequences consisting of zeros

    Parameters
    ----------
    array: array-like
        Numpy array

    Returns
    -------
    seq_list: list of ndarray
        List of negative sequences

    Examples
    --------
    >>> from sciquence import sequences as sq
    >>> import numpy as np
    >>> x = np.array([1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0])
    >>> print sq.nseq(x)
    [array([0, 0, 0, 0, 0, 0]), array([0, 0, 0, 0])]]

    '''

    return [np.array(list(group)) for elem, group in groupby(array) if not elem]


def pseq(array):
    '''

    Returns sequences consisting of ones

    Parameters
    ----------
    array: array-like
        Numpy array

    Returns
    -------
    seq_list: list of ndarray
        List of positive sequences

    Examples
    --------
    >>> from sciquence import sequences as sq
    >>> import numpy as np
    >>> x = np.array([1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0])
    >>> print sq.nseq(x)
    [array([1, 1, 1, 1, 1, 1]), array([1, 1, 1, 1, 1])]
    '''

    return [np.array(list(group)) for elem, group in groupby(array) if elem]


def seqi(array):
    '''

    Get list of sequences and corresponding list of indices

    Parameters
    ----------
    array: ndarray
        Numpy array

    Returns
    -------
    seq_list: list of ndarray
        List of sequences
    idx_list: list of ndarray
        List of seqences indices

    '''

def nseqi(array):
    pass


def pseqi(array):
    pass


############# Trimming sequences ##############



############## Comparisions ##############

def lseq_equal(lseqa, lseqb):
    '''

    Compare two lists of ndarrays

    Parameters
    ----------
    lseqa: list of ndarray
        List of sequneces
    lseqb: list of ndarray
        List of sequneces

    Returns
    -------
    ans: bool
        True if lists equal, otherwise False

    Examples
    --------
    >>> from sciquence import sequences as sq
    >>> import numpy as np
    >>> x = [np.array([1, 2, 3, 4]), np.array([6, 7, 8])]
    >>> y = [np.array([1., 2.8, 3., 4.]), np.array([6.1, 7., 8.5])]
    >>> z = [np.array([1, 2, 3, 4]), np.array([6, 7, 8])]
    >>> print sq.lseq_equal(x, y)
    False
    >>> print sq.lseq_equal(x, z)
    True

    '''
    ans = [np.array_equal(a, b) for a, b in zip(lseqa, lseqb)]
    return np.logical_and.reduce(ans)


