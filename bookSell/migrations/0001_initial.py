# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-18 15:45
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('year_published', models.IntegerField()),
                ('description', models.CharField(max_length=500)),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='cover_photos')),
                ('genre', models.IntegerField(choices=[(0, b'Science fiction'), (1, b'Drama'), (2, b'Action and Adventure'), (3, b'Romance'), (4, b'Mystery'), (5, b'Health'), (6, b"Children's"), (7, b'Science'), (8, b'History'), (9, b'Biographies')])),
            ],
        ),
        migrations.CreateModel(
            name='BookForSale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.IntegerField()),
                ('sold', models.BooleanField(default=False)),
                ('condition', models.IntegerField(choices=[(0, 'Poor'), (1, 'Fair'), (2, 'Good'), (3, 'New')])),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookSell.Book')),
                ('userBought', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_bought', to=settings.AUTH_USER_MODEL)),
                ('userSelling', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users_selling', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BookRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('comment', models.CharField(max_length=500)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookSell.Book')),
            ],
        ),
        migrations.CreateModel(
            name='sellBookForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500)),
                ('year_published', models.IntegerField()),
                ('genre', models.IntegerField(choices=[(0, b'Science fiction'), (1, b'Drama'), (2, b'Action and Adventure'), (3, b'Romance'), (4, b'Mystery'), (5, b'Health'), (6, b"Children's"), (7, b'Science'), (8, b'History'), (9, b'Biographies')])),
                ('cost', models.IntegerField()),
                ('condition', models.IntegerField(choices=[(0, 'Poor'), (1, 'Fair'), (2, 'Good'), (3, 'New')], default=3)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=30)),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('comment', models.CharField(max_length=500)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookSell.BookForSale')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookSell.UserProfile')),
            ],
        ),
        migrations.AddField(
            model_name='bookrating',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookSell.UserProfile'),
        ),
    ]
