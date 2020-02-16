# Generated by Django 3.0.1 on 2020-01-23 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lances', '0002_auto_20191228_1007'),
    ]

    operations = [
        migrations.AddField(
            model_name='lances',
            name='categorias_1',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='lances',
            name='categorias_2',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='lances',
            name='descricao_1',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='lances',
            name='descricao_2',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='lances',
            name='imagem1_1',
            field=models.ImageField(max_length=30, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='lances',
            name='imagem1_2',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='lances',
            name='imagem2_1',
            field=models.ImageField(max_length=30, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='lances',
            name='imagem2_2',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='lances',
            name='imagem3_1',
            field=models.ImageField(max_length=30, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='lances',
            name='imagem3_2',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='lances',
            name='imagem4_1',
            field=models.ImageField(max_length=30, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='lances',
            name='imagem4_2',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='lances',
            name='imagem5_1',
            field=models.ImageField(max_length=30, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='lances',
            name='imagem5_2',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='lances',
            name='latitude_1',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='lances',
            name='latitude_2',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='lances',
            name='longitude_1',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='lances',
            name='longitude_2',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='lances',
            name='titulo_1',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='lances',
            name='titulo_2',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='lances',
            name='visualizado_1',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='lances',
            name='visualizado_2',
            field=models.IntegerField(default=0, null=True),
        ),
    ]