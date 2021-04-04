from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from decouple import config

from megha import settings
from  .models import *
from django.core.mail import send_mail

# Create your views here.

def index(request):
    sec1 = IndexSectionOne.objects.filter().first()
    sec2 = IndexSectionTwo.objects.filter().first()
    m_images = MediumImage.objects.all()
    sec3 = IndexSectionThree.objects.filter().first()
    sec4 = IndexSectionFour.objects.filter().first()
    questions = Questions.objects.all()
    sec5 = OrderSection.objects.filter().first()
    steps = OrderStep.objects.all()
    data = {
        'sec_1' : sec1,
        'sec_2' : sec2,
        'sec_3' : sec3,
        'sec_4' : sec4,
        'sec_5' : sec5,
        'm_images' : m_images,
        'questions' : questions,
        'steps' : steps
    }
    # send_mail(
    #     'Subject here',
    #     'Here is the message.',
    #     'from@example.com',
    #     ['to@example.com'],
    #     fail_silently=False,
    # )
    return render(request, 'index.html', data)

def contactus(request):
    # send_mail(
    #     'Subject here',
    #     'Here is the message.',
    #     'from@example.com',
    #     ['sandeepkushaj3@gmail.com'],
    #     fail_silently=False,
    # )
    return render(request, 'contact-us.html')

def testimonials(request):
    sec1 = TestimonialsSectionOne.objects.filter().first()
    sec2 = TestimonialsSectionTwo.objects.filter().first()
    videos = Video.objects.all()
    testimonials = Testimonial.objects.all()
    data = {
        'sec_1' : sec1,
        'sec_2' : sec2,
        'videos' : videos
    }
    if testimonials[0]:
        data['test0'] = testimonials[0]

    if testimonials[1]:
        data['test1'] = testimonials[1]

    if testimonials[2]:
        data['test2'] = testimonials[2]

    if testimonials[3]:
        data['test3'] = testimonials[3]

    if testimonials[4]:
        data['test4'] = testimonials[4]

    if testimonials[5]:
        data['test5'] = testimonials[5]

    return render(request, 'Testimonials.html', data)

def make_order(request):
    if request.method == 'POST':
        full_name = request.POST['name']
        contact_no = request.POST['contact']
        address = request.POST['message']
        quantity = request.POST['qty']
        district = request.POST['district']
        remarks = request.POST['remarks']

        from_email = full_name
        email_to = [config('TO_EMAIL', cast=str)]
        subject = 'ORDER'
        message = 'Full Name : ' + full_name + '\nContact Number : ' + contact_no + '\nAddress : ' + address + '\nQuantity : ' + quantity + '\nDistrict : ' + district + '\nRemarks : ' + remarks + '\n'
        try:
            send_mail(subject, message, from_email, email_to, fail_silently=False)
            response = {
                'message' : 'Order was sent successfully...'
            }
            return JsonResponse(response, status=200)
        except Exception as e:
            print(e)
            response = {
                'message': 'Order was not sent...'
            }
            return JsonResponse(response, status=400)

def make_question(request):
    if request.method == 'POST':
        full_name = request.POST['name']
        contact_no = request.POST['contact']
        email = request.POST['e_mail']
        subject = 'QUESTION'
        message = request.POST['message']
        msg = 'Full Name : '+ full_name + '\nContact Number : ' + contact_no + '\nMessage : ' + message + '\n'
        to_email = [config('TO_EMAIL', cast=str)]

        try:
            send_mail(subject,msg,email, to_email, fail_silently=False)
            response = {
                'message': 'Question was sent successfully...'
            }
            return JsonResponse(response, status=200)
        except Exception as e:
            print(e)
            response = {
                'message': 'Question was not sent...'
            }
            return JsonResponse(response, status=400)