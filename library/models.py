from django.db import models
from datetime import datetime

# Create your models here.
class item(models.Model):
    id = models.IntegerField(blank=False, null=False, primary_key=True)
    title = models.CharField(max_length=50, blank=False, null=False)
    author = models.CharField(max_length=50, blank=False, null=False)
    price = models.FloatField(blank=False, null=False)
    available = models.IntegerField(blank=False, null=False, default=0)
    published_on = models.DateField(blank=True, null=True)
    uploaded_on = models.DateTimeField(default=datetime.now)
    summary = models.TextField(blank=True, null=True)
    category = models.ForeignKey('library.category', blank=False, null=False, on_delete=models.CASCADE)
    sub_category = models.IntegerField(blank=False, null=False, default=0)
    item_type = models.ForeignKey('library.item_type', blank=False, null=False, on_delete=models.CASCADE)
    uploaded_by = models.ForeignKey('client.user', blank=False, null=False, on_delete=models.CASCADE)
    deleted_on = models.DateTimeField(blank=True, null=True)
    quantity = models.IntegerField(blank=False, null=False, default=1)
    rating = models.IntegerField(blank=False, null=False, default=3)

    def __str__(self):
        return self.title


class item_type(models.Model):
    id = models.IntegerField(blank=False, null=False, primary_key=True)
    title = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.title


class category(models.Model):
    id = models.IntegerField(blank=False, null=False, primary_key=True)
    title = models.CharField(max_length=50, blank=False, null=False)
    status = models.IntegerField(blank=False, null=False)
    created_on = models.DateTimeField(default=datetime.now)
    update_on = models.DateTimeField(blank=True, null=True)
    deleted_on = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title


class sub_category(models.Model):
    id = models.IntegerField(blank=False, null=False, primary_key=True)
    category_id = models.ForeignKey(category, blank=False, null=False, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=False, null=False)
    status = models.IntegerField(blank=False, null=False)
    created_on = models.DateTimeField(default=datetime.now)
    update_on = models.DateTimeField(blank=True, null=True)
    deleted_on = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title


class borrowed(models.Model):
    id = models.IntegerField(blank=False, null=False, primary_key=True)
    item = models.ForeignKey(item, blank=False, null=False, on_delete=models.CASCADE)
    user = models.ForeignKey('client.user', blank=False, null=False, on_delete=models.CASCADE)
    borrowed_on = models.DateTimeField(default=datetime.now)
    max_duration = models.IntegerField(blank=False, null=False)
    returned = models.IntegerField(blank=False, null=False, default=-1)

    def __str__(self):
        return str(self.item)
