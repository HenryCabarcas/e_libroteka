from rest_framework.response import Response


def response(code: int, messages: list = [], result: list = []):
    return Response({
        "state": "success" if code < 300 else "error",
        "code": code,
        "result": result,
        "messages": messages
    }, code)
