# Generated by Django 4.1.6 on 2023-02-13 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_author', models.CharField(max_length=50, verbose_name='Автор книги')),
                ('book_title', models.CharField(max_length=50, verbose_name='Название книги')),
                ('book_content', models.TextField(verbose_name='Содержание')),
                ('pub_date', models.DateTimeField(verbose_name='Год издания')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=50, verbose_name='Имя автора')),
                ('comment_text', models.CharField(max_length=200, verbose_name='Текст комментария')),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books_app.book')),
            ],
        ),
    ]