from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, FileResponse
from django.conf import settings
import os


def download_sample(request):
    # Path to your CSV file in the static folder
    file_path = os.path.join(settings.BASE_DIR, 'expenses', 'static', 'example.csv')

    # Open the file and return it as a downloadable response
    return FileResponse(open(file_path, 'rb'), as_attachment=True, filename='example.csv')
def upload_csv(request):
    print("KKKKKKKKKKKkk")
    if request.method == 'POST' and request.FILES['csvFile']:
        csv_file = request.FILES['csvFile']

        import csv
        import io

        # Read and process the CSV
        file_data = csv_file.read().decode("utf-8")  # Read the file contents as string
        csv_reader = csv.reader(io.StringIO(file_data))
        rows = []
        for row in csv_reader:
            # Process each row, for example, save it to the database
            if row[0]!='' and row[1].isnumeric():
                rows.append(row[:2])
                print(row[:2])  # For now, just printing the row to console

        return JsonResponse({'message': 'CSV file uploaded and processed successfully', 'rows': rows})
    return JsonResponse({'error': 'No file uploaded'}, status=400)


# Create your views here.
def my_expenses(request):
    return render(request,'my_expenses/expense_list.html')


