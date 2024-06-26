from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import IntegrityError, OperationalError
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail, BadHeaderError
from .models import Customer
from django.contrib.auth.models import User
import random
from django.contrib.auth.decorators import login_required
import smtplib
import socket


# Helper function to check internet connection
def check_internet_connection():
    try:
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        return False

def Logout(request):
    logout(request)
    return redirect('account')

def Welcome(request):
    return render(request, "welcome.html")

def Account(request):
    context = {}
    if request.POST and 'register' in request.POST:
        context['register'] = True
        try:
            name = request.POST.get('name')
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')

            # OTP generation
            num_digit = 6
            lower_bound = 10**(num_digit - 1)
            upper_bound = 10**num_digit - 1
            rnd = random.randint(lower_bound, upper_bound)

            # Send email with account details and OTP
            if check_internet_connection():
                sendEmail(name, username, email, rnd)
            else:
                messages.error(request, "No internet connection. Please try again later.")
                return render(request, 'account.html', context)

            request.session['registration_data'] = {
                'name': name,
                'username': username,
                'email': email,
                'password': password,
                'rnd': rnd,
            }

            # Redirect to OTP verification page
            if check_internet_connection():
                return redirect('otp_verification')

        except IntegrityError as e:
            print(f"IntegrityError: {e}")
            error_message = "Duplicate username or invalid input data"
            messages.error(request, error_message)
        except ValidationError as e:
            print(f"ValidationError: {e}")
            error_message = "Invalid data provided"
            messages.error(request, error_message)
        except Exception as e:
            print(f"Unexpected error: {e}")
            messages.error(request, "An unexpected error occurred. Please try again.")

    elif 'login' in request.POST:
        context['register'] = False
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials.')

    return render(request, 'account.html', context)

def sendEmail(name, username, email, rnd):
    try:
        send_mail(
            "This is a confirmation message from Ach'z SaGaCiTy.",  # Subject of the email
            'Hello {},\n\nYour account details:\nUsername: {}\nOTP: {}'.format(name, username, rnd),
            'your_sender_email@example.com',  # Sender's email address
            [email],  # List of recipient email addresses
            fail_silently=False,  # Set to True to suppress errors
        )
    except (BadHeaderError, smtplib.SMTPException) as e:
        print(f"Failed to send email: {e}")
        raise e
    except Exception as e:
        print(f"Unexpected error in sendEmail: {e}")
        raise e

def otp_verification(request):
    if request.method == 'POST':
        registration_data = request.session.get('registration_data')
        if registration_data:
            rnd = registration_data.get('rnd')

            # Retrieve entered OTP from form
            otp1 = request.POST.get('otp1')
            otp2 = request.POST.get('otp2')
            otp3 = request.POST.get('otp3')
            otp4 = request.POST.get('otp4')
            otp5 = request.POST.get('otp5')
            otp6 = request.POST.get('otp6')

            entered_otp = otp1 + otp2 + otp3 + otp4 + otp5 + otp6

            if entered_otp.isdigit() and int(entered_otp) == rnd:
                try:
                    # Check for internet connection
                    if not check_internet_connection():
                        messages.error(request, "No internet connection. Please try again later.")
                        return render(request, 'otp_verification.html')

                    # Create user and customer accounts
                    user = User.objects.create_user(
                        username=registration_data['username'],
                        password=registration_data['password'],
                        email=registration_data['email'],
                    )
                    customer = Customer.objects.create(
                        user=user,
                        name=registration_data['name']
                    )
                    messages.success(request, 'Account created successfully')

                    # Clear session data
                    del request.session['registration_data']

                    # Redirect to more-details page with user ID

                    
                    return redirect('more_details',user.id)

                except IntegrityError as e:
                    print(f"IntegrityError: {e}")
                    messages.error(request, 'Failed to create account. Please try again.')
                except OperationalError as e:
                    print(f"OperationalError: {e}")
                    messages.error(request, 'Database error occurred. Please try again.')
                except Exception as e:
                    print(f"Unexpected error: {e}")
                    messages.error(request, 'An unexpected error occurred. Please try again.')

            else:
                messages.error(request, 'Invalid OTP. Please try again.')

    return render(request, 'otp_verification.html')


def MoreDetails(request,user_id):
    user = User.objects.get(id=user_id)
    print(user)
    try:
        print(f"Found user: {user}")
        if not check_internet_connection():
            messages.error(request, "No internet connection. Please try again later.")
            return redirect('more_details',user.id)
        
        if request.method == 'POST' and 'save' in request.POST:
            print("Inside POST save block")
            image = request.FILES.get('image')
            address = request.POST.get('address')
            place = request.POST.get('location')
            pin = request.POST.get('pin')
            dob = request.POST.get('dob')

            customer, created = Customer.objects.get_or_create(user=user)

            customer.image = image
            customer.address = address
            customer.place = place
            customer.pin = pin
            customer.dob = dob


            # Save the changes
            customer.save()

            success_message = 'Additional details saved successfully'
            messages.success(request, success_message)
            sendEmailDetails(user)
            return redirect('account')

    except IntegrityError as e:
        print(f"IntegrityError: {e}")
        error_message = "Error saving additional details"
        messages.error(request, error_message)
    # print(user.customer_profile.user_id)

    return render(request,"more_details.html",{'user':user})


def sendEmailDetails(user):
    # Retrieve the customer's details
    try:
        customer = Customer.objects.get(user=user)
        name = customer.name
        address = customer.address
        user_email = user.email
        username = user.username
        dob = customer.dob
        place = customer.place
        pin = customer.pin

        # Send email
        send_mail(
            "Thank you for being a member of Ach'z SaGaCiTy.",  # Subject of the email
            'Hello {},\n\nYour account details:\nUsername: {}\nAddress: {}\nDob: {}\nPlace: {}\nPin: {}'.format(name, username, address,dob,place,pin),
            'your_sender_email@example.com',  # Sender's email address
            [user_email],  # List of recipient email addresses
            fail_silently=False,  # Set to True to suppress errors
        )
    except Customer.DoesNotExist:
        print(f"Customer details not found for user: {user.id}")
    except Exception as e:
        print(f"Failed to send email: {e}")
        raise e
