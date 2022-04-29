from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5 import QtCore
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication
import sqlite3 as sql


class DataBase_Connection():
    def __init__(self):
        print("DataBase Connected Successfully")
        # conn = sql.connect('industry_database.db')
        
        # cursor = conn.cursor()
        # query1 = '''CREATE TABLE IF NOT EXISTS Users (
        #                     Sl_No	INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        #                     Name	TEXT NOT NULL,
        #                     Contact_Number NUMBER(10) NOT NULL,
        #                     ID_Type	VARCHAR(15) NOT NULL,
        #                     ID_Number	NUMBER (15) NOT NULL,
        #                     User_Name	VARCHAR(10) NOT NULL,
        #                     Password	VARCHAR(15) NOT NULL);'''     
        # try:
        #     cursor.execute(query1)
        # except Exception as e:
        #     print(e)
        
        # query2 = '''CREATE TABLE IF NOT EXISTS Temp_Order_Billing (
        #             id	INTEGER,
        #             Customer_Name	varchar(20) NOT NULL,
        #             Phone_No	number(10) NOT NULL,
        #             Date	date NOT NULL,
        #             Product_Name	varchar(20) NOT NULL,
        #             Quantity	INTEGER NOT NULL,
        #             Total	INTEGER NOT NULL,
        #             Status	char (10) NOT NULL,
        #             FOREIGN KEY(Product_Name) REFERENCES Products(Product_Name),
        #             PRIMARY KEY(id AUTOINCREMENT))'''           
        # try:
        #     cursor = conn.cursor()
        #     cursor.execute(query2)
        # except Exception as e:
        #     print(e)

        # conn.commit()
        self.OrderDeleteAll()

    def OrderDeleteAll(self):
        conn = sql.connect('industry_database.db')        
        try:
            cursor = conn.cursor()
            cursor.execute('''DELETE FROM Temp_Order_Billing ''')
            conn.commit()
        except Exception as e:
            print(e)

    def totalUsers(self):
        conn = sql.connect('industry_database.db')        
        try:
            cursor = conn.cursor()
            cursor.execute('''select * from Users''')
            row = cursor.fetchall()
            return str(len(row))
        except Exception as e:
            print(e)


    def totalEmployees(self):
        conn = sql.connect('industry_database.db')        
        try:
            cursor = conn.cursor()
            cursor.execute('''select * from Employee''')
            row = cursor.fetchall()
            return str(len(row))
        except Exception as e:
            print(e)

    def totalPurchases(self):
        conn = sql.connect('industry_database.db')    
        try:
            cursor = conn.cursor()
            cursor.execute('''select * from Purchases''')
            row = cursor.fetchall()
            return str(len(row))
        except Exception as e:
            print(e)

    def totalChemicals(self):
        conn = sql.connect('industry_database.db')        
        try:
            cursor = conn.cursor()
            cursor.execute('''select * from Chemical_Stock''')
            row = cursor.fetchall()
            return str(len(row))
        except Exception as e:
            print(e)

    def totalProducts(self):
        conn = sql.connect('industry_database.db')           
        try:
            cursor = conn.cursor()
            cursor.execute('''select * from Products''')
            row = cursor.fetchall()
            return str(len(row))
        except Exception as e:
            print(e)

    def lowChemical(self):
        conn = sql.connect('industry_database.db')         
        try:
            cursor = conn.cursor()
            cursor.execute('''select * from Chemical_Stock where Quantity < 500''')
            row = cursor.fetchall()
            return str(len(row))
        except Exception as e:
            print(e)
    
    def numberSales(self):
        conn = sql.connect('industry_database.db')         
        try:
            cursor = conn.cursor()
            cursor.execute('''select * from Order_Billing''')
            row = cursor.fetchall()
            return str(len(row))
        except Exception as e:
            print(e)

    def orderCompleted(self):
        conn = sql.connect('industry_database.db')         
        try:
            cursor = conn.cursor()
            cursor.execute('''select * from Order_Billing where Status = 'Completed' ''')
            row = cursor.fetchall()
            return str(len(row))
        except Exception as e:
            print(e)

    def orderPending(self):
        conn = sql.connect('industry_database.db')         
        try:
            cursor = conn.cursor()
            cursor.execute('''select * from Order_Billing where Status = 'Pending' ''')
            row = cursor.fetchall()
            return str(len(row))
        except Exception as e:
            print(e)

    