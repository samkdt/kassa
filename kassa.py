import tkinter as tk

hj=1080
br=1920
num=0
knapp=[]

class prod:
	def __init__(self, id, namn, antal, pris):
		self.id=id	
		self.namn=namn	
		self.antal=antal
		self.pris=pris	
		self.totpris=pris*antal

def update_input():
	text['text']= num

def knapp_del():
	global num
	if(len(str(num)) > 1):
		num=int(str(num)[:-1])
	else: num=0
	update_input()
	
def knapp_clear():
	global num
	num=0
	update_input()
	
def knap_tryck(inp):
	global num
	num=num*10
	num+=inp
	update_input()
	
	

root = tk.Tk()

#avkomentera för full skärm
#
#root.overrideredirect(True)
#root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

wind = tk.Canvas(root, height=hj, width=br)
wind.pack()

#numer display
input = tk.Frame(root, bg="#ff00ff", bd=5)
input.place(relx=0.49, rely=0.15,relheight=0.1, relwidth=0.5, anchor="nw")

text= tk.Label(input, text=num, font=100)
text.place(relheight=1, relwidth=0.68)

knap_bort = tk.Button(input, text="<", command=lambda: knapp_del())
knap_bort.place(relx=0.69, relheight=1, relwidth=0.2)

knap_c = tk.Button(input, text="C", command=lambda: knapp_clear())
knap_c.place(relx=0.90, relheight=1, relwidth=0.1)

#kategory


#knappar
numpad= tk.Frame(root, bg="#ff00ff", bd=5)
numpad.place(relx=0.49, rely=0.25,relheight=0.75, relwidth=0.5, anchor="nw")

knapp_0 = tk.Button(numpad, text="0", command=lambda: knap_tryck(0))
knapp_0.place(relx=0, rely=0.78, relwidth=1, relheight=0.22) 

knapp_1 = tk.Button(numpad, text="1", command=lambda: knap_tryck(1))
knapp_1.place(relx=0, rely=0, relwidth=0.3, relheight=0.25) 

knapp_2 = tk.Button(numpad, text="2", command=lambda: knap_tryck(2))
knapp_2.place(relx=0.35, rely=0, relwidth=0.3, relheight=0.25) 

knapp_3 = tk.Button(numpad, text="3", command=lambda: knap_tryck(3))
knapp_3.place(relx=0.7, rely=0, relwidth=0.3, relheight=0.25) 

knapp_4 = tk.Button(numpad, text="4", command=lambda: knap_tryck(4))
knapp_4.place(relx=0, rely=0.26, relwidth=0.3, relheight=0.25) 

knapp_5 = tk.Button(numpad, text="5", command=lambda: knap_tryck(5))
knapp_5.place(relx=0.35, rely=0.26, relwidth=0.3, relheight=0.25) 

knapp_6 = tk.Button(numpad, text="6", command=lambda: knap_tryck(6))
knapp_6.place(relx=0.7, rely=0.26, relwidth=0.3, relheight=0.25) 

knapp_7 = tk.Button(numpad, text="7", command=lambda: knap_tryck(7))
knapp_7.place(relx=0, rely=0.52, relwidth=0.3, relheight=0.25) 

knapp_8 = tk.Button(numpad, text="8", command=lambda: knap_tryck(8))
knapp_8.place(relx=0.35, rely=0.52, relwidth=0.3, relheight=0.25)

knapp_9 = tk.Button(numpad, text="9", command=lambda: knap_tryck(9))
knapp_9.place(relx=0.7, rely=0.52, relwidth=0.3, relheight=0.25) 

knapp_0 = tk.Button(numpad, text="0", command=lambda: knap_tryck(0))
knapp_0.place(relx=0, rely=0.78, relwidth=1, relheight=0.22) 

root.mainloop()
