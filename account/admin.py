# coding: utf-8
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.admin import UserAdmin
from account.models import Account, OferClubUser, Partner, Filial, Affiliate



class OferClubUserCreationForm(UserCreationForm):
    """
    A form that creates a user, with no privileges, from the given email and
    password.
    """

    def __init__(self, *args, **kargs):
        super(OferClubUserCreationForm, self).__init__(*args, **kargs)
        del self.fields['username']

    class Meta:
        model = OferClubUser
        fields = ('full_name', 'email', 'gender', 'birthday', 'city')


class OferClubUserChangeForm(UserChangeForm):
    """
    A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """

    def __init__(self, *args, **kargs):
        super(OferClubUserChangeForm, self).__init__(*args, **kargs)
        del self.fields['username']

    class Meta:
        model = OferClubUser
        fields = ('full_name', 'email', 'gender', 'birthday', 'city')


class OferClubUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_(u'Informações'), {'fields': ('full_name', 'gender', 'birthday', 'city', 'credit')}),
        (_(u'Permissões'), {'fields': ('is_active', 'is_staff', )}),
        (_(u'Datas importantes'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'full_name', 'password1', 'password2')}
        ),
    )
    form = OferClubUserChangeForm
    add_form = OferClubUserCreationForm
    # actions = ['activate_users', 'deactivate_users', ]
    list_display = ('email', 'full_name', 'gender', 'date_joined', 'is_staff')
    search_fields = ('email', 'full_name')
    date_hierarchy = 'date_joined'
    ordering = ('-date_joined',)
    readonly_fields = ('date_joined', 'last_login')

class FilialCreationForm(UserCreationForm):
    """
    A form that creates a user, with no privileges, from the given email and
    password.
    """

    def __init__(self, *args, **kwargs):
        kwargs['initial'] = {'is_staff': True}
        super(FilialCreationForm, self).__init__(*args, **kwargs)
        del self.fields['username']
        

    class Meta:
        model = Filial
        fields = ('full_name', 'email', 'city')


class FilialChangeForm(UserChangeForm):
    """
    A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """

    def __init__(self, *args, **kwargs):
        kwargs['initial'] = {'is_staff': True}
        super(FilialChangeForm, self).__init__(*args, **kwargs)
        del self.fields['username']

    class Meta:
        model = Filial
        fields = ('full_name', 'email', 'city')


class FilialAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_(u'Informações'), {'fields': ('full_name', 'partner', 'phone', 'cellphone', 'city')}),
        (_(u'Informações Bancária'), {'fields': ('owner_name', 'bank_name', 'agency', 'number', 'cpf')}),
        (_(u'Permissões'), {'fields': ('is_active', 'is_staff', 'groups', )}),
        (_(u'Datas importantes'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'full_name', 'partner', 'city', 'password1', 'password2')}
        ),
    )
    form = FilialChangeForm
    add_form = FilialCreationForm
    # actions = ['activate_users', 'deactivate_users', ]
    list_display = ('email', 'full_name', 'date_joined', 'is_staff')
    search_fields = ('email', 'full_name')
    date_hierarchy = 'date_joined'
    ordering = ('-date_joined',)
    readonly_fields = ('date_joined', 'last_login')


class AffiliateCreationForm(UserCreationForm):
    """
    A form that creates a user, with no privileges, from the given email and
    password.
    """

    def __init__(self, *args, **kargs):
        super(AffiliateCreationForm, self).__init__(*args, **kargs)
        del self.fields['username']

    class Meta:
        model = Affiliate
        fields = ('full_name', 'email', 'city')


class AffiliateChangeForm(UserChangeForm):
    """
    A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """

    def __init__(self, *args, **kargs):
        super(AffiliateChangeForm, self).__init__(*args, **kargs)
        del self.fields['username']

    class Meta:
        model = Affiliate
        fields = ('full_name', 'email', 'city')


class AffiliateAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_(u'Informações'), {'fields': ('full_name', 'phone', 'cellphone', 'city')}),
        (_(u'Informações Bancária'), {'fields': ('owner_name', 'bank_name', 'agency', 'number', 'cpf')}),
        (_(u'Permissões'), {'fields': ('is_active', 'is_staff', )}),
        (_(u'Datas importantes'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'full_name', 'city', 'password1', 'password2')}
        ),
    )
    form = AffiliateChangeForm
    add_form = AffiliateCreationForm
    # actions = ['activate_users', 'deactivate_users', ]
    list_display = ('email', 'full_name', 'date_joined', 'is_staff')
    search_fields = ('email', 'full_name')
    date_hierarchy = 'date_joined'
    ordering = ('-date_joined',)
    readonly_fields = ('date_joined', 'last_login')




class FilialInline(admin.StackedInline):
    fieldsets = (
        (None, {'fields': ('email', 'password', 'is_staff', 'full_name', 'partner', 'phone', 'cellphone', 'city','owner_name', 'bank_name', 'agency', 'number', 'cpf','is_active', 'last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'full_name', 'partner', 'city', 'password1', 'password2')}
        ),
    )
    model = Filial
    form = FilialChangeForm
    add_form = FilialCreationForm
    readonly_fields = ('date_joined', 'last_login')
    min_num = 1
    extra = 0

# class PartnerAdmin(admin.ModelAdmin):
    # inlines = [
    #     FilialInline,
    # ]


# Register your models here.
admin.site.register(OferClubUser, OferClubUserAdmin)
admin.site.register(Filial, FilialAdmin)
admin.site.register(Affiliate, AffiliateAdmin)
# admin.site.register(Account)
admin.site.register(Partner)