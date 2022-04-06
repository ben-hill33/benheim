# React Native

## A little history lesson

When building apps, there's really two big operating systems to write for, iOS and Android.

Apple went from building apps in Objective - C and swift and Android built using Java and Kotlin.

Which created the distinctions between _Native_, _Web_, and _Native-like_ methods to design mobile apps.

- Native used the above methods in Obj C and Java but you have to build two versions of the same app in order to deploy
- Web writes websites and make them mobile responsive first, but they weren't as fast as Native
- Native-like writes in frameworks like React Native that has direct access to Apple and Android and compiles it into the Native languages

But why React Native and not something like Flutter?

## Why React Native?

1. It has a big community
     - meaning there's plenty of support during development
2. Big companies are using it
    -  It's proven and tested and
    -  companies are hiring for it over others
3. Cross platform
   - You can use React Native with the base languages like Swift and it'll work inside the framework

Check out the [React Native docs](https://reactnative.dev/docs/getting-started)

## React Native Internals

Think of the internals in two parts
- Views
  - React native compiles views into Native Views
- Logic
  - Needs a JavaScript virtual machine or JS Core engine to read the Native logic
  - React Native (RN) Bridge is what communicates to Native Platform/API
    - Message Broker pattern, a bridge that translates between languages

## Is there CSS in React Native?

Actually? No. CSS is used to make web apps. 

## React DOM vs React Native

- React DOM was designed to build web apps
- React Native is designed to build mobile apps

Where you'd have to import ReactDOM for React, you'll have to import react-native

This means there will be subtle differences in the syntax between using React DOM and RN. 

Styling for instance you can't use `px` for how you want to style a box, it would just be "50"

## Recommended Setup

Refer back to Udemy course for environment setup [here](https://www.udemy.com/course/complete-react-native-mobile-development-zero-to-mastery-with-hooks/learn/lecture/24607544#overview)



 (../index.md)
