from django.views.generic import TemplateView

class IndexView(TemplateView):
    """ A view to return the home page """
    template_name = "home/index.html"


class PrivacyView(TemplateView):
    """ A view to return the privacy policy page """
    template_name = "home/privacy.html"