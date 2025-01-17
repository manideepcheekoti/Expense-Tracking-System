# Expense Management System  

This project is a comprehensive **Expense Management System** featuring a **Streamlit frontend application** and a **FastAPI backend server**. It is designed to simplify personal finance management by allowing users to log daily expenses and analyze spending patterns efficiently.  

---


## Features

### 1. **Add/Update Expenses**
- **Log Daily Expenses**: Users can input expenses, specifying the amount, category (e.g., Rent, Food, Entertainment), and optional notes for additional context.
- **Automatic Fetching**: Existing expenses for a selected date are automatically retrieved and displayed for easy review or editing.
- **Validation**: Ensures data accuracy before sending it to the backend for storage.

### 2. **Analytics and Insights**
- **Category-Wise Breakdown**: Displays a bar chart showing percentage contributions of each category to the total expenses for a chosen date range.
- **Detailed Table**: Provides a tabular view of total amounts and percentages for each category, formatted for clarity and ease of understanding.
- **Spending Trends**: Helps users identify patterns in their spending habits.

### 3. **Backend Functionality**
- **Data Storage**: Efficiently handles storing and retrieving expense data.
- **Calculations**: Accurately calculates totals and category-wise percentages.
- **Error Handling**: Covers scenarios like invalid date inputs and empty datasets to ensure smooth functionality.

---

## Objectives
1. Simplify the process of logging and managing expenses.
2. Provide actionable insights into spending habits.
3. Ensure reliability and accuracy through robust backend operations.

---

## Tools and Technologies  

- **Languages**: Python, SQL  
- **Frameworks**:  
  - Frontend: Streamlit  
  - Backend: FastAPI  
- **Libraries**:  
  - Data Processing: `pandas`  
  - Visualization: `matplotlib`, `seaborn`  
- **Database**: SQL for expense storage and retrieval  

---


## Installation

### Prerequisites
- Python 3.8 or later
- pip (Python package manager)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/manideepcheekoti/Expense-Tracking-System.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Expense-Tracking-System
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

---

## Testing  

1. Run test cases for backend:  
   ```bash  
   pytest tests/backend  
   ```  

2. Run test cases for frontend:  
   ```bash  
   pytest tests/frontend  
   ```  

---

## How It Works

### 1. **Expense Management**
- Navigate to the **Add/Update tab** to log new expenses or edit existing ones.
- Select a date to automatically fetch stored expenses for review or updates.
- Add new expense entries by specifying the amount, category, and optional notes.

### 2. **Analytics and Visualization**
- Switch to the **Analytics tab** to analyze spending habits over a chosen date range.
- View category-wise spending trends via an interactive bar chart.
- Consult the detailed table for a complete breakdown of expenses, including percentages.

### 3. **Backend Operations**
- Data is stored and retrieved seamlessly, ensuring reliability.
- Built-in validations handle invalid inputs, ensuring accurate calculations.

---

## Key Insights
- **Category-Based Spending**: Identify which categories consume the most of your budget.
- **Spending Patterns**: Analyze trends over time to make informed financial decisions.
- **Real-Time Management**: Update expenses on the go with instant feedback.

---

## Future Enhancements
1. **Budget Tracking**: Allow users to set budgets and receive alerts when nearing the limit.
2. **Recurring Expenses**: Enable users to automate the entry of recurring expenses like rent or subscriptions.
3. **Expense Comparison**: Compare expenses across different time periods for deeper insights.

---

## Contributing
Contributions are welcome! If you’d like to enhance the project, feel free to fork the repository, make changes, and submit a pull request.

---


