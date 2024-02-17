from pathlib import Path 
import tkinter as tk
from tkinter import *
import random
from tkinter import messagebox

root = tk.Tk()

# width_px = root.winfo_screenwidth()
# height_px = root.winfo_screenheight()
# root.geometry(f'{width_px}x{height_px}')
root.title('Aceitas?')
root.attributes('-fullscreen', True)

# Define o caminho para o arquivo de ícone
# icon_path = Path.joinpath(Path(__file__).parents[0], Path('icons/dia-dos-namorados.ico'))
icon_path = Path.joinpath(Path(r'C:\Users\Guilherme\Desktop\valentine-days'), Path('icons/dia-dos-namorados.ico'))

# Define o ícone da janela
root.iconbitmap(icon_path)
root.configure(background='#ffc8dd')

move_count = 0  # Inicializa o contador de movimentos
move_limit = 10  # Define o limite de movimentos para exibir a mensagem

def move_button_1(e):
    global move_count
    button_center_x = button_1.winfo_x() + button_1.winfo_width() / 2
    button_center_y = button_1.winfo_y() + button_1.winfo_height() / 2
    distance = ((e.x - button_center_x) ** 2 + (e.y - button_center_y) ** 2) ** 0.5
    if distance < 90:
        margin_x = 100  # Margem horizontal
        margin_y = 100  # Margem vertical
        max_x = root.winfo_width() - button_1.winfo_width() - margin_x
        max_y = root.winfo_height() - button_1.winfo_height() - margin_y
        x = random.randint(margin_x, max_x)
        y = random.randint(margin_y, max_y)
        button_1.place(x=x, y=y)
        move_count += 1  # Incrementa o contador de movimentos
        if move_count == 10:
            messagebox.showinfo('Meu amor', 'ACEITA LOGO POR FAVOR')
        if move_count == 20:
            messagebox.showinfo('Meu amor', 'EU NAO AGUENTO MAISSSSSS')

def accepted():
    messagebox.showinfo(
        'Meu amor', "Eu te amo meu amor, lanchinho mais tarde?"
    )
    root.destroy()

def denied():
    button_1.destroy()

margin = Canvas(root, width=500, bg='#ffc8dd', height=100, bd=0, highlightthickness=0, relief='ridge')
margin.pack()

text_id = Label(root, bg='#ffc8dd', text='Quer namorar comigo?', fg='#590d22', font=('Montserrat', 24, 'bold'))
text_id.pack()

button_1 = tk.Button(root, text='Não', bg='#ffb3c1', command=denied, relief=RIDGE, bd=3, font=('Montserrat', 18, 'bold'))
button_1.pack()

root.bind('<Motion>', move_button_1)

button_2 = tk.Button(root, text='Sim', bg='#ffb3c1', relief=RIDGE, bd=3, command=accepted, font=('Montserrat', 18, 'bold'))
button_2.pack()

root.mainloop()


