from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView
from Contact_us_page.forms import FeedbackBoxForm,CommunicationForm
from site_config.models import SiteSetting


def Contact_Us_page(request):


    if request.method == "POST":
        communication = CommunicationForm(request.POST)

        if communication.is_valid():
            communication.save()
            return redirect('Communication_Massage')

    else:
        communication = CommunicationForm()


    data = SiteSetting.objects.first()

    context = {
        'site_setting': data,
        'form': FeedbackBoxForm(),
        'communication': communication,
    }

    return render(request, 'contact_us/contact_us.html', context)

class CommunicationMassageView(TemplateView):

    template_name = 'communication_box/communication_success.html'

class FeedbackMassageView(TemplateView):

    template_name = 'feedback_box/success_feedback_massage.html'