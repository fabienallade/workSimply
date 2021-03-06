# Generated by Django 3.0.3 on 2020-07-12 11:23

from django.db import migrations, models
import django.db.models.deletion
import products.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.FileField(upload_to='')),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
                ('images', models.ImageField(upload_to=products.models.upload_post_image, verbose_name='Image')),
                ('category', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='categories.Category')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
    ]
