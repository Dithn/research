"""
Submission by: @changchuanhong
"""
import KrustalMST
import numpy as np
from io import StringIO 
import sys

# Reference: https://stackoverflow.com/questions/16571150/how-to-capture-stdout-output-from-a-python-function-call
class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self
    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio    # free up some memory
        sys.stdout = self._stdout

class UnitTests:
    def __init__(self):
        """
        Automatically run the test cases once initialized
        """
        self.error_string = 'Matrix is not symmetrical. Please try again.'
        self.test_different_dimension_matrix()
        self.test_asymmetrical_matrix()
        self.test_MST_calculations()

    def test_different_dimension_matrix(self):
        """
        Checks to see if the code handles a matrix of different dimension elegantly
        """
        matrix =    [[1,2,3],
                    [4,5,6]]

        with Capturing() as output:
            KrustalMST.MST(matrix)

        if output[0] == self.error_string:
            print('test_different_dimension_matrix passed')
        else:
            print('test_different_dimension_matrix failed')
        
    def test_asymmetrical_matrix(self):
        matrix =    [[1,2,3,4],
                    [1,2,3,4],
                    [1,2,3,4],
                    [1,2,3,4]]
        
        with Capturing() as output:
            KrustalMST.MST(matrix)
        if output[0] == self.error_string:
            print('test_asymmetrical_matrix passed')
        else:
            print('test_asymmetrical_matrix failed')

    def test_MST_calculations(self):
        """
        Verifies that adjacency matrix is calculated correctly.
        """
        matrix =    [[1,2,3],
                    [2,1,4],
                    [3,4,1]]
        expected_adjacency_matrix = np.array(  [[0., 1., 1.],
                                                [1., 0., 0.],
                                                [1., 0., 0.]])
        result_adjacency = KrustalMST.MST(matrix).buildMST()
        comparison = result_adjacency == expected_adjacency_matrix
        
        if comparison.all():
            print('test_MST_calculations passed')
        else:
            print('test_MST_calculations failed')

UnitTests()
