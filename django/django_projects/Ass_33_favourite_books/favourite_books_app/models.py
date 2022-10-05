from django.db import models
import re
import bcrypt

class UserManager(models.Manager):
    def basic_validator_register(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors["email"] = "Invalid email address"
        if len(postData['first_name']) < 2:
            errors["first_name"] = "User first name must be at least 2 characters."
        if len(postData['last_name']) < 2:
            errors["last_name"] = "User last name must be at least 2 characters."
        if len(postData['password']) < 8:
            errors["password"] = "The password name must be at least 8 characters."
        if postData['password'] != postData['confirm_password']: 
            errors["passowrd_confirmation"] = "Passwords dont match, please check them."
        if User.objects.filter(email = postData['email']).exists():
            errors["email"] = "Enterd Email is already exists."
        return errors

    def basic_validator_login(self, postData):
        errors = {}
        user = User.objects.filter(email = postData['email'])                                           #if the entered email is wrong.
        if len(user) < 1:
            errors["email_login"] = "Entered email isnt registered in the data base."
        userr = User.objects.filter(email = postData['email'])                                          #if the entered email is correct but the password is wrong.
        if userr:
            logged_user = userr[0]
            if not bcrypt.checkpw(postData['password'].encode(), logged_user.password.encode()):
                errors["password_login"] = "Entered password does not match the one in the data base."
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #liked_books MTM
    #books_uploaded OTM
    objects = UserManager()



class BookManager(models.Manager):
    def basic_validator_book(self, postData):
        errors = {}
        if len(postData['title']) < 1:
            errors["title"] = "Title is required, please fill it!"
        if len(postData['description']) < 5:
            errors["description"] = "Description must be at least 5 characters."
        return errors

class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    uploaded_by = models.ForeignKey(User, related_name = "books_uploaded" , on_delete = models.CASCADE)  #the one to many 
    users_who_like = models.ManyToManyField(User, related_name = "liked_books")                          #the many to many
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()