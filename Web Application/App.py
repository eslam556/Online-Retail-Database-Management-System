#python -m streamlit run App.py

import streamlit as st
from streamlit_lottie import st_lottie
import json
from Procedures import *
import time
import random
from datetime import datetime, timedelta
import requests

# App settings
st.set_page_config(page_title = "Online Retail Application", page_icon = "🛒", layout="centered")

# Load Lottie animation from file
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Welcome page
def WelcomePage():
    with st.container():

        # Title and subtitle
        st.markdown(
            """
            <div style="text-align: center;">
                <h1 style="font-size: 3em; color: #4CAF50;">🛒 Online Retail</h1>
                <p style="font-size: 1.2em; color: #666;">Seamlessly explore and order your favorite products</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        # Animation
        lottie_coding = load_lottieurl("https://lottie.host/5e36a5f4-f79f-4b12-93c2-031223dfabbd/ivi5PCejO9.json")
        st_lottie(
            lottie_coding,
            height=300
        )

        # Button to proceed
        st.markdown("### Ready to start your shopping journey?")
        begin = st.button("Begin Your Order", use_container_width=True)

        # Go to account page
        if begin:
            st.session_state["current_page"] = "AccountAccessPage"
            st.rerun()

# Choose login or register
def AccountAccessPage():
    st.title("🛒 Welcome to Online Retail System")

    st.write("Are you an existing customer or new here?")

    col1, col2 = st.columns(2)
    with col1:
        # Existing user
        if st.button("🔐 Login", use_container_width=True):
            st.session_state["current_page"] = "LoginPage"  # Navigate to login
            st.rerun()
    with col2:
        # New user
        if st.button("📝 Register", use_container_width=True):
            st.session_state["current_page"] = "RegistrationPage"  # Navigate to registration
            st.rerun()

def RegistrationPage():
    with st.container():
        st.title("📝 Register as a Customer")

    with st.form("customer_form"): # Registration form
        st.subheader("Personal Information")

        # Input fields
        fname = st.text_input("First Name*", max_chars=50)
        lname = st.text_input("Last Name*", max_chars=50)
        email = st.text_input("Email", max_chars=50)
        city = st.text_input("City", max_chars=50)
        state = st.text_input("State", max_chars=50)

        st.markdown("---")
        st.subheader("📞 Phone Numbers (at least one required)")
        
        # Phone numbers
        phone1 = st.text_input("Phone 1*", max_chars=50)
        phone2 = st.text_input("Phone 2 (optional)", max_chars=50)
        phone3 = st.text_input("Phone 3 (optional)", max_chars=50)

        col1, col2 = st.columns(2)

        with col1:
            # Register button
            submit = st.form_submit_button("Register")
        with col2:
            # Back button
            back = st.form_submit_button("🔙 Back to Login")

        if submit:
            # Validation
            if not fname or not lname:
                st.error("First and Last names are required.")
            elif not phone1:
                st.error("At least Phone 1 is required.")
            else:
                try:
                    # Insert customer & phone numbers into DB
                    insert_customer(fname, lname, email, city, state)
                    insert_customer_phone_number(phone1, phone2, phone3)

                    # Store customer data
                    st.session_state['customer'] = {
                                    'fname': fname,
                                    'lname': lname,
                                    'email': email,
                                    'city': city,
                                    'state': state
                                }
                    
                    st.success("Customer registered successfully!")
                    st.balloons()

                    time.sleep(2.5)

                    st.session_state["current_page"] = "OrderPage" # Redirect to order page
                    st.rerun()

                except Exception as e:
                    st.error(f"An error occurred: {e}")

        if back:
            st.session_state["current_page"] = "AccountAccessPage" # Back to account page
            st.rerun()
    
def LoginPage():
    st.title("🔐 Customer Login")

    # Initialize login flag
    if "login_success" not in st.session_state:
        st.session_state.login_success = False

    with st.form("login_form"): # Login form
        email = st.text_input("Email") # Email input
        
        col1, col2 = st.columns(2)

        with col1:
            submitted = st.form_submit_button("Login") # Login button
        with col2:
            back = st.form_submit_button("🔙 Back to Register")
        
        if submitted:
            if not email:
                st.error("Please enter the Email.")
            else:
                result = validate_customer_login(email) # Check if email exists in DB
                if result:
                    st.success(f"Welcome back, {result.F_Name} {result.L_Name}! 🎉")
                    st.balloons()
                    st.session_state.login_success = True
                    st.session_state["current_page"] = "OrderPage"  # Next page after login
                    st.rerun()
                else:
                    st.error("Invalid credentials. Please try again.")

        if back:
            st.session_state["current_page"] = "AccountAccessPage"
            st.rerun()

def OrderPage():
    st.title("🛍️ Product Selection")

    categories = ["Furniture", "Technology", "Office Supplies"]

    if 'selected_categories' not in st.session_state:
        st.session_state.selected_categories = [] # Initialize selected categories

    # Multi-select category
    selected_categories = st.multiselect("Select one or more categories:", categories, default=st.session_state.selected_categories)

    # Store selection
    st.session_state.selected_categories = selected_categories

    if selected_categories:
        df = get_products_by_category(selected_categories) # Fetch filtered products from DB

        if not df.empty:
            st.subheader("Browse Products")

            if 'product_page' not in st.session_state:
                st.session_state.product_page = 1 # Initialize pagination

            rows_per_page = 20
            total_rows = len(df)
            total_pages = (total_rows + rows_per_page - 1) // rows_per_page

            start_idx = (st.session_state.product_page - 1) * rows_per_page
            end_idx = start_idx + rows_per_page
            current_page_data = df[start_idx:end_idx] # Paginate

            for i in range(0, len(current_page_data), 3):
                cols = st.columns(3)
                for j, col in enumerate(cols):
                    if i + j < len(current_page_data):
                        row = current_page_data.iloc[i + j]
                        product_name = row['Name']
                        product_price = row['Price']
                        product_category = row['Category']
                        product_id = row['Product_ID']

                        with col:
                            st.markdown(f"#### {product_name}")
                            st.markdown(f"💵 **Price**: ${product_price:.2f}")
                            st.markdown(f"📦 **Category**: {product_category}")
                            
                            qty_key = f"qty_{product_id}"
                            add_key = f"add_{product_id}"
                            
                            qty = st.number_input("Quantity", min_value=0, step=1, value=0, key=qty_key)

                            if st.button("🛒 Add to Cart", key=add_key): # Add to cart
                                if 'cart' not in st.session_state:
                                    st.session_state.cart = []
    
                                total_price = product_price * qty  # Calculate total price
    
                                st.session_state.cart.append({
                                    'name': product_name,
                                    'price': product_price,
                                    'quantity': qty,
                                    'total_price': total_price  # Store the total price
                                })
                                st.success(f"✅ Added {qty} x {product_name} to cart!")

            st.markdown("---")

            # Pagination buttons
            col1, col2, col3 = st.columns([1, 6, 1])
            with col1:
                if st.button("⬅️ Previous") and st.session_state.product_page > 1:
                    st.session_state.product_page -= 1
                    st.rerun()
            with col3:
                if st.button("Next ➡️") and st.session_state.product_page < total_pages:
                    st.session_state.product_page += 1
                    st.rerun()

            st.markdown(f"<center>Page {st.session_state.product_page} of {total_pages}</center>", unsafe_allow_html=True)

        else:
            st.warning("No products found for the selected category.")
    else:
        st.info("Please select at least one category.")
    
    # View cart button
    if st.button("🛒 View Cart"):
        st.session_state.current_page = "CartPage"
        st.rerun()

def CartPage():
    st.title("🛒 Your Shopping Cart")

    # If cart is empty go to the order page
    if 'cart' not in st.session_state or len(st.session_state.cart) == 0:
        st.info("Your cart is empty. Go back and add some products!")
        if st.button("Go Back"):
            st.session_state.current_page = "OrderPage"
            st.rerun()

    st.subheader("🧾 Items in Your Cart:")

    items_to_remove = []
    updated_cart = []
    total_price = 0

    # Display each cart item with edit/remove options
    for i, item in enumerate(st.session_state.cart):
        col1, col2, col3, col4 = st.columns([4, 2, 2, 1])
        with col1:
            st.markdown(f"**{item['name']}**")
        with col2:
            qty_key = f"qty_{i}"
            new_qty = st.number_input("Qty", min_value=1, step=1, value=item['quantity'], key=qty_key)
        with col3:
            st.markdown(f"**${item['price']:.2f}** each")
            st.markdown(f"Subtotal: **${item['price'] * new_qty:.2f}**")
        with col4:
            if st.button("❌", key=f"remove_{i}"):
                items_to_remove.append(i) # Mark for item removed

        # Add updated item
        updated_cart.append({
            'name': item['name'],
            'price': item['price'],
            'quantity': new_qty,
            'total_price': item['price'] * new_qty
        })
        total_price += item['price'] * new_qty
        
    # Remove items from cart
    if items_to_remove:
        for i in sorted(items_to_remove, reverse=True):
            del st.session_state.cart[i]
        st.rerun()

    # Update cart
    st.session_state.cart = updated_cart

    st.markdown("---")
    st.markdown(f"### 🧮 Total Price: **${total_price:.2f}**")

    # Navigation buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🛍️ Continue Shopping"):
            st.session_state.current_page = "OrderPage"
            st.rerun()
    with col2:
        if st.button("🚚 Proceed to Shipping", use_container_width=True):
            st.session_state["current_page"] = "ShippingPage"
            st.rerun()

def ShippingPage():
    st.title("🚚 Shipping Details")

    with st.form("shipping_form"):
        st.subheader("🏠 Enter Shipping Information")

        # Input for shipping address & method
        shipping_address = st.text_input("Shipping Address (max 50 characters)", max_chars=50)
        shipping_method = st.selectbox("Shipping Method", ["Flight", "Road", "Ship"])

        col1, col2 = st.columns(2)

        with col1:
            submitted = st.form_submit_button("Confirm Shipping")
        with col2:
            back = st.form_submit_button("🔙 Back to Cart")

        if submitted:
            if not shipping_address:
                st.error("Please enter the shipping address.")
            else:
                try:
                    # Simulate tracking number and delivery date
                    tracking_number = random.randint(1, 32767)  # Ranges compatible with the DB
                    days_map = {"Flight": 1, "Road": 3, "Ship": 7}
                    delivery_date = (datetime.now() + timedelta(days=days_map[shipping_method])).date()

                    st.success("✅ Shipping details saved successfully!")
                    st.markdown(f"**Tracking Number:** `{tracking_number}`")
                    st.markdown(f"**Estimated Delivery Date:** `{delivery_date}`")
                    
                    # Save shipping details to session
                    st.session_state['shipping_info'] = {
                        "tracking_number": tracking_number,
                        "shipping_method": shipping_method,
                        "shipping_address": shipping_address,
                        "delivery_date": delivery_date
                    }
                    
                    time.sleep(2.5)

                    # Go to payment page
                    st.session_state["current_page"] = "PaymentPage"
                    st.rerun()

                except Exception as e:
                    st.error(f"An error occurred: {e}")

        # Go back to cart page
        if back:
            st.session_state["current_page"] = "CartPage"
            st.rerun()

def PaymentPage():
    st.title("💳 Payment Details")

    if "cart" not in st.session_state or not st.session_state.cart:
        st.warning("🛒 Your cart is empty.")
        return

    # Selecting payment method
    st.subheader("Select Payment Method")
    payment_method = st.radio("Payment Method", ["Credit Card", "Visa", "Master Card", "Cash"])

    # Card number input if card payment selected
    if payment_method in ["Visa", "Master Card", "Credit Card"]:
        card_number = st.text_input(f"Enter your {payment_method} number:", max_chars=16)
    else:
        card_number = None

    # Inserting a coupon code if any
    coupon_code = st.text_input("Enter Coupon Code (optional)")
    discount = 0
    if coupon_code:
        discount_value = check_coupon_discount(coupon_code) # Check if the code exists in DB
        if discount_value is not None:
            discount = discount_value
            st.success(f"✅ Coupon applied! Discount: ${discount:.2f}")
        else:
            st.warning("⚠️ Invalid or expired coupon.")

    # Calculate total product price
    total_amount = sum(product['total_price'] for product in st.session_state.cart)
    final_amount = max(total_amount - discount, 0)  # Prevent negative total

    st.markdown(f"### 💳 Total Amount: ${final_amount:.2f}")

    col1, col2 = st.columns(2)

    with col1:
        # Confirm Payment Button
        if st.button("Confirm Payment"):
            if payment_method in ["Visa", "Master Card", "Credit Card"] and not card_number:
                st.warning("Please enter your card number.")
            else:

                # Save payment info to session
                st.session_state['payment_method'] = {
                    "card_number": card_number,
                    "payment_method": payment_method,
                    "final_amount": final_amount,
                    "coupon_code": coupon_code
                }
                time.sleep(2.5)

                st.session_state.current_page = "SummaryPage"
                st.rerun()
    with col2:

        # Go back to shipping page
        if st.button("🔙 Back to Shipping"):
            st.session_state.current_page = "ShippingPage"
            st.rerun()

def updating_database():

    # Retrieve shipping and payment info
    shipping = st.session_state.shipping_info
    payment_method = st.session_state.payment_method
    
    # Extract shipping details
    tracking_number = shipping.get('tracking_number')
    delivery_date = shipping.get('delivery_date')
    shipping_method = shipping.get('shipping_method')
    shipping_address = shipping.get('shipping_address')

    # Extract coupon details
    coupon = payment_method.get('coupon_code')

    # Extract payment details
    payment_amount = payment_method.get('final_amount')
    payment_method_name = payment_method.get('payment_method')

    # Insert shipping details into the database
    insert_shipping(tracking_number, delivery_date, shipping_method, shipping_address)

    # Insert order details into the database
    insert_orders(payment_amount, payment_method_name, coupon)


def SummaryPage():
    st.title("📦 Order Summary")

    # Check if necessary session state variables exist
    if 'cart' not in st.session_state or not st.session_state.cart:
        st.warning("No order found. Please add items to your cart first.")
        return

    if 'shipping_info' not in st.session_state:
        st.warning("Shipping information missing.")
        return

    if 'payment_method' not in st.session_state:
        st.warning("Payment method not selected.")
        return

    # Shipping Info
    st.subheader("🚚 Shipping Information")
    shipping = st.session_state.shipping_info
    st.write(f"**Shipping Address:** {shipping.get('shipping_address', 'N/A')}")
    st.write(f"**Shipping Method:** {shipping.get('shipping_method', 'N/A')}")
    st.write(f"**Delivery Date:** {shipping.get('delivery_date', 'N/A')}")

    # Cart Items
    st.subheader("🛍️ Items Ordered")
    total_price = 0
    for item in st.session_state.cart:
        subtotal = item['price'] * item['quantity']
        total_price += subtotal
        st.markdown(
    f"- **{item['name']}** (x{item['quantity']}) — {item['price']:.2f} each → **{subtotal:.2f}**")

    # Payment Info
    st.subheader("💳 Payment Method")
    payment_method = st.session_state.payment_method
    st.write(f"**Method:** {payment_method['payment_method']}")

    # Mask card number if available
    if payment_method["payment_method"] in ["Visa", "Master Card", "Credit Card"]:
        card_number = payment_method.get("card_number", "")
        if card_number:
            masked_card = f"{'*' * (len(card_number) - 4)}{card_number[-4:]}"
            st.write(f"**Card Number:** {masked_card}")

    # Final Total
    st.markdown("---")
    st.markdown(f'### 🧾 Total Amount: **${payment_method["final_amount"]:.2f}**')

    # Finalize or Go Back
    col1, col2 = st.columns(2)
    with col1:
        if st.button("✅ Confirm & Place Order"):
            st.success("🎉 Order placed successfully!")
            
            updating_database() # Insert records into database
            
    with col2:
        if st.button("🔙 Back to Payment"):
            st.session_state.current_page = "PaymentPage"
            st.rerun()

# Navigation between pages based on session state
current_page = st.session_state.get("current_page", "WelcomePage")

if current_page == "WelcomePage":
    WelcomePage()
if current_page == "AccountAccessPage":
    AccountAccessPage()
if current_page == "RegistrationPage":
    RegistrationPage()
if current_page == "LoginPage":
    LoginPage()
if current_page == "OrderPage":
    OrderPage()
if current_page == "CartPage":
    CartPage()
if current_page == "ShippingPage":
    ShippingPage()
if current_page == "PaymentPage":
    PaymentPage()
if current_page == "SummaryPage":
    SummaryPage()