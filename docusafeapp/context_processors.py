# docusafeapp/context_processors.py

def username(request):
    # Make the username available in templates
    return {'username': request.user.username if request.user.is_authenticated else None}
