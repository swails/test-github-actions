import os

def myfunction():
    """ A stupid function """
    if os.environ.get('TEST_STATUS', 'FAIL') == 'SUCCESS':
        return 0

    return 1
