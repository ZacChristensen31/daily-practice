This was basically a DFS to find the deepest node that existed. Keep searching nodes until a node
doesn't have a left and a right, then return the node plus the depth.

At the then, we just find the deepest node in the left and the right, then add them together if they have
the same depth.

THe nifty way to do it is to use a depth_map that keeps track of the sum of each depth, and just calculate
as you traverse through the tree.