from ui_login import *
from ui_Splash import *
from database import *
import ui_Dashboard_admin
from ui_Dashboard_admin import *
import ui_ui_Dashboard_Employee
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5 import QtCore
from PyQt5.QtCore import QTimer 
from PyQt5.QtWidgets import QMainWindow, QInputDialog, QLineEdit, QDialog
from PyQt5.QtWidgets import QApplication
import sys
import PySide2
from PySide2 import *
import os
from PySide2 import QtGui
from Custom_Widgets.Widgets import *
import sqlite3 as sql



#-----------------Dashboard----------------------------

class Main(QMainWindow):
    
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = ui_Dashboard_admin.Ui_MainWindow()
        self.ui.setupUi(self)
        loadJsonStyle(self, self.ui)
        self.dashBoard()
        self.showMaximized()
        self.Handel_Buttons()

    def Handel_Buttons(self):

        #----------------MenuButtons---------------------

        self.ui.dashboard_btn.clicked.connect(lambda: self.dashBoard())
        self.ui.order_btn.clicked.connect(lambda: self.OrderPage())
        self.ui.inventory_btn.clicked.connect(lambda: self.InventoryPage())
        self.ui.purchase_btn.clicked.connect(lambda: self.PurchasePage())
        self.ui.wholesaler_btn.clicked.connect(lambda: self.WholeSalerPage())
        self.ui.sale_history_btn.clicked.connect(lambda: self.SaleHistory())
        self.ui.employee_btn.clicked.connect(lambda: self.EmployeePage())
        self.ui.users_btn.clicked.connect(lambda: self.UserPage())
        self.ui.inventory_add_new_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_new))
        self.ui.custom_querying.clicked.connect(lambda: self.CustomQuery())
        self.ui.developer_info.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.info_page))
        self.ui.inventory_sort1_combo.currentIndexChanged.connect(lambda: self.Inventory_Combo_Details())
        #--------------------------------------------------

        #---------------TopMenuButtons---------------------

        self.ui.logout_btn.clicked.connect(self.logOut)        
        self.ui.users_btn_2.clicked.connect(lambda: self.PopUser())
        self.ui.refresh_btn.clicked.connect(lambda: self.refresh())

        # #--------------------------------------------------

        # #-----------------OrderPageButtons-----------------

        self.ui.order_add_btn.clicked.connect(lambda: self.OrderaddBtn())        
        self.ui.order_generate_bill_btn.clicked.connect(lambda: self.generateBill())
        self.ui.order_back_btn.clicked.connect(lambda: self.backOrder())
        self.ui.order_delete.clicked.connect(lambda: self.OrderDeleteLast())         
        self.ui.order_save.clicked.connect(lambda: self.OrderSave())
        self.ui.order_clear_btn.clicked.connect(lambda: self.orderClear())
        self.ui.order_total_btn.clicked.connect(lambda: self.orderTotal())
        self.ui.order_product_combo.currentIndexChanged.connect(lambda: self.OrderAvailableQuantity())

        # #--------------------------------------------------

        # #-----------------InventoryPageButtons-----------------

        self.ui.inventory_chemical_low_btn.clicked.connect(lambda: self.Inventory_ChemicalLow())        
        self.ui.Inventory_RadioButton.toggled.connect(lambda: self.InventorySortReset())
        self.ui.inventory_chemical_all_btn.clicked.connect(lambda: self.Inventory_ChemicalAll())      
        self.ui.inventory_product_low_btn.clicked.connect(lambda: self.Inventory_ProductLow())  
        self.ui.inventory_product_all_btn.clicked.connect(lambda: self.Inventory_ProductAll())  
        self.ui.inventory_search_btn.clicked.connect(lambda: self.Inventorysearch())  
        self.ui.inventory_update_btn.clicked.connect(lambda: self.InventoryUpdate())  

        # #--------------------------------------------------

        # #-----------------PurchasesPageButtons-----------------

        self.ui.purchases_clear_btn.clicked.connect(lambda: self.PurchaseClear())
        self.ui.Purchase_RadioButton.toggled.connect(lambda: self.PurchaseSortReset())     
        self.ui.purchaases_wholesaler__combo.currentIndexChanged.connect(lambda: self.PurchaseCombo2())
        self.ui.purchaases_wholesaler__combo_2.currentIndexChanged.connect(lambda: self.PurchaseCombo3())
        self.ui.purchases_add_btn.clicked.connect(lambda: self.PurchaseAdd())
        self.ui.purchases_delete_btn.clicked.connect(lambda: self.PurchaseDelete())
        self.ui.purchases_search_btn.clicked.connect(lambda: self.PurchaseSearch())

        # #--------------------------------------------------

        # #-----------------WholesalerPageButtons-----------------

        self.ui.wholesaler_show_all_btn.clicked.connect(lambda: self.wholesalerAll())
        self.ui.wholesaler_sort1_combo.currentIndexChanged.connect(lambda: self.WholeSalerCombo1())
        self.ui.wholesaler_search.clicked.connect(lambda: self.WholeSalerSearch())        
        self.ui.Wholesaler_RadioButton.toggled.connect(lambda: self.WholeSalerSortReset())
        self.ui.wholesaler_add_btn.clicked.connect(lambda: self.AddWholeSaler())
        self.ui.wholesaler_clear_btn.clicked.connect(lambda: self.WholeSalerPageClear())
        self.ui.wholesaler_delete_btn.clicked.connect(lambda: self.WholeSalerPageDelete())
        self.ui.wholesaler_addmore_btn_2.clicked.connect(lambda: self.WholeSalerPageAddChemical())

        # #--------------------------------------------------

        # #-----------------NewProduct-ChemicalPageButtons-----------------

        # self.ui.exit_btn.clicked.connect(lambda: self.)
        # self.ui.exit_btn.clicked.connect(lambda: self.)
        # self.ui.exit_btn.clicked.connect(lambda: self.)

        # #--------------------------------------------------

        # #-----------------SaleHistoryPageButtons-----------------

        self.ui.sale_history_show_all_btn.clicked.connect(lambda: self.SaleHistoryAll())
        self.ui.sale_history_delete.clicked.connect(lambda: self.SaleHistoryDel())
        self.ui.sale_history_update.clicked.connect(lambda: self.SaleHistoryUpdate())
        self.ui.sale_history_search_btn.clicked.connect(lambda: self.SaleHistorySearchCombo2())
        self.ui.sale_history_checkbox.toggled.connect(lambda: self.SaleHistorySortReset())
        #self.ui.sale_history_deleteAll.clicked.connect(lambda: self.SaleHistoryDeleteAll())

        # #--------------------------------------------------

        # #-----------------EmployeePageButtons-----------------

        self.ui.Employee_RadioBtn.toggled.connect(lambda: self.EmployeeTableSorting())
        # self.ui.exit_btn.clicked.connect(lambda: self.)
        # self.ui.exit_btn.clicked.connect(lambda: self.)
        # self.ui.exit_btn.clicked.connect(lambda: self.)
        # self.ui.exit_btn.clicked.connect(lambda: self.)

        # #--------------------------------------------------

        # #-----------------UsersPageButtons-----------------

        self.ui.users_add_btn_2.clicked.connect(lambda: self.UserAdd())
        self.ui.users_clear_btn.clicked.connect(lambda: self.UserClear())
        self.ui.users_delete_btn.clicked.connect(lambda: self.UserDel())
        self.ui.users_update_btn.clicked.connect(lambda: self.UserUpdate())
        self.ui.User_RadioBtn.toggled.connect(lambda: self.UserTableSorting())

        # #--------------------------------------------------

        # #-----------------CustomQueryPageButtons-----------------

        self.ui.query_search.clicked.connect(lambda: self.QuerySearch())
        self.ui.query_reset.clicked.connect(lambda: self.QueryTableReset())
        self.ui.query_RadioBtn.toggled.connect(lambda: self.QueryTableSorting())
        self.ui.query_clear.clicked.connect(lambda: self.QueryClear())
        self.ui.query1.clicked.connect(lambda: self.Query1())
        self.ui.query2.clicked.connect(lambda: self.Query2())
        self.ui.query3.clicked.connect(lambda: self.Query3())
        self.ui.query4.clicked.connect(lambda: self.Query4())
        self.ui.query5.clicked.connect(lambda: self.Query5())
        self.ui.query_header.clicked.connect(lambda: self.InputHeader())
        self.ui.query_save.clicked.connect(lambda: self.futureDevelopment())

        # #--------------------------------------------------


    #------------TopButtonFunctionalities-----------------------

    def logOut(self):
        self.close()
        print("You have been successfully logged out!")
        QMessageBox.information(self, "Logout", Login.User_Name+"\nYou have been successfully logged out!")

    def PopUser(self):
        QMessageBox.information(self, "User Details", "User Name : "+Login.User_ID+"\nName : "+Login.User_Name+"\nID : "+Login.ID)
              
    def refresh(self):
        DataBase_Connection()
        conn = sql.connect('industry_database.db')
        conn.commit()
        
    #-----------------------------------------------------

    #---------------Dashboard Setup-----------------------
    def dashBoard(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_dashboard)
        self.ui.user_name.setText(Login.User_Name)
        self.dashBoardDetails()

    def dashBoardDetails(self):
        self.ui.total_users.setText(DataBase_Connection.totalUsers(self))
        self.ui.total_employee.setText(DataBase_Connection.totalEmployees(self))
        self.ui.total_product.setText(DataBase_Connection.totalProducts(self))
        self.ui.total_purchases.setText(DataBase_Connection.totalPurchases(self))
        self.ui.total_chemical.setText(DataBase_Connection.totalChemicals(self))
        self.ui.low_chemical.setText(DataBase_Connection.lowChemical(self))
        self.ui.number_of_sales.setText(DataBase_Connection.numberSales(self))
        self.ui.order_completed.setText(DataBase_Connection.orderCompleted(self))
        self.ui.order_pending.setText(DataBase_Connection.orderPending(self))

    #--------------------------------------------------------

    #-------------------PurchasePage-------------------------

    def PurchasePage(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_purchases)
        self.PurchaseAll()
        self.ui.purchase_date.setDate(QDate.currentDate())
        self.PurchaseCombo1()

    def PurchaseAll(self):
        try:
            conn = sql.connect('industry_database.db')
            cursor = conn.cursor()
            cursor.execute('''select P.Invoice_No, D.Dealer_Company, D.Dealer_Name, DS.Chemical_Name,P.Date_of_Purchase, P.Quantity, P.Cost_of_One, P.Total
                                from Purchases as P, Chemical_Dealers as D, Dealer_Chemical_Supply as DS
                                where P.Supplier_Id = DS.Supply_Id and DS.Dealer_Id =  D.Sl_No''')
            row = cursor.fetchall()
            self.ui.tableWidget_4.setRowCount(0)
            for row_number, row_data in enumerate(row):
                self.ui.tableWidget_4.insertRow(row_number)
                for coloumn_number, data in enumerate(row_data):
                    self.ui.tableWidget_4.setItem(row_number, coloumn_number, QTableWidgetItem(str(data)))
        except Exception as e:
            print(e)
            QMessageBox.warning(self, "Error", "Please Check again\nError: "+str(e))

    def PurchaseSearch(self):
        invoice = self.ui.purchaseSearch.text()
        query = '''select P.Invoice_No, D.Dealer_Company, D.Dealer_Name, DS.Chemical_Name,P.Date_of_Purchase, P.Quantity, P.Cost_of_One, P.Total
                                from Purchases as P, Chemical_Dealers as D, Dealer_Chemical_Supply as DS
                                where P.Supplier_Id = DS.Supply_Id and DS.Dealer_Id =  D.Sl_No and Invoice_No = ?'''
        if (invoice != "" and invoice.isdigit()):
            try:
                conn = sql.connect('industry_database.db')
                cursor = conn.cursor()
                cursor.execute(query, (invoice,))
                row = cursor.fetchall()
                self.ui.tableWidget_4.setRowCount(0)
                for row_number, row_data in enumerate(row):
                    self.ui.tableWidget_4.insertRow(row_number)
                    for coloumn_number, data in enumerate(row_data):
                        self.ui.tableWidget_4.setItem(row_number, coloumn_number, QTableWidgetItem(str(data)))
            except Exception as e:
                print(e)
                QMessageBox.warning(self, "Error", "Please Check again\nError: "+str(e))
        else:
            QMessageBox.warning(self, "Error", "Check the Input fields")

    def PurchaseAdd(self):
        comp = self.ui.purchaases_wholesaler__combo.currentText()
        wholesaler = self.ui.purchaases_wholesaler__combo_2.currentText()
        chemical = self.ui.purchases_chemical_combo.currentText()
        date = self.ui.purchase_date.date().toPython()
        quantity = self.ui.purchases_quantity.text()
        quantity = int(quantity)
        cost = self.ui.purchases_cost_of_one.text()
        invoice = self.ui.purchases_invoice_number.text()
        query1 = '''SELECT Sl_No
                    FROM Chemical_Dealers
                    WHERE Dealer_Company = ? and Dealer_Name = ? '''
        query2 = '''SELECT Supply_Id
                    FROM Dealer_Chemical_Supply
                    WHERE Dealer_Id = ? and Chemical_Name = ? '''
        query3 = '''insert into Purchases values (?,?,?,?,?,?)'''
        if comp != '' and wholesaler != '' and chemical != '' and date != '' and quantity > 0 and cost != '' and invoice != '' and cost.isdigit() and invoice.isdigit():
            try:
                conn = sql.connect('industry_database.db')
                newCost = self.PurchaseTotal()
                cost = int(cost)
                cursor = conn.cursor()
                cursor.execute(query1, (comp,wholesaler,))
                row = cursor.fetchone()
                if row is None:
                    QMessageBox.warning(self, "Error", "The Dealer Does Not Exist")
                else:
                    try:
                        cursor.execute(query2, (int(row[0]), chemical,))
                        row1 = cursor.fetchone()
                        if row1 is None:
                            QMessageBox.warning(self, "Error", "The Dealer Does Not Supply Particular Chemical")
                        else:
                            cursor.execute(query3, (invoice, int(row1[0]), date, quantity, cost, newCost,))
                            conn.commit()
                            self.ChemicalPriceUpdate()
                            self.PurchaseAll()
                    except Exception as e:
                        print(e)
                        QMessageBox.warning(self, "Error", "Please Check again\nError: "+str(e))   
            except Exception as e:
                print(e)
                QMessageBox.warning(self, "Error", "Please Check again\nError: "+str(e))    
        else:
            QMessageBox.warning(self, "Error", "Check all Input fields")

    def ChemicalPriceUpdate(self):
        cost = self.ui.purchases_cost_of_one.text()
        cost = int(cost)
        date = self.ui.purchase_date.date().toPython()
        chemical = self.ui.purchases_chemical_combo.currentText()
        query = ''' select Chemical_Id from Chemical_Stock where Chemical_Name = ? '''
        query2 = '''update Chemical_Stock set Price = ?, Date_of_Purchase = ? where Chemical_Id = ?'''
        try:
            conn = sql.connect('industry_database.db')
            cursor = conn.cursor()
            cursor.execute(query, (chemical,))
            row = cursor.fetchone()
            if row is None:
                QMessageBox.warning(self, "Error", "The Chemical Does Not Exist")
            else:
                cursor.execute(query2, (cost,date,int(row[0]),))
                conn.commit()
                self.ChemicalQuantityUpdate(int(row[0]))
        except Exception as e:
            print(e)
            QMessageBox.warning(self, "Error", "please Check again\nError: "+str(e))

    def ChemicalQuantityUpdate(self, id):
        quantity = self.ui.purchases_quantity.text()
        query1 = '''select Quantity from Chemical_Stock where Chemical_Id = ?'''
        query2 = '''update Chemical_Stock set Quantity = ? where Chemical_Id = ?'''
        try:
            conn = sql.connect('industry_database.db')
            cursor = conn.cursor()
            cursor.execute(query1, (id,))
            row = cursor.fetchone()
            if row is None:
                QMessageBox.warning(self, "Error", "Please Check the Id\nError: ID Not Found ")
            else:
                sum = (int(row[0]) + int(quantity))
                cursor.execute(query2, (sum,id,))
                conn.commit()
                QMessageBox.information(self, "Successful", "Successfully Saved")
        except Exception as e:
            print(e)
            QMessageBox.warning(self, "Error", "please Check again\nError: "+str(e))

    def PurchaseTotal(self):
        quantity = self.ui.purchases_quantity.text()
        cost = self.ui.purchases_cost_of_one.text()
        if quantity != 0 and quantity != '' and cost != '' and cost.isdigit():
            result = (int(quantity) * int(cost))
            self.ui.purchases_total.setText(str(result))
        else:
            QMessageBox.warning(self, "Error", "Please Check Quantity or Cost")
        return int(result)

    def PurchaseClear(self):
        self.ui.purchaases_wholesaler__combo.setCurrentIndex(0)
        self.ui.purchaases_wholesaler__combo_2.setCurrentIndex(0)
        self.ui.purchases_chemical_combo.setCurrentIndex(0)
        self.ui.purchase_date.setDate(QDate.currentDate())
        self.ui.purchases_quantity.setValue(0)
        self.ui.purchases_cost_of_one.setText('')
        self.ui.purchases_invoice_number.setText('')

    def PurchaseDelete(self):
        invoice = self.ui.purchases_invoice_number.text()
        query1 = '''select * from Purchases where Invoice_No = ?'''
        query2 = '''delete from Purchases where Invoice_No = ?'''
        if invoice != '' and invoice.isdigit():
            invoice = int(invoice)
            try:
                conn = sql.connect('industry_database.db')
                cursor = conn.cursor()
                cursor.execute(query1, (invoice,))
                row = cursor.fetchone()
                if row is None:
                    QMessageBox.warning(self, "Error", "Please Check the Invoice ID\nError: Invoice ID Not Found ")
                else:
                    self.ChemicalQuantityDelete()
                    cursor.execute(query2, (invoice,))
                    conn.commit()
                    self.PurchaseAll()
            except Exception as e:
                print(e)
                QMessageBox.warning(self, "Error", "please Check again\nError: "+str(e))
        else:
            QMessageBox.warning(self, "Error", "Please Check the Invoice ID\nError: Invoice ID Not Found ")

    def ChemicalQuantityDelete(self):
        invoice = self.ui.purchases_invoice_number.text()
        invoice = int(invoice)
        query1 = '''SELECT Chemical_Id, C.Quantity, P.Quantity
                    FROM Chemical_Stock C, Dealer_Chemical_Supply as DS, Purchases as P
                    WHERE Invoice_No = ? and P.Supplier_Id = DS.Supply_Id and DS.Chemical_Name = C.Chemical_Name '''
        query2 = ''' update Chemical_Stock set Quantity = ? where Chemical_Id = ? '''
        try:
            conn = sql.connect('industry_database.db')
            cursor = conn.cursor()
            cursor.execute(query1, (invoice,))
            row = cursor.fetchone()
            if row is None:
                QMessageBox.warning(self, "Error", "Chemical Not Found Because Dealer Does Not Exist")
            else:
                sum = (int(row[1]) - int(row[2]))
                cursor.execute(query2, (sum, int(row[0]),))
                conn.commit()
                QMessageBox.information(self, "Successful", "Successfully Deleted")
        except Exception as e:
            print(e)
            QMessageBox.warning(self, "Error", "please Check again\nError: "+str(e))


    def PurchaseCombo1(self):
        self.ui.purchaases_wholesaler__combo.clear()
        query1 = '''select DISTINCT Dealer_Company from Chemical_Dealers'''
        try:
            conn = sql.connect('industry_database.db')
            cursor = conn.cursor()
            cursor.execute(query1)
            row = cursor.fetchall()
            for i in row:
                self.ui.purchaases_wholesaler__combo.addItems(i)
        except Exception as e:
            print(e)
            QMessageBox.warning(self, "Error", "please Check again\nError: "+str(e))

    def PurchaseCombo2(self):
        self.ui.purchaases_wholesaler__combo_2.clear()
        comp = self.ui.purchaases_wholesaler__combo.currentText()
        query1 = '''select Dealer_Name from Chemical_Dealers where Dealer_Company = ? '''
        if comp != '':
            try:
                conn = sql.connect('industry_database.db')
                cursor = conn.cursor()
                cursor.execute(query1, (comp,))
                row = cursor.fetchall()
                for i in row:
                    self.ui.purchaases_wholesaler__combo_2.addItems(i)
            except Exception as e:
                print(e)
                QMessageBox.warning(self, "Error", "please Check again\nError: "+str(e))
    
    def PurchaseCombo3(self):
        self.ui.purchases_chemical_combo.clear()
        comp = self.ui.purchaases_wholesaler__combo.currentText()
        wholesaler = self.ui.purchaases_wholesaler__combo_2.currentText()
        query2 = '''select DS.Chemical_Name 
                    from Chemical_Dealers, Dealer_Chemical_Supply as DS
                    where Dealer_Company = ? and Dealer_Name = ? and Sl_No = Dealer_Id '''
        try:
            conn = sql.connect('industry_database.db')
            cursor = conn.cursor()
            cursor.execute(query2, (comp,wholesaler,))
            row = cursor.fetchall()
            for i in row:
                self.ui.purchases_chemical_combo.addItems(i)
        except Exception as e:
            print(e)
            QMessageBox.warning(self, "Error", "please Check again\nError: "+str(e))

    def PurchaseSortReset(self):
        if self.ui.Purchase_RadioButton.isChecked():
            self.ui.tableWidget_4.setSortingEnabled(True)
        else:
            self.ui.tableWidget_4.setSortingEnabled(False)

    #--------------------------------------------------------

    #-------------------OrderPage----------------------------
    def OrderPage(self):
        self.ui.order_product_combo.clear()
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_order)
        self.comboProducts()
        self.ui.order_date.setDate(QDate.currentDate())
        self.OrderPageDisplay()

    def OrderSave(self):
        conn = sql.connect('industry_database.db')        
        try:
            cursor = conn.cursor()
            cursor.execute('''insert into Order_Billing (Customer_Name,Phone_No,Date,Product_Name,Quantity,Total,Status) 
                                select Customer_Name,Phone_No,Date,Product_Name,Quantity,Total,Status  
                                from Temp_Order_Billing ''')
            conn.commit()
            QMessageBox.information(self, "Successful", "Successfully Saved into DataBase")
            DataBase_Connection.OrderDeleteAll(self)
            self.OrderPageDisplay()
        except Exception as e:
            print(e)

    def OrderaddBtn(self):
        name = str(self.ui.customer_name.text())
        contactNumber = self.ui.customer_contact_number.text()
        product = self.ui.order_available_quantity.text()
        product = int(product)
        quantity = int(self.ui.order_quantity.text())
        status = 'pending'
        date = self.ui.order_date.date().toPython()
        product_name = str(self.ui.order_product_combo.currentText())
        if ((name, contactNumber) != "") and (quantity >= 500) and contactNumber.isdigit() and ((product - quantity)>0):
            contactNumber = int(contactNumber)
            total = self.orderTotal()
            conn = sql.connect('industry_database.db')        
            query = '''insert into Temp_Order_Billing (Customer_Name,Phone_No,Date,Product_Name,Quantity,Total,Status) values (?,?,?,?,?,?,?)'''
            try:
                cursor = conn.cursor()
                cursor.execute(query,(name,contactNumber,date,product_name,quantity,total,status,))
                conn.commit()
            except Exception as e:
                print(e)
            self.OrderPageDisplay()
        else:
            QMessageBox.warning(self, "Blank", "Input all fields and Quantity should be greater 500\nQuantity Ordered Should be Less than Available Order")

    def OrderDeleteLast(self):
        try:
            conn = sql.connect('industry_database.db') 
            cursor = conn.cursor()
            cursor.execute('''DELETE FROM Temp_Order_Billing WHERE id=(SELECT MAX(id) FROM Temp_Order_Billing) ''')
            conn.commit()
            self.OrderPageDisplay()
        except Exception as e:
            print(e)

    def OrderAvailableQuantity(self):
        product = self.ui.order_product_combo.currentText()
        query = '''select Quantity from Products where Product_Name = ? '''
        if product != '':
            try:
                conn = sql.connect('industry_database.db')
                cursor = conn.cursor()
                cursor.execute(query, (product,))
                row = cursor.fetchone() 
                self.ui.order_available_quantity.setText(str(row[0]))
            except Exception as e:
                print(e)

    def comboProducts(self):        
        query = '''select Product_Name from Products'''
        try:
            conn = sql.connect('industry_database.db')
            cursor = conn.cursor()
            cursor.execute(query)
            row = cursor.fetchall()
            for i in row:
                self.ui.order_product_combo.addItems(i)
        except Exception as e:
            print(e)

    def OrderPageDisplay(self):         
        try:
            conn = sql.connect('industry_database.db')
            cursor = conn.cursor()
            cursor.execute('''select id,Customer_Name,Phone_No,Product_Name,Quantity,Date,Total,Status from Temp_Order_Billing ''')
            row = cursor.fetchall()
            self.ui.tableWidget_8.setRowCount(0)
            for row_number, row_data in enumerate(row):
                self.ui.tableWidget_8.insertRow(row_number)
                for coloumn_number, data in enumerate(row_data):
                    self.ui.tableWidget_8.setItem(row_number, coloumn_number, QTableWidgetItem(str(data)))
        except Exception as e:
            print(e)
    
    def orderTotal(self):
        name = self.ui.customer_name.text()
        product_name = self.ui.order_product_combo.currentText()
        quantity = int(self.ui.order_quantity.text())
        contactNumber = self.ui.customer_contact_number.text()
        if ((name, contactNumber) != "") and (quantity >= 500):
            conn = sql.connect('industry_database.db')        
            query = '''select Price from Products where Product_Name = ?'''
            try:
                cursor = conn.cursor()
                cursor.execute(query, (product_name,))
                row = cursor.fetchone()
                price = (int(row[0])*quantity)
                self.ui.order_cost.setText(str(price))
                return int(price)
            except Exception as e:
                print(e)
        else:
            QMessageBox.warning(self, "Blank", "Input all fields and Quantity should be greater 500")

    def generateBill(self):
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_2)
        self.futureDevelopment()
    def backOrder(self):
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_1)
    def futureDevelopment(self):
        QMessageBox.information(self, "Hello", "This Function will be added in Future development..")
    def orderClear(self):
        self.ui.customer_name.setText("")
        self.ui.customer_contact_number.setText("")
        self.ui.order_quantity.setValue(0)
        self.ui.order_date.setDate(QDate.currentDate())

    #----------------------------------------------------

    #-------------------InventoryPage------------------------

    def InventoryPage(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_inventory)

    def Inventory_ChemicalAll(self):
        self.ui.tableWidget.setHorizontalHeaderLabels(['ID', 'Chemical Name', 'Quantity', 'Price', 'Date of Purchase','Dealer_Company','Dealer_Name',''])    
        try:
            conn = sql.connect('industry_database.db')
            cursor = conn.cursor()
            cursor.execute('''select Chemical_Stock.Chemical_Id,Dealer_Chemical_Supply.Chemical_Name,Quantity,Price, Date_of_Purchase, Dealer_Company, Dealer_Name
                            from Chemical_Stock, Chemical_Dealers,Dealer_Chemical_Supply
                            where (Chemical_Dealers.Sl_No = Dealer_Chemical_Supply.Dealer_Id and Chemical_Stock.Chemical_Name = Dealer_Chemical_Supply.Chemical_Name) 
                            order by Chemical_Id''')
            row = cursor.fetchall()
            self.ui.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(row):
                self.ui.tableWidget.insertRow(row_number)
                for coloumn_number, data in enumerate(row_data):
                    self.ui.tableWidget.setItem(row_number, coloumn_number, QTableWidgetItem(str(data)))
        except Exception as e:
            print(e)
            QMessageBox.warning(self, "Error", "Please Check again\nError: "+str(e))

    def Inventory_ChemicalLow(self):
        self.ui.tableWidget.setHorizontalHeaderLabels(['ID', 'Chemical Name', 'Quantity', 'Price', 'Date of Purchase','Dealer_Company','Dealer_Name',''])
        conn = sql.connect('industry_database.db')         
        try:
            cursor = conn.cursor()
            cursor.execute('''select DISTINCT Chemical_Stock.Chemical_Id,Dealer_Chemical_Supply.Chemical_Name,Quantity,Price, Date_of_Purchase, Dealer_Company, Dealer_Name
                            from Chemical_Stock, Chemical_Dealers,Dealer_Chemical_Supply
                            where (Chemical_Dealers.Sl_No = Dealer_Chemical_Supply.Dealer_Id and Chemical_Stock.Chemical_Name = Dealer_Chemical_Supply.Chemical_Name) 
                            and Quantity<1000 order by Chemical_Id''')
            row = cursor.fetchall()
            self.ui.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(row):
                self.ui.tableWidget.insertRow(row_number)
                for coloumn_number, data in enumerate(row_data):
                    self.ui.tableWidget.setItem(row_number, coloumn_number, QTableWidgetItem(str(data)))
        except Exception as e:
            print(e)
            QMessageBox.warning(self, "Error", "Please Check again\nError: "+str(e))

    def Inventory_ProductLow(self):
        self.ui.tableWidget.setHorizontalHeaderLabels(['ID', 'Product Name', 'Price', 'Quantity', 'Chemical1','Chemical2','Chemical3','Chemical4',])
        conn = sql.connect('industry_database.db')         
        try:
            cursor = conn.cursor()
            cursor.execute('''select * from Products where Quantity < 1000''')
            row = cursor.fetchall()
            self.ui.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(row):
                self.ui.tableWidget.insertRow(row_number)
                for coloumn_number, data in enumerate(row_data):
                    self.ui.tableWidget.setItem(row_number, coloumn_number, QTableWidgetItem(str(data)))
        except Exception as e:
            print(e)
            QMessageBox.warning(self, "Error", "Please Check again\nError: "+str(e))

    def Inventory_ProductAll(self):
        self.ui.tableWidget.setHorizontalHeaderLabels(['ID', 'Product Name', 'Price', 'Quantity', 'Chemical1','Chemical2','Chemical3','Chemical4',])
        conn = sql.connect('industry_database.db')         
        try:
            cursor = conn.cursor()
            cursor.execute('''select * from Products''')
            row = cursor.fetchall()
            self.ui.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(row):
                self.ui.tableWidget.insertRow(row_number)
                for coloumn_number, data in enumerate(row_data):
                    self.ui.tableWidget.setItem(row_number, coloumn_number, QTableWidgetItem(str(data)))
        except Exception as e:
            print(e)
            QMessageBox.warning(self, "Error", "Please Check again\nError: "+str(e))
     
    
    def Inventory_Combo_Details(self):
        self.ui.inventory_sort2_combo.clear()
        item = self.ui.inventory_sort1_combo.currentText()
        chemical = ['Date', 'Quantity', 'Price']
        product = ['Quantity', 'Price']
        if item == 'Chemical':
            for i in range(3):
                self.ui.inventory_sort2_combo.addItem(chemical[i])
        elif item == 'Product':
            for i in range(2):
                self.ui.inventory_sort2_combo.addItem(product[i])

    def Inventorysearch(self):
        item = self.ui.inventory_sort1_combo.currentText()
        if item == 'Chemical':
            self.InventorySortChemical()
        elif item == 'Product':
            self.InventorySortProducts()


    def InventorySortReset(self):
        if self.ui.Inventory_RadioButton.isChecked():
            self.ui.tableWidget.setSortingEnabled(True)
        else:
            self.ui.tableWidget.setSortingEnabled(False)

    def InventorySortProducts(self):
        item = self.ui.inventory_sort1_combo.currentText()
        sort_type = self.ui.inventory_sort2_combo.currentText()
        query1 = '''select * from Products order by Quantity'''
        query2 = '''select * from Products order by Price'''
        if (item == 'Product'):
            self.ui.tableWidget.setHorizontalHeaderLabels(['ID', 'Product Name', 'Price', 'Quantity', 'Chemical1','Chemical2','Chemical3','Chemical4',])
            conn = sql.connect('industry_database.db')         
            try:
                cursor = conn.cursor()
                if (sort_type == 'Quantity'):
                    cursor.execute(query1)
                elif (sort_type == 'Price'):
                    cursor.execute(query2)
                row = cursor.fetchall()
                self.ui.tableWidget.setRowCount(0)
                for row_number, row_data in enumerate(row):
                    self.ui.tableWidget.insertRow(row_number)
                    for coloumn_number, data in enumerate(row_data):
                        self.ui.tableWidget.setItem(row_number, coloumn_number, QTableWidgetItem(str(data)))
            except Exception as e:
                print(e)
                QMessageBox.warning(self, "Error", "Please Check again\nError: "+str(e))


    def InventorySortChemical(self):
        item = self.ui.inventory_sort1_combo.currentText()
        sort_type = self.ui.inventory_sort2_combo.currentText()
        query1 = '''select Chemical_Stock.Chemical_Id,Dealer_Chemical_Supply.Chemical_Name,Quantity,Price, Date_of_Purchase, Dealer_Company, Dealer_Name
                            from Chemical_Stock, Chemical_Dealers,Dealer_Chemical_Supply
                            where (Chemical_Dealers.Sl_No = Dealer_Chemical_Supply.Dealer_Id and Chemical_Stock.Chemical_Name = Dealer_Chemical_Supply.Chemical_Name) 
                            order by Date_of_Purchase'''
        query2 = '''select DISTINCT Chemical_Stock.Chemical_Id,Dealer_Chemical_Supply.Chemical_Name,Quantity,Price, Date_of_Purchase, Dealer_Company, Dealer_Name
                            from Chemical_Stock, Chemical_Dealers,Dealer_Chemical_Supply
                            where (Chemical_Dealers.Sl_No = Dealer_Chemical_Supply.Dealer_Id and Chemical_Stock.Chemical_Name = Dealer_Chemical_Supply.Chemical_Name) 
                            order by Quantity'''
        query3 = '''select DISTINCT Chemical_Stock.Chemical_Id,Dealer_Chemical_Supply.Chemical_Name,Quantity,Price, Date_of_Purchase, Dealer_Company, Dealer_Name
                            from Chemical_Stock, Chemical_Dealers,Dealer_Chemical_Supply
                            where (Chemical_Dealers.Sl_No = Dealer_Chemical_Supply.Dealer_Id and Chemical_Stock.Chemical_Name = Dealer_Chemical_Supply.Chemical_Name) 
                            order by Price'''
        if (item == 'Chemical'):
            self.ui.tableWidget.setHorizontalHeaderLabels(['ID', 'Chemical Name', 'Quantity', 'Price', 'Date of Purchase','Dealer_Company','Dealer_Name',''])         
            try:
                conn = sql.connect('industry_database.db')
                cursor = conn.cursor()
                if (sort_type == 'Date'):
                    cursor.execute(query1)
                elif (sort_type == 'Quantity'):
                    cursor.execute(query2)
                elif (sort_type == 'Price'):
                    cursor.execute(query3)
                row = cursor.fetchall()
                self.ui.tableWidget.setRowCount(0)
                for row_number, row_data in enumerate(row):
                    self.ui.tableWidget.insertRow(row_number)
                    for coloumn_number, data in enumerate(row_data):
                        self.ui.tableWidget.setItem(row_number, coloumn_number, QTableWidgetItem(str(data)))
            except Exception as e:
                print(e)
                QMessageBox.warning(self, "Error", "Please Check again\nError: "+str(e))

    def InventoryUpdate(self):
        product = self.ui.inventory_update_combo.currentText()
        id = self.ui.inventory_Id.text()
        price = self.ui.inventory_price.text()
        quantity = self.ui.inventory_quantity.text()
        query1 = '''update Chemical_Stock set Price = ? where Chemical_Id = ?'''
        query2 = '''update Products set Price = ? where Product_Id = ?'''
        query3 = '''select * from Chemical_Stock where Chemical_Id = ?'''
        query4 = '''select * from Products where Product_Id = ?'''
        if (product == 'Chemical'):
            conn = sql.connect('industry_database.db')         
            try:
                cursor = conn.cursor()
                if (id.isdigit()):
                    if (price != "" and quantity == "0"):
                        price = int(price)
                        id = int(id)
                        if self.CheckForExistance(query3, id) is True:
                            cursor.execute(query1, (price, id,))
                            conn.commit()
                            QMessageBox.information(self, "Succesfull", "Successfully Updated")
                    elif (price == "" and quantity != "0"):
                        self.InventoryUpdateQuantity()
                    elif (price == "" and quantity == "0"):
                        QMessageBox.warning(self, "Error", "Update info Blank")
                    elif (price != "" and quantity != "0"):
                        price = int(price)
                        id = int(id)
                        if self.CheckForExistance(query3, id) is True:
                            cursor.execute(query1, (price, id,))
                            conn.commit()
                            self.InventoryUpdateQuantity()
                else:
                    QMessageBox.warning(self, "Error", "ID is not a Number") 
            except Exception as e:
                print(e)
                QMessageBox.warning(self, "Error", "Please Check again\nError: "+str(e))       

        elif (product == 'Product'):
            conn = sql.connect('industry_database.db')         
            try:
                cursor = conn.cursor()
                if (id.isdigit()):
                    if (price != "" and quantity == "0"):
                        price = int(price)
                        id = int(id)
                        if self.CheckForExistance(query4, id) is True:
                            cursor.execute(query2, (price, id,))
                            conn.commit()
                            QMessageBox.information(self, "Succesfull", "Successfully Updated")
                    elif (price == "" and quantity != "0"):
                        self.InventoryUpdateQuantity()
                    elif (price == "" and quantity == "0"):
                        QMessageBox.warning(self, "Error", "Update info Blank")
                    elif (price != "" and quantity != "0"):
                        price = int(price)
                        id = int(id)
                        if self.CheckForExistance(query4, id) is True:
                            cursor.execute(query2, (price, id,))
                            conn.commit()
                            self.InventoryUpdateQuantity()
                else:
                    QMessageBox.warning(self, "Error", "ID is not a Number") 
            except Exception as e:
                print(e)
                QMessageBox.warning(self, "Error", "Please Check again\nError: "+str(e))    
            
    def InventoryUpdateQuantity(self):
        product = self.ui.inventory_update_combo.currentText()
        id = self.ui.inventory_Id.text()     
        id = int(id)   
        quantity = self.ui.inventory_quantity.text()
        query1 = '''select Quantity from ? where ? = ?'''
        query2 = '''update ? set Quantity = ? where ? = ?'''
        if product == 'Chemical':
            query1 = '''select Quantity from Chemical_Stock where Chemical_Id = ?'''
            query2 = '''update Chemical_Stock set Quantity = ? where Chemical_Id = ?'''
        elif product == 'Product':
            query1 = '''select Quantity from Products where Product_Id = ?'''
            query2 = '''update Products set Quantity = ? where Product_Id = ?'''    
        try:
            conn = sql.connect('industry_database.db')
            cursor = conn.cursor()
            cursor.execute(query1, (id,))
            row = cursor.fetchone()
            if row is None:
                QMessageBox.warning(self, "Error", "Please Check the Id\nError: ID Not Found ")
            else:
                sum = (int(row[0]) + int(quantity))
                cursor.execute(query2, (sum,id,))
                QMessageBox.information(self, "Succesfull", "Successfully Updated")
            conn.commit()
        except Exception as e:
            print(e)
            QMessageBox.warning(self, "Error", "please Check again\nError: "+str(e))    


    def CheckForExistance(self, query1,a):
        try:
            conn = sql.connect('industry_database.db')
            cursor = conn.cursor()
            cursor.execute(query1, (a,))
            row = cursor.fetchone()
            if row is None:
                QMessageBox.warning(self, "Error", "please Check the Id\nError: ID Not Found")
            else:
                return True
        except Exception as e:
            print(e)
            QMessageBox.warning(self, "Error", "please Check again\nError: "+str(e))    


    #--------------------------------------------------------

    #-------------------WholeSalerPage-----------------------

    def WholeSalerPage(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_wholesaler)
        self.WholeSalerCombo1()
        self.wholeSalerPageCombo()

    def wholesalerAll(self):
        self.ui.tableWidget_3.setHorizontalHeaderLabels(['Dealer ID', 'Dealer Compamy', 'Wholesaler Name', 'Phone No', 'ID Type','ID Number','Address'])         
        try:
            conn = sql.connect('industry_database.db')
            cursor = conn.cursor()
            cursor.execute('''select * from Chemical_Dealers''')
            row = cursor.fetchall()
            self.ui.tableWidget_3.setRowCount(0)
            for row_number, row_data in enumerate(row):
                self.ui.tableWidget_3.insertRow(row_number)
                for coloumn_number, data in enumerate(row_data):
                    self.ui.tableWidget_3.setItem(row_number, coloumn_number, QTableWidgetItem(str(data)))
        except Exception as e:
            print(e)
            QMessageBox.warning(self, "Error", "please Check again\nError: "+str(e))

    def WholeSalerCombo1(self):
        self.ui.wholesaler_sort2_combo.clear()
        item = self.ui.wholesaler_sort1_combo.currentText()
        if item == 'Chemical':
            try:
                conn = sql.connect('industry_database.db')
                cursor = conn.cursor()
                cursor.execute('''select Chemical_Name from Chemical_Stock''')
                row = cursor.fetchall()
                for i in row:
                    self.ui.wholesaler_sort2_combo.addItems(i)
            except Exception as e:
                print(e)
                QMessageBox.warning(self, "Error", "please Check again\nError: "+str(e))
        elif item == 'Company':         
            try:
                conn = sql.connect('industry_database.db')    
                cursor = conn.cursor()
                cursor.execute('''select DISTINCT Dealer_Company from Chemical_Dealers''')
                row = cursor.fetchall()
                for i in row:
                    self.ui.wholesaler_sort2_combo.addItems(i)
            except Exception as e:
                print(e)
                QMessageBox.warning(self, "Error", "Please Check again\nError: "+str(e))

    def WholeSalerSearch(self):
        Combo1 = self.ui.wholesaler_sort1_combo.currentText()
        Combo2 = self.ui.wholesaler_sort2_combo.currentText()
        query1 = '''select Sl_No, Dealer_Company, Dealer_Name, Dealer_Chemical_Supply.Chemical_Name,Phone_No
                    from Chemical_Dealers, Dealer_Chemical_Supply
                    where Dealer_Chemical_Supply.Dealer_Id = Chemical_Dealers.Sl_No and Chemical_Name = ?'''
        query2 = '''select Sl_No, Dealer_Company, Dealer_Name, Dealer_Chemical_Supply.Chemical_Name, Phone_No, Id_Type, Id_Number, Address
                    from Chemical_Dealers, Dealer_Chemical_Supply
                    where Dealer_Chemical_Supply.Dealer_Id = Chemical_Dealers.Sl_No and Dealer_Company = ?'''
        if Combo1 == 'Chemical':
            if (Combo2 != ''):
                try:
                    self.ui.tableWidget_3.setHorizontalHeaderLabels(['Dealer ID', 'Dealer Compamy', 'Wholesaler Name','Deals', 'Phone No','','',''])
                    conn = sql.connect('industry_database.db')
                    cursor = conn.cursor()
                    cursor.execute(query1, (Combo2,))
                    row = cursor.fetchall()
                    self.ui.tableWidget_3.setRowCount(0)
                    for row_number, row_data in enumerate(row):
                        self.ui.tableWidget_3.insertRow(row_number)
                        for coloumn_number, data in enumerate(row_data):
                            self.ui.tableWidget_3.setItem(row_number, coloumn_number, QTableWidgetItem(str(data)))
                except Exception as e:
                    print(e)
                    QMessageBox.warning(self, "Error", "Please Check again\nError: "+str(e))
            else:
                QMessageBox.warning(self, "Error", "Nothing Is Selected/DataBase is Empty")

        elif Combo1 == 'Company':
            if (Combo2 != ''):
                try:
                    self.ui.tableWidget_3.setHorizontalHeaderLabels(['Dealer ID', 'Dealer Compamy', 'Wholesaler Name', 'Deals', 'Phone No', 'ID Type','ID Number','Address'])
                    conn = sql.connect('industry_database.db')
                    cursor = conn.cursor()
                    cursor.execute(query2, (Combo2,))
                    row = cursor.fetchall()
                    self.ui.tableWidget_3.setRowCount(0)
                    for row_number, row_data in enumerate(row):
                        self.ui.tableWidget_3.insertRow(row_number)
                        for coloumn_number, data in enumerate(row_data):
                            self.ui.tableWidget_3.setItem(row_number, coloumn_number, QTableWidgetItem(str(data)))
                except Exception as e:
                    print(e)
                    QMessageBox.warning(self, "Error", "Please Check again\nError: "+str(e))
            else:
                QMessageBox.warning(self, "Error", "Nothing Is Selected/DataBase is Empty")

    def wholeSalerPageCombo(self):
        self.ui.wholesaler_chemical_combo.clear()         
        try:
            conn = sql.connect('industry_database.db')
            cursor = conn.cursor()
            cursor.execute('''select Chemical_Name from Chemical_Stock''')
            row = cursor.fetchall()
            for i in row:
                self.ui.wholesaler_chemical_combo.addItems(i)
        except Exception as e:
            print(e)
            QMessageBox.warning(self, "Error", "Please Check again\nError: "+str(e))

    def WholeSalerSortReset(self):
        if self.ui.Wholesaler_RadioButton.isChecked():
            self.ui.tableWidget_3.setSortingEnabled(True)
        else:
            self.ui.tableWidget_3.setSortingEnabled(False)

    def AddWholeSaler(self):
        comp = self.ui.wholesaler_comp.text()
        name = self.ui.wholesaler_name.text()
        phone_Number = self.ui.wholesaler_phone_no.text()
        address = self.ui.wholesaler_address.text()
        chemical = self.ui.wholesaler_chemical_combo.currentText()
        id_type = self.ui.wholesaler_id_type_combo.currentText()
        id_number = self.ui.wholesaler_id_number.text()
        query1 = '''INSERT INTO Chemical_Dealers(Dealer_Company, Dealer_Name, Phone_No, Id_Type, Id_Number, Address) values (?,?,?,?,?,?)'''
        query2 = '''select Sl_No from Chemical_Dealers where Dealer_Company = ? and Dealer_Name = ? '''
        query3 = '''insert into Dealer_Chemical_Supply(Dealer_Id, Chemical_Name) values (?, ?)'''
        if (phone_Number != "" and comp != "" and name != "" and address != "" and chemical != ""  and id_type != "" and id_number != "" and phone_Number.isdigit() and id_number.isdigit()):
            phone_Number = int(phone_Number)
            id_number = int(id_number)
            try:
                conn = sql.connect('industry_database.db')
                cursor = conn.cursor()
                cursor.execute(query1, (comp,name,phone_Number,id_type,id_number,address,))
                conn.commit()
                cursor.execute(query2, (comp,name,))
                row = cursor.fetchone()
                no = int(row[0])
                cursor.execute(query3, (no,chemical,))
                conn.commit()
                QMessageBox.information(self, "Succesfull", "Successfully Added")
                self.wholesalerAll()
            except Exception as e:
                print(e)
                QMessageBox.warning(self, "Error", "Please Check again\nError: "+str(e))
        else:
            QMessageBox.warning(self, "Error", "Please check the inputs again ")

    def WholeSalerPageAddChemical(self):
        query1 = '''select Dealer_Id, Chemical_Name from Dealer_Chemical_Supply where Dealer_Id = ? and Chemical_Name = ?'''
        query2 = '''insert into Dealer_Chemical_Supply (Dealer_Id, Chemical_Name) VALUES (?,?)'''
        Chemicals = []
        DealerID, ok = QInputDialog.getText(self, "Dealer ID", "Input Dealer ID")
        if ok == True and DealerID.isdigit():
            try:
                conn = sql.connect('industry_database.db')
                cursor = conn.cursor()
                cursor.execute('''select Chemical_Name from Chemical_Stock''')
                row = cursor.fetchall()
                for j in row:
                    for i in j:
                        Chemicals.append(str(i)) 
                chemical, select = QInputDialog.getItem(self, "Chemicals", "Select Chemical",Chemicals,0, False)
                if select and chemical:
                    try:
                        conn = sql.connect('industry_database.db')
                        cursor = conn.cursor()
                        cursor.execute(query1, (int(DealerID),str(chemical),))
                        row1 = cursor.fetchone()
                        if row1 is None:   
                            try:
                                cursor.execute(query2, (int(DealerID),str(chemical),))
                                conn.commit()
                                QMessageBox.information(self, "Succesfull", "Successfully Added")
                            except Exception as e:
                                print(e)
                                QMessageBox.warning(self, "Error", "Please Check again\nError: "+str(e))
                        else:
                            QMessageBox.warning(self, "Error", "Dealer already Supplies the Chemical")
                    except Exception as e:
                        print(e)
                        QMessageBox.warning(self, "Error", "Please Check again\nError: "+str(e))
            except Exception as e:
                print(e)
                QMessageBox.warning(self, "Error", "Please Check again\nError: "+str(e))

    def WholeSalerPageClear(self):
        self.ui.wholesaler_comp.setText('')
        self.ui.wholesaler_name.setText('')
        self.ui.wholesaler_phone_no.setText('')
        self.ui.wholesaler_address.setText('')
        self.ui.wholesaler_id_number.setText('')
        self.ui.wholesaler_chemical_combo.setCurrentIndex(0)
        self.ui.wholesaler_id_type_combo.setCurrentIndex(0)

    def WholeSalerPageDelete(self):
        billNumber = self.ui.wholesaler_delete.text()
        conn = sql.connect('industry_database.db')        
        query2 = '''delete from Chemical_Dealers where Sl_No = ? '''
        query3 = '''DELETE from Dealer_Chemical_Supply where Dealer_Id = ?'''
        if (billNumber != "") and billNumber.isdigit():
            billNumber = int(billNumber)
            try:
                conn = sql.connect('industry_database.db')  
                cursor= conn.cursor() 
                query = '''select Sl_No from Chemical_Dealers where Sl_No = ? '''
                cursor.execute(query,(billNumber,))
                row = cursor.fetchone()
                if row is None:
                    QMessageBox.warning(self, "Invalid", "Invalid Dealer ID")
                else:
                    try:
                        cursor = conn.cursor()
                        cursor.execute(query2, (billNumber,))
                        conn.commit()
                        cursor.execute(query3, (billNumber,))
                        conn.commit()
                        QMessageBox.information(self, "Successful", "Successfully Deleted from DataBase\nPlease Refresh")
                        self.ui.wholesaler_delete.setText("")
                    except Exception as e:
                        print(e)
                        QMessageBox.warning(self, "Error", "please Check again\nError: "+str(e))
            except Exception as e:
                        print(e)
                        QMessageBox.warning(self, "Error", "please Check again\nError: "+str(e))
        else:
            QMessageBox.warning(self, "Blank", "Input all fields")

    #--------------------------------------------------------

    #----------------SaleHistory-------------------------
    def SaleHistory(self):
        self.ui.sale_history_sort1_combo.clear()
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_sale_history)
        self.SaleHistoryComboProducts1()

    def SaleHistoryAll(self):         
        try:
            conn = sql.connect('industry_database.db')
            cursor = conn.cursor()
            cursor.execute('''select Bill_Number,Customer_Name,Product_Name,Quantity,Total,Date,Status,Phone_No from Order_Billing ''')
            row = cursor.fetchall()
            self.ui.tableWidget_2.setRowCount(0)
            for row_number, row_data in enumerate(row):
                self.ui.tableWidget_2.insertRow(row_number)
                for coloumn_number, data in enumerate(row_data):
                    self.ui.tableWidget_2.setItem(row_number, coloumn_number, QTableWidgetItem(str(data)))
        except Exception as e:
            print(e)
            QMessageBox.warning(self, "Error", "please Check again\nError: "+str(e))

    def SaleHistoryDel(self):
        billNumber = self.ui.employee_update_ssn_3.text()
        conn = sql.connect('industry_database.db')        
        query2 = '''delete from Order_Billing where Bill_Number = ? '''
        if (billNumber != "") and billNumber.isdigit():
            billNumber = int(billNumber)
            try:
                conn = sql.connect('industry_database.db')  
                cursor= conn.cursor() 
                query = '''select Bill_Number from Order_Billing where Bill_Number = ? '''
                cursor.execute(query,(billNumber,))
                row = cursor.fetchone()
                if row is None:
                    QMessageBox.warning(self, "Invalid", "Invalid Bill Number")
                else:
                    try:
                        cursor = conn.cursor()
                        cursor.execute(query2, (billNumber,))
                        conn.commit()
                        QMessageBox.information(self, "Successful", "Successfully Deleted from DataBase\nPlease Refresh")
                        self.ui.employee_update_ssn_3.setText("")
                    except Exception as e:
                        print(e)
                        QMessageBox.warning(self, "Error", "please Check again\nError: "+str(e))
            except Exception as e:
                        print(e)
                        QMessageBox.warning(self, "Error", "please Check again\nError: "+str(e))
        else:
            QMessageBox.warning(self, "Blank", "Input all fields")


    def SaleHistoryUpdate(self):
        billNumber = self.ui.employee_update_ssn_3.text()
        status= self.ui.emplyee_update_department_combo_3.currentText()
        conn = sql.connect('industry_database.db')        
        query2 = '''update Order_Billing set Status = ? where Bill_Number = ? '''
        try:
            if (billNumber != "") and (status != "") and billNumber.isdigit():
                billNumber = int(billNumber)
                try:
                    conn = sql.connect('industry_database.db')  
                    cursor= conn.cursor() 
                    query = '''select Bill_Number from Order_Billing where Bill_Number = ? '''
                    cursor.execute(query,(billNumber,))
                    row = cursor.fetchone()

                    if row is None:
                        QMessageBox.warning(self, "Invalid", "Invalid Bill Number")
                    else:
                        try:
                            cursor = conn.cursor()
                            cursor.execute(query2, (status,billNumber,))
                            conn.commit()
                            QMessageBox.information(self, "Successful", "Successfully updated the Status of Order in DataBase\nPlease Refresh to view changes")
                            self.ui.emplyee_update_department_combo_3.setCurrentIndex(0)
                        except Exception as e:
                            print(e)
                            QMessageBox.warning(self, "Error", "please Check again\nError: "+str(e))
                except Exception as e:
                        print(e)
                        QMessageBox.warning(self, "Error", "please Check again\nError: "+str(e))
            else:
                QMessageBox.warning(self, "Invalid", "Invalid Bill Number")  
        except Exception as e:
            print(e)
            QMessageBox.warning(self, "Error", "please Check again\nError: "+str(e))

    def SaleHistoryDeleteAll(self):         
        try:
            conn = sql.connect('industry_database.db')
            cursor = conn.cursor()
            cursor.execute('''delete from Order_Billing''')
            conn.commit()
            QMessageBox.information(self, "Successful", "Successfully Deleted All Order in DataBase")
            self.SaleHistoryAll()
        except Exception as e:
            print(e)

    def SaleHistorySearch(self):
        billNumber = self.ui.sale_history_billsearch.text()
        conn = sql.connect('industry_database.db')        
        query = '''select Bill_Number,Customer_Name,Product_Name,Quantity,Total,Date,Status,Phone_No from Order_Billing where Bill_Number = ? '''
        if (billNumber != "") and billNumber.isdigit():
            billNumber = int(billNumber)
            try:
                conn = sql.connect('industry_database.db')  
                cursor= conn.cursor() 
                cursor.execute(query,(billNumber,))
                row = cursor.fetchall()
                if row is None:
                    QMessageBox.warning(self, "Invalid", "Invalid Bill Number")
                else:
                    self.ui.tableWidget_2.setRowCount(0)
                    for row_number, row_data in enumerate(row):
                        self.ui.tableWidget_2.insertRow(row_number)
                        for coloumn_number, data in enumerate(row_data):
                            self.ui.tableWidget_2.setItem(row_number, coloumn_number, QTableWidgetItem(str(data)))
            except Exception as e:
                        print(e)
                        QMessageBox.warning(self, "Error", "please Check again\nError: "+str(e))
        else:
            QMessageBox.warning(self, "Blank", "Input any fields")


    def SaleHistoryComboProducts1(self):        
        query = '''select Product_Name from Products'''
        try:
            conn = sql.connect('industry_database.db')
            cursor = conn.cursor()
            cursor.execute(query)
            row = cursor.fetchall()
            self.ui.sale_history_sort1_combo.insertItem(0,'')
            for i in row:
                self.ui.sale_history_sort1_combo.addItems(i)
        except Exception as e:
            print(e)


    def SaleHistorySearchCombo1(self):
        productsort = self.ui.sale_history_sort1_combo.currentText()
        conn = sql.connect('industry_database.db')        
        query = '''select Bill_Number,Customer_Name,Product_Name,Quantity,Total,Date,Status,Phone_No from Order_Billing where Product_Name = ? '''
        if (productsort != ""):
            try:
                conn = sql.connect('industry_database.db')  
                cursor= conn.cursor() 
                cursor.execute(query,(productsort,))
                row = cursor.fetchall()
                if row is None:
                    QMessageBox.warning(self, "No Orders", "No Orders on the Current Product")
                else:
                    self.ui.tableWidget_2.setRowCount(0)
                    for row_number, row_data in enumerate(row):
                        self.ui.tableWidget_2.insertRow(row_number)
                        for coloumn_number, data in enumerate(row_data):
                            self.ui.tableWidget_2.setItem(row_number, coloumn_number, QTableWidgetItem(str(data)))
            except Exception as e:
                        print(e)
                        QMessageBox.warning(self, "Error", "please Check again\nError: "+str(e))
        else:
            QMessageBox.warning(self, "Blank", "Input or Select any fields")

    def SaleHistorySearchCombo2(self):
        Allsort = self.ui.sale_history_sort2_combo.currentText()
        productsort = self.ui.sale_history_sort1_combo.currentText()
        billNumber = self.ui.sale_history_billsearch.text()
        conn = sql.connect('industry_database.db')        
        query1 = '''select Bill_Number,Customer_Name,Product_Name,Quantity,Total,Date,Status,Phone_No from Order_Billing where Product_Name = ? order by Date '''
        query2 = '''select Bill_Number,Customer_Name,Product_Name,Quantity,Total,Date,Status,Phone_No from Order_Billing where Product_Name = ? order by Quantity'''
        query3 = '''select Bill_Number,Customer_Name,Product_Name,Quantity,Total,Date,Status,Phone_No from Order_Billing where Product_Name = ? order by Status'''

        if ((Allsort != "") and (productsort != "")):
            if (Allsort == "Date"):
                try:
                    conn = sql.connect('industry_database.db')  
                    cursor= conn.cursor()
                    cursor.execute(query1,(productsort,))
                    row = cursor.fetchall()
                    if row is None:
                        QMessageBox.warning(self, "No Orders", "No Orders Yet")
                    else:
                        self.ui.tableWidget_2.setRowCount(0)
                        for row_number, row_data in enumerate(row):
                            self.ui.tableWidget_2.insertRow(row_number)
                            for coloumn_number, data in enumerate(row_data):
                                self.ui.tableWidget_2.setItem(row_number, coloumn_number, QTableWidgetItem(str(data)))
                except Exception as e:
                            print(e)
                            QMessageBox.warning(self, "Error", "please Check again\nError: "+str(e))

            elif (Allsort == "Quantity"):
                try:
                    conn = sql.connect('industry_database.db')  
                    cursor= conn.cursor()
                    cursor.execute(query2, (productsort,))
                    row = cursor.fetchall()
                    if row is None:
                        QMessageBox.warning(self, "No Orders", "No Orders Yet")
                    else:
                        self.ui.tableWidget_2.setRowCount(0)
                        for row_number, row_data in enumerate(row):
                            self.ui.tableWidget_2.insertRow(row_number)
                            for coloumn_number, data in enumerate(row_data):
                                self.ui.tableWidget_2.setItem(row_number, coloumn_number, QTableWidgetItem(str(data)))
                except Exception as e:
                            print(e)
                            QMessageBox.warning(self, "Error", "please Check again\nError: "+str(e))

            elif (Allsort == "Order Status"):
                try:
                    conn = sql.connect('industry_database.db')  
                    cursor= conn.cursor()
                    cursor.execute(query3,(productsort,))
                    row = cursor.fetchall()
                    if row is None:
                        QMessageBox.warning(self, "No Orders", "No Orders Yet")
                    else:
                        self.ui.tableWidget_2.setRowCount(0)
                        for row_number, row_data in enumerate(row):
                            self.ui.tableWidget_2.insertRow(row_number)
                            for coloumn_number, data in enumerate(row_data):
                                self.ui.tableWidget_2.setItem(row_number, coloumn_number, QTableWidgetItem(str(data)))
                except Exception as e:
                            print(e)
                            QMessageBox.warning(self, "Error", "please Check again\nError: "+str(e))
        elif (((Allsort == "") and (productsort == "")) | billNumber.isdigit()):
            self.SaleHistorySearch()

        elif ((Allsort == "") and (productsort != "")):
            self.SaleHistorySearchCombo1()

        else:
            QMessageBox.information(self, "Table Sorting", "Enable Table Sorting to Use Custom Sort ")

    def SaleHistorySortReset(self):
        if self.ui.sale_history_checkbox.isChecked():
            self.ui.tableWidget_2.setSortingEnabled(True)
        else:
            self.ui.tableWidget_2.setSortingEnabled(False)
             
    #----------------------------------------------------

    #----------------CustomQueryPage--------------------

    def CustomQuery(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.custom_query)

    def QuerySearch(self):
        query = self.ui.query_inbox.toPlainText()
        self.QueryResults(query)

    def QueryResults(self, query):
        if (query != ""):
            try:
                conn = sql.connect('industry_database.db')  
                cursor= conn.cursor() 
                cursor.execute(query)
                row = cursor.fetchall()
                if row is None:
                    conn.commit()
                    QMessageBox.warning(self, "Successfull", "Successfully Executed")
                else:
                    self.ui.query_table.setRowCount(0)
                    for row_number, row_data in enumerate(row):
                        self.ui.query_table.insertRow(row_number)
                        for coloumn_number, data in enumerate(row_data):
                            self.ui.query_table.setItem(row_number, coloumn_number, QTableWidgetItem(str(data)))
            except Exception as e:
                        print(e)
                        QMessageBox.warning(self, "Error", "Please Check again\nError: "+str(e))
        else:
            QMessageBox.warning(self, "Blank", "Input is Blank")

    def QueryTableReset(self):
        self.ui.query_table.setRowCount(0)
        self.ui.query_table.setHorizontalHeaderLabels(['','','','','','','','','','','',])

    def QueryTableSorting(self):
        if self.ui.query_RadioBtn.isChecked():
            self.ui.query_table.setSortingEnabled(True)
        else:
            self.ui.query_table.setSortingEnabled(False)

    def QueryClear(self):
        self.ui.query_inbox.clear()

    def Query1(self):
        self.QueryClear()
        query = '''/* Retrieve The Pending Order Details with respect to available Quantity */

SELECT B.Bill_Number, B.Customer_Name, P.Product_Name, B.Date as Date_of_Order, P.Quantity as Quantity_Available, B.Quantity as Quantity_Ordered,P.Price, B.Total

FROM Order_Billing B, Products P

WHERE B.Product_Name = P.Product_Name and B.Status= 'Pending' or B.Status = 'pending' '''
        self.ui.query_inbox.insertPlainText(query)

    def Query2(self):
        self.QueryClear()
        query = '''/* Chemical Inventry Details Sort By Quantity */

SELECT DISTINCT Chemical_Stock.Chemical_Id,Dealer_Chemical_Supply.Chemical_Name,Quantity,Price, Date_of_Purchase, Dealer_Company, Dealer_Name
    
from Chemical_Stock, Chemical_Dealers,Dealer_Chemical_Supply
    
where (Chemical_Dealers.Sl_No = Dealer_Chemical_Supply.Dealer_Id and Chemical_Stock.Chemical_Name = Dealer_Chemical_Supply.Chemical_Name) 
    
order by Quantity '''
        self.ui.query_inbox.insertPlainText(query)

    def Query3(self):
        self.QueryClear()
        query = ''' /*All the Chemical Raw Material Dealers Info*/

select Sl_No, Dealer_Company, Dealer_Name, Dealer_Chemical_Supply.Chemical_Name, Phone_No, Id_Type, Id_Number, Address

from Chemical_Dealers, Dealer_Chemical_Supply

where Dealer_Chemical_Supply.Dealer_Id = Chemical_Dealers.Sl_No '''
        self.ui.query_inbox.insertPlainText(query)

    def Query4(self):
        self.QueryClear()
        query = '''/*Purchase History Details from Wholesale Dealers*/

select P.Invoice_No, D.Dealer_Company, D.Dealer_Name, DS.Chemical_Name,P.Date_of_Purchase, P.Quantity, P.Cost_of_One, P.Total

from Purchases as P, Chemical_Dealers as D, Dealer_Chemical_Supply as DS

where P.Supplier_Id = DS.Supply_Id and DS.Dealer_Id =  D.Sl_No'''
        self.ui.query_inbox.insertPlainText(query)

    def Query5(self):
        self.QueryClear()
        query = '''/* Natural Join With Chemical Dealer & Chemical Supplier */

select Sl_No, Dealer_Company, Dealer_Name, Dealer_Chemical_Supply.Chemical_Name, Phone_No, Id_Type, Id_Number, Address

from Chemical_Dealers NATURAL JOIN Dealer_Chemical_Supply

where Dealer_Chemical_Supply.Dealer_Id = Chemical_Dealers.Sl_No '''
        self.ui.query_inbox.insertPlainText(query)

    def InputHeader(self):
        header, result = QInputDialog.getText(self, "InputHeader", "Input Header Names with ','")
        if result == True:
            result1 = header.split(',')
            self.ui.query_table.setHorizontalHeaderLabels(result1)

    #----------------------------------------------------

    #-----------------EmployeePage-----------------------

    def EmployeePage(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_employee)
        self.EmployeePageAll()

    def EmployeePageAll(self):
        try:
            conn = sql.connect('industry_database.db')
            cursor = conn.cursor()
            cursor.execute('''select * from Employee''')
            row = cursor.fetchall()
            self.ui.tableWidget_7.setRowCount(0)
            for row_number, row_data in enumerate(row):
                self.ui.tableWidget_7.insertRow(row_number)
                for coloumn_number, data in enumerate(row_data):
                    self.ui.tableWidget_7.setItem(row_number, coloumn_number, QTableWidgetItem(str(data)))
        except Exception as e:
            print(e)
            QMessageBox.warning(self, "Error", "please Check again\nError: "+str(e))

    def EmployeeTableSorting(self):
        if self.ui.Employee_RadioBtn.isChecked():
            self.ui.tableWidget_7.setSortingEnabled(True)
        else:
            self.ui.tableWidget_7.setSortingEnabled(False)

    #----------------------------------------------------

    #---------------------Users--------------------------

    def UserPage(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_users)
        self.UserPageAll()

    def UserPageAll(self):
        try:
            conn = sql.connect('industry_database.db')
            cursor = conn.cursor()
            cursor.execute('''select * from Users''')
            row = cursor.fetchall()
            self.ui.tableWidget_5.setRowCount(0)
            for row_number, row_data in enumerate(row):
                self.ui.tableWidget_5.insertRow(row_number)
                for coloumn_number, data in enumerate(row_data):
                    self.ui.tableWidget_5.setItem(row_number, coloumn_number, QTableWidgetItem(str(data)))
        except Exception as e:
            print(e)
            QMessageBox.warning(self, "Error", "please Check again\nError: "+str(e))

    def UserAdd(self):
        name = self.ui.users_name.text()
        phoneNumber = self.ui.users_contact_no.text()
        username = self.ui.users_username.text()
        password = self.ui.users_password.text()
        id = self.ui.users_id_type_combo_2.currentText()
        id_Number = self.ui.users_id_no.text()
        Type = self.ui.users_acc_type_combo.currentText()
        query1 = '''INSERT INTO Users (Name, Contact_Number, Id_Type, Id_Number, User_Name, Password, Type ) VALUES (?,?,?,?,?,?,?)'''
        if (name != "" and phoneNumber != "" and username != "" and password != "" and id != ""  and id_Number != "" and phoneNumber.isdigit() and id_Number.isdigit()):
            phoneNumber = int(phoneNumber)
            id_Number = int(id_Number)
            try:
                conn = sql.connect('industry_database.db')
                cursor = conn.cursor()
                cursor.execute(query1, (name,phoneNumber,id, id_Number, username, password,Type,))
                conn.commit()
                QMessageBox.information(self, "Succesfull", "Successfully Added")
                self.UserPageAll()
                self.UserClear()
            except Exception as e:
                print(e)
                QMessageBox.warning(self, "Error", "please Check again\nError: "+str(e))
        else:
            QMessageBox.warning(self, "Error", "Please check the inputs again ")

    def UserClear(self):
        self.ui.users_name.setText('')
        self.ui.users_contact_no.setText('')
        self.ui.users_username.setText('')
        self.ui.users_password.setText('')
        self.ui.users_id_type_combo_2.setCurrentIndex(0)
        self.ui.users_id_no.setText('')

    def UserDel(self):
        userID = self.ui.users_userID.text()
        query1 = '''select * from Users where Sl_No = ?'''
        query2 = '''Delete from Users where Sl_No = ?'''
        if userID != '' and userID.isdigit():
            userID = int(userID)
            try:
                conn = sql.connect('industry_database.db')
                cursor = conn.cursor()
                cursor.execute(query1, (userID,))
                row = cursor.fetchone()
                if row is None:
                    QMessageBox.warning(self, "Invalid", "Invalid User ID\nPlease check the inputs again ")
                else:
                    cursor.execute(query2, (userID,))
                    conn.commit()
                    QMessageBox.information(self, "Succesfull", "Successfully Added")
                    self.UserPageAll()
                    self.UserClear()
            except Exception as e:
                print(e)
                QMessageBox.warning(self, "Error", "please Check again\nError: "+str(e))
        else:
            QMessageBox.warning(self, "Error", "Please check the inputs again ")

    def UserUpdate(self):
        userID = self.ui.users_userID.text()
        userName = self.ui.users_username_2.text()
        userPassword = self.ui.users_new_password.text()
        query1 = '''select * from Users where Sl_No = ?'''
        query2 = '''update Users set User_Name = ? where Sl_No = ?'''
        query3 = '''update Users set User_Name = ?, Password = ? where Sl_No = ? '''
        query4 = '''update Users set Password = ? where Sl_No = ? '''
        if userID != '' and userID.isdigit():
            userID = int(userID)
            try:
                conn = sql.connect('industry_database.db')
                cursor = conn.cursor()
                cursor.execute(query1, (userID,))
                row = cursor.fetchone()
                if row is None:
                    QMessageBox.warning(self, "Invalid", "Invalid User ID\nPlease check the inputs again ")
                elif userName != '' and userPassword == '':
                    cursor.execute(query2, (userName,userID,))
                    conn.commit()
                    QMessageBox.information(self, "Succesfull", "Successfully Added")
                    self.UserPageAll()
                elif userName != '' and userPassword != '':
                    cursor.execute(query3, (userName,userPassword,userID,))
                    conn.commit()
                    QMessageBox.information(self, "Succesfull", "Successfully Added")
                    self.UserPageAll()
                elif userName == '' and userPassword != '':
                    cursor.execute(query4, (userPassword,userID,))
                    conn.commit()
                    QMessageBox.information(self, "Succesfull", "Successfully Added")
                    self.UserPageAll()
            except Exception as e:
                print(e)
                QMessageBox.warning(self, "Error", "please Check again\nError: "+str(e))
        else:
            QMessageBox.warning(self, "Error", "Please check the User ID")

    def UserTableSorting(self):
        if self.ui.User_RadioBtn.isChecked():
            self.ui.tableWidget_5.setSortingEnabled(True)
        else:
            self.ui.tableWidget_5.setSortingEnabled(False)

    #----------------------------------------------------


#---------------------main----------------------------
def main():
    app = QApplication.instance()
    if app is None: 
        app = QApplication(sys.argv)
        DataBase_Connection()
        login = Login()
        if login.exec_() == QDialog.Accepted:
            window = SplashScreen()
            window.show()
            sys.exit(app.exec_())

#------------------------------------------------------



#------------------mainDemo-----------------------------
def main2():
    app = QApplication(sys.argv)
    DataBase_Connection()
    window = Main()
    window.show()
    sys.exit(app.exec_())    

#-----------------------------------------------------




if __name__ == "__main__":
    main()



    
