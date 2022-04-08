## Authorization & Authentication in Servers

## [JWT (JSON Web Token)](https://jwt.io/introduction/)

JWT is an open standard that defines a compact and self-contained way for securely transmitting information between parties as a JSON object. 
- This information can be verified because it's digitaly signed via a
  - Secret, or public/private key pair 

Signed tokens can verify the integrity of the claims contained within it, while encrypted tokens hide those claims from other parties. 
- When tokens are signed via public/private key pairs, the signature also certifies that only the party holding the key is the one that signed it. 

### Authorization
- Authorization is the most common use case for JWT.
  - Once the user is logged in (authentication), each subsequent request will include the JWT, allowing the user to access routes, services, and resources that are permited with that token. 
  - Single Sign On is a feature that widely uses JWT nowadays, because of its small overhead and its ability to be easily used across different domains. 

### Structure
JWT's consist of three parts (separated by a dot `.`)

**Header**
    - The header typically consists of two parts, the _token type_, and the signing algorithm (HMAC, SHA256, RSA)
    - The JSON is _Base64Url_ encoded to form the first part of the JWT
```
{
  "alg": "HS256",
  "typ": "JWT"
}
```

**Payload**
    - The payload contains the _claims_, which are statements about, typically, the user. 
    - There are three types of claims
      - _Registered_
        - A set of predefined claims which are not mandatory but recommended, to provide a set of useful, interoperable claims like `iss`(issuer), `exp`(expiration time), `sub` (subject), `aud` (audience).
        - The claim names are only three characters long as JWT is meant to be compact
      - _Public_
        - Can be defined at will using JWT's. To avoid collisions they should be defined in the [IANA JSON Web Token Registry](https://www.iana.org/assignments/jwt/jwt.xhtml) or be defined as a URI that contains a collision resistant namespace.
      - _Private_
        - Custom claims created to share information between parties

Example payload:
```
{
  "sub": "1234567890",
  "name": "John Doe",
  "admin": true
}
```
Like the header, the payload is then _base64_ encoded to form the second part of the JWT

**NOTE:** Don't put secret information in the header or payload as they can be read by anyone

**Signature**

To create the signature, you take the encoded header, payload, secret, and the algorithm specified in the header, and sign that. 

HMAC SHA256 example:
```
HMACSHA256(
  base64UrlEncode(header) + "." +
  base64UrlEncode(payload),
  secret)
```

The output is three _base64-URL_ strings separated by dots that can be easily passed in HTML and HTTP environments

You can test JWT's [here](https://jwt.io/#debugger-io)

## [JWT's with Django REST Framework](https://simpleisbetterthancomplex.com/tutorial/2018/12/19/how-to-use-jwt-authentication-with-django-rest-framework.html)

- For more about how to start a DRF project, click [here](https://simpleisbetterthancomplex.com/tutorial/2018/11/22/how-to-implement-token-authentication-using-django-rest-framework.html)

To install:
- poetry add djangorestframework_simplejwt
- settings.py
```
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}
```
- urls.py
```
from django.urls import path
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    # Your URLs...
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
```
- views.py _example_
```
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)
```

- app/urls.py example
```
from django.urls import path
from myapi.core import views

urlpatterns = [
    path('hello/', views.HelloView.as_view(), name='hello'),
]
```

Try using [httpie](https://httpie.io/) for new project

## [Configuring Django Settings: Best Practices](https://djangostars.com/blog/configuring-django-settings-best-practices/)

## [How does SSH work](https://www.hostinger.com/tutorials/ssh-tutorial-how-does-ssh-work)

## Resources
- [Whitenoise](http://whitenoise.evans.io/en/stable/)
- [CORS](https://en.m.wikipedia.org/wiki/Cross-origin_resource_sharing)
- [Platform as a service](https://en.wikipedia.org/wiki/Platform_as_a_service)
- [Infrastructure as a service](https://en.wikipedia.org/wiki/Infrastructure_as_a_service)

## API Integration


<!-- [Real Python Article](https://realpython.com/api-integration-in-python/)
 -->
