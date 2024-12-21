
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os
import pandas as pd
import matplotlib
matplotlib.use('Agg')  
import matplotlib.pyplot as plt
import seaborn as sns

def upload_csv(request):
    return render(request, 'home.html')

def analysis(request):
    context = {}
    if request.method == "POST" and request.FILES.get('csv_file'):
        csv_file = request.FILES['csv_file']

        upload_dir = os.path.join(settings.MEDIA_ROOT, 'uploads')
        os.makedirs(upload_dir, exist_ok=True)
        fs = FileSystemStorage(location=upload_dir)
        file_path = fs.save(csv_file.name, csv_file)
        file_full_path = os.path.join(upload_dir, file_path)

        try:
            # To  Read CSV files
            data_of = pd.read_csv(file_full_path)

            # Data preview and description
            context['head'] = data_of.head().to_html()
            context['description'] = data_of.describe().to_html()

            # Missing values in CSV file 
            missing_values = data_of.isnull().sum()
            context['missing_values'] = missing_values.to_frame(name='Missing Values').to_html()

            # Ensure histogram directory exists or not 
            histogram_dir = os.path.join(settings.MEDIA_ROOT, 'histograms')
            os.makedirs(histogram_dir, exist_ok=True)

            # Generate histograms of the given data
            histograms = {}
            numerical_columns = data_of.select_dtypes(include=['number']).columns
            if not numerical_columns.any():
                context['error'] = "No numerical columns found in the uploaded CSV file."
                return render(request, 'home.html', context)

            for column in numerical_columns:
                fig, ax = plt.subplots()
                sns.histplot(data_of[column], kde=True, ax=ax)
                histogram_path = os.path.join(histogram_dir, f"{column}_histogram.png")
                fig.savefig(histogram_path)
                plt.close(fig)
                histograms[column] = os.path.join(settings.MEDIA_URL, 'histograms', f"{column}_histogram.png")
           
            context['histograms'] = histograms

        except Exception as e:
            context['error'] = f"An error occurred: {str(e)}"

        finally:
            # delete  the uploaded file
            if os.path.exists(file_full_path):
                os.remove(file_full_path)

    return render(request, 'analysis.html', context)
