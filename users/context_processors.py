from django.shortcuts import get_object_or_404

from users.models import Profile


def profile_processor(request):
    if request.user.is_authenticated:
        user_profile = get_object_or_404(Profile, user=request.user)
        return {'user_profile': user_profile}
    else:
        return {'user_profile': None}
