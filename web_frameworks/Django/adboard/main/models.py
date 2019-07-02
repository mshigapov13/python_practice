from django.db import models

class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, unique=True, verbose_name='Name')
    order = models.SmallIntegerField(default=0, db_index=True, verbose_name='Order')
    super_rubric = models.ForeignKey('SuperRubric', on_delete=models.PROTECT, null=True, blank=True, verbose_name='SuperRubric')

class SuperRubricManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(super_rubric_isnull=True)

class SuperRubric(Rubric):
    objects = SuperRubricManager()

    def __str__(self):
        return self.name
    
    class Meta:
        proxy = True
        ordering = ('order', 'name')
        verbose_name = 'SuperRubric'
        verbose_name_plural = 'SuperRubrics'

class SubRubricManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(super_rubric_isnull=False)

class SubRubric(Rubric):
    objects = SubRubricManager()

    def __str__(self):
        return '%s - %s' % (self.super_rubric.name, self.name)
    
    class Meta:
        proxy = True
        ordering = ('super_rubric__order', 'super_rubric__name', 'order', 'name')
        verbose_name = 'SubRubric'
        verbose_name_plural = 'SubRubrics'


from .utilities import get_timestamp_path

class Bb(models.Model):
    rubric = models.ForeignKey(SubRubric, on_delete=models.PROTECT, verbose_name='Rubric')
    title = models.CharField(max_length=40, verbose_name='Product')
    content = models.TextField(verbose_name='Description')
    price = models.FloatField(default=0, verbose_name='Price')
    contacts = models.TextField(verbose_name='Contacts')
    image = models.ImageField(blank=True, upload_to=get_timestamp_path, verbose_name='Image')
    is_active = models.BooleanField(default=True, db_index=True, verbose_name='Need to output?')
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Published')
    
    class Meta:
        verbose_name_plural = 'Ads'
        verbose_name = 'Ad'
        ordering = ['-created_at']
