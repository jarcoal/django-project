from django.http import HttpRequest


def get_ip_address(request: HttpRequest, check_x_forwarded_for: bool = True) -> str:
    """
    Returns the IP address of the client, looking in the
    X-Forwarded-For header if necessary.
    """

    if check_x_forwarded_for:
        if forwarded_for := request.META.get("HTTP_X_FORWARDED_FOR"):
            # Heroku places the IP address as the last entry.
            return forwarded_for.split(",")[-1]

    return request.META["REMOTE_ADDR"]


def ip_cache_key(group: str, request: HttpRequest) -> str:
    """
    Helper for django-ratelimit to use our IP address util
    for cache key lookups instead of the built-in one.
    """

    return get_ip_address(request)
