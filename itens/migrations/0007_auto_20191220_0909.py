# Generated by Django 3.0.1 on 2019-12-20 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itens', '0006_auto_20191220_0905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incluir_item',
            name='imagem1',
            field=models.ImageField(blank=True, upload_to='static'),
        ),
        migrations.AlterField(
            model_name='incluir_item',
            name='imagem2',
            field=models.ImageField(blank=True, upload_to='static'),
        ),
        migrations.AlterField(
            model_name='incluir_item',
            name='imagem3',
            field=models.ImageField(blank=True, upload_to='static'),
        ),
        migrations.AlterField(
            model_name='incluir_item',
            name='imagem4',
            field=models.ImageField(blank=True, upload_to='static'),
        ),
        migrations.AlterField(
            model_name='incluir_item',
            name='imagem5',
            field=models.ImageField(blank=True, upload_to='static'),
        ),
    ]
