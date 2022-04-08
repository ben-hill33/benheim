# OAuth

1. _Why is authentication important?_
   - Authentication is important because it enables organizations to keep their networks secure by permitting only authenticated users to access its protected resources, which may include computer systems, networks, databases, websites and other network-based apps or services.
1. _Why should we be careful about storing a user’s password?_
   - If you do not take the right precautions when storing passwords, you could expose your user passwords to an attacker. Many people use the same email and password combination all over the Internet. If you expose their password, they could be left vulnerable on other websites or web applications as well.
1. _What is the difference between hashing and encryption?_
   - Encryption is a two-way function; what is encrypted can be decrypted with the proper key. Hashing, however, is a one-way function that scrambles plain text to produce a unique message digest. With a properly designed algorithm, there is no way to reverse the hashing process to reveal the original password.
1. _What is the difference between encryption and encoding?_
   - Encoding is for maintaining data usability and can be reversed by employing the same algorithm that encoded the content, i.e. no key is used. Encryption is for maintaining data confidentiality and requires the use of a key (kept secret) in order to return to plaintext.
1. _What is a token used for?_
   - A token is used to make security decisions and to store tamper-proof information about some system entity. While a token is generally used to represent only security information, it is capable of holding additional free-form data that can be attached while the token is being created.

## Vocab

- _authentication_
  - **Noun**
    - The process or action of proving or showing something to be true, genuine, or valid.
  - **Computing**
    - The process or action of verifying the identity of a user or process.
- _authorization_
  - **noun**
    - the action or fact of authorizing or being authorized.
  - **computing**
    - A security mechanism to determine access levels or user/client priveleges relates to system resources including files, services, computer programs, data and application features.
- _encryption_
  - noun
    - the process of converting information or data into code, especially to prevent unauthorized access.
- _hashing_
  - a function that converts one value to another. Hashing data is a common practice in CS and is used for several different purposes. The table may be an array, database, or other data structure.
- _session_
  - uses sessionStorage object to store data on a temporary basis for a single browser window or tab. The data disappears when the session ends (when the user closes that browser window or tab).
- _cookie_
  - cookies are small files which are stored on user's computer. They are designed to hold a modest amount of data specific to a particular client or website, and can be accessed either by the web server or the client computer.
- _token_

  - token based authentication requres users to obtain a computer-generated code (or token) before they're granted network entry.

- _Basic Auth_
  - is a simple authentication scheme built into the HTTP protocol. The client sends HTTP requests with the Authorization header that contains the word **basic** followed by a space and a base64-encoded string username:password
- _encoding_
  - is the process of converting data or a given sequence of characters, symbols, alphabet, into a specified format, for the secured transmission of data.
- _secret_
  - is the piece of information or parameter that is used to encrypt and decrypt messages in a symmetric encryption.
- _cryptography_
  - the science of protecting information by transforming it into a secure format

### [What is OAuth Really All About?](https://www.youtube.com/watch?v=t4-416mg6iU)

- Why OAuth?
  - Meant for authorization, not for authentication between services.

Current version is OAuth 2.0

- _Common analogy:_
  - Giving your expensive car to the valet to park your car, you would have a master key and a valet key.
  - Valey key would have limited access to the the car's features.
  - This limitation is referred to as access delegation
- _The OAuth Flow:_
  - If you have one service that is asking another service for things that you've stored in the google cloud for example, the requesting service will ask google for permission to view those.
  - Google, or your cloud service, will say no unless both services are using OAuth. If they are, your cloud service will ask you, the user, if the requesting service is legit and if they can have access to the data they're requesting.
  - If you give your cloud service permission, then google will give the requesting service a one time use **token** that has limited access to the users data (like the valey key).

### [OAuth terms and flows explained](https://www.youtube.com/watch?v=3pZ3Nh8tgTE)

**Terminologies**

- _Resource (protected resource)_
  - something that is being sought by all the different actors in the OAuth flow.
- _Resource Owner_
  - The person who owns the access to the resource at any given time.
  - An entity (the user) capable of granting access to a protected resource.
- _Resource Server_
  - The server hosting the protected resource
- _Client_
  - An application making protected resource requests on behalf of the resource owner and with its authorization.
- _Authorization Server_
  - The server issuing access tokens to the client
  - The resource server has the burden of security because they are the ones who are hosting the resource.

**Flows**

- _Authorization Code Flow (OAuth flow one. is the safest way for authorization)_
  1.  Resource owner asks the client to access things from the resource server
  1.  Client asks authorization server for the specific resource they are wanting to access.
  1.  Auth server asks resource owner for permission to grant access to the client and what permissions to grant that client.
  1.  Resource owner gives permission (or not).
  1.  Auth server gives client an authorization token
  1.  Client uses token to contact auth server for an access token
  1.  Auth server grants one access token to client when they've verified the correct authorization token. Access token is like a hotel room key where they are granted access to one room in their hotel to use
  1.  An API call is made using the access token to the resource host
  1.  Resource host validates the token and provides the client with the data that's being requested.
- _Implicit Flow (OAuth flow 2)_
  1. Resource owner asks the client to access things from the resource server
  1. Client asks authorization server for the specific resource they are wanting to access.
  1. Auth server asks resource owner for permission to grant access to the client and what permissions to grant that client.
  1. Resource owner gives permission (or not).
  1. Here is the difference from flow one. The Authorization token isn't exchanged and access token is granted immediately.
     - The drawback here is that someone else can impersonate this client with the access token. It is more secure for the client to request an auth token and exchange for
- _Client Credentials Flow (OAuth Flow 3)_
  - When the client is well trusted (confidential clients)
  - Basically means making an API call to a service that is trusted by the authorization server.

#### Articles

- [OAuth2 simplified](https://aaronparecki.com/oauth-2-simplified/)
- [Build a Node API with OAuth](https://developer.okta.com/blog/2018/08/21/build-secure-rest-api-with-node)

#### Lecture notes

- **Auth Flow Example**

  - 1. /sign in
       -> express
       -> router
       -> middleware "basic"
       -> decode username:password
       -> model
       -> token
       <- back to sign in

- \*\*

- **Front row tab times**
  - 6:42 Schedule
  - 7:19 Auth example
  - 7:40 Break
  - 7:52 Code review
  - 8:06 server.js clean up
  - 8:17 mongo test
  - 8:30 bearer auth

  
