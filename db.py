import mysql.connector
import datetime as dt


con=mysql.connector.connect(host="localhost",user="RAJA",password="(mistry1313)*",database="sms")


class purchase:
    # Adding items
    def add(self,pid,cid, item, p_qty,purch_p,tot, pdate):
        self.bs(cid,p_qty)
        self.totm(cid,tot)
        self.totqty1(cid,p_qty)

        self.cur =con.cursor()
        qry = "insert into purchase (pid,cid,item,p_qty,purch_p,tot,pdate) values (%s,%s,%s,%s,%s,%s,%s);"
        user = (pid,cid, item,p_qty,purch_p,tot, pdate)
        self.cur.execute(qry, user)
        con.commit()

    def totm(self,cid,purch_p):
        t=self.pamount(cid)+purch_p
        self.cur=con.cursor()
        qry="insert into totp(cid,totp) values (%s,%s);"
        self.cur.execute(qry,(cid,t))
        con.commit()



    def pamount(self,cid):
        self.cur=con.cursor()
        qry="select totp from totp where cid=%s;"
        self.cur.execute(qry,(cid,))
        res=self.cur.fetchall()
        if res:
            res1=res[-1]
            res2=res1[-1]
            return res2
        else:
            return 0
    # balance stock
    def bs(self,cid, p_qty):
        t = self.select(cid) + p_qty
        self.cur = con.cursor()
        qry = "insert into bs(cid,bstock) values (%s,%s);"
        self.cur.execute(qry, (cid, t))
        con.commit()
    def totqty(self,cid):
        self.cur=con.cursor()
        qry="select ptot from ptotqty where cid=%s "
        self.cur.execute(qry,(cid,))
        res=self.cur.fetchall()
        if res:
            res1=res[-1]
            res2=res1[-1]
            #print(res2)
            return res2
        else:
            return 0


    def totqty1(self,cid,p_qty):
        t=self.totqty(cid)+p_qty
        self.cur=con.cursor()
        qry="insert into ptotqty(cid,ptot) values(%s,%s)"
        self.cur.execute(qry,(cid,t))
        con.commit()



    def select(self,cid):
        self.cur = con.cursor()
        qry = "select bstock from bs where cid=%s;"
        self.cur.execute(qry, (cid,))
        res = self.cur.fetchall()
        if res:
            res1 = res[-1]
            res2 = res1[-1]
            #print(res2)
            #print(type(res2))
            return res2
        else:
            return 0

    def fetch(self):
        self.cur=con.cursor()
        self.cur.execute("select * from purchase")
        row=self.cur.fetchall()
        return row

class sold:
    # sold items

    def soldp(self,sid,cid,item,s_qty,sold_p,tot,sdate,b):
        self.bs(cid,s_qty)
        self.totm(cid,tot)
        self.addtotqty(cid,s_qty)
        self.cur = con.cursor()
        qry = "insert into sold (sid,cid,item,s_qty,sold_p,tot,sdate,billid) values(%s,%s,%s,%s,%s,%s,%s,%s);"
        user=(sid,cid,item,s_qty,sold_p,tot,sdate,b)
        self.cur.execute(qry,user)
        con.commit()
    def totm(self,cid,sold_p):
        t=self.samount(cid)+sold_p
        self.cur=con.cursor()
        qry="insert into tots (cid,tots) values(%s,%s);"
        self.cur.execute(qry,(cid,t))
        con.commit()

    def samount(self,cid):
        self.cur=con.cursor()
        qry="select tots from tots where cid=%s;"
        self.cur.execute(qry,(cid,))
        res=self.cur.fetchall()
        if res:
            res1=res[-1]
            res2=res1[-1]
            return res2
        else:
            return 0

    def bs(self,cid,s_qty):
        t=self.select(cid)-s_qty
        self.cur = con.cursor()
        qry = "insert into bs(cid,bstock) values (%s,%s);"
        self.cur.execute(qry, (cid, t))
        con.commit()

    def select(self,cid):
        self.cur = con.cursor()
        qry = "select bstock from bs where cid=%s"
        self.cur.execute(qry, (cid,))
        res = self.cur.fetchall()
        if res:
            res1 = res[-1]
            res2 = res1[-1]
            #print(res2)
            #print(type(res2))
            return res2
        else:
            return 0

    def fetch(self):
        t='Selling'
        self.cur=con.cursor()
        qry="select * from sold where sid=%s"
        self.cur.execute(qry,(t,))
        res=self.cur.fetchall()
        return res

    def totqty(self, cid):
        self.cur = con.cursor()
        qry = "select stot from stotqty where cid=%s"
        self.cur.execute(qry, (cid,))
        res=self.cur.fetchall()
        if res:
            res1=res[-1]
            res2=res1[-1]
            return res2
        else:
            return 0

    def addtotqty(self,cid,s_qty):
        t=self.totqty(cid)+s_qty
        qry="insert into stotqty(cid,stot) values(%s,%s)"
        self.cur.execute(qry,(cid,t))
        con.commit()

    def getbillid(self):
        self.cur=con.cursor()
        qry="select billid from sold"
        self.cur.execute(qry)
        res=self.cur.fetchall()
        if res:
            res1=res[-1]
            res2=res1[-1]
            return res2
        else:
            return 0
