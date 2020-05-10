# -*- coding: utf-8 -*-

import sys
import os
import unittest
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__) + '/src' )))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__) + '/tests' )))

#from core import get_answer
from core import main



if __name__ == '__main__':
    f = open('packets/tcp.txt','r')
    g = open('packets/udp.txt','r')  
    
    main(f)

