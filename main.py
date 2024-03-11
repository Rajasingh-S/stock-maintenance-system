from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from db import *
o1=purchase()
o2=sold()
dele=delete()
b=bill()
dx=orderdisplay()

win=Tk()
win.title("Stock Maintenance System")
win.geometry("1366x768")
win.state("zoomed")

#Purchase Entry Frame

frame=Frame(win,bg="grey")
frame.pack(side=TOP,fill=X)

titlel=Label(frame,text="purchase  Entry",bg="grey",fg="red",font=("calibri",18,"bold"))
titlel.grid(row=0,column=0)

titlel2=Label(frame,text="Selling Entry",bg="grey",fg="red",font=("calibri",18,"bold"))
titlel2.grid(row=0,column=5)

# Entry box text
itemidp=StringVar()
itemids=StringVar()

itemnamep=StringVar()
itemnames=StringVar()

qtyp=IntVar()
qtys=IntVar()

pricep=IntVar()
prices=IntVar()

totqty=IntVar()
sellqty=IntVar()
purp=IntVar()
sellp=IntVar()
bs=IntVar()

# Creating Labels and Entry boxes
# Item Id
itemidl=Label(frame,bg="grey",fg="white",text="Item Id",font=("courier",18,"bold"))
itemidl.grid(row=1,column=0,sticky="w",padx=20,pady=20)
textitemid=Entry(frame,bg="goldenrod3",fg="black",font=("Courier",16),bd=0,textvariable=itemidp)
textitemid.grid(row=1,column=1,sticky="w")

itemidl2=Label(frame,bg="grey",fg="white",font=("courier",18,"bold"),text="Item Id")
itemidl2.grid(row=1,column=4,sticky="w")
itemidl2=Entry(frame,fg="black",bd=0,font=("courier",16),state="readonly",textvariable=itemids,readonlybackground="goldenrod3")
itemidl2.grid(row=1,column=5,sticky="w")

#Item name
itemnamel=Label(frame,bg="grey",fg="white",text="Item Name",font=("courier",18,"bold"))
itemnamel.grid(row=2,column=0,padx=20,pady=20,sticky="w")
textitemname=Entry(frame,bg="goldenrod3",fg="black",font=("Courier",16),bd=0,textvariable=itemnamep)
textitemname.grid(row=2,column=1,sticky="w")

itemnamel2=Label(frame,bg="grey",fg="white",font=("courier",18,"bold"),text="Item Name")
itemnamel2.grid(row=2,column=4,sticky="w")
textitemname2=Entry(frame,fg="black",bd=0,font=("courier",16),textvariable=itemnames,state="readonly",readonlybackground="goldenrod3")
textitemname2.grid(row=2,column=5,sticky="w")

# Quantity

purqtyl=Label(frame,bg="grey",fg="white",text="Quantity",font=("courier",18,"bold"))
purqtyl.grid(row=3,column=0,padx=20,pady=20,sticky="w")
textpurqty=Entry(frame,bg="goldenrod3",fg="black",font=("Courier",16),bd=0,textvariable=qtyp)
textpurqty.grid(row=3,column=1,sticky="w")

purqtyl2=Label(frame,bg="grey",fg="white",font=("courier",18,"bold"),text="Quantity")
purqtyl2.grid(row=3,column=4,sticky="w")
textqty2=Entry(frame,fg="black",bd=0,font=("courier",16),bg="goldenrod3",textvariable=qtys)
textqty2.grid(row=3,column=5,sticky="w")

# Price

sellpricel=Label(frame,bg="grey",fg="white",text="Price",font=("courier",18,"bold"))
sellpricel.grid(row=4,column=0,padx=20,pady=20,sticky="w")
textsell=Entry(frame,bg="goldenrod3",fg="black",font=("Courier",16),bd=0,textvariable=pricep)
textsell.grid(row=4,column=1,sticky="w")

sellpricel2=Label(frame,bg="grey",fg="white",font=("courier",18,"bold"),text="Price")
sellpricel2.grid(row=4,column=4,sticky="w",padx=10)
textsell2=Entry(frame,fg="black",bd=0,font=("courier",16),bg="goldenrod3",textvariable=prices)
textsell2.grid(row=4,column=5)
# New Frame

frame2=Frame(frame,bg="grey")
frame2.grid(row=5,column=0,columnspan=5)

