from .models import Visitor


class VisitorCountMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Get the URL of the current request
        url = request.path

        # Use get_or_create to ensure a Visitor object exists
        visitor, created = Visitor.objects.get_or_create(url=url)

        # If the visitor was just created, set visit_count to 1
        if created:
            visitor.visit_count = 1
        else:
            visitor.visit_count += 1  # Increment visit count if the visitor already existed

        visitor.save()

        response = self.get_response(request)
        return response
