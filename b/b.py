
import sys
import os
sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../a'))


from main import Name

from a import a


if __name__ == "__main__":
    print(a.getEnum() == Name.FIRST)