# Total Quantity
totql=Label(frame2,text="tot.qty",fg="blue",font=("courier",18,"bold"),bg="grey")
totql.grid(row=0,column=0)
texttotq=Entry(frame2,bd=0,state="readonly",readonlybackground="brown",textvariable=totqty,font=("calibri",16,"bold"),fg="white",width=6)
texttotq.grid(row=0,column=1,sticky="w")

# selling Quantity

sellql=Label(frame2,text="Sell.Qty",fg="blue",font=("courier",18,"bold"),bg="grey")
sellql.grid(row=0,column=2,sticky="w",padx=20)
textsellq=Entry(frame2,bd=0,state="readonly",readonlybackground="brown",textvariable=sellqty,font=("calibri",16,"bold"),fg="white",width=6)
textsellq.grid(row=0,column=3)

# Purchasae price

purpl=Label(frame2,text="Pur.Price",fg="blue",font=("courier",18,"bold"),bg="grey")
purpl.grid(row=0,column=4,sticky="w",padx=20)
textpurp=Entry(frame2,bd=0,state="readonly",readonlybackground="brown",textvariable=purp,font=("calibri",16,"bold"),fg="white",width=6)
textpurp.grid(row=0,column=5)

# Selling price

sellpl=Label(frame2,text="Sell.Price",fg="blue",font=("courier",18,"bold"),bg="grey")
sellpl.grid(row=0,column=6,sticky="w",padx=20)
sellptext=Entry(frame2,bd=0,state="readonly",readonlybackground="brown",textvariable=sellp,font=("calibri",16,"bold"),fg="white",width=6)
sellptext.grid(row=0,column=7)

# Balance Stock

bsl=Label(frame2,text="Bal.St",fg="blue",font=("courier",18,"bold"),bg="grey")
bsl.grid(row=0,column=8,sticky="w",padx=20)
bstext=Entry(frame2,bd=0,state="readonly",readonlybackground="brown",textvariable=bs,font=("calibri",16,"bold"),fg="white",width=6)
bstext.grid(row=0,column=9)





# for using clicking event in getdata
def getdata(Event):
    data=tv.focus()
    data2=tv.item(data)
    global rows
    rows=data2["values"]
   # errror=0
    #print(rows)
    #print(data2)
    itemidp.set(rows[1])
    itemnamep.set(rows[2])
    #pricep.set(rows[4])
    #qtyp.set(rows[5])

    itemids.set(rows[1])
    itemnames.set(rows[2])


    # Total Quantity

    totpurchase=o1.pamount(rows[1])
    purp.set(totpurchase)

    # balance Stock

    bst=o1.select(rows[1])
    bs.set(bst)

    # Purchase Quantity

    qty=o1.totqty(rows[1])
    totqty.set(qty)

    # Sold total Price

    totsprice=o2.samount(rows[1])
    sellp.set(totsprice)

    #selling total quantity
    stotqty=o2.totqty(rows[1])
    sellqty.set(stotqty)
    global error
    error=1
    return rows
# def tempbill():
# global billi
billi = 0
#print('kaka',billi)
def sell():
    if itemids.get()=="" or itemnames.get()=="" or qtys.get()=="" or prices.get()=="":
        messagebox.showerror('Input Error','Fill All Details')
    else:
        # Checking balance Stock
        balancestock=o2.select(itemids.get())
        if balancestock<qtys.get():
            messagebox.showerror('','Please Enter Available Stocks only')
            return
        if balancestock==0:
            messagebox.showerror('','Currently Not Available')
            return

        if qtys.get()==0:
            messagebox.showerror('','Must Enter Quantity')
            return

        x=1
        if x==1:
            t=b.getbillid(-1)
            totbillid=t
            a=-2
            while t==-1:
               t=b.getbillid(a)
               a+=-1
               #print('a:',a,' t:',t)
               x=0
        if x==0:
            t+=1
        '''
        # Adding process total of bill
        totp=b.getlastot()
        while totbillid!=-1:
            totp+=prices.get()
        b.inserttot(t,totp)
        '''
        #print("main check:",t)
        billid='s'+str(t)
        b.bills(t,billid,dt.date.today())
        tot=qtys.get()*prices.get()
        z=t
        k=str(z)
        #print(type(t))
        dx.dis('Selling',itemids.get(),itemnames.get(),qtys.get(),prices.get(),tot,dt.date.today(),k)
        o2.soldp('Selling',itemids.get(),itemnames.get(),qtys.get(),prices.get(),tot,dt.date.today(),t)
        tot=qtys.get()*prices.get()
        b.mainbill(itemnames.get(),qtys.get(),prices.get(),tot,t)
        messagebox.showinfo('','Successfully Added')
    # Purpose of Deleting operation
    global rows
    rows=[]

    clear()
    display()


