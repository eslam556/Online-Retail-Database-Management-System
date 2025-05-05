Create database Online_Retail;

GO

use Online_Retail;

GO

create table Customers(
	Customer_ID INT IDENTITY(1,1) PRIMARY KEY,
	F_Name varchar(50),
	L_Name varchar(50),
	Email varchar(50),
	City varchar(50),
	State varchar(50),
	Account_Created_At date);

GO

create table Customer_Phones(
	Customer_ID int,
	Phone varchar(50),
	primary key (Customer_ID,phone),
	foreign key (Customer_ID) references Customers(Customer_ID));

GO

create table Product_category(
    Category_ID INT IDENTITY(1,1) PRIMARY KEY,
    Name varchar(50));

GO

create table Products( 
	Product_ID INT IDENTITY(1,1) PRIMARY KEY,
	Name varchar(100),
	Price float,
	Description varchar(255),
	Stock smallint,
	Category_ID int,
	foreign key (Category_ID) references Product_category(Category_ID));

GO

create table Coupons(
	Coupon_ID INT IDENTITY(1,1) PRIMARY KEY,
	Coupon_Code varchar(50),
	Discount_Value float,
	Times_Used tinyint,
	Expiry_Date date);

GO

create table Shipping(
	Shipping_ID INT IDENTITY(1,1) PRIMARY KEY,
	Track_Number smallint,
	Delivery_Date date,
	Shipping_Method varchar(50),
	Shipping_Address varchar(50));

GO

create table Orders(
	Order_ID INT IDENTITY(1,1) PRIMARY KEY,
	Status varchar(50),
	Order_date date,
	Customer_ID int,
	Shipping_ID int,
	Coupon_ID int,
	Payment_ID int,
	Payment_Amount smallint,
	Payment_Method varchar(50),
	Payment_Date date,
	Foreign key (Customer_ID) references Customers(Customer_ID),
	Foreign key (Shipping_ID) references Shipping(Shipping_ID),
	Foreign key (Coupon_ID) references Coupons(Coupon_ID));

GO

create table Orders_Items(
	Order_Items_ID INT IDENTITY(1,1) PRIMARY KEY,
	Order_ID int,
	Product_ID int,
	Quantity tinyint,
	foreign key	(Order_ID) references Orders(Order_ID),
	foreign key	(Product_ID) references Products(Product_ID));

GO

create table Feedback(
	Feedback_ID INT IDENTITY(1,1) PRIMARY KEY,
	Comment varchar(max),
	Rating int,
	Feedback_Date date,
	Product_id int,
	Customer_id int,
	Foreign Key (Product_id) references Products(Product_id),
	Foreign Key (Customer_id) references Customers(Customer_id));