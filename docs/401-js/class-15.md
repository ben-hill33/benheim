# Access Control (ACL)

1. _When is Basic Authorization used vs. Bearer Authorization?_

- They can both do the same thing but bearer should only be used over HTTPS

2. _What does the JSON Web Token package do?_

- Async
  - If a callback is supplied, the callback is called with the **err** or the JWT
- Synchronous
  - Returns the JWT as a string

3. _What considerations should we make when creating and storing a SECRET?_

- Some considerations should be who we are allowing to have access to it but also having a public and private key stored in .env. This way it would be much more difficult to access that data

## Vocab

- _encryption:_
  - The process of converting information or data into a code, especially to prevent unauthorized access.
- _token:_
  - A token is a piece of data that has no meaning or use on its own, but combined with the correct tokenization system, becomes a vital player in securing your application. Token based authentication works by ensuring that each request to a server is accompanied by a signed token which the server verifies for authenticity and only then responds to the request.
- _bearer:_
  - Bearer authentication (aka token authentication) is an HTTP authentication scheme that involves security tokens called **bearer tokens**. Could be understood as "give access to the bearer of this token."
- _secret:_
  - JWTs can be signed using a secret or a public/private key pair using RSA or ECDSA
- _JSON Web Token:_
  - JWT is an open standard(RFC 7519) that defines a compact and self-contained way for securely transmitting between parties as a JSON object. This data can be verified and trusted because it is digitally signed.
- _RBAC:_

  - Role-based Access Control
    - is an approach to restricting system access to authorized users. Is used by the majority of enterprises with more than 500 employees.
    - a policy-neutral access-control mechanism defined around roles and priveleges.

- [RBAC tutorial](https://www.youtube.com/watch?v=C4NP8Eon3cA)
  - In enterprise setting, access may be based on job function or role of a user
    - Payroll manager, project member
    - Access rights are associated with roles
  - Users authenticate themselves to the system
  - Users then can activate one or more roles for themselves
- **RBAC Benefits**
  - Policy need not be updated when a certain person with a role leaves the organization
  - New employee should be able to activate the desired role
  - Revisiting least privelege
    - User in one role has access to a subset of the files
    - Switch roles to gain access to other resources
  - SELinux supports RBAC

### Material

- [5 Steps to RBAC](https://www.csoonline.com/article/3060780/5-steps-to-simple-role-based-access-control.html)
- [wiki - RBAC](https://en.wikipedia.org/wiki/Role-based_access_control)

#### Lecture notes

- Authentication
  - /signup - create account
  - /signin - authenticate (user/password) basic
  - (oauth) - authenticate remotely
- Authorization
  - Some cons to using role based access control is it doesn't grow well
- Code plan
  - ACL {} could go in model
  - Model - + role field
  - ACL middleware - usermodel - is the user authorized to do a thing? if yes, next()
  - add role to users schema (role: {type: String, })
- need to tell each route what a user "can" do (router.get('/article', bearer, can('read')))

#### FR Tab Times

6:47 - Authorization
6:49 - Blog stuff'n'stuff
6:55 - Roles/Perms
6:57 - RBAC stuff
7:08 - Table example
7:15 - Break
7:27 - Coding plan
7:35 - Currying (higher order function)
7:43 - add a role to code
7:49 - add ACL
7:51 - router.get('/article' things..)
7:53 - acl.js (where currying comes in)
8:01 - Change tokenObject
8:04 - OR! change acl.js (can method)
8:09 - just kidding on read, update please
8:22 - lab breakdown

[Table of Contents](../index.md)
