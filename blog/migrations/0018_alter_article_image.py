# Generated by Django 4.1 on 2022-10-30 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_alter_article_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(default='images/noprofile.jpg', upload_to='images/articles'),
        ),
    ]
