# Generated by Django 3.0.1 on 2019-12-20 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itens', '0013_auto_20191220_0950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incluir_item',
            name='imagem1',
            field=models.ImageField(blank=True, null=True, upload_to='static/img/produtos/'),
        ),
        migrations.AlterField(
            model_name='incluir_item',
            name='imagem2',
            field=models.ImageField(blank=True, null=True, upload_to='static/img/produtos/'),
        ),
        migrations.AlterField(
            model_name='incluir_item',
            name='imagem3',
            field=models.ImageField(blank=True, null=True, upload_to='static/img/produtos/'),
        ),
        migrations.AlterField(
            model_name='incluir_item',
            name='imagem4',
            field=models.ImageField(blank=True, null=True, upload_to='static/img/produtos/'),
        ),
        migrations.AlterField(
            model_name='incluir_item',
            name='imagem5',
            field=models.ImageField(blank=True, null=True, upload_to='static/img/produtos/'),
        ),
    ]
