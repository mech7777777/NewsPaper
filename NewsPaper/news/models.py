from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum

# Create your models here.
class Author(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    user_rating = models.SmallIntegerField(default=0)
    def update_rating(self):
        sum_rating_post = self.post_set.all().aggregate(postrating = Sum('rating'))
        pRat = 0
        pRat += sum_rating_post.get('postrating')

        sum_rating_com_author = self.post_set.all().aggregate(commentRating = Sum('rating'))
        cRat = 0
        cRat += sum_rating_com_author.get('commentRating')

        self.user_rating = pRat*3 + cRat
        self.save()
        


class Category(models.Model):
    name_category = models.CharField(max_length = 120,unique=True)

class Post(models.Model):
    author = models.ForeignKey(Author, on_delete= models.CASCADE)
    NEWS = 'NW'
    ARTICLE = 'AR'
    CATEGORY_CHOICES = (
        (NEWS,'Новость'),
        (ARTICLE, 'Статья'),
    )
    categoryType = models.CharField( max_length=2, choices=CATEGORY_CHOICES, default=ARTICLE)
    timeCreate = models.DateTimeField(auto_now_add=True)
    postCategory = models.ManyToManyField(Category, through='PostCategory')
    heading = models.CharField(max_length=255)
    textArticle = models.TextField()
    rating = models.SmallIntegerField(default=0)
    def like (self):
        self.rating += 1 
        self.save()
    def dislike(self):
        self.rating -= 1
        self.save() 
    def preview(self):
        return self.textArticle[0:123] + '...'
    def __str__(self):
        return f'{self.heading.title()}: {self.textArticle[:20]}'

class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category  = models.ForeignKey(Category,on_delete=models.CASCADE)

class Comment(models.Model):
    comPost = models.ForeignKey(Post,on_delete=models.CASCADE)
    comUser = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(default="Ничего")
    time_create = models.DateTimeField(auto_now_add=True)
    rating = models.SmallIntegerField(default=0)
    def like (self):
        self.rating =+ 1
        self.save() 
    def dislike(self):
        self.rating =- 1 
        self.save()
    def __str__(self):
        return f'{self.comment}'