from .models import Tag

nav_display_tags = Tag.objects.filter(nav_display=True)

def nav_tag(request):
    return {'nav_display_tags': nav_display_tags}
