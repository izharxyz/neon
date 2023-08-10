from django.shortcuts import get_object_or_404

from users.models import Profile


def profile_processor(request):
    if not request.user.is_authenticated:
        return {'user_profile': None}
    else:
        user_profile = get_object_or_404(Profile, user=request.user)
        return {'user_profile': user_profile}
