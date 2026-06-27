from django.shortcuts import render, redirect

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView

from Contact_us_page.forms import FeedbackBoxForm
from site_config.models import SiteSetting


def Contact_Us_page(request):
    data = SiteSetting.objects.first()
    context = {
        'site_setting': data,
        'form': FeedbackBoxForm()
    }
    return render(request, 'contact_us/contact_us.html', context)


class FeedbackBoxView(FormView):
    form_class = FeedbackBoxForm
    success_url = reverse_lazy("feedback_massage")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class FeedbackMassageView(TemplateView):

    template_name = 'feedback_box/success_feedback_massage.html'