from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden


class SuperUserRequiredMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return HttpResponseForbidden()
        return super().dispatch(request, *args, **kwargs)