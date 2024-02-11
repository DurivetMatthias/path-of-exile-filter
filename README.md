# Path of Exile item filters with Python

## Introduction

Welcome Exile!

I wanted to simplify the management of my own item filters.
That also presented the opportunity to practice coding.
In this repo I tend to over-engineer some parts, because it's fun.
I hope you find some learnings in the code.

## Composition over inheritance

The fundamental Class in this codebase is the `Rule` class.
Each rule is made up of a list of extensions.
An `Extension` is very similar to the properties in <https://www.pathofexile.com/item-filter/about>
But it is also possible to write a higher level `Extension`.

## File structure

The primary goal of the file structure is to logically divide the rule definitions.
All build specific rules can be found in `app/builds`.
All build generally applicable rules can be found in `app/common`.
All the possible rule extensions are gathered in `app/extensions`.
