This was a pathing problem (which was fun as we are doing this in CS 6601 currently)

Essentially, build the grid and find the fastest path was really the only thing to do. A simple BFS
ended up working, and wasn't really that inefficient if you approached it correctly. We weren't able to use
A* because of unit costs I guess? I attempted it and it didn't work, but I might have implemented incorrectly.

Edit: I think my solution was correct, but I was inefficient in my get neighbors as I had to pass in the graph
each time. I simply needed to declare the function inside of solve(), which I'm not in the habit of doing
(though because it's in an isolated test it's alright to do so for these sorts of things)