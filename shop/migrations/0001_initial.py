# Generated by Django 3.1.1 on 2020-09-17 20:25

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields
import wagtail.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('description', wagtail.core.fields.RichTextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='shop_images')),
                ('allergens', multiselectfield.db.fields.MultiSelectField(choices=[('d', 'dairy'), ('e', 'eggs'), ('m', 'meat'), ('n', 'nuts')], max_length=7)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Toastie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('description', wagtail.core.fields.RichTextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='shop_images')),
                ('ingredients', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.ingredient')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
