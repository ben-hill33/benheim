# TypeScript Overview

What is TypeScript?
- JavaScript

The goal of the Type system is to:
- Help catch errors _during_ development
- Uses 'type annotations' to analyze code
- Only active _during development_
- Doesn't provide any performance optimization
  - No effect on how our code gets executed
- TypeScript just helps us write better code!

We don't write typescript, we run our JS code through a typescript compiler.

## [Types](https://www.typescriptlang.org/docs/handbook/basic-types.html)

Easy way to refer to the different properties and functions that a value has
- Primitive types
  - string
  - numbers
  - booleans
  - Date
- Object types
  - functions
  - arrays
  - classes
  - objects

Why do we care about types?
- Types are used by TS compiler to analyze our code for errors
- Allows other engineers to understand what values are flowing around our codebase
- Everything we can assign to a variable has a type

Type annotations
- Code we add to tell TS what type of value a variable will refer to 

Type inference
- TS tries to figure out what type of value a variable refers to


### Resources

- [TypeScript Homepage](https://www.typescriptlang.org/)
- [Playground](https://www.typescriptlang.org/play?#code/PTAEHUFMBsGMHsC2lQBd5oBYoCoE8AHSAZVgCcBLA1UABWgEM8BzM+AVwDsATAGiwoBnUENANQAd0gAjQRVSQAUCEmYKsTKGYUAbpGF4OY0BoadYKdJMoL+gzAzIoz3UNEiPOofEVKVqAHSKymAAmkYI7NCuqGqcANag8ABmIjQUXrFOKBJMggBcISGgoAC0oACCoASMFmgY7p7ehCTkVOle4jUMdRLYTqCc8LEZzCZmoNJODPHFZZXVtZYYkAAeRJTInDQS8po+rf40gnjbDKv8LqD2jpbYoACqAEoAMsK7sUmxkGSCc+VVQQuaTwVb1UBrDYULY7PagbgUZLJH6QbYmJAECjuMigZEMVDsJzCFLNXxtajBBCcQQ0MwAUVWDEQNUgADVHBQGNJ3KAALygABEAAkYNAMOB4GRogLFFTBPB3AExcwABT0xnM9zsyhc9wASmCKhwDQ8ZC8iElzhB7Bo3zcZmY7AYzEg-Fg0HUiS58D0Ii8AoZTJZggFSRxAvADlQAHJhAA5SASAVBFQAeW+ZF2gldWkgx1QjgUrmkeFATgtOlGWH0KAQiBhwiudokkuiIgMHBx3RYbC43CCJSAA)

  
