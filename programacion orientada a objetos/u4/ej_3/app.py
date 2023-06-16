from tkinter import ttk, messagebox, Tk, StringVar, W, E, Label, Button

class Aplicacion(Tk):
    __precioArs: StringVar
    __precioDls: StringVar

    def __init__(self):
        super().__init__()
        self.title("Conversor de moneda")
        self.__precioArs = StringVar()
        self.__precioDls = StringVar()
        self.__precioDls.trace('w', self.calcular)

        frame = ttk.Frame(self, padding=20)
        frame.grid(row=0, column=0)

        self.precioEntry = ttk.Entry(frame, width=15, textvariable=self.__precioDls)
        self.precioEntry.grid(column=2, row=1, sticky=(W, E))
        self.precioEntry.focus()

        Label(frame, textvariable=self.__precioArs).grid(column=2, row=2, sticky=(W, E))
        Button(frame, text='Salir', padx=10, pady=5, command=self.salir).grid(column=3, row=3, sticky=W)
        Label(frame, text="dólares").grid(column=3, row=1, sticky=W)
        Label(frame, text="es equivalente a").grid(column=1, row=2, sticky=E)
        Label(frame, text="pesos").grid(column=3, row=2, sticky=W)

        for child in frame.winfo_children():
            child.grid_configure(padx=5, pady=5)

    def calcular(self, *args):
        if self.precioEntry.get() == '':
            self.__precioArs.set('')
        else:
            try:
                valor = float(self.precioEntry.get())
                self.__precioArs.set('{:.2f}'.format(valor))
            except ValueError:
                messagebox.showerror('Error de tipo', 'Debe ingresar un valor numérico')
                self.__precioDls.set('')
                self.precioEntry.focus()

    def salir(self):
        self.destroy()

if __name__ == '__main__':
    app = Aplicacion()
    app.mainloop()
