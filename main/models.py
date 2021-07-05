from django.db import models
import re

from django.db.models.base import Model

# VALIDATIONS

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.+_-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def registration_validator(self, postData):
        # ALL THE VALIDATION FOR THE FORM
        errors = {}
        if len(postData['name']) < 2 and len(postData['name']) > 50:
            errors['name'] = "Invalid name. Name must be at least 3 characters"
        if len(postData['alias']) < 2:
            errors['alias'] = "Invalid alias. Alias must be at least 3 characters"
        if not EMAIL_REGEX.match(postData['email']):   
            errors['email'] = "Invalid email address!"
        users_with_email = User.objects.filter(email = postData['email'])
        if len(users_with_email) >= 1:
            errors['duplicate'] = "Email already exists."
        if len(postData['password']) < 5:
            errors['password'] = "Password must be at least 5 characters"
        if postData['password'] != postData['confirm_password']:
            errors['pw_match'] = "Password must match!"
        return errors       

class BookManager(models.Manager):
    def book_validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors['title'] = "Invalid title. Title must be at least 3 characters"
        return errors 

class AuthorManager(models.Manager):
    def author_validator(self, postData):
        errors = {}
        if len(postData['author_name']) < 2 or len(postData['author_name']) > 50:
            errors['author_name'] = "Invalid name. Name must be at least 3 characters"
        author_in_db = Author.objects.filter(name=postData['author_name'])
        if len(author_in_db) >= 1:
            errors['duplicate'] = 'Author already exists in our DB.'
        return errors  

class ReviewManager(models.Manager):
    def review_validator(self, postData):
        errors = {}
        if len(postData['content']) < 2:
            errors['content'] = "Invalid content. Content must be at least 3 characters"
        return errors 

# Julio, Pablo, Sergio, Marcelo, Luisa, Luis, Alexis

# MODELS CREATION
class User(models.Model):
    name = models.CharField(max_length=50)
    alias = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Book(models.Model):
    title = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()

class Author(models.Model):
    name = models.CharField(max_length=75)
    books = models.ManyToManyField(Book, related_name="authors")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = AuthorManager()

class Review(models.Model):
    content = models.TextField()
    rating = models.IntegerField()
    user_review = models.ForeignKey(User, related_name="user_reviews", on_delete=models.CASCADE)
    book_reviewed = models.ForeignKey(Book, related_name="book_reviews", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ReviewManager()