CREATE DATABASE [Online Retail DM];

GO

USE [Online Retail DM];

GO

CREATE TABLE Dim_Customer(
Customer_Key INT PRIMARY KEY IDENTITY(1,1),
Customer_ID INT,
Customer_Full_Name VARCHAR(100),
Customer_Email VARCHAR(50),
Customer_City VARCHAR(50),
Customer_State VARCHAR(50),
Customer_Since DATE,
Customer_Account_Age_Days INT,
Customer_Segment VARCHAR(20)
);

GO

CREATE TABLE Dim_Product(
Product_Key INT PRIMARY KEY IDENTITY(1,1),
Product_ID INT,
Product_Name VARCHAR(100),
Product_Description VARCHAR(255),
Product_Stock SMALLINT,
Product_Category VARCHAR(50),
Product_Price FLOAT
);

GO

CREATE TABLE Dim_Coupon(
Coupon_Key INT PRIMARY KEY IDENTITY(1,1),
Coupon_ID INT,
Coupon_Code VARCHAR(50),
Coupon_Discount_Value FLOAT,
Coupon_Usage_Number TINYINT,
Coupon_Expiry_Date DATE,
Is_Expired BIT
);

GO

CREATE TABLE Dim_Payment(
Payment_Key INT PRIMARY KEY IDENTITY(1,1),
Payment_ID INT,
Payment_Amount SMALLINT,
Payment_Method VARCHAR(50)
);

GO

CREATE TABLE Dim_Date (
    Date_Key INT PRIMARY KEY IDENTITY(1,1),
    FullDate DATE,
    DayOfWeek TINYINT,
    DayName VARCHAR(10),
    DayOfMonth TINYINT,
    DayOfYear SMALLINT,
    WeekOfYear TINYINT,
    MonthNumber TINYINT,
    MonthName VARCHAR(10),
    Quarter TINYINT,
    QuarterName VARCHAR(10),
    Year SMALLINT,
    IsWeekend BIT,
    IsHoliday BIT,
    HolidayName VARCHAR(50)
);

GO

CREATE TABLE Fact_Sales(
Sales_Key INT PRIMARY KEY IDENTITY(1,1),
Order_Key INT,
Order_Date_Key INT,
Product_Key INT,
Customer_Key INT,
Payment_Key INT,
Coupon_Key INT,
Order_Quantity TINYINT,
Product_Unit_Price FLOAT,
Order_Total_Price FLOAT,
Discount_Amount FLOAT,
Final_Total_Price FLOAT,

FOREIGN KEY (Order_Date_Key) REFERENCES Dim_Date(Date_Key),
FOREIGN KEY (Product_Key) REFERENCES Dim_Product(Product_Key),
FOREIGN KEY (Customer_Key) REFERENCES Dim_Customer(Customer_Key),
FOREIGN KEY (Payment_Key) REFERENCES Dim_Payment(Payment_Key),
FOREIGN KEY (Coupon_Key) REFERENCES Dim_Coupon(Coupon_Key)
);