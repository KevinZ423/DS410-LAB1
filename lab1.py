# I collaborated with:
#


from dask import delayed
from typing import List
import time


@delayed
def addthem(x: List[float]) -> float:
    """ adds the elements in the list x """
    time.sleep(1)
    return sum(x)


@delayed
def increment(x: float) -> float:
    """ adds 1 to x """
    time.sleep(1)
    return x+1


def go(myarray, branch_factor):

    a = [myarray[i:i + branch_factor] for i in range(0, len(myarray), branch_factor)]
    print(a)
    for i in range(0, len(a)):
        for j in range(0, len(a[i])):
            a[i][j] = delayed(increment)(a[i][j])
        print(a)
    while len(a) > 1:
        for i in range(0, len(a)):
            a[i] = delayed(addthem)(a[i])
        print(a)
        a = [a[i:i + branch_factor] for i in range(0, len(a), branch_factor)]
        print(a)

    result = delayed(addthem)(a[0])

    delayed_object = go([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3)
    delayed_object.visualize('tree.png')  # creates a png  image  of the  graph
    result = delayed_object.compute()  # result = 66
    print(f"The result is {result}")
    pass
