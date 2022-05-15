import heapq


class PriorityQueue:
    def __init__(self):
        self.queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self.queue, (priority, self._index, item))
        self._index += 1

    def pop(self):
        priority, index, item = heapq.heappop(self.queue)
        return priority, item

    def isEmpty(self):
        return len(self.queue) == 0

    def top(self):
        priority, index, item = self.queue[0]
        return priority, item

    def __repr__(self):
        return str(self.queue)

    def __str__(self):
        return str(self.queue)

    def __iter__(self):
        return iter(sorted(self.queue))

    def __contains__(self, key):
        return key in [n[-1] for n in self.queue]

    def __eq__(self, other):
        return self.queue == other.queue
