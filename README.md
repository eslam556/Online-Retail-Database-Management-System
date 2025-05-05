# 🛒 ONLINE RETAIL MANAGEMENT SYSTEM

### 📅 May 06, 2025  
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

The **Online Retail Management System** is a full-stack solution that manages customer purchases, inventory, shipping, and payments. It includes integration using **SSIS**, integrated analytics using **SSAS**, interactive reports via **SSRS**, and a web interface built in **Streamlit** for seamless customer interaction.

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

## 🚀 Project Workflow

The development followed a structured data pipeline:

1. **Date Dimension Generation**: A date dimension script was executed to populate calendar attributes.
2. **ETL Process (SSIS)**: Data was extracted from the OLTP system, transformed, and loaded into a structured Data Mart.
3. **Data Mart Creation**: Dimension and Fact tables were built to support analytical processing.
4. **SSAS Cubes**: Built to enable fast and multidimensional insights.
5. **SSRS Reports**: Developed from the cubes to support operational and strategic reporting.
6. **Streamlit Web App**: Designed for real-time customer interaction and order placement.

![Project Workflow](https://github.com/eslam556/Online-Retail-Database-Management-System/blob/main/Project%20WorkFlow.jpg)
---
## 🧩 ER Diagram

The ERD illustrates the structure of the database, defining entities such as **Customers**, **Orders**, **Products**, and their relationships:

- **One-to-Many**: Customer → Orders  
- **One-to-Many**: Product Category → Products  
- **One-to-Many**: Customer → Feedback  
- **One-to-Many**: Orders → Orders_Items  
- **Many-to-Many**: Orders ↔ Products (via Orders_Items)

![ER Digram](https://github.com/eslam556/Online-Retail-Database-Management-System/blob/main/Database/ERD.jpg)

---

## 🔗 Logical Mapping

The logical schema reflects the real-world relationships:

- `Customers` ←→ `Customer_Phones`: One-to-many  
- `Orders` ←→ `Orders_Items` ←→ `Products`: Many-to-many  
- `Coupons`, `Shipping`, and `Payments` are linked to `Orders` via foreign keys  
- `Feedback` connects `Customers` and `Products`

![Mapping](https://github.com/eslam556/Online-Retail-Database-Management-System/blob/main/Database/Mappings.jpg)

---

## 🛠️ Database Implementation

Implemented using **SQL Server**, the schema includes:

- Tables: `Customers`, `Orders`, `Products`, `Orders_Items`, `Coupons`, `Shipping`, `Feedback`, etc.  
- Constraints: Primary and foreign keys ensure data relationships.  
- Data types optimized for performance and scalability.

![Database Digram](https://github.com/eslam556/Online-Retail-Database-Management-System/blob/main/Database/Database%20Digram.jpg)
---
## 🧱 Data Mart (Star Schema)

A star schema was implemented to support analytical workloads. It consists of:

### Dimension Tables
- **Dim_Customer**: Customer profiles, location, and segmentation  
- **Dim_Product**: Product details, stock, category, and price  
- **Dim_Coupon**: Coupon codes, discounts, usage, and expiration  
- **Dim_Payment**: Payment method and transaction amount  
- **Dim_Date**: Calendar attributes for time-based analysis  

### Fact Table
- **Fact_Sales**: Captures each order transaction, linking to all dimensions with metrics such as quantity, total price, and discount  

This structure enables flexible slicing and aggregation for business intelligence.

![Data Mart Digram](https://github.com/eslam556/Online-Retail-Database-Management-System/blob/main/Data%20Mart/Data%20Mart%20Model.png)
---

## 🧪 SSIS (SQL Server Integration Services)

**SSIS** was used to design and execute ETL packages that:

- Extract data from the transactional database  
- Clean and transform fields (e.g., compute account age, mark expired coupons)  
- Load structured data into dimension and fact tables in the Data Mart  
- Ensure referential integrity and automate scheduled data loads  

![ETL Pipeline](https://github.com/eslam556/Online-Retail-Database-Management-System/blob/main/SSIS/ETL%20Pipeline.jpg)
---

## 📊 Database Analysis (SSAS)

Three analytical cubes were developed using **SQL Server Analysis Services (SSAS)** to deliver fast, multidimensional insights:

- **Sales Performance**: Measures total sales, average order value, and discount impact over time.  
- **Customer Behavior**: Analyzes order frequency, segment trends, and city/state-level customer patterns.  
- **Promotion Effectiveness**: Evaluates coupon usage, redemption rates, and sales lift from promotions.

These cubes enable slicing, dicing, and drilling into KPIs to support business decision-making.

![Sales Perfromance Cube](https://github.com/eslam556/Online-Retail-Database-Management-System/blob/main/SSAS/Sales%20Performace%20Cube%20Structure.jpg)
![Customer Behavior Cube](https://github.com/eslam556/Online-Retail-Database-Management-System/blob/main/SSAS/Customer%20Behavior%20Cube%20Structure.jpg)
![Promotion Effictivness](https://github.com/eslam556/Online-Retail-Database-Management-System/blob/main/SSAS/Promotion%20Effectivness%20Cube%20Structure.jpg)
---

## 📈 Database Reporting (SSRS)

Reports were created using **SQL Server Reporting Services (SSRS)** based on the three cubes:

- **Sales Performance Reports**: Show sales by year, product category, and city with drilldown capabilities.  
- **Customer Behavior Reports**: Visualize top cities by customer count, segment breakdowns, and customer acquisition trends.  
- **Promotion Effectiveness Reports**: Display coupon usage frequency, revenue impact, and redemption statistics.

Each report is designed to be interactive and help stakeholders monitor performance and uncover insights.

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
