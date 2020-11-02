302separation
===

Time:       2 weeks

Team:       1

Language:   Python


The project
----
In 1929, a Hungarian named [**Frigyes Karinthy**](https://en.wikipedia.org/wiki/Frigyes_Karinthy) established the theory of [**six degrees of separation**](https://en.wikipedia.org/wiki/Six_degrees_of_separation): every per-son in the world can be connected to any other person via a chain of individual relationships, that has nomore than six links. Nowadays, social networks makes it easy to evaluate the degree of separation between two individuals, and to test this theory.

Starting with a file that contains a list of friendship links between different Facebook accounts, the goal of this project is to use [**graph theory**](https://en.wikipedia.org/wiki/Graph_theory) to compute the degree of separation between two people.


Your program must display the following:
* the **list of people** in alphabetical order (the order that will be used to build the matrices)
* the **adjacency matrix**
* the **matrix of the shortest paths**, with lengths less than or equal ton.

If two names are given as argument to the program, it must instead display the degree of separation be-tween those two people, or -1 if they are not connected.

> Friendships are reciprocal in Facebook: if A is friends with B, B is also friends with A


## USAGE:

```
>> ./302separation -h
USAGE
    ./302separation file [n | p1 p2]
DESCRIPTION
    file    file that contains the list of Facebook connections
    n       maximum length of the paths
    pi      name of someone in the file
```

Author [**Corentin COUTRET-ROZET**](https://github.com/sheiiva)