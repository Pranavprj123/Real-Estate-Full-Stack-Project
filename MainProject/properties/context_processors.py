from .models import ChatMessage

def notifications(request):
    if request.user.is_authenticated:
        unread = ChatMessage.objects.filter(receiver=request.user, is_read=False).count()
        return {'unread_count': unread}
    return {'unread_count': 0}
