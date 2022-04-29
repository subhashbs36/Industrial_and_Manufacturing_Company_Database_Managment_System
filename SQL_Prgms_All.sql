
CREATE TABLE IF NOT EXISTS Users (
                            Sl_No	INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                            Name	varchar(15) NOT NULL,
                            Contact_Number NUMBER(10) NOT NULL,
                            ID_Type	VARCHAR(15) NOT NULL,
                            ID_Number	NUMBER (15) NOT NULL,
                            User_Name	VARCHAR(10) NOT NULL,
                            Password	VARCHAR(15) NOT NULL);
							
							
insert into Users values(1, 'Subhash', 1234567890, 'Aadhar', 1234569870, 'Subhash', '123');

insert into Users values(2, 'Subhash', 1234567890, 'Aadhar', 1234569870, 'a', '1');

insert into Users values(3, 'Admin', 1234567890, 'Aadhar', 1234569870, 'admin', 'admin@123');

CREATE TABLE Chemical_Stock (
	Chemical_Id	INTEGER NOT NULL,
	Chemical_Name	varchar NOT NULL UNIQUE,
	Quantity	INTEGER NOT NULL,
	Price	INTEGER,
	Date_of_Purchase	date NOT NULL,
	PRIMARY KEY(Chemical_Id AUTOINCREMENT)
);

CREATE TABLE Chemical_Dealers (
	Sl_No	INTEGER NOT NULL,
	Dealer_Company	varchar(20) NOT NULL,
	Dealer_Name	varchar(20) NOT NULL,
	Chemical_Name	varchar(20) NOT NULL,
	Phone_No	number(10) NOT NULL,
	Id_Type	varchar(10) NOT NULL,
	Id_Number	number(10) NOT NULL,
	Address	varchar(25) NOT NULL,
	PRIMARY KEY(Sl_No AUTOINCREMENT),
	FOREIGN KEY(Chemical_Name) REFERENCES Chemical_Stock(Chemical_Name)
);

CREATE TABLE Purchases (
	Invoice_No	number(10) NOT NULL,
	Dealer_Name	varchar(20) NOT NULL,
	Chemical_Name	varchar(20) NOT NULL,
	Date_of_Purchase	date NOT NULL,
	Quantity	INTEGER NOT NULL,
	Cost_of_One	number NOT NULL,
	Total	number NOT NULL,
	FOREIGN KEY(Dealer_Name) REFERENCES Chemical_Dealers(Dealer_Name),
	FOREIGN KEY(Chemical_Name) REFERENCES Chemical_Stock(Chemical_Name),
	PRIMARY KEY(Invoice_No)
);

CREATE TABLE Products (
	Product_Id	INTEGER NOT NULL,
	Product_Name	varchar(20) NOT NULL UNIQUE,
	Price	INTEGER,
	Chemical1	varchar,
	Chemical2	varchar,
	Chemical3	varchar,
	Chemical4	varchar,
	PRIMARY KEY(Product_Id AUTOINCREMENT),
	FOREIGN KEY(Chemical3) REFERENCES Chemical_Stock(Chemical_Id),
	FOREIGN KEY(Chemical2) REFERENCES Chemical_Stock(Chemical_Id),
	FOREIGN KEY(Chemical1) REFERENCES Chemical_Stock(Chemical_Id),
	FOREIGN KEY(Chemical4) REFERENCES Chemical_Stock(Chemical_Id)
);

CREATE TABLE Products_Stock (
	Product_Id	INTEGER NOT NULL UNIQUE,
	Quantity	INTEGER,
	FOREIGN KEY(Product_Id) REFERENCES Products(Product_Id) on delete cascade
);

CREATE TABLE Order_Billing (
	Bill_Number	INTEGER NOT NULL,
	Customer_Name	varchar(20) NOT NULL,
	Phone_No	number(10) NOT NULL,
	Date	date NOT NULL,
	Product_Name	varchar(20) NOT NULL,
	Quantity	INTEGER NOT NULL,
	Total	INTEGER NOT NULL,
	Status	char (10) NOT NULL,
	FOREIGN KEY(Product_Name) REFERENCES Products(Product_Name),
	PRIMARY KEY(Bill_Number AUTOINCREMENT)
);

CREATE TABLE Employee (
	SSN	INTEGER NOT NULL,
	Name	varchar (20) NOT NULL,
	DOB	date NOT NULL,
	Department	varchar (15) NOT NULL,
	Id_Type	varchar (10) NOT NULL,
	Id_Number	INTEGER NOT NULL,
	Salary	INTEGER NOT NULL,
	PRIMARY KEY(SSN AUTOINCREMENT)
);

CREATE TABLE Temp_Order_Billing (
	id	INTEGER,
	Customer_Name	varchar(20) NOT NULL,
	Phone_No	number(10) NOT NULL,
	Date	date NOT NULL,
	Product_Name	varchar(20) NOT NULL,
	Quantity	INTEGER NOT NULL,
	Total	INTEGER NOT NULL,
	Status	char(10) NOT NULL,
	FOREIGN KEY(Product_Name) REFERENCES Products(Product_Name),
	PRIMARY KEY(id AUTOINCREMENT)
);



