# Revenue Leakage Analysis Dashboard – Power BI

## 📌 Project Overview
This project is a **Revenue Leakage Analysis Dashboard** built in **Power BI** to identify, measure, and visualize financial leakages across multiple clients and service categories.  
The goal is to provide a **data-driven view** of where revenue losses are occurring, enabling leadership teams to take corrective actions that directly improve profitability.

---

## 🎯 Objective
In many organizations, revenue leakage occurs due to **under-billing, unpaid invoices, rate mismatches, and unclaimed SLA credits**.  
This dashboard:
- Highlights **total potential leakage** and its key components.
- Pinpoints **top offending clients** causing the most financial impact.
- Provides **time-based trends** for better forecasting and decision-making.
- Allows **interactive filtering** by industry, geography, and time period.

---

## 📊 Dashboard Features
1. **Top KPI Cards**
   - **Total Potential Leakage** – Overall loss amount.
   - **Under-billed Hours**
   - **Unpaid Invoices**
   - **Rate Mismatch**
   - **Unclaimed SLA Credits**

2. **Leakage Composition Chart**
   - Stacked column chart showing category-wise leakage for each client.

3. **Top Offenders**
   - Horizontal bar chart listing clients with the highest total leakage.

4. **Detailed Audit Table**
   - Drill-down table with client-level and category-level details.

5. **Trend Analysis**
   - Line chart to visualize leakage over time (Month/Quarter/Year).

6. **Interactive Slicers**
   - Industry, Country, and Date filters for targeted insights.

---

## 📂 Dataset Details
- **Source:** Internal financial records (sample data for demonstration)
- **Granularity:** Client-level monthly records
- **Fields Used:**
  - `ClientName`
  - `Country`
  - `Industry`
  - `MonthlyFee`
  - `Leak_Hours_Revenue`
  - `Leak_Rate_Revenue`
  - `UnpaidAmount`
  - `Leakage_SLA_Credit`
  - `TotalLoss`
  - `Date`

---

## 🛠 Tools & Technologies
- **Power BI Desktop** – Data visualization & dashboard creation
- **DAX (Data Analysis Expressions)** – For custom measures
- **Microsoft Excel** – Initial data cleaning
- **GitHub** – Version control & project showcasing

---

## 📈 Insights & Key Takeaways
- **High-Risk Clients:**  
  A small group of clients contributes disproportionately to total leakage, requiring urgent contractual and operational reviews.
  
- **Category Analysis:**  
  Unpaid invoices and under-billed hours account for the majority of revenue loss.
  
- **Geographic Impact:**  
  Leakage patterns vary by region, with certain countries showing consistently higher unpaid amounts.
  
- **Trend Monitoring:**  
  Leakage is stable overall but spikes during contract renewals or billing cycle transitions.

---

## 📷 Dashboard Preview
![Revenue Leakage Dashboard](dashboard.png)

---

## 📢 How to Use This Dashboard
1. Download the `.pbix` file from this repository.
2. Open it in **Power BI Desktop**.
3. Use slicers to filter data by industry, country, and time.
4. Hover over visuals to see detailed tooltips and breakdowns.

---

## 📌 Business Value
By implementing this dashboard:
- Finance teams can **recover lost revenue** by targeting the most impactful leakage sources.
- Operations teams can **improve billing accuracy** and contract compliance.
- Leadership can **monitor trends** and prioritize high-risk accounts.

---

## 🔗 Dataset Access
*(Replace with your dataset link if public)*  
[Sample Dataset Download](dataset.csv)

---

## 👤 Author
**Vivek Patel**  
Data Analyst | Power BI Developer | Data Storyteller  
[LinkedIn Profile](https://www.linkedin.com/) | [GitHub Profile](https://github.com/)

---

## 📄 License
This project is for educational and portfolio purposes only.  
All sample data is anonymized and does not represent actual client information.
