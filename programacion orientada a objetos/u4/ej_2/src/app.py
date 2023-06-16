from tkinter import *
from tkinter import messagebox

class app(Tk):
	__precioSinIva: StringVar
	__precioConIva: StringVar
	__valorIVA: StringVar

	def __init__(self):
		super().__init__()
		self.title("")
		self.__precioSinIva = StringVar()
		self.__precioConIva = StringVar()
		self.__valorIVA = StringVar()
		self.radioValue = IntVar()

		Label(self, text="Cálculo de IVA", bg="lightblue", anchor="center").grid(row=0, columnspan=2, padx=10, pady=10, sticky="nswe", ipadx=10, ipady=10)
		Label(self, text="Precio sin IVA: ").grid(column=0, row=1,sticky=W)
		self.precioEntry= Entry(self, textvariable=self.__precioSinIva, width=20)
		self.precioEntry.grid(column=1, row=1, sticky=E)
		
		Radiobutton(self, text="IVA 21 %", value=0, command=self.setIVA, variable=self.radioValue).grid(row=2, column=0, sticky="w")
		Radiobutton(self, text="IVA 10.5 %", value=1,command=self.setIVA, variable=self.radioValue).grid(row=3, column=0, sticky="w")
		
		Label(self, text="IVA: ").grid(column=0, row=4,sticky=W)
		Label(self, textvariable= self.__valorIVA).grid(column=1, row=4,sticky=W)
		Label(self, text="Precio con IVA: ").grid(column=0, row=5,sticky=W)
		Label(self, textvariable= self.__precioConIva).grid(column=1, row=5,sticky=W) 
		
		Button(self, text="Calcular", bg="#00b347" ,height=1, width=20, command=self.calcular).grid(column=0, row=6, sticky=W)
		Button(self, text="Salir", bg="#ff9e81", height=1, width=20, command=quit).grid(column=1, row=6, sticky=E) 
		
		self.radioValue.set(-1)
		self.__valorIVA.set(" ")

		for child in self.winfo_children():
			child.grid_configure(padx=5, pady=5)
			
	def setIVA(self):
		if self.radioValue.get() == 0:
			self.__valorIVA.set("21")
		else:
			self.__valorIVA.set("10.5")

	def calcular(self):
		try:
			valor = float(self.precioEntry.get())
			valor += valor * float(self.__valorIVA.get()) / 100
			self.__precioConIva.set('{:.2f}'.format(valor))		
		except ValueError:
			messagebox.showerror("Error", "Debe ingresar un valor numérico")