from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, FileResponse
import os
from django.conf import settings
def profile(request):
    return render(request,'profile/profile.html')


def download_resume(request):
    file_path = os.path.join(settings.BASE_DIR, 'expenses', 'static', 'Paridhi-Jain-2.10yoe.pdf')
    return FileResponse(open(file_path, 'rb'), as_attachment=True, filename='Paridhi-Jain-2.10yoe.pdf')
