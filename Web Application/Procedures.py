import pyodbc
import pandas as pd

# Function to establish a connection to the database
def get_connection():
    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 18 for SQL Server};"
        "SERVER=ESLAM\SQLEXPRESS;"
        "DATABASE=Online Retail;"
        "Trusted_Connection=yes;"
        "TrustServerCertificate=yes"
)
    return conn

# Function to insert customer details into the Customers table
def insert_customer(fname, lname, email, city, state):
    conn = get_connection()  # Establish a connection to the database
    cursor = conn.cursor() # Create a cursor to interact with the database

    # Execute stored procedure to insert customer details into the database
    cursor.execute(
        """
        EXEC InsertCustomerWithPhone ?, ?, ?, ?, ?;
        """, fname, lname, email, city, state)
    conn.commit() # Commit the transaction to the database
    conn.close() # Close the connection

# Function to insert customer phone numbers into the database
def insert_customer_phone_number(phone1 = None, phone2 = None, phone3 = None):
    conn = get_connection()
    cursor = conn.cursor()

    # Execute stored procedure to add customer phone numbers into the database
    cursor.execute(
        """
        EXEC AddCustomerPhones ?, ?, ?;
        """, phone1, phone2, phone3)
    conn.commit()
    conn.close()

# Function to validate customer login by email
def validate_customer_login(email):
    conn = get_connection()
    cursor = conn.cursor()

    # Execute stored procedure to validate customer login using email
    cursor.execute("EXEC ValidateCustomerLogin ?", email)
    result = cursor.fetchone()

    conn.close()
    return result # Return the result of the validation

# Function to get products by category
def get_products_by_category(category_name):
    if not category_name: # Check if the category name is provided
        return pd.DataFrame() # Return an empty DataFrame if no category name is provided
    
    category_string = ",".join(category_name) # Convert the list of category names into a comma-separated string

    conn = get_connection()
    cursor = conn.cursor()

    # Execute stored procedure to get products for the given category
    cursor.execute("EXEC GetProductsByCategory ?", category_string)

    rows = cursor.fetchall() # Fetch all the rows returned by the query
    columns = [column[0] for column in cursor.description] # Get the column names

    rows = [tuple(row) for row in rows] # Convert rows to tuples

    conn.close() 

    return pd.DataFrame(rows, columns = columns) # Return the data as a pandas DataFrame

# Function to insert shipping details into the database
def insert_shipping(track_number, delivery_date, shipping_method, shipping_address):
    conn = get_connection()
    
    cursor = conn.cursor()

    # Execute stored procedure to insert shipping details into the database
    cursor.execute(
        "EXEC InsertShippingDetails @Track_Number=?, @Delivery_Date=?, @Shipping_Method=?, @Shipping_Address=?",
        (track_number, delivery_date, shipping_method, shipping_address)
    )
    
    conn.commit()
    conn.close()

# Function to check the validity of a coupon and return the discount value
def check_coupon_discount(coupon_code):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        # Execute stored procedure to check coupon validity and get discount value
        cursor.execute("EXEC CheckCouponValidity ?", coupon_code)
        row = cursor.fetchone()
        if row:
            return row[0]  # Return the discount value if coupon is valid
        else:
            return None # Return None if coupon is invalid
    finally:
        conn.commit()
        conn.close()

# Function to insert order details into the Orders table
def insert_orders(Payment_Amount, Payment_Method, coupon_code):
    conn = get_connection()
    
    cursor = conn.cursor()

    # Get the coupon ID based on the coupon code
    cursor.execute("SELECT Coupon_ID FROM Coupons WHERE Coupon_Code = ?;", coupon_code)
    coupon_row = cursor.fetchone()

    if coupon_row:
        coupon_id = coupon_row[0]
    else:
        coupon_id = None  # If the coupon code is invalid or expired, set coupon_id to None

    # Execute stored procedure to insert order details into the database
    cursor.execute(
        "EXEC InsertOrder ?, ?, ?",
        (coupon_id, Payment_Amount, Payment_Method)
    )
    
    conn.commit()
    conn.close()