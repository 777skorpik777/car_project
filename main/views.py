from django.http import JsonResponse
from django.views import View
from django.views.generic import TemplateView

from car_project.settings import TELEGRAM_VALUE, VIBER_VALUE, PHONE_VALUE
from car_project.utils import get_client_ip
from main.forms import CustomerRequestForm


# Create your views here.


class LandingView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['telegram_value'] = TELEGRAM_VALUE
        context['viber_value'] = VIBER_VALUE
        context['phone_value'] = PHONE_VALUE

        return context


class CustomerRequestFormView(View):

    def post(self, request):
        form = CustomerRequestForm(get_client_ip(request), request.POST)

        if form.is_valid():
            form.save()
            return JsonResponse({"status": "success"})

        return JsonResponse({"status": "error", "detail": form.errors})
