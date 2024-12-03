from collections import deque

class ApprovalQueue:

    #Manages approval requests for age-restricted items.

    def __init__(self):
        self.queue = deque()

    def add_approval_request(self, order_id, item):

        #Adds an approval request to the queue.

        self.queue.append((order_id, item))

    def process_next(self, staff):

        #Processes the next approval request.
        if self.queue:
            order_id, item = self.queue.popleft()
            return staff.approve_age_restricted_item(order_id, item.name)

        return "No approval requests pending."
