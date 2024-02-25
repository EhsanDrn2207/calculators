import tkinter as tk

window = tk.Tk()

lbl_result = tk.Label(
    master=window,
    text='0',
    width=30,
    height=3,
)

lbl_result.grid(row=0, column=0, columnspan=4)


def insert_number_in_calc_result(btn_text):
    current = lbl_result['text']
    if btn_text == 'C':
        lbl_result['text'] = '0'
        
    elif current == '0':
        lbl_result['text'] = btn_text
        
    elif btn_text == '=':
        lbl_result['text'] = str(eval(current))
        
    else:
        if btn_text == '.':
            if current[-1] != '.':
                lbl_result['text'] += btn_text
            else:
                pass
        elif btn_text in ['+', '-', '*']:
            if current[-1] in ['+', '-', '*']:
                lbl_result['text'] = current[:-1] + btn_text
            else:
                lbl_result['text'] += btn_text
        else:
            lbl_result['text'] += btn_text
    
calc_keys = [
    {
        'text': '7', #(row=1, column=0)
        'command': lambda: insert_number_in_calc_result('7'),
    },  
    {
        'text': '8', #(row=1, column=1)
        'command': lambda: insert_number_in_calc_result('8'),
    },
    {
        'text': '9', #(row1, column=2)
        'command': lambda: insert_number_in_calc_result('9'),
    },
    {
        'text': '+', #(row=1, column3)
        'command': lambda: insert_number_in_calc_result('+'),
    },
        {
        'text': '4',
        'command': lambda: insert_number_in_calc_result('4'),
    },  
    {
        'text': '5',
        'command': lambda: insert_number_in_calc_result('5'),
    },
    {
        'text': '6',
        'command': lambda: insert_number_in_calc_result('6'),
    },
    {
        'text': '-',
        'command': lambda: insert_number_in_calc_result('-'),
    },
        {
        'text': '3',
        'command': lambda: insert_number_in_calc_result('3'),
    },  
    {
        'text': '2',
        'command': lambda: insert_number_in_calc_result('2'),
    },
    {
        'text': '1',
        'command': lambda: insert_number_in_calc_result('1'),
    },
    {
        'text': '*',
        'command': lambda: insert_number_in_calc_result('*'),
    },
    {
        'text': '.',
        'command': lambda: insert_number_in_calc_result('.'),
    },
    {
        'text': '0',
        'command': lambda: insert_number_in_calc_result('0'),
    },
    {
        'text': 'C',
        'command': lambda: insert_number_in_calc_result('C'),
    },
    {
        'text': '=',
        'command': lambda: insert_number_in_calc_result('='),
    },
]

calc_obj_keys= []

for key_data in calc_keys:
    btn = tk.Button(
    master=window,
    text= key_data['text'],
    height=3,
    command= key_data['command'],
    )
    calc_obj_keys.append(btn)    

for i, calc_obj_key in enumerate(calc_obj_keys):
    calc_obj_key.grid(row= (i//4)+1, column=i%4, sticky='nsew')
    

window.mainloop()