from django.db import models


class Book(models.Model):
    book_author = models.CharField('Автор книги', max_length=50)
    book_title = models.CharField('Название книги', max_length=50)
    book_content = models.TextField('Содержание')
    pub_date = models.CharField('Год издания', max_length=15)

    # def __str__(self):
    #     return self.book_author, self.book_title

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

class Comment(models.Model):
    # привязка комментарий к книге и удаления всех комментарий, если книгу удалить
    comment = models.ForeignKey(Book, on_delete=models.CASCADE)
    author_name = models.CharField('Имя автора', max_length=50)
    comment_text = models.CharField('Текст комментария', max_length=200)

    # def __str__(self):
    #     return self.author_name

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
