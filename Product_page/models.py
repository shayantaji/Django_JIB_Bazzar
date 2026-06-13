from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse
from  slugify import slugify


class ProductCategory(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان',db_index=True)
    url_title = models.CharField(max_length=300, db_index=True, verbose_name='عنوان در url')
    is_active = models.BooleanField(verbose_name='فعال / غیرفعال')
    is_delete = models.BooleanField(verbose_name='حذف شده / نشده')

    def __str__(self):
        return self.title

    class Meta:

        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'


class Product(models.Model):
    category = models.ForeignKey(ProductCategory,on_delete=models.CASCADE,related_name='products_category',verbose_name='دسته بندی')

    title = models.CharField(max_length=300,verbose_name='نام محصول')

    slug = models.SlugField(unique=True,verbose_name='نام در url',blank=True,null=True)

    image = models.ImageField(upload_to='images/products/',verbose_name='تصویر محصول')

    short_description = models.CharField(max_length=500,verbose_name='توضیح کوتاه')

    description = models.TextField(verbose_name='توضیحات',blank=True,null=True)

    price = models.PositiveIntegerField(verbose_name='قیمت')

    inventory = models.PositiveIntegerField(default=1,verbose_name='تعداد موجودی')

    sold_count = models.PositiveIntegerField(default=0,verbose_name='تعداد فروش')

    is_featured = models.BooleanField(default=False,verbose_name='محصول ویژه/محصول غیر ویژه')

    is_active = models.BooleanField(default=True,verbose_name='فعال/غیرفعال')

    created_date = models.DateTimeField(auto_now_add=True,verbose_name='تاریخ ایجاد محصول')

    RATING_CHOICES = [
        (0, '0'),
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]

    rating = models.PositiveSmallIntegerField(
        choices=RATING_CHOICES,
        default=0,
        verbose_name='امتیاز محصول',
        null=True,
        blank=True
    )

    @property
    def star_range(self):
        return range(self.rating)

    def get_absolute_url(self):
        return reverse('product-detail', args=[self.slug])

    def __str__(self):
        return f"{self.title}  {self.price}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

class ProductGallery(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='gallery'
    )
    image = models.ImageField(upload_to='images/products/product_gallery/')

    def __str__(self):
        return f" گالری {self.product.title}"

    class Meta:
        verbose_name = 'گالری'
        verbose_name_plural = 'گالری محصولات'