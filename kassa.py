import tkinter as tk
from fpdf import FPDF
import os
import datetime

class art:
	def __init__(self, namn, moms):
		self.namn=namn
		self.moms=moms

class alt:
	def __init__(self, namn, mng):
		self.namn=namn
		self.mng=mng

class prod:
	def __init__(self, namn, antal, pris, moms):
		self.namn=namn	
		self.antal=antal
		self.pris=pris	
		self.moms=moms

	def totpris(self):
		return (self.pris*self.antal)

class betal(prod):
	def __init__(self, namn, antal, pris):
		self.namn=namn	
		self.antal=antal
		self.pris=pris	


hj=1080
br=1920
num=0
kvitto=[]
artiklar=[art("livsmedel",12), art("godis",12), art("hygien",25), art("dricka",12)]
betal_alt=["kort","kontant"]


def vaxel():
	global kvitto
	opt=0
	for x in range(0,len(kvitto)):
		opt+=kvitto[x].totpris()
	return opt
	
def betmng():
	global kvitto
	betal=[]
	for x in range(0, len(kvitto)):
		if(kvitto[x].totpris()<0):
			print(kvitto[x].namn)
			if(len(betal)==0):
				betal.append(alt(kvitto[x].namn, kvitto[x].totpris()))
			else:
				cont=0
				for y in range(0, len(betal)):
					if(kvitto[x].namn == betal[y].namn):
						betal[y].mng+=kvitto[x].totpris()
						cont=1
				if(cont==0):
					betal.append(alt(kvitto[x].namn, kvitto[x].totpris()))
	for x in range(0, len(betal)):
		print(betal[x].namn+" "+str(betal[x].mng))
	return betal



def genkvitto():
	betal=betmng()
	global kvitto
	nu=datetime.datetime.now()
	mapp=nu.strftime("kvitton/%Y/%m/%d/")
	kb=80
	kl=100+(len(kvitto)*10)
	pdf = FPDF('P','mm',(kb, kl))
	pdf.set_margins(0,0,0)
	pdf.add_page()
	pdf.set_font('Arial', 'B', 12)
	pdf.cell(kb, 10, 'kvitto', 'B', 2, 'C')
	pdf.cell((kb*0.5), 10, 'datum:', 'T', 0, 'L')
	pdf.cell((kb*0.5), 10, nu.strftime("%Y-%m-%d"), 'T', 1, 'R')
	pdf.cell((kb*0.5), 10, 'tid:', 'B', 0, 'L')
	pdf.cell((kb*0.5), 10, nu.strftime("%H:%M"), 'B', 1, 'R')
	pdf.cell((kb*0.15), 10, 'antal', 1, 0, 'L')
	pdf.cell((kb*0.7), 10, 'namn', 1, 0, 'L')
	pdf.cell((kb*0.15), 10, 'pris', 1, 1, 'L')
	
	for x in range(0,len(kvitto)):
		if(kvitto[x].totpris()>0):
			pdf.cell((kb*0.15), 10, str(kvitto[x].antal), 1, 0, 'L')
			pdf.cell((kb*0.7), 10, kvitto[x].namn , 1, 0, 'L')
			pdf.cell((kb*0.15), 10, str(kvitto[x].totpris()), 1, 1, 'L')
	
	pdf.cell(kb, 5,"",0,1)
	pdf.set_font('Arial', 'B', 24)
	pdf.cell((kb*0.5), 10, 'Totalt:', 0, 0, 'L')
	pdf.cell((kb*0.5), 10, str(totalt())+"SEK", 0, 1, 'R')
	if(vaxel()<0):
		pdf.cell((kb*0.5), 10, 'växel:', 0, 0, 'L')
		pdf.cell((kb*0.5), 10, str(vaxel()*-1)+"SEK", 0, 1, 'R')
	pdf.set_font('Arial', 'B', 16)
	pdf.cell((kb*0.5), 10, '', 0, 1, 'L')
	for x in range(0, len(betal)):
		pdf.cell((kb*0.5), 5, betal[x].namn, 0, 0, 'L')
		pdf.cell((kb*0.5), 5, str(betal[x].mng*-1)+"SEK", 0, 1, 'R')
	
	if not os.path.exists(mapp):
		os.makedirs(mapp)
	pdf.output( mapp+nu.strftime("%H_%M_%S.pdf"), 'F')
	pdf.output( "senaste.pdf", 'F')
	kvitto.clear()
	update_display()


def update_input():
	global num
	text['text']= num

