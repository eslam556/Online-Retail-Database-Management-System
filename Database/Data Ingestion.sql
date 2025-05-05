USE [Online Retail];

BULK INSERT
	Customers
FROM
	'D:\courses\ITI Power BI\4.DataBase\Database Project\Data Source\Customers.csv'
WITH
	(
	FIRSTROW = 2,
	FIELDTERMINATOR = ',',
	TABLOCK
	);

GO

BULK INSERT
	Orders
FROM
	'D:\courses\ITI Power BI\4.DataBase\Database Project\Data Source\Orders.csv'
WITH
	(
	FIRSTROW = 2,
	FIELDTERMINATOR = ',',
	TABLOCK
	);

GO

BULK INSERT
	Coupons
FROM
	'D:\courses\ITI Power BI\4.DataBase\Database Project\Data Source\Coupons.csv'
WITH
	(
	FIRSTROW = 2,
	FIELDTERMINATOR = ',',
	TABLOCK
	);

GO

BULK INSERT
	Customer_Phones
FROM
	'D:\courses\ITI Power BI\4.DataBase\Database Project\Data Source\Customers Phones.csv'
WITH
	(
	FIRSTROW = 2,
	FIELDTERMINATOR = ',',
	TABLOCK
	);

GO

BULK INSERT
	Orders_Items
FROM
	'D:\courses\ITI Power BI\4.DataBase\Database Project\Data Source\Order Items.csv'
WITH
	(
	FIRSTROW = 2,
	FIELDTERMINATOR = ',',
	TABLOCK
	);

GO

BULK INSERT
	Product_Category
FROM
	'D:\courses\ITI Power BI\4.DataBase\Database Project\Data Source\Product Category.csv'
WITH
	(
	FIRSTROW = 2,
	FIELDTERMINATOR = ',',
	TABLOCK
	);

GO

BULK INSERT
	Shipping
FROM
	'D:\courses\ITI Power BI\4.DataBase\Database Project\Data Source\Shipping.csv'
WITH
	(
	FIRSTROW = 2,
	FIELDTERMINATOR = ',',
	TABLOCK
	);

GO

BULK INSERT
	Products
FROM
	'D:\courses\ITI Power BI\4.DataBase\Database Project\Data Source\Products.csv'
WITH
	(
	FIRSTROW = 2,
	FIELDTERMINATOR = ',',
	TABLOCK
	);

GO

BULK INSERT
	Feedback
FROM
	'D:\courses\ITI Power BI\4.DataBase\Database Project\Data Source\Feedback.csv'
WITH
	(
	FIRSTROW = 2,
	FIELDTERMINATOR = ',',
	TABLOCK
	);