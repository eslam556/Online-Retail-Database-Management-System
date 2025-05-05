USE [Online Retail];

GO

CREATE PROCEDURE InsertCustomerWithPhone
@FName NVARCHAR(20),
@LName NVARCHAR(20),
@Email NVARCHAR(50),
@City NVARCHAR(20),
@State NVARCHAR(20)
AS
BEGIN
	INSERT INTO Customers (F_Name, L_Name, email, city, state, Account_Created_At)
	VALUES (@FName, @LName, @Email, @City, @State, GETDATE());

END;

GO

CREATE PROCEDURE AddCustomerPhones
    @Phone1 VARCHAR(50),
    @Phone2 VARCHAR(50),
    @Phone3 VARCHAR(50)
AS
BEGIN
	
	DECLARE @Customer_ID INT;

	SELECT
		TOP 1 @Customer_ID = Customer_ID
	FROM
		Customers
	ORDER BY
		Customer_ID DESC;

    IF @Phone1 IS NOT NULL
        INSERT INTO Customer_Phones (Customer_ID, Phone) VALUES (@Customer_ID, @Phone1);

    IF @Phone2 IS NOT NULL
        INSERT INTO Customer_Phones (Customer_ID, Phone) VALUES (@Customer_ID, @Phone2);

    IF @Phone3 IS NOT NULL
        INSERT INTO Customer_Phones (Customer_ID, Phone) VALUES (@Customer_ID, @Phone3);
END;

GO

CREATE PROCEDURE ValidateCustomerLogin
@Email VARCHAR(50)
AS
BEGIN
	SELECT F_Name, L_Name
    FROM Customers
    WHERE Email = @Email
END;

GO

CREATE PROCEDURE GetProductsByCategory
@CategoryName VARCHAR(MAX)
AS
BEGIN
	SELECT
		P.Product_ID,
		P.Name,
		P.Price,
		P.Stock,
		C.Name AS Category
	FROM
		Products P
	JOIN
		Product_category C
	ON
		P.Category_ID = C.Category_ID
	WHERE
		C.Name IN (SELECT VALUE FROM string_split(@CategoryName, ','))
END;

GO

CREATE PROCEDURE InsertShippingDetails
@Track_Number SMALLINT,
@Delivery_Date DATE,
@Shipping_Method VARCHAR(50),
@Shipping_Address VARCHAR(50)
AS
BEGIN
    INSERT INTO Shipping (Track_Number, Delivery_Date, Shipping_Method, Shipping_Address)
    VALUES (@Track_Number, @Delivery_Date, @Shipping_Method, @Shipping_Address)
END;

GO

CREATE PROCEDURE CheckCouponValidity
    @Coupon_Code VARCHAR(50)
AS
BEGIN
    -- Return discount if valid
    SELECT
		Discount_Value
    FROM
		Coupons
    WHERE
		Coupon_Code = @Coupon_Code
		AND Expiry_Date >= CAST(GETDATE() AS DATE);
END;

GO

CREATE PROCEDURE InsertOrder
    @Coupon_ID INT = NULL,
    @Payment_Amount SMALLINT,
    @Payment_Method VARCHAR(50)
AS
BEGIN
	DECLARE @Customer_ID INT;

	SELECT
		TOP 1 @Customer_ID = Customer_ID
	FROM
		Customers
	ORDER BY
		Customer_ID DESC;

	DECLARE @Shipping_ID INT;

	SELECT
		TOP 1 @Shipping_ID = Shipping_ID
	FROM
		Shipping
	ORDER BY
		Shipping_ID DESC;

	DECLARE @Payment_ID INT

    -- Get the max current Payment_ID and add 1, or start from 1 if table is empty
    SELECT @Payment_ID = ISNULL(MAX(Payment_ID), 0) + 1 FROM Orders

    INSERT INTO Orders (Status, Order_date, Customer_ID, Shipping_ID, Coupon_ID, Payment_ID, Payment_Amount, Payment_Method, Payment_Date)
    VALUES ('Confirmed', GETDATE(), @Customer_ID, @Shipping_ID, @Coupon_ID, @Payment_ID, @Payment_Amount, @Payment_Method, GETDATE())
END;