def totalt():
	global kvitto
	tot=0
	for x in range(0,len(kvitto)):
		if(kvitto[x].totpris()>0):
			tot+=kvitto[x].totpris()
	return tot

def update_display():
	if(vaxel()<0):
		totis['text']="totalt: "+str(totalt())+ "\t växel: "+ str(vaxel()*-1)
	else:
		totis['text']="totalt: "+str(totalt())+ "\t kvar att betala: "+ str(vaxel())
		
	antal['text']="antal\n"
	namn['text']="namn\n"
	pris['text']="pris\n"
	totpris['text']="pris f.a.\n"

	knapp_bet0['bg']="#dddddd"
	knapp_bet0['activebackground']="#dddddd"
	knapp_bet1['bg']="#dddddd"
	knapp_bet1['activebackground']="#dddddd"

	for x in range(0,len(kvitto)):
		antal['text']+=str(kvitto[x].antal) + "\n"
		namn['text']+=kvitto[x].namn + "\n"
		pris['text']+=str(kvitto[x].pris) + "\n"
		totpris['text']+=str(kvitto[x].totpris()) + "\n"

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

def knapp_tryck(inp):
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
	update_input()
	update_display()

def knapp_remove():
	global kvitto
	kvitto.pop(len(kvitto)-1)
	update_display()	

def knapp_betal(inp):
	global num
	if(len(kvitto)>0):
		if(inp == 0):
			knapp=knapp_bet0
		if(inp== 1):	
			knapp=knapp_bet1
	
		if(num == 0):
			if(knapp['bg']=="#00ff00"):
				kvitto.append(betal(betal_alt[inp],1,(vaxel()*-1)))
				update_display()
			else:
				knapp['bg']="#00ff00"
				knapp['activebackground']="#00ff00"
		else:
			kvitto.append(betal(betal_alt[inp],1,(num*-1)))
			update_display()
		if(vaxel()<=0):
			genkvitto()
	num=0
	update_input()


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

knapp_mer=tk.Button(set, text="+", bg="#dddddd", fg="#000000", command=lambda: knapp_plus())
knapp_mer.place(relx=0,rely=0,relheight=0.5,relwidth=(1/3))

knapp_min=tk.Button(set, text="-", bg="#dddddd", fg="#000000", command=lambda: knapp_minus())
knapp_min.place(relx=0.333,rely=0,relheight=0.5,relwidth=(1/3))

knapp_undo=tk.Button(set, text="ångra", bg="#dddddd", fg="#000000", command=lambda: knapp_remove())
knapp_undo.place(relx=0.666,rely=0,relheight=0.5,relwidth=(1/3))


knapp_bet0=tk.Button(set, text=betal_alt[0], bg="#dddddd", fg="#000000", command=lambda: knapp_betal(0))
knapp_bet0.place(relx=0,rely=0.5,relheight=0.5,relwidth=0.5)

knapp_bet1=tk.Button(set, text=betal_alt[1], bg="#dddddd", fg="#000000", command=lambda: knapp_betal(1))
knapp_bet1.place(relx=0.5,rely=0.5,relheight=0.5,relwidth=0.5)


#artiklar
artik=tk.Frame(root, bg="#ff00ff", bd=5)
artik.place(relx=0.5,rely=0.75,relheight=0.25,relwidth=0.5)

art_0=tk.Button(artik, text=artiklar[0].namn, bg="#dddddd", fg="#000000", command=lambda: knapp_art(0))
art_0.place(relx=0, rely=0,relheight=0.5,relwidth=0.5)

art_1=tk.Button(artik, text=artiklar[1].namn, bg="#dddddd", fg="#000000", command=lambda: knapp_art(1))
art_1.place(relx=0.5, rely=0,relheight=0.5,relwidth=0.5)

art_2=tk.Button(artik, text=artiklar[2].namn, bg="#dddddd", fg="#000000", command=lambda: knapp_art(2))
art_2.place(relx=0.0, rely=0.5,relheight=0.5,relwidth=0.5)

art_3=tk.Button(artik, text=artiklar[3].namn, bg="#dddddd", fg="#000000", command=lambda: knapp_art(3))
art_3.place(relx=0.5, rely=0.5,relheight=0.5,relwidth=0.5)


#kvitto display
kvitt = tk.Frame(root, bg="#ff00ff", bd=5)
kvitt.place(relx=0, rely=0, relheight=0.70, relwidth=0.5)

antal=tk.Label(kvitt,text="antal\n", anchor="nw", bg="#dddddd", fg="#000000",font=100)
antal.place(relx=0, rely=0, relheight=1, relwidth=0.1)

