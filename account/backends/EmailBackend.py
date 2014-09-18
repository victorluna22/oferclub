from account.models import OferClubUser


class EmailBackend(object):
    def authenticate(self, email=None, password=None):
        kwargs = {'email': email}
        try:
            user = OferClubUser.objects.get(**kwargs)
            if user.check_password(password):
                return user
        except OferClubUser.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return OferClubUser.objects.get(pk=user_id)
        except OferClubUser.DoesNotExist:
            return None
