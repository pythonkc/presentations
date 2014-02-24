!SLIDE

## Generators

Jon Smajda

February 27, 2014

!SLIDE

1. Powerful language feature
2. Increasingly important
3. Initially unsettling

!SLIDE

## Python lists are friendly

~~~~{python}
>>> mylist = [1, 2, 3]

>>> mylist  # Let's take a look
[1, 2, 3]

>>> len(mylist)  # How big?
3

>>> mylist[:2]  # Peek at first two items
[1, 2]

>>> [i*i for i in mylist]  # Square 'em all
[1, 4, 9]

>>> mylist  # Still there!
[1, 2, 3]
~~~~

!SLIDE

## One day you're expecting a list...    
#### and you get a generator.

~~~~{python}
>>> mygen  # Oh hello, 0x106f39fa0, nice to see you.
<generator object <genexpr> at 0x106f39fa0>

>>> len(mygen)  # How dare you?
TypeError: object of type 'generator' has no len()

>>> mygen[:2]  # No peeking! 
TypeError: 'generator' object has no attribute '__getitem__'

>>> list(mygen)  # Ok, just gimme a list.
[1, 2, 3]

>>> [i*i for i in mygen]  # Where did it all go!
[]
~~~~

!SLIDE

Why does Python hate you?

!SLIDE

## Back to basics

!SLIDE

### What is a generator?

A special type of *iterable*.

!SLIDE

### Ok, what is an iterable?

#### Short answer:

Something you can *iterate* over to produce a *stream of values*.

!SLIDE

### Lists, Dictionaries, Strings...

~~~~{python}
for i in [1, 2, 3]:
    print(i)

for key, value in {1: 'One', 2: 'Two'}.iteritems():
    print(value)

for i in 'Python':
    print(i)
~~~~

!SLIDE

### 

#### Long answer:

Iteration in python works on things that implement an `__iter__` method to return iterators with `__next__` (or `next`) methods that handle `StopIteration` exceptions.


!SLIDE

More or less what `for i in mylist: print i` is doing:

~~~~{python}
mylist = [1, 2, 3]
iterator = iter(mylist) # calls mylist.__iter__()
while True:
    try:
        # call iterator.next() (or __next__() in 3)
        print(next(iterator))  
    except StopIteration:
        break
~~~~
!SLIDE

### Two Points

1. How nice that we don't have to write *that* all the time.

2. How nice that Python provides such a nice interface for objects we want to iterate over?

!SLIDE

## A Common Use For Iteration

We want to iterate over an iterable and return a new iterable:

~~~~{python}
def square(numbers):
    squared = []
    for number in numbers:
        squared.append(number * number)
    return squared

# Or:
def square(numbers):
    return [i*i for i in numbers]
~~~~

!SLIDE

### The Problem

You have to hold *two* complete lists in memory: the original list and the new one.

~~~~{python}
def square(numbers):
    return [i*i for i in numbers]
~~~~

!SLIDE

### The Solution

Maybe don't really *need* to hold that whole list in memory.

*If* we're only going to iterate over it one item at a time...    
we just need *one thing at a time*.

!SLIDE

### The Solution

~~~~{python}
# Instead of returning the whole list
def square(numbers):
    squared = []
    for number in numbers:
        squared.append(number * number)
    return squared

# We *yield* one thing at a time 
def square(numbers):
    for i in numbers:
        yield i*i

~~~~

!SLIDE

Instead of a list, you get a *recipe*.

~~~~{python}
>>> sq = square([0, 1, 2])
>>> sq
<generator object square at 0x10707b190>
~~~~

<em>(A recipe that self-destructs after you use it once.)</em>


!SLIDE

#### `"This generator will self-destruct"`

![](self-destruct.jpg)


!SLIDE

As long as we're only iterating, we can't even tell the difference:

~~~~{python}
for i in square([0, 1, 2]):
    print i
~~~~

!SLIDE

Because generators behave just like other iterables:

~~~~{python}
>>> sq = square([0, 1, 2])
>>> sq
<generator object square at 0x10707b190>
>>> next(sq)
1
>>> next(sq)
4
>>> next(sq)
9
>>> next(sq)
StopIteration
>>> list(sq)  # ...except for this part
[]
~~~~

!SLIDE

Because everybody loves comprehensions: just use `()` instead of `[]`:

~~~~{python}
# This returns a list
def square(numbers):
    return [i*i for i in numbers]

# This returns a generator
def square(numbers):
    return (i*i for i in numbers)
~~~~

!SLIDE

So, generators are a great tool if:

1. You only need to iterate and be done.

2. You run the risk of large amounts of data.



!SLIDE

### Python 2.7

There are generator alternatives:

~~~~
range  -> xrange
map    -> itertools.imap
filter -> itertools.ifilter
~~~~


!SLIDE

### Python 3.3

Generators by default:

~~~~
range
map
filter
~~~~


!SLIDE

Because of common iterator interface/protocol, many functions that take a list can take a generator:

~~~~{python}
>>> sum([i*i for i in [1, 2, 3]])
14
>>> sum(i*i for i in [1, 2, 3])
14
~~~~

!SLIDE

And our `square` generator can also take a generator from, say, `xrange`

~~~~{python}
>>> square([1, 2, 3])
>>> square(xrange(0, 1000000))
>>> sum(square(xrange(0, 1000000)))
~~~~

You can really see the advantages of generators when you start:

1. Dealing with more data
2. Chaining generator functions together


!SLIDE

### Quick Demo?


!SLIDE

### Just getting started

1. `.send`
2. asyncio/"Tulip"

!SLIDE

### Resources

1. Ned Batchelder, [How to Loop Like A Native](http://pyvideo.org/video/1758/)

2. Jeff Knupp, [Yield and Generators Explained](https://www.jeffknupp.com/blog/2013/04/07/improve-your-python-yield-and-generators-explained/)

3. Guido van Rossum, [From List Comprehensions to Generator Expressions](http://python-history.blogspot.com/2010/06/from-list-comprehensions-to-generator.html)

4. David Beazley, [A Curious Course on Coroutines and Concurrency](http://www.dabeaz.com/coroutines/Coroutines.pdf)

5. [PEP380: Syntax for Delegating to a Subgenerator](http://legacy.python.org/dev/peps/pep-0380/)
