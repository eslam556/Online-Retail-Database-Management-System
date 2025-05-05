# 🛒 ONLINE RETAIL MANAGEMENT SYSTEM

### 📅 April 25, 2025  
### 🏢 Information Technological Institute  
### 🎓 Power BI Development Track

---

## 👥 Team Members
- Mohamed Saeed  
- Eslam Mohamed  
- Kareem Emad  
- Mohamed Ahmed  

---

## 📌 Executive Summary

The **Online Retail Management System** is a full-stack solution that manages customer purchases, inventory, shipping, and payments. It includes integrated analytics using **SSAS**, interactive reports via **SSRS**, and a web interface built in **Streamlit** for seamless customer interaction.

---

## ❗ Problem Statement

Retail businesses need a centralized system to manage inventory, track orders, optimize promotions, and deliver personalized customer experiences. This project addresses these needs with a robust database, built-in analytics, reporting capabilities, and an intuitive web application.

---

## 💼 Business Case

- Each customer can place multiple orders.
- Customers may have multiple phone numbers.
- Customers can rate and leave feedback on purchased products.
- Orders are tied to one customer, include multiple items, and may use coupons.
- Products are organized by categories and can appear in multiple orders.
- Coupons manage discounts, usage limits, and expiry dates.
- Orders are linked to detailed shipping records and payment info.

---

## 🧩 ER Diagram

The ERD illustrates the structure of the database, defining entities such as **Customers**, **Orders**, **Products**, and their relationships:

- **One-to-Many**: Customer → Orders  
- **One-to-Many**: Product Category → Products  
- **One-to-Many**: Customer → Feedback  
- **One-to-Many**: Orders → Orders_Items  
- **Many-to-Many**: Orders ↔ Products (via Orders_Items)

![ER Digram](https://github.com/eslam556/Online-Retail-Database-Application/blob/main/Database/ERD.jpg)

---

## 🔗 Logical Mapping

The logical schema reflects the real-world relationships:

- `Customers` ←→ `Customer_Phones`: One-to-many  
- `Orders` ←→ `Orders_Items` ←→ `Products`: Many-to-many  
- `Coupons`, `Shipping`, and `Payments` are linked to `Orders` via foreign keys  
- `Feedback` connects `Customers` and `Products`

![Mapping](https://github.com/eslam556/Online-Retail-Database-Application/blob/main/Database/Mappings.jpg)

---

## 🛠️ Database Implementation

Implemented using **SQL Server**, the schema includes:

- Tables: `Customers`, `Orders`, `Products`, `Orders_Items`, `Coupons`, `Shipping`, `Feedback`, etc.  
- Constraints: Primary and foreign keys ensure data relationships.  
- Data types optimized for performance and scalability.

![Database Digram](https://github.com/eslam556/Online-Retail-Database-Application/blob/main/Database/Database%20Digram.jpg)
---

## 📊 Database Analysis (SSAS)

**SQL Server Analysis Services (SSAS)** was implemented to:

- Transform transactional data into multidimensional cubes  
- Enable slicing, dicing, drill-down, and aggregation  
- Support decision-makers with visual KPIs and performance metrics

---

## 📈 Database Reporting (SSRS)

**SQL Server Reporting Services (SSRS)** provides:

- Interactive and paginated reports  
- Insights into customer feedback trends, product popularity, order revenue, inventory status, and city-based performance  
- Linked reports for state-level breakdowns

---

## 🌐 Web Application (Streamlit)

Built using **Streamlit**, this customer-facing interface enables:

### ✅ Purpose

To provide an interactive and real-time ordering system while integrating directly with the backend SQL Server database.

### ⚙️ Key Features

- **Customer Registration & Login**  
  - Email verification to prevent duplicates  
  - Requires first name, last name, and phone number  

- **Product Browsing**  
  - Filter products by category  
  - Set quantities for each item  

- **Cart System**  
  - Add/remove items  
  - Recalculate subtotals and totals dynamically  

- **Shipping & Payment**  
  - Enter shipping address  
  - Choose shipping method and payment option  
  - Apply coupon codes if available  

- **Order Summary**  
  - Display all order details before confirmation  

### 🔌 Backend Integration

- Email existence check  
- Insert new customer and phone number  
- Filter products by category  
- Insert shipping info  
- Validate coupon codes  
- Insert order, payment, and order items via stored procedures  

## [App Walkthrough](https://drive.google.com/file/d/1NQBbRY54SnNdNE-DVTki9ULIQPZ1Qqeq/view?usp=sharing)
---

## 🔮 Conclusion & Future Enhancements

The project delivers a complete online retail system tailored for SMEs. Future enhancements may include:

- Integration with real-time payment gateways  
- Admin dashboard for managing orders, inventory, and promotions  
- AI-powered product recommendation system  

---
