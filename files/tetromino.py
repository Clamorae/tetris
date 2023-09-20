import numpy as np

class o:
    up = np.matrix([[' ',' ',' ',' '],[' ','@','@',' '],[' ','@','@',' '],[' ',' ',' ',' ']])
    right = np.matrix([[' ',' ',' ',' '],[' ','@','@',' '],[' ','@','@',' '],[' ',' ',' ',' ']])
    down = np.matrix([[' ',' ',' ',' '],[' ','@','@',' '],[' ','@','@',' '],[' ',' ',' ',' ']])
    left = np.matrix([[' ',' ',' ',' '],[' ','@','@',' '],[' ','@','@',' '],[' ',' ',' ',' ']])

class i:
    up = np.matrix([[' ','@',' ',' '],[' ','@',' ',' '],[' ','@',' ',' '],[' ','@',' ',' ']])
    right = np.matrix([[' ',' ',' ',' '],[' ',' ',' ',' '],['@','@','@','@'],[' ',' ',' ',' ']])
    down = np.matrix([[' ','@',' ',' '],[' ','@',' ',' '],[' ','@',' ',' '],[' ','@',' ',' ']])
    left = np.matrix([[' ',' ',' ',' '],[' ',' ',' ',' '],['@','@','@','@'],[' ',' ',' ',' ']])

class j:
    up = np.matrix([[' ',' ',' ',' '],[' ',' ','@',' '],[' ',' ','@',' '],[' ','@','@',' ']])
    right = np.matrix([[' ',' ',' ',' '],['@',' ',' ',' '],['@','@','@',' '],[' ',' ',' ',' ']])
    down = np.matrix([[' ','@','@',' '],[' ',' ','@',' '],[' ',' ','@',' '],[' ',' ',' ',' ']])
    left = np.matrix([[' ',' ',' ',' '],[' ','@','@','@'],[' ',' ',' ','@'],[' ',' ',' ',' ']])

class l:
    up = np.matrix([[' ',' ',' ',' '],[' ','@',' ',' '],[' ','@',' ',' '],[' ','@','@',' ']])
    right = np.matrix([[' ',' ',' ',' '],['@','@','@',' '],['@',' ',' ',' '],[' ',' ',' ',' ']])
    down = np.matrix([[' ','@','@',' '],[' ',' ','@',' '],[' ',' ','@',' '],[' ',' ',' ',' ']])
    left = np.matrix([[' ',' ',' ',' '],[' ',' ',' ','@'],[' ','@','@','@'],[' ',' ',' ',' ']])

class s:
    up = np.matrix([[' ',' ',' ',' '],[' ',' ','@','@'],[' ','@','@',' '],[' ',' ',' ',' ']])
    right = np.matrix([[' ',' ',' ',' '],[' ','@',' ',' '],[' ','@','@',' '],[' ',' ','@',' ']])
    down = np.matrix([[' ',' ',' ',' '],[' ',' ','@','@'],[' ','@','@',' '],[' ',' ',' ',' ']])
    left = np.matrix([[' ',' ',' ',' '],[' ','@',' ',' '],[' ','@','@',' '],[' ',' ','@',' ']])
    
class z:
    up = np.matrix([[' ',' ',' ',' '],[' ',' ',' ',' '],[' ','@','@',' '],[' ',' ','@','@']])
    right = np.matrix([[' ',' ',' ',' '],[' ',' ','@',' '],[' ','@','@',' '],[' ','@',' ',' ']])
    down = np.matrix([[' ',' ',' ',' '],[' ',' ',' ',' '],[' ','@','@',' '],[' ',' ','@','@']])
    left = np.matrix([[' ',' ',' ',' '],[' ',' ','@',' '],[' ','@','@',' '],[' ','@',' ',' ']])
    
class t:
    up = np.matrix([[' ',' ',' ',' '],[' ',' ',' ',' '],[' ',' ','@',' '],[' ','@','@','@']])
    right = np.matrix([[' ',' ',' ',' '],['@',' ',' ',' '],['@','@',' ',' '],['@',' ',' ',' ']])
    down = np.matrix([[' ',' ',' ',' '],[' ',' ',' ',' '],[' ','@','@','@'],[' ',' ','@',' ']])
    left = np.matrix([[' ',' ',' ',' '],[' ',' ',' ','@'],[' ',' ','@','@'],[' ',' ',' ','@']])