from tkinter import *
from functools import partial

pizzaPalace = Tk(className="PIZZA PALACE")
pizzaPalace.geometry("500x400")

rowNo = 2

pizzas = [["Margherita", "£3.55"],["Pepperoni","£3.99"],["Hawaiian","£4.25"],["Italian","£4.59"],["Vegetable Feast","£3.99"]]
receipt = []

def results(stuffedC, var):
    myVal = var.get()
    print(myVal)
    if myVal == 1:
        print("It worked!")
    stuffedC.destroy()
    
def stuffedCrusts(desire):
    stuffedC = Tk(className = "Stuffed Crusts")
    stuffedC.geometry("500x400")
    
    message = Label(stuffedC, text="If you would like stuffed Crusts, it will be an extra £1 per person")
    message.grid(row=2, columnspan=8)

    message = Label(stuffedC, text="The pizza chosen is " + str(desire))
    message.grid(row=3, columnspan=8)

    var = IntVar()
    check = Checkbutton(stuffedC, text="Add Stuffed Crusts", variable=var, onvalue=1, offvalue=0)
    check.grid(row=4,sticky= W)

    message2 = Label(stuffedC, text="How many people are eating?")
    message2.grid(row=5, column = 0)

    choice = StringVar()
    choice.set("N/A")
    amount = OptionMenu(stuffedC, choice, "N/A","1","2","3","4","5","6","7","8")
    amount.grid(row=5, column= 1, sticky= W)

    Quit = Button(stuffedC, text="Finished and Save", command= partial(results, stuffedC, var))
    Quit.grid(row=6)
    
    stuffedC.mainloop()

def total(pizza, price):
    print(receipt)


label1 = Label(pizzaPalace, text="Welcome to Pizza Palace!")
label1.grid(column=5)

label2 = Label(pizzaPalace, text="PLease select your pizza and how many you would like to order...")
label2.grid(row=1, columnspan=8)

for i in pizzas:
    pizza = Label(pizzaPalace, text=i[0])
    pizza.grid(row=rowNo)
    price = Label(pizzaPalace,text=i[1])
    price.grid(row=rowNo, column=2)
    buttonA = Button(pizzaPalace, text="+", command=partial(stuffedCrusts, i[0]))
    buttonA.grid(row=rowNo, column=3)
    rowNo +=1
    receipt.append(i[0])
    receipt.append(i[1])

finish = Button(pizzaPalace, text= "Finish and Pay", command= partial(total, i[0], i[1]))
finish.grid(row=8)
pizzaPalace.mainloop()

