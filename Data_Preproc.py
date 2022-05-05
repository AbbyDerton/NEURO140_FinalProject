# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 03:07:29 2022

@author: Abbernator
"""

def Clean_Reviews(df):   
    
    #import required packages
    from string import digits
    import numpy as np
    remove_digits = str.maketrans('', '', digits)
    remove_these = ["zero","one","two","three","four","five", "rated", "stars"]
    
    result_col = []    
    count = 0
    for review in df['Review']:
        if str(type(review)) == "<class 'str'>":
            review = review.translate(remove_digits)
            reviewwords = review.split()
            
            resultwords  = [word for word in reviewwords if word.lower() not in remove_these]
            result = ' '.join(resultwords)
            result_col.append(result)
            
    
    df['Review_Clean'] = result_col
    return(df)
