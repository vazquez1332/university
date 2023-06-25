from tkinter import *
from tkinter import ttk
from functools import partial

class Calculadora():

	def __init__(self, tkWindow=Tk()):
		self.__mainframe=ttk.Frame(tkWindow,padding="10 10 10 10")
		self.__mainframe.grid(column=0,row=0)
		self.__memoria=StringVar()
		self.__op=StringVar()

		ttk.Label(self.__mainframe,textvariable=self.__memoria).grid(column=1,row=0,sticky="E")
		ttk.Label(self.__mainframe,textvariable=self.__op).grid(column=2,row=0,sticky="E")
		self.__visor=StringVar()
		self.__visor_entry=ttk.Entry(self.__mainframe,width=30,textvariable=self.__visor)
		self.__visor_entry.grid(column=0,row=1,columnspan=4)

		self.__0=ttk.Button(self.__mainframe,text="0",width="3",padding="10",command=partial(self.escribir,"0"))
		self.__1=ttk.Button(self.__mainframe,text="1",width="3",padding="10",command=partial(self.escribir,"1"))
		self.__2=ttk.Button(self.__mainframe,text="2",width="3",padding="10",command=partial(self.escribir,"2"))
		self.__3=ttk.Button(self.__mainframe,text="3",width="3",padding="10",command=partial(self.escribir,"3"))
		self.__4=ttk.Button(self.__mainframe,text="4",width="3",padding="10",command=partial(self.escribir,"4"))
		self.__5=ttk.Button(self.__mainframe,text="5",width="3",padding="10",command=partial(self.escribir,"5"))
		self.__6=ttk.Button(self.__mainframe,text="6",width="3",padding="10",command=partial(self.escribir,"6"))
		self.__7=ttk.Button(self.__mainframe,text="7",width="3",padding="10",command=partial(self.escribir,"7"))
		self.__8=ttk.Button(self.__mainframe,text="8",width="3",padding="10",command=partial(self.escribir,"8"))
		self.__9=ttk.Button(self.__mainframe,text="9",width="3",padding="10",command=partial(self.escribir,"9"))

		self.__punto=ttk.Button(self.__mainframe,text=".",width="3",padding="10",command=partial(self.escribir,"."))
		self.__suma=ttk.Button(self.__mainframe,text="+",width="3",padding="10",command=partial(self.operar,"+"))
		self.__resta=ttk.Button(self.__mainframe,text="-",width="3",padding="10",command=partial(self.operar,"-"))
		self.__division=ttk.Button(self.__mainframe,text="/",width="3",padding="10",command=partial(self.operar,"/"))
		self.__multiplicacion=ttk.Button(self.__mainframe,text="*",width="3",padding="10",command=partial(self.operar,"*"))
		self.__igual=ttk.Button(self.__mainframe,text="=",width="11",padding="10",command=self.total)
		self.__borrar=ttk.Button(self.__mainframe,text="<<",width="3",padding="10",command=self.borrar)
		self.__imaginario=ttk.Button(self.__mainframe,text="i",width="3",padding="10",)
		self.__limpiar=ttk.Button(self.__mainframe,text="CL",width="3",padding="10",command=self.limpiar)

		self.__9.grid(column=2,row=3)
		self.__8.grid(column=1,row=3)
		self.__7.grid(column=0,row=3)
		self.__6.grid(column=2,row=4)
		self.__5.grid(column=1,row=4)
		self.__4.grid(column=0,row=4)
		self.__3.grid(column=2,row=5)
		self.__2.grid(column=1,row=5)
		self.__1.grid(column=0,row=5)
		self.__0.grid(column=0,row=6)

		self.__punto.grid(column=1,row=6)
		self.__igual.grid(column=2,row=6,columnspan=2)
		self.__division.grid(column=3,row=2)
		self.__multiplicacion.grid(column=3,row=3)
		self.__resta.grid(column=3,row=4)
		self.__suma.grid(column=3,row=5)
		self.__borrar.grid(column=1,row=2)
		self.__imaginario.grid(column=2,row=2)
		self.__limpiar.grid(column=0,row=2)

		tkWindow.mainloop()

	def escribir(self,num):
		self.__visor.set(str(self.__visor.get())+num)

	def borrar(self):
		visor=self.__visor.get()
		visor=visor[:-1]
		self.__visor.set(visor)

	def limpiar(self):
		self.__visor.set("")
		self.__memoria.set("")
		self.__op.set("")

	def total(self):
		mem=self.__memoria.get()
		oper=self.__op.get()
		visor=self.__visor.get()

		if mem=="":
			if visor=="":
				self.__memoria.set(0)
			else:
				self.__memoria.set(visor)

		else:
			if oper!="":
				if visor!="":
					res=eval(f"{mem}{oper}{visor}")
					if res%1==0:
						res=int(res)
					self.__memoria.set(res)
			else:
				self.__memoria.set(visor)

		self.__op.set("")
		self.__visor.set("")

	def operar(self,op):
		mem=self.__memoria.get()
		oper=self.__op.get()
		visor=self.__visor.get()

		if visor=="":
			if op=="-":
				if oper!="":
					self.escribir(op)
				else:
					self.__op.set(op)
		else:
			if mem=="":
				self.__memoria.set(visor)
				self.__op.set(op)
				self.__visor.set("")
				
			elif oper!="":
				self.total()
				self.__op.set(op)
				self.__visor.set("")
				
			else:
				self.__op.set(op)


		
				