def clear():
    itemidp.set("")
    itemids.set("")

    itemnamep.set("")
    itemnames.set("")

    qtyp.set(0)
    qtys.set(0)

    pricep.set(0)
    prices.set(0)

    totqty.set(0)
    sellqty.set(0)
    purp.set(0)
    sellp.set(0)
    bs.set(0)
    textdis.delete(1.0,END)


def pur():
    if itemidp.get()=="" or itemnamep.get()=="" or qtyp.get()=="" or pricep.get()=="":
        messagebox.showerror('Input Error','Fill All Details')
    else:
        if  qtyp.get()==0:
            messagebox.showerror('','Must Enter Quantity')
            return
        tot=qtyp.get()*pricep.get()
        dx.dis('Purchase',itemidp.get(),itemnamep.get(),qtyp.get(),pricep.get(),tot,dt.date.today(),'')
        o1.add('Purchase',itemidp.get(),itemnamep.get(),qtyp.get(),pricep.get(),tot,dt.date.today())
        messagebox.showinfo('','Successfully Added')
        clear()
        display()
def display():
    tv.delete(*tv.get_children())
    '''
    for row in o1.fetch():
       # print("1 oook")
        tv.insert("",END,values=row)
    for row in o2.fetch():
       # print("2 oook")
        tv.insert("",END,values=row)
    '''
    global error
    error=0
    for row in dx.getdis():
        if row[0]=='Selling':
            row=list(row)
            row[7]='      s'+str(row[7])
        tv.insert("",END,values=row)

def delete():
   if error==1:
        if rows:
            #print("del",rows)
            #print(rows[0])
            rows[1]=str(rows[1])
            #print("Item id",rows[1],type(rows[1]))
            dele.purch(rows[1])
            dele.bsdel(rows[1])
            dele.delptotqty(rows[1])
            dele.delstotqty(rows[1])
            # Getting last billid

            #temp = b.lastbillid()


            t = b.getbillid(-1)
            a = -2
            while t == -1:
                t = b.getbillid(a)
                a += -1
                #print('a:', a, ' t:', t)
            t+=1


            dele.delsold(rows[1])
            o2.soldp("", "", "", 0, 0, 0, "", t)

            dele.deltotp(rows[1])
            dele.deltots(rows[1])
            dele.deldis(rows[1])
           # print("jbhjvhj")
            #dele.sno(rows[2])
            rows.clear()
            messagebox.showinfo('','Deleted')
            clear()
            display()

   else:
        messagebox.showerror('','Not selected')
# Creating Buttons
purb=Button(frame,text="PUR",bg="black",fg="green",bd=0,font=("family",12,"bold"),width=7,height=0,command=pur)
purb.grid(row=1,column=2)

pur=Button(frame,text="SELL",bg="black",fg="green",bd=0,font=("family",12,"bold"),width=7,height=0,command=sell)
pur.grid(row=2,column=2)

clr=Button(frame,text="CLR",bg="black",fg="green",font=("family",12,"bold"),bd=0,width=7,height=0,command=clear)
clr.grid(row=3,column=2)

d=Button(frame,text="DEL",bg="black",fg="green",font=("family",12,"bold"),bd=0,width=7,height=0,command=delete)
d.grid(row=4,column=2)



# Creating Tree View
frametree=Frame(win,bg="pink")
frametree.place(x=0,y=360,width=750,height=335)
# Creating Scroll bars for Treeview
treescroll=Scrollbar(frametree,orient=VERTICAL)
treescroll.pack(side=RIGHT,fill=Y)

# Body of Tree
style=ttk.Style()
style.configure("mystyle.Treeview",font=("calibri",14),rowheight=28)

# Body of Heading
style.configure("mystyle.Treeview.Heading",font=("calibri",16,"bold"))

treelabel=Label(frametree,bg="pink",text="Transactions",fg="black",font=("courier",16,"bold"))
treelabel.pack()

