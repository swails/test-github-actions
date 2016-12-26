from __future__ import absolute_import

from nose.tools import assert_equal
from ..mymodule import myfunction

def test_my_function():
    """ Tests my function """
    assert_equal(myfunction(), 0)
