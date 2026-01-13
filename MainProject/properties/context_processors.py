from .models import Property

def property_count(request):
    return {
        "total_properties": Property.objects.count()
    }
