from datetime import datetime

from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Permission
from django.contrib.auth.decorators import login_required, permission_required

from course.models import Course, Deadline, Group, Update, GroupMember, CourseMember

def index(request):
	context = {'User' : request.user}

	user_courses = [course.course for course in CourseMember.objects.filter(user=request.user.id)]
	new_updates = []
	for course in user_courses:
		new_updates.append(len(Update.objects.filter(course=course).filter(created__gte=request.user.last_login)))

	deadlines = []
	for course in user_courses:
		for deadline in Deadline.objects.filter(course=course):
			deadlines.append(deadline)

	deadlines = sorted(deadlines)
	grouped_deadlines = dict()
	for deadline in deadlines:
		if deadline.date_due in grouped_deadlines:
			grouped_deadlines[deadline.date_due].append(deadline)
		else:
			grouped_deadlines[deadline.date_due] = [deadline]
	print grouped_deadlines
	context['deadlines'] = grouped_deadlines

	user_updates = []

	for course in user_courses:
		for update in Update.objects.filter(course=course):
			user_updates.append(update)

	for group in GroupMember.objects.filter(user=request.user):
		for update in Update.objects.filter(group=group):
			user_updates.append(update)

	context['user_updates'] = user_updates

	context['user_courses'] = zip(user_courses, new_updates)
	return render(request, 'core/index.html', context)

def user_course_list(request):
	context = {'User' : request.user}

	user_courses = [course.course for course in CourseMember.objects.filter(user=user)]
	new_updates = []
	for course in user_courses:
		new_updates.append(len(Update.objects.filter(course=course).filter(created__gte=request.user.last_visit)))

	context['user_courses', zip(user_courses, new_updates)]
	return render(request, 'core/index.html', context)

def course_page(request, course_id):
	context = {'User' : request.user}

	course = Course.objects.get(pk=course_id)
	deadlines = Deadline.objects.filter(course=course_id).filter(date_due__gte=datetime.today())

	return render(request, 'core/index.html', context)

def test(request):
	context = {'User' : request.user}

	user_courses = [course.course for course in CourseMember.objects.filter(pk=request.user.id)]
	new_updates = []
	for course in user_courses:
		new_updates.append(len(Update.objects.filter(course=course).filter(created__gte=request.user.last_login)))

	deadlines = []
	for course in user_courses:
		for deadline in Deadline.objects.filter(course=course):
			deadlines.append(deadline)

	deadlines = sorted(deadlines)
	grouped_deadlines = dict()
	for deadline in deadlines:
		if deadline.date_due in grouped_deadlines:
			grouped_deadlines[deadline.date_due].append(deadline)
		else:
			grouped_deadlines[deadline.date_due] = [deadline]
	print grouped_deadlines
	context['deadlines'] = grouped_deadlines

	context['user_courses'] = zip(user_courses, new_updates)
	return render(request, 'core/index.html', context)