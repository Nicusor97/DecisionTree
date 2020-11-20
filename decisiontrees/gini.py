# -*- coding: utf-8 -*-
"""File defining the gini algorithm that will be used on the loaded information"""

from utils import uniqueCounts


def gini(rows):
    """Method that simulates the gini algorithm. 
    
    Args:
        rows: The rows from the csv file that was loaded.
    """

    total = len(rows)
    counts = uniqueCounts(rows)
    imp = 0.0

    for k1 in counts:
        p1 = float(counts[k1])/total  
        for k2 in counts:
            if k1 == k2: continue
            p2 = float(counts[k2])/total
            imp += p1*p2
    return imp