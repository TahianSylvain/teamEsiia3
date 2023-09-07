from notifications_app.models import BroadcastNotification


def notifications(request):
    allnotifications = BroadcastNotification.objects.all()
    print(allnotifications)
    return {'notifications': allnotifications}