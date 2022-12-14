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


class Message(models.Model):
    message = models.TextField()
    user = models.ForeignKey(User, related_name = "messages", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, related_name = "comments", on_delete = models.CASCADE)
    message = models.ForeignKey(Message, related_name = "comments", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

def create_post(request):
    user = User.objects.get(id = request.session['userid'])
    Message.objects.create(message = request.POST['message'], user = user)