namn=tk.Label(kvitt,text="namn\n", anchor="nw", bg="#dddddd", fg="#000000", font=100)
namn.place(relx=0.1, rely=0, relheight=1, relwidth=0.6)

pris=tk.Label(kvitt,text="pris\n", anchor="nw", bg="#dddddd", fg="#000000", font=100)
pris.place(relx=0.6, rely=0, relheight=1, relwidth=0.2)

totpris=tk.Label(kvitt,text="pris f.a.\n", anchor="nw", bg="#dddddd", fg="#000000", font=100)
totpris.place(relx=0.8, rely=0, relheight=1, relwidth=0.3)

kvitt_bot=tk.Frame(root, bg="#ff00ff",bd=5)
kvitt_bot.place(relx=0, rely=0.70, relheight=0.05, relwidth=0.5)

totis=tk.Label(kvitt_bot,text="totalt: 0", anchor="nw", bg="#dddddd", fg="#000000", font=100)
totis.place(relx=0, rely=0, relheight=1, relwidth=1.2)

#numer display
input = tk.Frame(root, bg="#ff00ff", bd=5)
input.place(relx=0.5, rely=0,relheight=0.1, relwidth=0.5, anchor="nw")

text= tk.Label(input, text=num, font=100, bg="#dddddd", fg="#000000")
text.place(relheight=1, relwidth=0.68)

kanpp_bort = tk.Button(input, text="<", bg="#dddddd", fg="#000000", command=lambda: knapp_del())
kanpp_bort.place(relx=0.69, relheight=1, relwidth=0.2)

knapp_c = tk.Button(input, text="C", bg="#dddddd", fg="#000000", command=lambda: knapp_clear())
knapp_c.place(relx=0.90, relheight=1, relwidth=0.1)

#kategory


#knappar
numpad= tk.Frame(root, bg="#ff00ff", bd=5)
numpad.place(relx=0.5, rely=0.1,relheight=0.65, relwidth=0.5, anchor="nw")

knapp_0 = tk.Button(numpad, text="0", bg="#dddddd", fg="#000000", command=lambda: knapp_tryck(0))
knapp_0.place(relx=0, rely=0.78, relwidth=1, relheight=0.22) 

knapp_1 = tk.Button(numpad, text="1", bg="#dddddd", fg="#000000", command=lambda: knapp_tryck(1))
knapp_1.place(relx=0, rely=0, relwidth=0.3, relheight=0.25) 

knapp_2 = tk.Button(numpad, text="2", bg="#dddddd", fg="#000000", command=lambda: knapp_tryck(2))
knapp_2.place(relx=0.35, rely=0, relwidth=0.3, relheight=0.25) 

knapp_3 = tk.Button(numpad, text="3", bg="#dddddd", fg="#000000", command=lambda: knapp_tryck(3))
knapp_3.place(relx=0.7, rely=0, relwidth=0.3, relheight=0.25) 

knapp_4 = tk.Button(numpad, text="4", bg="#dddddd", fg="#000000", command=lambda: knapp_tryck(4))
knapp_4.place(relx=0, rely=0.26, relwidth=0.3, relheight=0.25) 

knapp_5 = tk.Button(numpad, text="5", bg="#dddddd", fg="#000000", command=lambda: knapp_tryck(5))
knapp_5.place(relx=0.35, rely=0.26, relwidth=0.3, relheight=0.25) 

knapp_6 = tk.Button(numpad, text="6", bg="#dddddd", fg="#000000", command=lambda: knapp_tryck(6))
knapp_6.place(relx=0.7, rely=0.26, relwidth=0.3, relheight=0.25) 

knapp_7 = tk.Button(numpad, text="7", bg="#dddddd", fg="#000000", command=lambda: knapp_tryck(7))
knapp_7.place(relx=0, rely=0.52, relwidth=0.3, relheight=0.25) 

knapp_8 = tk.Button(numpad, text="8", bg="#dddddd", fg="#000000", command=lambda: knapp_tryck(8))
knapp_8.place(relx=0.35, rely=0.52, relwidth=0.3, relheight=0.25)

knapp_9 = tk.Button(numpad, text="9", bg="#dddddd", fg="#000000", command=lambda: knapp_tryck(9))
knapp_9.place(relx=0.7, rely=0.52, relwidth=0.3, relheight=0.25) 

knapp_0 = tk.Button(numpad, text="0", bg="#dddddd", fg="#000000", command=lambda: knapp_tryck(0))
knapp_0.place(relx=0, rely=0.78, relwidth=1, relheight=0.22) 

root.mainloop()
