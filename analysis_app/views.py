from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def upload_csv(request):
    return render(request, 'home.html')

def analysis(request):
    context = {}
    if request.method == "POST" and request.FILES.get('csv_file'):
        csv_file = request.FILES['csv_file']
        fs = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'uploads'))
        file_path = fs.save(csv_file.name, csv_file)
        file_full_path = os.path.join(settings.MEDIA_ROOT, 'uploads', file_path)

        try:
            data = pd.read_csv(file_full_path)

            head = data.head().to_html()
            description = data.describe().to_html()

            missing_values = data.isnull().sum()
            context['missing_values'] = missing_values.to_frame(name='Missing Values').to_html()

            histogram_dir = os.path.join(settings.MEDIA_ROOT, 'histograms')
            os.makedirs(histogram_dir, exist_ok=True)

            histograms = {}
            numerical_columns = data.select_dtypes(include=['number']).columns
            for column in numerical_columns:
                plt.figure()
                sns.histplot(data[column], kde=True)
                histogram_path = os.path.join(histogram_dir, f"{column}_histogram.png")
                plt.savefig(histogram_path)
                plt.close()
                histograms[column] = f"histograms/{column}_histogram.png"

            context['head'] = head
            context['description'] = description
            context['histograms'] = histograms

        except Exception as e:
            return render(request, 'home.html', {'error': str(e)})

    return render(request, 'analysis.html', context)



