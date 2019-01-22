from tkinter import *
from tkinter.filedialog import askopenfilename

class Application(Frame):
    nazwa_pliku = ""
    sciezka_pliku = ""
    tekst_od = ""
    tekst_do = ""
    tekst_do_num = 0
    wynik = ""
    radioVar = 0 # 1 to ciąg, 2 ilość znaków

    def __init__(self,master):
        Frame.__init__(self,master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.button1 = Button(self, text = "Przeglądaj", command = self.fileopen)
        self.button1.grid(pady = "10", row = 0, column = 0, sticky = W)
        self.labelTekst = Label(self, text = "Wybrany plik: ")
        self.labelTekst.grid(row = 0, sticky = E)
        self.labelPlik = Label(self)
        self.labelPlik.grid(row = 1, sticky = W)
        self.radioZnaki = Radiobutton(self, text = "Określ koniec ciągiem znaków", variable = self.radioVar, value = 1, command = self.radioAkcjaZnak)
        self.radioZnaki.grid(pady = "1", row = 2, column = 0, sticky = W)
        self.radioIlosc = Radiobutton(self, text = "Określ ilość znaków wycięcia", variable = self.radioVar, value = 0, command = self.radioAkcjaIlosc)
        self.radioIlosc.grid(row = 3, column = 0, sticky = W)
        self.labelOd = Label(self, text = "Wytnij od: ")
        self.labelOd.grid(pady = "1", row = 4, column = 0, sticky = W)
        self.entryOd = Entry(self)
        self.entryOd.grid(row = 4, sticky = E)
        self.labelDo = Label(self, text = "Wytnij do: ")
        self.labelDo.grid(row = 5, sticky = W)
        self.entryDo = Entry(self)
        self.entryDo.grid(row = 5, sticky = E)
        self.button2 = Button(self, text = "Przerabiaj", command = self.glownaAkcja)
        self.button2.grid(pady = "10", row = 6, sticky = W)

    def fileopen(self):
        Application.sciezka_pliku = askopenfilename()
        Application.nazwa_pliku = Application.sciezka_pliku[Application.sciezka_pliku.rfind("/")+1:]
        self.labelPlik.config(text=Application.nazwa_pliku)

    def radioAkcjaZnak(self):
        self.labelDo.config(text="Wytnij do: ")
        Application.radioVar = 1

    def radioAkcjaIlosc(self):
        self.labelDo.config(text="Ilość znak: ")
        Application.radioVar = 2
            
    def glownaAkcja(self):
        with open(Application.sciezka_pliku,"r") as plik:
            tekst = plik.read()
        print(tekst)
        Application.tekst_od = self.entryOd.get()
        fragment_tekstu = ""
        
        if Application.radioVar == 1:
            Application.tekst_do = self.entryDo.get()
            fragment_tekstu = tekst[tekst.find(Application.tekst_od):tekst.find(Application.tekst_do)]
            print(fragment_tekstu)
        elif Application.radioVar == 2:
            Application.tekst_do_num = self.entryDo.get()
            intt = tekst.find(Application.tekst_od) + int(self.entryDo.get())
            fragment_tekstu = tekst[tekst.find(Application.tekst_od):intt]
            print(fragment_tekstu)

        with open("nowy_plik.txt","w") as plik2:
            plik2.write(fragment_tekstu)   
            
                
        
root = Tk()
root.title("CutMe")
root.geometry("220x200")

app = Application(root)
root.mainloop()
