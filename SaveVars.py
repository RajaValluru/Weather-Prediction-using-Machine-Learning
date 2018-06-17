# -*- coding: utf-8 -*-
"""
Created on Sat Apr  7 13:28:08 2018

@author: msval
"""
import dill
filename= 'globalsave.pkl'
dill.dump_session(filename)

# and to load the session again:
#dill.load_session(filename)