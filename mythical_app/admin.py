from django.contrib import admin
from .models import (
	Ability,
	Diagnosis,
	Employee,
	Invoice,
	LineItem,
	Observation,
	Owner,
	Patient,
	PatientAbility,
	Payment,
	ProcedureDefinition,
	Universe,
	Visit,
	VisitDiagnosis,
	VisitProcedure,
)

admin.site.register(
	[
		Ability,
		Diagnosis,
		Employee,
		Invoice,
		LineItem,
		Observation,
		Owner,
		Patient,
		PatientAbility,
		Payment,
		ProcedureDefinition,
		Universe,
		Visit,
		VisitDiagnosis,
		VisitProcedure,
	]
)
