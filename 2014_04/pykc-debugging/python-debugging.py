#!/usr/bin/env python
"""
Caleb Hyde
Thursday, April 24, 2014
"""

def divid(x, y):
    return x / y

if __name__ == '__main__':
    divid(4,2)
    print(divid(4,2))

    print(divid(2, 4))
    print(divid(2.0, 0))
    
    import pandas as pd
    df = pd.DataFrame('not really a data set')
