from django.shortcuts import render

from .models import Patient


def patient_list(request):
	patients = Patient.objects.select_related("owner", "universe").order_by("name")
	return render(request, "mythical_app/patient_list.html", {"patients": patients})
