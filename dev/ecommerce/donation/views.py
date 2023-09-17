from django.shortcuts import render


# Create your views here.
def my_donation(request):
    return render(request, 'donation/my-donation.html')


def payment_success(request):
    return render(request, 'donation/payment-success.html')


def payment_failed(request):
    return render(request, 'donation/payment-failed.html')
