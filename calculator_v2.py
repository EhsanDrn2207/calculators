import tkinter as tk
import random

#creating GUI
root = tk.Tk()
root.title("Esd calculator")
root.iconbitmap('E:\Program Files\Python\second_ProjectFile\calculator.ico')

#creating lable for showing result of caculation
lbl_result = tk.Label(
    master=root,
    text='0',
    width=30,
    height=3,
)

lbl_result.grid(row=0, column=0, columnspan=5)

def change_color():
    my_list = ['green', 'red', 'blue', 'black']
    color = random.choice(my_list)
    if color == lbl_result['fg']:
        my_list.remove(f'{lbl_result["fg"]}')
        new_color = random.choice(my_list)
        lbl_result['fg'] = new_color
    else:
        lbl_result['fg'] = color

def attach_numbers(btn_text):
    current = lbl_result['text']
    operation = ['+', '*', '-', '/']
    numbers = 1
    point = 0
    
    if btn_text == 'C':
        lbl_result['text'] = '0' #clear lebal
        numbers, point = 1, 0

    elif btn_text == 'correct':
        try:
            if current[-1] == '.':
                point -= 1
            elif current[-1] in operation:
                numbers -= 1
        except IndexError:
            pass

        lbl_result['text'] = current[:-1] #modify lebal
        
    elif current == '0':
        lbl_result['text'] = btn_text   #0002 invalid
         
    elif btn_text == '=':
        try:
            lbl_result['text'] = str(eval(current)) #Evaluation
            numbers, point = 1, 0
            
        except SyntaxError:
            pass
            
    elif btn_text == '.': # 2.5.54 , ..23, 23.23... invalid
        for i in current:
            if i in operation:
                numbers += 1
            elif i == '.':
                point += 1
            if abs((numbers) - (point)) == 2: # 14*..412 invalid
                numbers -= 1
        if numbers > point :
            lbl_result ['text'] += btn_text
        else:
            pass
            
    elif btn_text in operation:
        if current[-1] in operation:
            lbl_result['text'] = current[:-1] + btn_text
        else:
            lbl_result['text'] += btn_text
            
    else:
        lbl_result['text'] += btn_text

#creating a list button's featurs which are different with each other
keys_featurs_list = [
    {
        'text' : '?',
        'command': change_color,
    },
    {
        'text' : '7',
        'command': lambda: attach_numbers('7'),
    },
    {
        'text' : '8',
        'command': lambda: attach_numbers('8'),
    },
    {
        'text' : '9',
        'command': lambda: attach_numbers('9'),
    },
    {
        'text' : '/',
        'command': lambda: attach_numbers('/'),
    },
    {
        'text' : 'correct',
        'command': lambda: attach_numbers('correct'),
    },
    {
        'text' : '4',
        'command': lambda: attach_numbers('4'),
    },
    {
        'text' : '5',
        'command': lambda: attach_numbers('5'),
    },
    {
        'text' : '6',
        'command': lambda: attach_numbers('6'),
    },
    {
        'text' : '*',
        'command': lambda: attach_numbers('*'),
    },
    {
        'text' : 'Quit',
        'command': quit,
        
    },
    {
        'text' : '1',
        'command': lambda: attach_numbers('1'),
    },
    {
        'text' : '2',
        'command': lambda: attach_numbers('2'),
    },
    {
        'text' : '3',
        'command': lambda: attach_numbers('3'),
    },
    {
        'text' : '-',
        'command': lambda: attach_numbers('-'),
    },
    {
        'text' : 'C',
        'command': lambda: attach_numbers('C'),
    },
    {
        'text' : '.',
        'command': lambda: attach_numbers('.'),
    },
    {
        'text' : '0',
        'command': lambda: attach_numbers('0'),
    },
    {
        'text' : '=',
        'command': lambda: attach_numbers('='),
    },
    {
        'text' : '+',
        'command': lambda: attach_numbers('+'),
    },
]

#connecting keyword to GUI  
def keywords_click():
    root.bind("1", lambda n: attach_numbers('1'))
    root.bind("2", lambda n: attach_numbers('2'))
    root.bind("3", lambda n: attach_numbers('3'))
    root.bind("4", lambda n: attach_numbers('4'))
    root.bind("5", lambda n: attach_numbers('5'))
    root.bind("6", lambda n: attach_numbers('6'))
    root.bind("7", lambda n: attach_numbers('7'))
    root.bind("8", lambda n: attach_numbers('8'))
    root.bind("9", lambda n: attach_numbers('9'))
    root.bind("0", lambda n: attach_numbers('0'))
    root.bind("+", lambda n: attach_numbers('+'))
    root.bind("-", lambda n: attach_numbers('-'))
    root.bind("*", lambda n: attach_numbers('*'))
    root.bind("/", lambda n: attach_numbers('/'))
    root.bind('<Return>', lambda n: attach_numbers('='))
    root.bind("<BackSpace>", lambda n: attach_numbers('correct'))
    root.bind(".", lambda n: attach_numbers('.'))
    root.bind('q', quit)
    root.bind("c", lambda n: attach_numbers('C'))

key_calc_objs = [] #?,7,8,9,/,correct,4,5,6,*,Quit,1,2,3,-,C,.,0,=,+

#creating calculator's buttons
for keys_featurs in keys_featurs_list:
    btn_calculator = tk.Button(
        master=root,
        text=keys_featurs['text'],
        width=6,
        height=2,
        command=keys_featurs['command'],
    )
    key_calc_objs.append(btn_calculator)

#griding calculator's buttons 
for i,key_calc_obj in enumerate(key_calc_objs):
    key_calc_obj.grid(row=(i//5)+1, column=i%5, sticky=('nswe'))
    
keywords_click()

root.mainloop()