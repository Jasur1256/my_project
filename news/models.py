# from django.db import models


# class NewsModel(models.Model):

    # title = models.CharField(max_length=250, verbose_name='Sarlavha')
    # image = models.ImageField(upload_to='media/news/', verbose_name='Post rasmi')
    # body = models.TextField(verbose_name='Post matni')
    # create_date = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
        # return self.title


    # class Meta:
        # db_table = 'News'
        # managed = True
        # verbose_name = 'News'
        # verbose_name_plural = 'News'

from django.utils import timezone
from django.db import models


class CategoryModel(models.Model):
    name = models.CharField(max_length=50, verbose_name='Kategoriya nomi')

    def __str__(self):
        return self.name


    class Meta:
        db_table = 'Categorys'
        managed = True
        verbose_name = 'Kategoriya'
        verbose_name_plural = 'Kategoriyalar'


class ActivedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='Faol')


class NewsModel(models.Model):

    class Status(models.TextChoices):
        Deactive = 'Faol emas', 'Faol emas'
        Active = 'Faol', 'Faol'

    title = models.CharField(max_length=250, verbose_name='Yangilik nomi')
    body = models.TextField(verbose_name="Yangilik haqida ma'lumotlar")
    image = models.ImageField(upload_to='news/images', verbose_name='Rasmi')
    category = models.ForeignKey(CategoryModel,
                                 on_delete=models.CASCADE,
                                 verbose_name='Kategoriyasi'
                                 )


    publish_time = models.DateTimeField(default=timezone.now, verbose_name='Yangilik yaratilgan vaqt')
    create_time = models.DateTimeField(auto_now_add=True)
    updeted_time = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50,
                          choices=Status.choices,
                          default=Status.Deactive,
                          verbose_name='Holati'
                          )

    objects = models.Manager()
    manager = ActivedManager()

    class Meta:
        ordering =['-publish_time']
        db_table = 'News'
        managed = True
        verbose_name = 'Yangilik'
        verbose_name_plural = 'Yangiliklar'


    def __str__(self):
        return self.title


class ContactModel(models.Model):

    name = models.CharField(max_length=50, verbose_name='Ism')
    email = models.EmailField(max_length=254, verbose_name='Email')
    message = models.TextField(verbose_name='Xabar')

    def __str__(self) -> str:
        return self.email


    class Meta:
        db_table = 'Contact'
        managed = True
        verbose_name = 'Aloqa'
        verbose_name_plural = 'Aloqa'


    


    
    
    
    
    