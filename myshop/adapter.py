from allauth.account.adapter import DefaultAccountAdapter
from django.shortcuts import resolve_url


class AccountAdapter(DefaultAccountAdapter):

    def get_login_redirect_url(self, request):
        threshold = 90 #seconds

        assert request.user.is_authenticated()
        if (request.user.last_login - request.user.date_joined).seconds < threshold:
            url = '/'
        else:
            url = '/'
        return resolve_url(url)
