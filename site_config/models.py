from django.db import models


class SiteSetting(models.Model):
    site_name = models.CharField(max_length=200, verbose_name='نام سایت')
    site_url = models.URLField(verbose_name='آدرس سایت')
    address = models.CharField(max_length=300, verbose_name='آدرس')
    phone = models.CharField(max_length=200, blank=True, null=True, verbose_name='تلفن')
    fax = models.CharField(max_length=200, blank=True, null=True, verbose_name='فکس')
    email = models.EmailField(blank=True, null=True, verbose_name='ایمیل')
    telegram_url = models.CharField( max_length=200,blank=True, null=True, verbose_name='لینک تلگرام')
    instagram_url = models.CharField( max_length=200,blank=True, null=True, verbose_name='لینک اینستاگرام')
    github_url = models.URLField(blank=True, null=True, verbose_name='لینک گیت هاب')
    linkedin_url = models.CharField( max_length=200,blank=True, null=True, verbose_name='لینک لینکدین')
    site_logo = models.ImageField(upload_to='images/site-setting/', verbose_name='لوگو سایت')
    favicon = models.ImageField(upload_to='images/site-setting/', blank=True, null=True, verbose_name='فاوآیکون سایت')
    copy_right = models.TextField(verbose_name='متن کپی رایت', blank=True, null=True)
    about_us_text = models.TextField(verbose_name='متن تیتر درباره ما', blank=True, null=True)
    about_us_super_text = models.TextField(verbose_name='متن اصلی درباره ما',null=True, blank=True)
    site_slogan = models.CharField(max_length=300, verbose_name='شعار سایت', blank=True, null=True)
    contact_us_text = models.TextField(verbose_name='متن تیتر تماس با ما', blank=True, null=True)
    is_main_setting = models.BooleanField(default=False, verbose_name='تنظیمات اصلی',max_length=250)
    working_hours = models.CharField(max_length=300,verbose_name='ساعت کاری')

    def __str__(self):
        return self.site_name

    class Meta:
        verbose_name = 'تنظیمات سایت'
        verbose_name_plural = 'تنظیمات '


class FooterLinkBox(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')

    class Meta:
        verbose_name = 'دسته بندی لینک های فوتر'
        verbose_name_plural = 'دسته بندی های لینک های فوتر'

    def __str__(self):
        return self.title


class FooterLink(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    url = models.URLField(max_length=500, verbose_name='لینک')
    footer_link_box = models.ForeignKey(to=FooterLinkBox, on_delete=models.CASCADE, verbose_name='دسته بندی')

    class Meta:
        verbose_name = 'لینک فوتر'
        verbose_name_plural = 'لینک های فوتر'

    def __str__(self):
        return self.title

class SiteServices(models.Model):
    site = models.ForeignKey(SiteSetting, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, verbose_name='عنوان خدمات')
    details = models.TextField(verbose_name='متن خدمات')
    image = models.ImageField(upload_to='images/site-services/',verbose_name='تصویر خدمات')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'خدمات'
        verbose_name_plural = 'خدمات سایت'


class  SocialMediaServices(models.Model):
    site = models.ForeignKey(SiteSetting, on_delete=models.CASCADE)
    massage= models.CharField(max_length=200,verbose_name='توضیحات',null=True,blank=True)


    def __str__(self):
        return   "بخش شبکه‌های اجتماعی"

    class Meta:
        verbose_name = 'بخش شبکه‌های اجتماعی'
        verbose_name_plural = ' شبکه‌ اجتماعی'


class SocialMediaServicesGallery(models.Model):

    social_media = models.ForeignKey(
        SocialMediaServices,
        on_delete=models.CASCADE,
        verbose_name='گالری تصاویر'
    )

    image = models.ImageField(
        upload_to='images/social_media/',verbose_name='تصویر'
    )

    def __str__(self):
        return 'گالری شبکه اجتماعی'

    class Meta:
        verbose_name = 'تصویر'
        verbose_name_plural = 'گالری تصاویر'