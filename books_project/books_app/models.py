from django.db import models


class Book(models.Model):
    book_author = models.CharField('Автор книги', max_length=50)
    book_title = models.CharField('Название книги', max_length=50)
    book_content = models.TextField('Содержание')
    pub_date = models.DateTimeField('Год издания')


class Comment(models.Model):
    # привязка комментарий к книге и удаления всех комментарий, если книгу удалить
    comment = models.ForeignKey(Book, on_delete=models.CASCADE)
    author_name = models.CharField('Имя автора', max_length=50)
    comment_text = models.CharField('Текст комментария', max_length=200)
