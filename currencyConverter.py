# import module
from tkinter import *
from tkinter import messagebox

# init tkinter
root = Tk()
root.title("Currency Converter")

# Default Height and Width
HEIGHT = 550
WIDTH = 600

# Create Canvas
canvas = Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack(fill="both")


# define getCurrency function
def getcurrency():
    try:
        inr = int(inrVar.get())
    except:
        messagebox.showerror("Error", "Wrong Value of Rupees")
        return
    # Calculate other currency
    usd = round(inr * 0.014, 2)
    bdt = round(inr * 1.19, 2)
    idr = round(inr * 199.54, 2)
    aud = round(inr * 0.021, 2)
    cny = round(inr * 0.10, 2)
    eur = round(inr * 0.013, 2)
    jpy = round(inr * 1.51, 2)
    setcurrency(usd, bdt, idr, aud, cny, eur, jpy)


# define setCurrency Function
def setcurrency(usd, bdt, idr, aud, cny, eur, jpy):
    usdVar.set(usd)
    bdtVar.set(bdt)
    idrVar.set(idr)
    audVar.set(aud)
    cnyVar.set(cny)
    eurVar.set(eur)
    jpyVar.set(jpy)


# define save Currency
def savecurrency():
    try:
        inr = int(inrVar.get())
    except:
        return

    idr = round(inr * 199.54, 2)

    if(inrVar.get() == '') or (idrVar.get() != str(idr)):
        return
    savetext = "Indian Rupee : "+inrVar.get()+"\nUnited States Dollar : "+usdVar.get()+\
               "\nBangladeshi Taka : "+bdtVar.get()+"\nIndonesian Rupiah : "+idrVar.get()+\
               "\nAustralian Dollar : "+audVar.get()+"\nChinese Yuan : "+cnyVar.get()+\
               "\nEuro : "+eurVar.get()+"\nJapanese Yen : "+jpyVar.get()+\
               "\n***************************\n"
    with open('currency.txt','a') as fh:
        fh.write(savetext)


# Design Frontend
# set Frame
mainFrame = Frame(root, bg="#fff")
mainFrame.place(relwidth=1, relheight=1)

# heading Label
headingLabel = Label(mainFrame, bg="#fff", text="Currency Converter", font=('Verdana', 18))
headingLabel.place(relx=.1, rely=.01, relwidth=.8)

# lower frame
lowerFrame = Frame(mainFrame, bg="#fff")
lowerFrame.place(relheight=.75, relwidth=.7, relx=.15, rely=.1)

# lower part
inrText = Label(lowerFrame, text="Indian Rupee", bg="#fff", anchor='w', font=('verdana', 13))
usdText = Label(lowerFrame, text="United States Dollar", bg="#fff", anchor='w', font=('verdana', 13))
bdtText = Label(lowerFrame, text="Bangladeshi Taka", bg="#fff", anchor='w', font=('verdana', 13))
idrText = Label(lowerFrame, text="Indonesian Rupiah", bg="#fff", anchor='w', font=('verdana', 13))
audText = Label(lowerFrame, text="Australian Dollar", bg="#fff", anchor='w', font=('verdana', 13))
cnyText = Label(lowerFrame, text="Chinese Yuan", bg="#fff", anchor='w', font=('verdana', 13))
eurText = Label(lowerFrame, text="Euro", bg="#fff", anchor='w', font=('verdana', 13))
jpyText = Label(lowerFrame, text="Japanese Yen", bg="#fff", anchor='w', font=('verdana', 13))

inrText.place(relwidth=.44, rely=0)
usdText.place(relwidth=.44, rely=.12)
bdtText.place(relwidth=.44, rely=.24)
idrText.place(relwidth=.44, rely=.36)
audText.place(relwidth=.44, rely=.48)
cnyText.place(relwidth=.44, rely=.6)
eurText.place(relwidth=.44, rely=.72)
jpyText.place(relwidth=.44, rely=.84)

inrVar = StringVar()
usdVar = StringVar()
bdtVar = StringVar()
idrVar = StringVar()
audVar = StringVar()
cnyVar = StringVar()
eurVar = StringVar()
jpyVar = StringVar()

inrEntry = Entry(lowerFrame, font=('verdana', 12), textvariable=inrVar, justify='center', bg="#e3e3e3")
usdLabel = Label(lowerFrame, textvariable=usdVar, font=('verdana', 12))
bdtLabel = Label(lowerFrame, textvariable=bdtVar, font=('verdana', 12))
idrLabel = Label(lowerFrame, textvariable=idrVar, font=('verdana', 12))
audLabel = Label(lowerFrame, textvariable=audVar, font=('verdana', 12))
cnyLabel = Label(lowerFrame, textvariable=cnyVar, font=('verdana', 12))
eurLabel = Label(lowerFrame, textvariable=eurVar, font=('verdana', 12))
jpyLabel = Label(lowerFrame, textvariable=jpyVar, font=('verdana', 12))

inrEntry.place(relwidth=.4, rely=0, relx=.5, relheight=.07)
usdLabel.place(relwidth=.4, rely=.12, relx=.5, relheight=.07)
bdtLabel.place(relwidth=.4, rely=.24, relx=.5, relheight=.07)
idrLabel.place(relwidth=.4, rely=.36, relx=.5, relheight=.07)
audLabel.place(relwidth=.4, rely=.48, relx=.5, relheight=.07)
cnyLabel.place(relwidth=.4, rely=.60, relx=.5, relheight=.07)
eurLabel.place(relwidth=.4, rely=.72, relx=.5, relheight=.07)
jpyLabel.place(relwidth=.4, rely=.84, relx=.5, relheight=.07)

# set default values
setcurrency(0, 0, 0, 0, 0, 0, 0)

# Calculate Button
calculateButton = Button(mainFrame, text="Calculate", command=getcurrency, relief='raised', bg="#00b894", fg="#fff",
                         font=('verdana', 12), activebackground="#0984e3", activeforeground="#fff")
calculateButton.place(relx=.2, rely=.82, relwidth=.25, relheight=.08)

# Save Button
saveButton = Button(mainFrame, text="Save", command=savecurrency, relief='raised', bg="#0984e3", fg="#fff",
                    font=('verdana', 12), activebackground="#00b894", activeforeground="#fff")
saveButton.place(relx=.55, rely=.82, relwidth=.25, relheight=.08)

#copyright
copyrightText = Label(mainFrame, text="Developed By Sandip Sadhukhan", bg="#fff")
copyrightText.place(relx=.1, rely=.93, relwidth=.8)

# program end
root.mainloop()
