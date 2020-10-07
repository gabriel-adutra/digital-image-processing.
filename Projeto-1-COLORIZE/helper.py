def rgb2hex(chan: list):
    '''

    Parameters
    ----------
    chan : list
        The 3 rgb channels.

    Returns
    -------
    hex_code : str

    '''
    dic = {0: 0,
           1: 1,
           2: 2,
           3: 3,
           4: 4,
           5: 5,
           6: 6,
           7: 7,
           8: 8,
           9: 9,
           10: 'A',
           11: 'B',
           12: 'C',
           13: 'D',
           14: 'E',
           15: 'F'}
    
    if not(len(chan)==3): raise ValueError('Input a three channel color')
   
    hex_code = '#'
    for i in range(3):
        div = chan[i] / 16
        res = ((div - int(div)) * 16)
        div = int(div)
        
        hex_code += str(dic[div])
        hex_code += str(dic[res])
        
    return hex_code

def nested_rgb2hex(list_: list):
    '''
    Use this if the input is a nested list i.e.:
        [[255,34,52], [55,78,125], [145, 255, 0]]

    Parameters
    ----------
    list_ : list
        list of channel lists

    Returns
    -------
    hex_list : list
        list of hex codes from list_

    '''
    
    return [rgb2hex(chan) for chan in list_]

def write_to_file(text: str, imagename: str):
    '''

    Parameters
    ----------
    text : str
        text to be written.
    imagename : str
        name of the image.

    Returns
    -------
    None.

    '''
    
    filename = 'paleta' + imagename[:-4]
    with open(filename, 'w') as f:
        print(text, file=f)
    return
        
'''
how to parse command line argument:
    pretend you have a file mul.py used as follows:
        python3 mul.py 2 3
    and outputs the multiplication of the two paramenters,
    the parsing inside the file could be:
        
        import sys
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])
        
        print(num1 * num2)
        
    ***remember to pay attention to the type conversion since 
    argvs come in as strings***
'''