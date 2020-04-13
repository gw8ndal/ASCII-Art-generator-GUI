from PIL import Image
import io
import easygui
from resizeimage import resizeimage
import webbrowser
import tkinter
import os


def opencommand():
	try:
		image_path = easygui.fileopenbox(title = 'Ouvrir une image', default = '*.png', filetypes = ['*.jpg', '*.jpeg', '*.png'],)
		opencommand.image_ouverte = Image.open(image_path)
	except:
		print("Impossible d'ouvrir l'image")
		opencommand()

def variable_largeur(*args):
	variable_largeur.largeur_var = largeur_var1.get()

def open_image():
	#	Replace Kwrite by your current text editor
	os.system('kwrite final_image.txt')

def convertisseur():
	resX = int(variable_largeur.largeur_var)
	resY = resX
	image = resizeimage.resize_thumbnail(opencommand.image_ouverte, [resX, resY])
	largeur, hauteur = image.size
	convertisseur.output = io.StringIO()
	image_nb = image.convert('L')
	for y in range(0, hauteur, 2):
		for x in range(largeur):
			value = image_nb.getpixel((x, y))
			if value < 28:
				convertisseur.output.write('@')
			elif value < 56:
				convertisseur.output.write('%')
			elif value < 84:
				convertisseur.output.write('#')
			elif value < 112:
				convertisseur.output.write('*')
			elif value < 140:
				convertisseur.output.write('+')
			elif value < 168:
				convertisseur.output.write('=')    
			elif value < 196:
				convertisseur.output.write('-')
			elif value < 224:
				convertisseur.output.write(':')
			else :
				convertisseur.output.write('.')
		convertisseur.output.write('\n')

	with open('final_image.txt', mode = 'w') as f:
		print(convertisseur.output.getvalue(), file = f)
	open_image()


app = tkinter.Tk()
app.title('ASCII Art Generator')
app.geometry('330x190')
app.resizable(False, False)

largeur_var1 = tkinter.StringVar()

largeur_var1.trace("w", variable_largeur)

Largeur_Frame = tkinter.LabelFrame(app, border = 0)
Largeur_label = tkinter.Label(Largeur_Frame, text = "Final image width (Recommended max 400)", font = 'Ubuntu 10')
Open_button = tkinter.Button(app, text = 'Open an image', command = opencommand, bg = '#9b59b6', fg = 'black', height = 2, width = 17)
Largeur_button = tkinter.Entry(Largeur_Frame, textvariable = largeur_var1, bg = '#9b59b6', fg = 'black', border = 0)
Confirm_button = tkinter.Button(app, text = 'Convert', command = convertisseur, bg = '#9b59b6', fg = 'black', height = 2, width = 17)

Open_button.pack(padx = 5, pady = 5)
Largeur_Frame.pack()
Largeur_label.pack(pady = 5)
Largeur_button.pack(padx = 5, pady = 5)
Confirm_button.pack(pady = 5)
app.mainloop()