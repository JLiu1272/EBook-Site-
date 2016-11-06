from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from .constants import genres

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    year_published = models.IntegerField()
    description = models.CharField(max_length=500)
    rating = models.IntegerField()
    genreChoices = []
    for index, genre in enumerate(genres):
        genreChoices.append((index, genre))
    genre = models.IntegerField(
        max_length=1,
        choices=tuple(genreChoices)
    )

    def __str__(self):
        return self.title

    def _get_books_for_sale_count(self):
        return len(BookForSale.objects.filter(book=self.id))
    books_for_sale_count = property(_get_books_for_sale_count)



class BookForSale(models.Model):
    cost = models.IntegerField()
    sold = models.BooleanField(default=False)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    userSelling = models.ForeignKey(User, related_name="users_selling")
    userBought = models.ForeignKey(User, related_name="user_bought", blank=True, null=True)
    conditionChoices = (
        (0, 'Poor'),
        (1, 'Fair'),
        (2, 'Good'),
        (3, 'New'),
    )
    condition = models.IntegerField(
        max_length=1,
        choices=conditionChoices,
    )

    def __str__(self):
        return self.book.title + " sold by " + self.userSelling.username


class sellBookForm(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    year_published = models.IntegerField()
    rating = models.IntegerField()
    genreChoices = []
    for index, genre in enumerate(genres):
        genreChoices.append((index, genre))
    genre = models.IntegerField(
        choices=tuple(genreChoices)
    )
    cost = models.IntegerField()
    conditionChoices = (
        (0, 'Poor'),
        (1, 'Fair'),
        (2, 'Good'),
        (3, 'New'),
    )
    condition = models.IntegerField(
        max_length=1,
        default=3,
        choices=conditionChoices,
    )


class UserProfile(models.Model):
	# This line is required. Links UserProfile to a User model instance.
	user = models.OneToOneField(User)

    # The additional attributes we wish to include.
	rating = models.CharField(max_length=30)
	phone = models.CharField(max_length=30)
	
	# Override the __unicode__() method to return out something meaningful!
	def __unicode__(self):
		return self.user.username