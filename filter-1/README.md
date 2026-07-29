# Path of Exile item filters with Python

## Introduction

Welcome Exile!

I wanted to simplify the management of my own item filters.
That also presented the opportunity to practice coding.
In this repo I tend to over-engineer some parts, because it's fun.

## Composition over inheritance

The fundamental Class in this codebase is the `Rule` class.
Each rule is made up of a list of `Extensions`.
An `Extension` is very similar to the properties in <https://www.pathofexile.com/item-filter/about>
Besides the base-level extensions defined by GGG it is also possible to create custom `Extension` to form more complex conditionals.
