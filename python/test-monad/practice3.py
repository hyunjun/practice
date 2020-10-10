#!/usr/bin/env python
# -*- coding: utf-8 -*-

timed_value = (
    fast(1)
    .bind(
        lambda x0: slow(x1)
        .bind(slow2)
        .bind(lambda x2: x0 * x2)
    )
)

final_value, time = timed_value.value, timed_value.time


#   timed_value == TimedValue (not a list)
timed_value = [
    x0 * x2
    for x0 in fast(1)
    for x1 in slow(x0)
    for x2 in slow2(x1)
]

final_value, time = timed_value.value, timed_value.time

#   lists = monad, comprehension can be written in terms of List.unit and List.bind
#   generalize comprehensions to all monads
#   But python doesn't allow overload the meaning of comprehension -> use AST transformation
def monad_comprehension(monad_cls):
    def decorator(f):
        #   ast transformation

@monad_comprehension(TimedValue)
def f():
    return [
        x0 * x2
        for x0 in fast(1)
        for x1 in slow(x0)
        for x2 in slow2(x1)
    ]

@monad_comprehension(Maybe)
def f():
    return [
        (x + y)
        for x in Maybe(5)
        for y in Maybe(6)
    ]

@monad_comprehension(Maybe)
def f():
    return [
        (x + y)
        for x in Maybe(None)
        for y in Maybe(6)
    ]

