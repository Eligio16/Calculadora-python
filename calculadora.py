import tkinter as tk
from tkinter import ttk,messagebox

class Calculadora(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('342x400')
        self.title('Calculadora')
        self.resizable(0,0)
        #Atributos
        self.expresion = ''
        self.entrada = None
        #String para obtener el valor del input
        self.entrada_texto = tk.StringVar()
        self._crear_widgets()

    def _configuracion_ventana(self):
        pass
        # self.columnconfigure(0, weight=1)
        # self.rowconfigure(1, weight=20)

    def _crear_widgets(self):
        #Creamos primer frame para la caja de texto
        frame_superior = tk.Frame(self, width=400, height=50, background='grey')
        frame_superior.pack(side=tk.TOP)
        #Caja de texto
        entry_valor = tk.Entry(frame_superior, font=('arial',18,'bold'), textvariable=self.entrada_texto,  width=25, justify=tk.RIGHT)
        entry_valor.grid(row=0, column=0, ipady=10,ipadx=5, pady=1)

        #Creamos un segundo frame para los botones
        frame_inferior = tk.Frame(self, width=400, height=400,bg='gray')
        frame_inferior.pack()

        #Renglon 1, boton limpiar
        button_limpiar = tk.Button(frame_inferior, text='C', width=35, height=4, bd=0, bg='#eee', cursor='hand2', command=self._evento_limpiar)
        button_limpiar.grid(row=0, column=0, columnspan=3, padx=1, pady=1, ipadx=1)
        button_div = tk.Button(frame_inferior, text='/', width=11, height=4, bd=0, bg='#eee', cursor='hand2', command=lambda: self._evento_click('/'))
        button_div.grid(row=0,column=3, padx=1, pady=1)

        #Renglon 2
        button_siete = tk.Button(frame_inferior, text='7', width=11, height=4, bd=0, bg='#fff', cursor='hand2', command=lambda: self._evento_click('7'))
        button_siete.grid(row=1, column=0, padx=1, pady=1)
        button_ocho = tk.Button(frame_inferior, text='8', width=11, height=4, bd=0, bg='#fff', cursor='hand2', command=lambda: self._evento_click('8'))
        button_ocho.grid(row=1, column=1, padx=1, pady=1)
        button_nueve = tk.Button(frame_inferior, text='9', width=11, height=4, bd=0, bg='#fff', cursor='hand2', command=lambda: self._evento_click('9'))
        button_nueve.grid(row=1, column=2, padx=1, pady=1)
        button_mult = tk.Button(frame_inferior, text='*', width=11, height=4, bd=0, bg='#eee', cursor='hand2', command=lambda: self._evento_click('*'))
        button_mult.grid(row=1, column=3, padx=1, pady=1)

        #Renglon 3
        button_cuatro = tk.Button(frame_inferior, text='4', width=11, height=4, bd=0, bg='#fff', cursor='hand2', command=lambda: self._evento_click('4'))
        button_cuatro.grid(row=2, column=0, padx=1, pady=1)
        button_siete = tk.Button(frame_inferior, text='5', width=11, height=4, bd=0, bg='#fff', cursor='hand2', command=lambda: self._evento_click('5'))
        button_siete.grid(row=2, column=1, padx=1, pady=1)
        button_seis = tk.Button(frame_inferior, text='6', width=11, height=4, bd=0, bg='#fff', cursor='hand2', command=lambda: self._evento_click('6'))
        button_seis.grid(row=2, column=2, padx=1, pady=1)
        button_resta = tk.Button(frame_inferior, text='-', width=11, height=4, bd=0, bg='#eee', cursor='hand2', command=lambda: self._evento_click('-'))
        button_resta.grid(row=2, column=3, padx=1, pady=1)

        #Renglon 4
        button_uno = tk.Button(frame_inferior, text='1', width=11, height=4, bd=0, bg='#fff', cursor='hand2', command=lambda: self._evento_click('1'))
        button_uno.grid(row=3, column=0, padx=1, pady=1)
        button_dos = tk.Button(frame_inferior, text='2', width=11, height=4, bd=0, bg='#fff', cursor='hand2', command=lambda: self._evento_click('2'))
        button_dos.grid(row=3, column=1, padx=1, pady=1)
        button_tres = tk.Button(frame_inferior, text='3', width=11, height=4, bd=0, bg='#fff', cursor='hand2', command=lambda: self._evento_click('3'))
        button_tres.grid(row=3, column=2, padx=1, pady=1)
        button_suma = tk.Button(frame_inferior, text='+', width=11, height=4, bd=0, bg='#eee', cursor='hand2', command=lambda: self._evento_click('+'))
        button_suma.grid(row=3, column=3, padx=1, pady=1)

        #Renglon 5
        button_cero = tk.Button(frame_inferior, text='0', width=22, height=4, bd=0, bg='#fff', cursor='hand2', command=lambda: self._evento_click('0'))
        button_cero.grid(row=4, column=0, columnspan=2, padx=1, pady=1,ipadx=4)
        button_punto = tk.Button(frame_inferior, text='.', width=11, height=4, bd=0, bg='#eee', cursor='hand2', command=lambda: self._evento_click('.'))
        button_punto.grid(row=4, column=2, padx=1, pady=1)
        button_igual = tk.Button(frame_inferior, text='=', width=11, height=4, bd=0, bg='#eee', cursor='hand2', command= self._evento_evaluar)
        button_igual.grid(row=4, column=3, padx=1, pady=1)

    def _evento_limpiar(self):
        self.expresion = ''
        self.entrada_texto.set(self.expresion)

    def _evento_click(self, elemento):
        #Concatenamos el nuevo elemento a la expresion existente
        self.expresion = f'{self.expresion}{elemento}'
        self.entrada_texto.set(self.expresion)

    def _evento_evaluar(self):
        try:
            if self.expresion:
                # eval evalua la expresion string como operacion aritmetica
                resultado = str(eval(self.expresion))
                self.entrada_texto.set(resultado)
        except Exception as e:
            messagebox.showerror('Error', f'Ocurrio un error: {e}')
            self.entrada_texto.set('')
        self.expresion = ''

Calculadora().mainloop()