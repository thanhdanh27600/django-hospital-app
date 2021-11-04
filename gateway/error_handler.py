from rest_framework.views import exception_handler, Response


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response is not None:
        return response
    print(str(exc))
    exc_list = str(exc)
    return Response({"error": exc_list}, status="403")
