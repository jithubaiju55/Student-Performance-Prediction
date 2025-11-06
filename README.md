# 🧠 Student Performance Prediction

## 🎯 Project Overview
This project aims to **predict students’ final marks** based on their **study hours, attendance percentage, and previous exam marks** using **Linear Regression**.  
It helps identify which factors influence academic performance the most.

---

## 📊 Dataset
The dataset consists of **300 student records** with the following columns:

| Column | Description |
|--------|-------------|
| `Student_ID` | Unique ID for each student |
| `Study_Hours` | Average study hours per day |
| `Attendance_Percentage` | Class attendance percentage |
| `Previous_Marks` | Previous exam marks (0–100) |
| `Final_Marks` | Final exam marks (0–100, target variable) |

You can find the dataset in this repository:  
📂 **`student_performance_dataset.csv`**

---

## 🧩 Technologies Used
- **Python 3**
- **Pandas** – Data manipulation  
- **NumPy** – Numerical operations  
- **Matplotlib** – Data visualization  
- **Scikit-learn** – Machine learning model

---

## ⚙️ Steps Performed
1. **Data Cleaning** – Handled missing values and verified dataset quality  
2. **Exploratory Data Analysis (EDA)** – Visualized relationships between variables  
3. **Model Building** – Applied Linear Regression to predict final marks  
4. **Model Evaluation** – Calculated MSE and R² Score to assess performance  

---

## 📈 Results
- **Mean Squared Error (MSE):** 23.51  
- **R² Score:** 0.75  
- **Key Influencing Factors:**
  - Study Hours (most impactful)
  - Attendance Percentage
  - Previous Marks

**Interpretation:**  
Students who maintain **higher attendance and consistent study hours** tend to achieve better grades.

---

## 📉 Sample Visualizations
- Study Hours vs Final Marks  
- Attendance vs Final Marks  
- Actual vs Predicted Marks  

*(You can include screenshots or generated plots here)*

---

## 🚀 How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/Student-Performance-Prediction.git
   ```
2. Install dependencies:
   ```bash
   pip install pandas numpy matplotlib scikit-learn
   ```
3. Run the Python script:
   ```bash
   python student_performance.py
   ```
   or open the Jupyter notebook:
   ```bash
   jupyter notebook Student_Performance_Prediction.ipynb
   ```

---

## 🧾 Future Improvements
- Use larger, real-world datasets (e.g., from Kaggle)  
- Add new features like parental education or sleep hours  
- Experiment with advanced models (Random Forest, XGBoost)

---

## 👨‍💻 Author
**Jithu Baiju**  
📧 Add your email here  
💼 Add your LinkedIn profile link here  
🌐 Add your portfolio or GitHub link here
