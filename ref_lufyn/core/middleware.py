from django.shortcuts import redirect, reverse
from django.core.exceptions import ObjectDoesNotExist



def check_user_profile_middleware(get_response):
    # One-time configuration and initialization.

    def get_full_redirect_path(url_name):
        return '{}?next={}'.format(reverse(url_name), reverse('assessments:assessment'))

    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = get_response(request)
        if request.path == '/lri/assessment/' and request.user.is_authenticated:
            if not request.user.phone_number:
                return redirect(get_full_redirect_path('profile:update_phone'))

            if not request.user.is_phone_number_verified:
                return redirect(get_full_redirect_path('profile:update_phone'))

            if not request.user.edu_info.count():
                return redirect(get_full_redirect_path('profile:set_group_id'))
        
        return response

    return middleware