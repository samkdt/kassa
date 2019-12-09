import tkinter as tk

class art:
	def __init__(self, namn, moms):
		self.namn=namn
		self.moms=moms

class prod:
	def __init__(self, namn, antal, pris, moms):
		self.namn=namn	
		self.antal=antal
		self.pris=pris	
		self.moms=moms
		self.totpris=pris*antal


hj=1080
br=1920
num=0
kvitto=[]
artiklar=[art("livsmedel",12), art("godis",12), art("hygien",25), art("dricka",12)]

def update_input():
	text['text']= num

def update_display():

	antal['text']="antal\n"
	namn['text']="namn\n"
	pris['text']="pris\n"
	totpris['text']="pris f.a.\n"

	for x in range(0,len(kvitto)):
		antal['text']+=str(kvitto[x].antal) + "\n"
		namn['text']+=kvitto[x].namn + "\n"
		pris['text']+=str(kvitto[x].pris) + "\n"
		totpris['text']+=str(kvitto[x].totpris) + "\n"

def knapp_art(artnr):
	global num
	global artiklar
	if(num!=0):
		kvitto.append(prod(artiklar[artnr].namn,1,num,artiklar[artnr].moms))
		num=0
	update_input()
	update_display()

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
	update_display()

def knap_tryck(inp):
	global num
	num=num*10
	num+=inp
	update_input()
	
def knapp_minus():
	global kvitto
	global num
	if(num == 0):
		kvitto[len(kvitto)-1].antal-=1
	else:
		kvitto[len(kvitto)-1].antal-=num
	num=0
	kvitto[len(kvitto)-1].totpris=kvitto[len(kvitto)-1].pris*kvitto[len(kvitto)-1].antal
	update_input()
	update_display()

def knapp_plus():
	global kvitto
	global num
	if(num == 0):
		kvitto[len(kvitto)-1].antal+=1
	else:
		kvitto[len(kvitto)-1].antal+=num
	num=0
	kvitto[len(kvitto)-1].totpris=kvitto[len(kvitto)-1].pris*kvitto[len(kvitto)-1].antal
	update_input()
	update_display()

def knapp_remove():
	global kvitto
	kvitto.pop(len(kvitto)-1)
	update_display()	


root = tk.Tk()


#avkomentera för full skärm
#
#root.overrideredirect(True)
#root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

wind = tk.Canvas(root, height=hj, width=br)
wind.pack()

#instälningar typ?
set=tk.Frame(root, bg="#ff00ff", bd=5)
set.place(relx=0, rely=0.75, relheight=0.25, relwidth=0.5)

knapp_mer=tk.Button(set, text="+", command=lambda: knapp_plus())
knapp_mer.place(relx=0,rely=0,relheight=0.5,relwidth=0.333)

knapp_min=tk.Button(set, text="-", command=lambda: knapp_minus())
knapp_min.place(relx=0.333,rely=0,relheight=0.5,relwidth=0.333)

knapp_undo=tk.Button(set, text="ångra", command=lambda: knapp_remove())
knapp_undo.place(relx=0.666,rely=0,relheight=0.5,relwidth=0.333)


knapp_kont=tk.Button(set, text="kontant")
knapp_kont.place(relx=0,rely=0.5,relheight=0.5,relwidth=0.5)

knapp_kort=tk.Button(set, text="kort")
knapp_kort.place(relx=0.5,rely=0.5,relheight=0.5,relwidth=0.5)


#artiklar
artik=tk.Frame(root, bg="#ff00ff", bd=5)
artik.place(relx=0.5,rely=0.75,relheight=0.25,relwidth=0.5)

art_0=tk.Button(artik, text=artiklar[0].namn, command=lambda: knapp_art(0))
art_0.place(relx=0, rely=0,relheight=0.5,relwidth=0.5)

art_1=tk.Button(artik, text=artiklar[1].namn, command=lambda: knapp_art(1))
art_1.place(relx=0.5, rely=0,relheight=0.5,relwidth=0.5)

art_2=tk.Button(artik, text=artiklar[2].namn, command=lambda: knapp_art(2))
art_2.place(relx=0.0, rely=0.5,relheight=0.5,relwidth=0.5)

art_3=tk.Button(artik, text=artiklar[3].namn, command=lambda: knapp_art(3))
art_3.place(relx=0.5, rely=0.5,relheight=0.5,relwidth=0.5)


#kvitto display
kvitt = tk.Frame(root, bg="#ff00ff", bd=5)
kvitt.place(relx=0, rely=0, relheight=0.75, relwidth=0.5)

antal=tk.Label(kvitt,text="antal\n", anchor="nw", bg="#dddddd")
antal.place(relx=0, rely=0, relheight=1, relwidth=0.1)

namn=tk.Label(kvitt,text="namn\n", anchor="nw")
namn.place(relx=0.1, rely=0, relheight=1, relwidth=0.7)

pris=tk.Label(kvitt,text="pris\n", anchor="nw")
pris.place(relx=0.8, rely=0, relheight=1, relwidth=0.1)

totpris=tk.Label(kvitt,text="pris f.a.\n", anchor="nw")
totpris.place(relx=0.9, rely=0, relheight=1, relwidth=0.1)

#numer display
input = tk.Frame(root, bg="#ff00ff", bd=5)
input.place(relx=0.5, rely=0,relheight=0.1, relwidth=0.5, anchor="nw")

text= tk.Label(input, text=num, font=100)
text.place(relheight=1, relwidth=0.68)

knap_bort = tk.Button(input, text="<", command=lambda: knapp_del())
knap_bort.place(relx=0.69, relheight=1, relwidth=0.2)

knap_c = tk.Button(input, text="C", command=lambda: knapp_clear())
knap_c.place(relx=0.90, relheight=1, relwidth=0.1)

#kategory


#knappar
numpad= tk.Frame(root, bg="#ff00ff", bd=5)
numpad.place(relx=0.5, rely=0.1,relheight=0.65, relwidth=0.5, anchor="nw")

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
