import heapq

class EventManager:

    def __init__(self, events):
        self.heap = []
        self.events = {}

        denqoravil = events

        for eventId, priority in denqoravil:
            self.events[eventId] = priority
            heapq.heappush(self.heap, (-priority, eventId))

    def updatePriority(self, eventId, newPriority):
        self.events[eventId] = newPriority
        heapq.heappush(self.heap, (-newPriority, eventId))

    def pollHighest(self):
        while self.heap:
            priority, eventId = heapq.heappop(self.heap)

            if eventId in self.events and self.events[eventId] == -priority:
                del self.events[eventId]
                return eventId

        return -1