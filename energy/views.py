import pandas as pd  # for data analysis
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from django.db.models import Sum
from django.db.models import Count, Avg, Q
from django.db.models import OuterRef, Subquery, Count

from django.db.models import Max

from .models import Customer, Consumption
from .utils import excel, rate_details, process


def home_view(request, *args, **kwargs):
    """ extracts data from file and save to DB """
    if request.method == 'POST':
        try:
            # extract file from request
            workbook = request.FILES['workbook']

            # check if file is not a workbook
            # TODO: shoud check for (.xlsx)
            if not workbook.name.endswith('.xlsx'):
                messages.error(request, 'Only workbooks(.xlsx) allowed!')
                # print("I'm here - only CSV files")
                return redirect('energy:home_view')

            # extract customer details and rating
            cus_list, rating_list = excel(workbook, pd)

            # add customer to db
            name, address, number = cus_list
            # customer model reference
            cus_ref = Customer.objects.create(name=name, address=address, number=number)
            # customer id
            cus_id = cus_ref.id

            # add to db using bulk_create()
            for rating in rating_list:
                rate, first, second, = rating
                Consumption.objects.bulk_create([
                    Consumption(customer_id=cus_id, rate=rate, first=first,
                                second=second, consumption=second - first,
                                cost=((second - first) * rate_details(str(process(rate)))))
                ])

            messages.success(request, f"Added Successfully")

        # no file was submitted
        except Exception as e:
            messages.error(request, 'Cannot upload an empty file!')
            # print("I'm here - empty file")
            return redirect('energy:home_view')

    # retrieve all customers from the Customer model
    customers = Customer.objects.all()

    # SUM(public.energy_consumption.cost)
    # customer with the highest ‘Total Energy Cost’.
    high_cost = Customer.objects.annotate(total_cost=Sum('consumptions__cost')).order_by('-total_cost')[:1]

    # SUM(public.energy_consumption.consumption)
    # customer with the highest ‘Day Rate’ consumption
    day_rate = Customer.objects.annotate(total_cost=Sum('consumptions__consumption')).filter(
        consumptions__rate='Day Rate').order_by('-total_cost')[:1]

    # SUM(public.energy_consumption.consumption)
    # customer with the highest ‘Night Rate’ consumption.
    night_rate = Customer.objects.annotate(total_cost=Sum('consumptions__consumption')).filter(
        consumptions__rate='Night Rate').order_by('-total_cost')[:1]

    context = {'customers': customers, 'high_cost': high_cost, 'day_rate': day_rate, 'night_rate': night_rate}
    return render(request, 'energy/home.html', context)


def rating_details(request, cus_id):
    """ shows the rating table for a customer """
    # retrieve single customer
    customer = get_object_or_404(Customer, id=cus_id)
    # retrieves ratings for a single customer
    customer_ratings = customer.consumptions.all()

    context = {'customer': customer, 'customer_ratings': customer_ratings}
    return render(request, 'energy/rating_details.html', context)
