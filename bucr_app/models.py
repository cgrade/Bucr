#!/usr/bin/ python3
""" Module that contains all the Database Models  used in Bucr
These Models represents all the Database Tables/Entities and the Model attributes
represents the Entity Fields."""


# import necessary dependencies
from django.db import models
from django.contrib.auth.models import User
import bucr_app


class UserProfile(models.Model):
    """A Class that represents the UserProfile Database Model"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=15, null=True)
    last_name = models.CharField(max_length=15, null=True)
    phone_number = models.CharField(max_length=15)
    image = models.ImageField(upload_to='profile_pictures')
    bio = models.TextField()

    def __str__(self):
        """String Representation of the UserProfile Model"""
        return (self.user.username)



# Defining the Restaurant Model Class
class Restaurant(models.Model):
    """A Class that represents the Restaurant Database Model"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    cuisine_type = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=15)
    opening_hours = models.CharField(max_length=100)
    image = models.ImageField(upload_to='restaurant_images')
  

    def __str__(self):
        """String Representation of the Restaurant Model"""
        return (self.name)


class Image(models.Model):
    file = models.ImageField(upload_to='restaurant_photos')

class Photo(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    images = models.ManyToManyField(Image, related_name='photos')
    caption = models.CharField(max_length=100)
    # Add any additional fields you need, such as a caption or description

# Defining the Table Model Class
class Table(models.Model):
    """A Class that represents the Table Database Model"""
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    table_number = models.CharField(max_length=10)
    capacity = models.PositiveIntegerField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        """String Representation of the Table Model"""
        return 'Table {}'.format(self.table_number)


# Defining the Reservation Model Class
class Reservation(models.Model):
    """A Class that represents the Reservation Database Model"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    num_guests = models.PositiveIntegerField()
    is_confirmed = models.BooleanField(default=False)

    def __str__(self):
        """String Representation of the Reservation Model"""
        return 'reservation at {} by {} for {}'.format(self.restaurant, self.user, self.num_guests)


# Defining the Review Model Class
class Review(models.Model):
    """A Class that represents the Review Database Model"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    comment = models.TextField()

    def __str__(self):
        """String Representation of the Review Model"""
        return (self.comment)


# Defining the Waitlist Model Class
class Waitlist(models.Model):
    """A Class that represents the Waitlist Database Model"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    num_guests = models.PositiveIntegerField()

    def __str__(self):
        """String Representation of the Waitlist Model"""
        return (self.name)
