from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin,LoginRequiredMixin

from .models import Client
from .forms import ClientForm


class ClientView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    """ A view to return a list of clients """
    template_name = "clients/view_clients.html"
    model = Client
    context_object_name = 'clients'
    paginate_by = 8


class CreateClientView(LoginRequiredMixin, CreateView):
    """
    A view to provide a Form to the user
    to create a client
    """
    form_class = ClientForm
    template_name = 'clients/add_client.html'
    success_url = "/clients/"
    model = Client

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateClientView, self).form_valid(form)


class EditClientView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    A view to provide a Form to the user
    to edit an event
    """
    form_class = ClientForm
    template_name = 'clients/edit_client.html'
    success_url = "/clients/"
    model = Client

    def test_func(self):
        return self.request.user == self.get_object().user


class ViewClientView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    """ A view to return a single client """
    template_name = "clients/view_client.html"
    model = Client
    context_object_name = 'client'

    def test_func(self):
        return self.request.user == self.get_object().user


class DeleteClientView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """ A view to delete a client """
    model = Client
    success_url = "/clients/"

    def test_func(self):
        return self.request.user == self.get_object().user