class delete:

    def purch(self,cid):
        self.cur=con.cursor()
        qry="delete from purchase where cid=%s"
        self.cur.execute(qry,(cid,))
        con.commit()

    def bsdel(self,cid):
        self.cur=con.cursor()
        qry="delete from bs where cid=%s"
        self.cur.execute(qry,(cid,))
        con.commit()

    def delptotqty(self,cid):
        self.cur=con.cursor()
        qry="delete from ptotqty where cid=%s"
        self.cur.execute(qry,(cid,))
        con.commit()

    def delstotqty(self,cid):
        self.cur=con.cursor()
        qry="delete from stotqty where cid=%s"
        self.cur.execute(qry,(cid,))
        con.commit()

    def delsold(self,cid):
        #temp=b.lastbillid()
        self.cur=con.cursor()
        qry="delete from sold where cid=%s"
        self.cur.execute(qry,(cid,))
        con.commit()
        #o2.soldp("","","","","","","",temp)

    def deltotp(self,cid):
        #print("Double ok")
        #print(cid)
        self.cur=con.cursor()
        qry="delete from totp where cid=%s"
        self.cur.execute(qry,(cid,))
        con.commit()

    def deltots(self,cid):
        self.cur=con.cursor()
        qry="delete from tots where cid=%s"
        self.cur.execute(qry,(cid,))
        con.commit()

    def deldis(self,cid):
        a=str(cid)
        qry="delete from display where itemid=%s"
        self.cur.execute(qry,(a,))
        con.commit()

"""
    def sno(self,pid):
        self.cur=con.cursor()
        qry="truncate table purchase"
        self.cur.execute(qry)
        con.commit()
"""
class bill:
    def bills(self,bill,billid,sdate):
        self.cur=con.cursor()
        qry="insert into bills(bill,billid,sdate) values(%s,%s,%s);"
        self.cur.execute(qry,(bill,billid,sdate))
        con.commit()

    # Getting date and bill id
    def getbillidanddate(self,bill):
        self.cur=con.cursor()
        qry="select bill,billid,sdate from bills where bill=%s;"
        self.cur.execute(qry,(bill,))
        res=self.cur.fetchall()
        # return res
        if res:
            res1=res[-1]
            return res1


    def getbillid(self,t):
        self.cur=con.cursor()
        qry="select billid from sold"
        self.cur.execute(qry)
        res=self.cur.fetchall()
        #print ('BIll id',res)
        if res:
            res1=res[t]
            res2=res1[-1]
            return res2
        else:
            return 1


    def mainbill(self,itemname,qty,price,tot,t):
        self.cur=con.cursor()
        qry="insert into mainbill(itemname,qty,price,tot,billid) values(%s,%s,%s,%s,%s);"
        self.cur.execute(qry,(itemname,qty,price,tot,t))
        con.commit()

    def gettingbody(self,billid):
        self.cur=con.cursor()
        qry="select sno,itemname,qty,price,tot from mainbill where billid=%s"
        self.cur.execute(qry,(billid,))
        res=self.cur.fetchall()
        return res

        # Getting Last bill id

    def lastbillid(self):
        self.cur = con.cursor()
        qry = "select * from sold"
        self.cur.execute(qry)
        res = self.cur.fetchall()
        res1 = res[-1]
        res2 = res1[-1]
        return res2

    # Getting total of billing
    def totalbill(self,billid):
        self.cur=con.cursor()
        qry="select tot from mainbill where billid=%s"
        self.cur.execute(qry,(billid,))
        res=self.cur.fetchall()
        return res

    def getlastot(self):
        self.cur=con.cursor()
        qry="select * from totalbill"
        self.cur.execute(qry)
        res=self.cur.fetchall()
        if res:
            res1=res[-1]
            res2=res1[-1]
            return res2
        else:
            return 0

    # Inserting total bill
    def inserttot(self,billid,tot):
        self.cur=con.cursor()
        qry="insert into totalbill(billid,tot) values(%s,%s)"
        self.cur.execute(qry,(billid,tot))
        con.commit()



class orderdisplay:
    def dis(self,type,itemid,itemname,qty,price,tot,date,billid):
        self.cur=con.cursor()
        qry="insert into display(type,itemid,itemname,qty,price,tot,date,billid) values(%s,%s,%s,%s,%s,%s,%s,%s)"
        self.cur.execute(qry,(type,itemid,itemname,qty,price,tot,date,billid))
        con.commit()

    def getdis(self):
        self.cur=con.cursor()
        qry="select * from display"
        self.cur.execute(qry)
        res=self.cur.fetchall()
        return res
