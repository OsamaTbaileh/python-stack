from django.db import models
import re

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors["email"] = "Invalid email address"
        if len(postData['first_name']) < 2:
            errors["first_name"] = "User first name must be at least 2 characters"
        if len(postData['last_name']) < 2:
            errors["last_name"] = "User last name must be at least 2 characters"
        if len(postData['password']) < 8:
            errors["password"] = "The password name must be at least 8 characters"
        if postData['password'] != postData['confirm_password'] : 
            errors["passowrd_confirmation"] = "Passwords dont match, please check them."

        return errors





class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
