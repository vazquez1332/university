from tkinter import Tk, StringVar, ttk, messagebox

class Aplicacion():
    __ventana = None
    __vestimenta: list[StringVar]
    __alimentos: list[StringVar]
    __educacion: list[StringVar]
    __ipc: StringVar

    def __init__(self) -> None:
        self.__ventana = Tk()
        self.__ventana.title("Calculadora IPC")
        self.__vestimenta = [StringVar(), StringVar(), StringVar()]
        self.__alimentos = [StringVar(), StringVar(), StringVar()]
        self.__educacion = [StringVar(), StringVar(), StringVar()]
        self.__ipc = StringVar()

        self.frame = ttk.Frame(self.__ventana, borderwidth=5, relief="sunken", padding=(20,20))
        self.style = ttk.Style(self.frame)
        self.style.configure("TLabel", padding=10)
        self.style.configure('TEntry', padding=5)
        self.style.configure("TButton", padding=5)

        ttk.Label(self.frame, text="Item").grid(row=0, column=0, sticky="NW")
        ttk.Label(self.frame, text="Vestimenta").grid(row=1, column=0, sticky="NW")
        ttk.Label(self.frame, text="Alimentos").grid(row=2, column=0, sticky="NW")
        ttk.Label(self.frame, text="Eduacion").grid(row=3, column=0, sticky="NW")
        ttk.Label(self.frame, text="Cantidad").grid(row=0, column=1, sticky="N")
        ttk.Label(self.frame, text="Precio Año Base").grid(row=0, column=2, sticky="NSEW")
        ttk.Label(self.frame, text="Precio Año Actual").grid(row=0, column=3, sticky="NSEW")

        for i in range(3):
            ttk.Entry(self.frame, textvariable=self.__vestimenta[i], width=10).grid(row=1, column=i+1)
            ttk.Entry(self.frame, textvariable=self.__alimentos[i], width=10).grid(row=2, column=i+1)
            ttk.Entry(self.frame, textvariable=self.__educacion[i], width=10).grid(row=3, column=i+1)
    
        ttk.Button(self.frame, text="Calcular IPC", command= self.calcularIPC).grid(row=4, column=1, padx=10, pady=20)
        ttk.Button(self.frame, text="Salir", command= quit).grid(row=4, column=2, padx=10, pady=20, sticky="E")
        ttk.Label(self.frame, text="IPC % XX-XX").grid(row=5, column=0, padx=5, pady=5)

        self.frame.grid()
        self.__ventana.mainloop()

    def calcularIPC(self) -> None:
        try:
            vestimenta = [float(value.get()) for value in self.__vestimenta]
            alimentos = [float(value.get()) for value in self.__alimentos]
            educacion = [float(value.get()) for value in self.__educacion]

            ipc_v = (vestimenta[0] * vestimenta[1]) / (vestimenta[0] * vestimenta[2])
            ipc_a = (alimentos[0] * alimentos[1]) / (alimentos[0] * alimentos[2])
            ipc_e = (educacion[0] * educacion[1]) / (educacion[0] * educacion[2])
            
            self.__ipc.set(int(ipc_v + ipc_a + ipc_e) * 100) 
            ttk.Label(self.frame, text=f"IPC % {self.__ipc.get()}").grid(row=5, column=0, padx=5, pady=5)
        
        except ValueError:
            messagebox.showerror(title= "Error", message= "Debe ingresar un valor numérico")

    