from django.shortcuts import render
from .models import *
from django.core.mail.message import EmailMessage

def index(request):
	return render(request, 'schedules/index.html')

def my_schedule(request):
	context = {
		'monday': AssignedShift.objects.filter(
				employee__user=request.user,
				day='Monday'
			).order_by('start_time'),
		'tuesday': AssignedShift.objects.filter(
				employee__user=request.user,
				day='Tuesday'
			).order_by('start_time'),
		'wednesday': AssignedShift.objects.filter(
				employee__user=request.user,
				day='Wednesday'
			).order_by('start_time'),
		'thursday': AssignedShift.objects.filter(
				employee__user=request.user,
				day='Thursday'
			).order_by('start_time'),
		'friday': AssignedShift.objects.filter(
				employee__user=request.user,
				day='Friday'
			).order_by('start_time'),
		'saturday': AssignedShift.objects.filter(
				employee__user=request.user,
				day='Saturday'
			).order_by('start_time'),
		'sunday': AssignedShift.objects.filter(
				employee__user=request.user,
				day='Sunday'
			).order_by('start_time'),
	}
	return render(request, 'schedules/my_schedule.html', context=context)

def request_cover(request, shift_id):
	shift = AssignedShift.objects.get(id=shift_id)
	shift.cover_requested = True
	shift.save()
	employee_list = []
	for user in User.objects.filter(employee__company=request.user.employee.company):
		if not (AssignedShift.objects.filter(
				start_time__range=(shift.start_time, shift.end_time)
			) | AssignedShift.objects.filter(
				end_time__range=(shift.start_time, shift.end_time)
			)
		).filter(day=shift.day, employee=user.employee):
			employee_list.append(user.email.encode('utf-8'))
	body = 'Shift: {0}, {1}-{2} ({3})\n'.format(
		shift.day, 
		shift.start_time,
		shift.end_time,
		shift.employee.user.email
	)
	body += 'To cover: 192.168.1.135:8080/schedules/cover/{0}/'.format(shift_id)
	EmailMessage(
		to=employee_list,
		cc=[request.user.email],
		from_email='auxo@horae.com',
		subject='AUXO: Your coworker has requested a shift be covered',
		body=body
	).send()
	return render(request, 'schedules/request_cover.html')

def cover_shift(request, shift_id):
	shift = AssignedShift.objects.get(id=shift_id)
	if shift.cover_requested:
		shift.cover_requested = False
		shift.employee = request.user.employee
		shift.save()
		return render(request, 'schedules/cover_shift.html')
	else:
		return render(request, 'schedules/shift_covered.html')
