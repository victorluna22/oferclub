from account.models import Account


class AccountsBackend(object):
    def authenticate(self, email=None, oauth_token=None):
        try:
            account = Account.objects.get(user__email=email,
                oauth_token=oauth_token)
            return account.user
        except Account.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            account = Account.objects.get(user__pk=user_id,
                provider='facebook')
            return account.user
        except Account.DoesNotExist:
            return None
