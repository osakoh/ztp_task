from django.db import models
from django.urls import reverse
from .utils import rate_details, process


class Customer(models.Model):
    """creates a row containing an id, customer name, address, and meter number in the db"""
    name = models.CharField(verbose_name="Customer Name", max_length=255, blank=False)
    address = models.CharField(verbose_name="Customer Address", max_length=255, blank=False)
    number = models.CharField(verbose_name="Meter Number", max_length=255, blank=False)

    class Meta:
        """order by latest"""
        ordering = ["-id"]

    def get_details(self):
        """ canonical url to view the rating details of a customer a specific heading """
        return reverse('energy:rating_details', args=[self.pk])

    def __str__(self):
        """
        string representation of 'Customer' model
        """
        return f"Customer Name: {self.name}"


class Consumption(models.Model):

    def energy_consumption(self):
        """calculates the energy consumption i.e second - first """
        return self.second - self.first

    def cal_cost(self):
        """ calculates the cost """
        return self.energy_consumption() * rate_details(str(process(self.rate)))

    """creates a row containing an id, rate name, first, and second reading in the db"""
    customer = models.ForeignKey(Customer, related_name='consumptions', on_delete=models.CASCADE)
    rate = models.CharField(verbose_name="Rate Name", max_length=255, null=True, blank=False)
    first = models.FloatField(verbose_name="1st Reading (kWh)", null=True, blank=False)
    second = models.FloatField(verbose_name="2nd Reading (kWh)", null=True, blank=False)
    consumption = models.FloatField(verbose_name="Energy Consumption", null=True, blank=True)
    cost = models.FloatField(verbose_name="Rate Cost", null=True, blank=True)

    def __str__(self):
        """
        string representation of 'Consumption' model
        """
        return f"Customer: {str(self.customer.name)} | Rate: {self.rate} | 1st: {self.first} | 2nd: {self.second}"
