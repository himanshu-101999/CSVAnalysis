# CSV Analysis Project


The CSV Analysis Project is designed to simplify the process of Exploratory Data Analysis (EDA) for users who may not have advanced technical expertise. The application allows users to upload a CSV file via a web interface  analyzes the dataset to provide a detailed overview, Visualizes key insights. leveraging powerful Python libraries like Pandas, Matplotlib,  Seaborn, The system can generate Statistical summaries, Identify missing data, and create intuitive Visualizations such as Histograms for numerical columns.


---

## Features

- **Upload CSV files** through a user-friendly web interface.
- **Display a preview** of the uploaded data (first 5 rows).
- **Perform statistical analysis**:
  - Calculate summary statistics (mean, median, standard deviation) for numerical columns.
  - Identify and handle missing values in the dataset.
- **Generate visualizations**:
  - Display histograms for numerical columns.
  - Render plots dynamically using Matplotlib and Seaborn.
- **Organized Results**: All data and visualizations are displayed in a clear and structured way.

---

## Prerequisites

- Python 3.8 or higher
- A virtual environment tool (optional but recommended)

---

## Installation and Setup Instructions

### Step 1: Clone the repository
```bash
git clone [(https://github.com/himanshu-101999/CSVAnalysis.git)]
cd csv_analysis_project
```

### Step 2: Create a virtual environment (optional but recommended)
```bash
python -m venv venv
# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### Step 3: Install dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run the development server
```bash
python manage.py runserver
```

### Step 5: Access the application
Open your browser and navigate to:
```
http://127.0.0.1:8000/
```

---

## Working

The project includes the following URL paths:

1. **Upload CSV File**:
   - Path: `upload/`
   - View: `views.upload_csv`
   - Functionality: Allows users to upload a CSV file for analysis.

2. **Data Analysis**:
   - Path: `analysis/`
   - View: `views.analysis`
   - Functionality: Processes the uploaded file, performs data analysis, and displays the results.

---

## Usage Instructions

1. Go to the `upload/` page to upload a CSV file.
2. After uploading, you will be redirected to the `analysis/` page to view:
   - A preview of the data (first 5 rows).
   - Summary statistics for numerical columns.
   - Missing values count.
   - Histograms for numerical columns.

---

## Project Structure

```
csv_analysis_project/
├── analysis_app/           # Main Django app
│   ├── templates/           # HTML templates
│   ├── views.py            # View logic
│   ├── models.py           # Models (if used)
│   ├── urls.py             # App URLs
├── media/                  # Directory for uploaded files and generated plots
├── static/                 # Static files (CSS, JS, etc.)
├── templates/              # Base templates
├── db.sqlite3               # SQLite database
├── manage.py               # Django management script
├── requirements.txt        # List of dependencies
├── testing_data.csv        # CSV file to test the system : TESTING DATASET
├── README.md               # Project documentation
```

---

## Dependencies

The project relies on the following Python packages:
- **Django**: For the web framework.
- **Pandas**: For data manipulation and analysis.
- **Matplotlib**: For generating visualizations.
- **Seaborn**: For enhanced data visualization.

### Install dependencies using:
```bash
pip install -r requirements.txt
```

---

## Example CSV File

Here’s an example of a sample CSV file format you can use for testing:

```
Name,Age,Salary,Department,Joining_Date
Alice,30,50000,HR,2020-01-15
Bob,27,54000,IT,2019-11-23
Charlie,22,49000,Finance,2021-06-30
David,32,62000,Sales,2018-09-12
Eva,29,58000,HR,2020-05-20
```

---

## Contributing

Contributions are welcome! Feel free to fork the repository, create a branch, and submit a pull request.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

## Contact

For any questions or suggestions, please reach out to the project owner at [himanshurajvis12@gmail.com].

