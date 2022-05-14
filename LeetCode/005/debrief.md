This was one of the harder questions I've solved up to this point (though in hindsight it wasn't really that bad)

We are given a list of edges (start, end, time), a starting node K, and a number of nodes N. We are tasked with 
finding the time it would take to reach all nodes, which is essentially just finding the time it takes to reach
the furthest away node from K.

Dijkstra's algorithm helped immensely here, which I had to setup separately. There were a few other gotchas that I
dealt with, such as a node not being a start OR end node in the list of edges. Other than that, things worked smoothly
after creating and utilizing Dijkstra's algorithm.