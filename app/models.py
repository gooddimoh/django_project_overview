from django.db import models


class ProductType(models.Model):
    name = models.CharField(max_length=300, default='default name')

    def __str__(self):
        return self.name


class ProductCategory(models.Model):
    name = models.CharField(max_length=300, default='default name')

    def __str__(self):
        return self.name


class StandardRequirement(models.Model):
    name = models.CharField(max_length=300, default='default name')
    requirementList = models.TextField(default='name')

    def __str__(self):
        return self.name


class StandardCategory(models.Model):
    name = models.CharField(max_length=300, default='default name')

    def __str__(self):
        return self.name


class KeyWords(models.Model):
    name = models.TextField(max_length=300)

    def __str__(self):
        return self.name


class Standard(models.Model):
    name = models.CharField(max_length=300, default='default name')
    level = models.IntegerField(default=0)
    description = models.TextField()
    link = models.TextField()
    keyword = models.ForeignKey(KeyWords, related_name='stkeyword', on_delete=models.CASCADE)
    category = models.ForeignKey(ProductCategory, related_name='stcategory', on_delete=models.CASCADE)
    requirement = models.ForeignKey(StandardRequirement, related_name='sttype', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=300, default='default name')
    description = models.TextField(max_length=800, blank=True, null=True)
    link = models.TextField(default='0')
    type = models.ForeignKey(ProductType, related_name='prtype', on_delete=models.CASCADE)
    category = models.ForeignKey(ProductCategory, related_name='prcategory', on_delete=models.CASCADE)
    keyword = models.ForeignKey(KeyWords, related_name='prkeyword', on_delete=models.CASCADE)


    def __str__(self):
        return self.name
