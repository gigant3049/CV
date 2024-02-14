from django.db import models
from django.utils import timezone
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.dispatch import receiver


class Author(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='media/articles/', null=True, blank=True)


class Category(models.Model):
    title = models.CharField(max_length=255)


class Tag(models.Model):
    title = models.CharField(max_length=255)


class Article(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media/articles/', blank=True, null=True)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)
    tags = models.ManyToManyField(Tag)
    categories = models.ManyToManyField(Category)

    class Meta:
        verbose_name = "Articles"


class SubArticle(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=True, blank=True)
    content = models.TextField(null=True, blank=True)


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', models.SET_NULL, null=True)
    top_level_comment_id = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    image = models.ImageField(upload_to='media/articles', null=True, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    @property
    def children(self):
        if not self.parent:
            return Comment.objects.filter(top_level_comment_id=self.id)
        return None


@receiver(pre_save, sender=Comment)
def pre_save_comments(sender, instance, *args, **kwargs):
    if instance.parent:
        if instance.parent.top_level_comment_id:
            instance.top_level_comment_id = instance.parent.top_level_comment_id
        else:
            instance.top_level_comment_id = instance.parent.id


@receiver(pre_save, sender=Article)
def pre_save_article(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.title + '-' + str(timezone.now()))