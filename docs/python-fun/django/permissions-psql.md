# Django Permissions & Postgresql

# [Django REST Framework Permissions](https://www.django-rest-framework.org/api-guide/permissions/)

Permissions determine whether a request should be granted or denied access, along with authentication and throttling.
- Permission checks are always run at the very start of the view, before any other code is allowed to proceed.
  - Checks will typically use the authentication information in the `request.user` and `request.path` properties to determine if the incoming req should be permitted
  - Are used to grant or deny access for different classes of users to different parts of the API
  - The simplest style of permission would be to allow access to any authenticated user, and deny access to any unauthenticated user.
    - This corresponds to the `IsAuthenticated` class in REST framework.
    - `IsAuthenticatedOrReadOnly` class does exactly what the name suggests. Full access to authenticated users and read only access to unauth users


 (../index.md)