tv=ttk.Treeview(frametree,columns=(1,2,3,4,5,6,7,8),style="mystyle.Treeview",yscrollcommand=treescroll.set)
# Scrollbar
treescroll.configure(command=tv.yview)
tv.heading("1",text="Type")
tv.column("1",width=2)

tv.heading("2",text="Id")
tv.column("2",width=2)

tv.heading("3",text="Item")
tv.column("3",width=2)

tv.heading("4",text="Qty")
tv.column("4",width=2)

tv.heading("5",text="Price")
tv.column("5",width=2)

tv.heading("6",text="tot")
tv.column("6",width=2)

tv.heading("7",text="Date")
tv.column("7",width=2)

tv.heading("8",text="Bill id")
tv.column("8",width=2)

tv.bind("<ButtonRelease-1>",getdata)
tv['show']=['headings']
tv.pack(fill=X)
display()

# Creating Billing TreeView

framebill=Frame(win,bg="pink")
framebill.place(x=750,y=360,width=615,height=335)
billL=Label(framebill,font=("courier",16,"bold"),bg="pink",fg="black",text="Billing View")
billL.pack()
# Creating Scroll bar for text box
textscroll=Scrollbar(framebill)
textscroll.pack(side=RIGHT,fill=Y)

# Creating text page
#listt=["Raja","Akash","Blesson"]
textdis=Text(framebill,width=55,height=12,font=("calibri",16),yscrollcommand=textscroll.set)
textscroll.configure(command=textdis.yview)
textdis.pack()
'''
for i in listt:
    textdis.insert(END,i+"\n")

'''
def billselling():
   if error==1:
       if rows[0] == 'Selling':
           # b.inserttot(-1,0)

           o2.soldp('*', rows[1], '', 0, 0, 0, 0, -1)
           # Getting date and bill id
           # Taking interger value in bill id
           lst = []
           y = rows[7]
           for i in y:
               lst.append(i)
           h = -1
           c = ''
           while lst[h] != 's':
               c = lst[h] + c
               h += -1
           s = int(c)

           #print("yyyyyyyyyyy", c)
           # Getting total of bill
           temptot = 0
           for i in b.totalbill(s):
               i = i[-1]
               temptot += i
           #print("tot", temptot)

           #print("sxsfcdfdc", s, type(s))
           temp = b.getbillidanddate(s)
           #print("row 7", rows[7], type(rows[7]))
           # Getting data of body for billing
           #print(temp[0])
           bo = b.gettingbody(temp[0])
           #print("bo0:", bo)
           length = len(bo)
           i = 0

           while i < length:
               t1 = list(bo[i])
               #print("t1:", t1)
               t1[0] = '         ' + str(i + 1) + '.                         '
               # x=str(t1[0])
               #  y='.  '
               # t1[0]="".join([x,y])
               t1[2] = '   ' + str(t1[2]) + '  X  '
               t1[3] = '₹' + str(t1[3])
               t1[4] = '    =   ' + '₹' + str(t1[4])
               bo[i] = tuple(t1)
               #print("ipl", bo[i])
               i += 1
           #print('bo1:', bo)
           t = list(temp)
           t[0] = '       Bill id:' + temp[1] + '                                                           '
           t[1] = 'Date:' + temp[2]
           del t[2]

           textdis.delete(1.0, END)

           # Displaying Bill id and Date
           for i in t:
               textdis.insert(END, i)
           textdis.insert(END, '' + '\n')
           textdis.insert(END,'---------------------------------------------------------------------------------------------------')
           # Displaying body of Bill

           for i in bo:
               #print('bo2', i)
               textdis.insert(END, '' + '\n')
               for j in i:
                   textdis.insert(END, j)
           # textdis.configure(state=DISABLED)
           temptot2 = '                                                           Total=₹' + str(temptot)
           # Inserting Total of bill
           textdis.insert(END, '' + '\n')
           textdis.insert(END, '                                                        ---------------------------------')
           textdis.insert(END, '' + '\n')
           textdis.insert(END, temptot2)
       else:
           messagebox.showerror('', 'Invalid')

   else:
       messagebox.showerror('',"Not selected")


# Creating button for billing
billbutton=Button(frame,command=billselling,bg="black",fg="green",text="BILL",width=7,height=0,bd=0,font=("family",12,"bold"))
billbutton.grid(row=0,column=2)





win.mainloop()

