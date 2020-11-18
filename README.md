# cookiecutter-node-monorepo-collection

A collection of [cookiecutters](https://www.github.com/cookiecutter/cookiecutter)
designed to automate the creation of node monorepos and their components (packages)

## Features
  - create node monorepos with the following tooling setup
    - [Typescript](https://www.typescriptlang.org/)
    - [Lerna](https://lerna.js.org/)
    - [Eslint](https://eslint.org/)
    - [prettier](https://prettier.io/)
    - [jest](https://jestjs.io/)
    - github remote
  - create generic [components](#why-components-instead-of-packages) quickly and easily 

## Someday features
  - improve usability (it works on my machine...)
  - add more configuration options
    - make typescript optional
    - add options for testing frameworks
    - add options for remote repository
  - add more specific types of component
    - graphql-api component
    - domain component
    - application component
    - database gateway component
    - frontend component
    - anything else that requires scaffolding or highly generic abstractions

## Installation and setup
  It works on my machine and to be honest I need to circle back and figure out exactly
  what needs to happen to make this more distributable (Python is not my strongest
  language)

## Why Components instead of Packages?
  Lerna's documentation states that it is best practice to locate all packages under a
  subdirectory named 'packages' but there is no real requirement to do so.

  I chose to use the name components in order to avoid shell completion conflicts with
  package.json which must be named as such.  

  Also, I was originally inspired to create this project after reading Uncle Bob's
  [Clean Architecture](https://www.amazon.com/Clean-Architecture-Craftsmans-Software-Structure/dp/0134494164)
  which refers to "smallest unit of deployment" as a "component" so I want to stick with
  that terminology if only to help solidify the idea that clean architecture is not
  bound to the frameworks and tools that we use to implement its design.
