# Django REST Framework & Docker

# [Beginners guide to Docker](https://wsvincent.com/beginners-guide-to-docker/)

Docker is a tool that makes containers and isolates entire applications. 
- The entire development environment is isolated: programming language, software packages, databases, and more. 
- With Docker we no longer have to mess around with venv's
- Docker can be shared among team members so everyone is working on the same setup
- The downside is _complexity_. Docker has a lot going on 

# Containers

Docker is really just Linux containers which are a type of virtualization. 
- Virtualization has its roots at the beginning of computer science when large, expensive mainframe computers were the norm. 
  - 
  - How could multiple programmers use the same single machine? 
    - The answer was virtual machines which are complete copies of a computer system from the operating system up

The downside to to virtual machines is size (typically guest OS can take up to 700MB) and speed (i.e. if one server supports three virtual machines, that's at least 2.1GB of disk space)

The answer to the downside is that since most computers rely on the same Linux OS, programmers can make use of virtualized _Linux containers_ (aka _containerization_)
  - _This is fundamentally what Docker is_

A good analogy is virtual machines are like homes: stand-alone buildings with their own infrastructure including plumbing, heating, utilities, etc. Docker containers are like apartments: they share common infrastructure like utilites, but come in various sizes that match the exact needs of an owner.

## Containers vs Virtual Environments

I use virtual environments for Python which will only isolate the package, they still rely on a global, system-level installation of Python.

## Installing Docker and commands

To install Docker, [download the desktop app on your computer](https://www.docker.com/get-started) and create an account
- Once docker is done installing, confirm your version by running `docker --version`

_Docker compose_ is an additional tool that is automatically included with Mac and Windows downnloads of Docker. 
- Check docker compose's version with `docker-compose --version`

To confirm Docker installed correctly, run `docker run hello-world`
- This will download an offical _image_ and then run the container

Command to inspect Docker is `docker info`
- Focus on the top lines which show containers and images

To create a new image, create or cd into a directory you want to create the image inside. 
- Run `touch Dockerfile` command
- In your editor, open the Dockerfile that the previous command just created.
  - Add this code into it 
```
# Dockerfile
FROM python:3.7-alpine
```
# [Django for APIs - Library Website](https://djangoforapis.com/library-website-and-api/)

## [Django REST framework](https://www.django-rest-framework.org/)


[Table of Contents](../index.md)
