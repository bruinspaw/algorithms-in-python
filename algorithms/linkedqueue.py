# Copyright (C) 2018, bruinspaw <bruinspaw@gmail.com>
#
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
# ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from dlist import DoublyLinkedList


class EmptyQueueError(Exception):
    """EmptyQueueError is raised while accessing an empty queue."""
    def __str__(self):
        return 'an empty queue'


class LinkedQueue:
    """FIFO Queue implementation using a doubly linked list for storage."""

    def __init__(self):
        """Create an empty queue."""
        self._queue = DoublyLinkedList()

    def __len__(self):
        """Return the size of the queue."""
        return len(self._queue)

    def __str__(self):
        """Return information for users."""
        return str(self._queue)

    def __repr__(self):
        """Return information for developers."""
        return '< %s object at %s >' % (self.__class__,
                                   hex(id(self)))
    def __iter__(self):
        """Return iterator."""
        return iter(self._queue)

    def is_empty(self):
        """Return True is the queue is empty."""
        return self._queue.is_empty()

    def enqueue(self, e):
        """Add element e to the back of the queue."""
        return self._queue.push_back(e)

    def dequeue(self):
        """Return and remove the element at the front of the queue."""
        if self.is_empty():
            raise EmptyQueueError
        return self._queue.pop_front()

    def first(self):
        """Return (do not remove) the element at the top of the queue."""
        if self.is_empty():
            raise EmptyQueueError
        return self._queue.first()


if __name__ == '__main__':
    q = LinkedQueue()
    q.enqueue(5)
    print(q)
    q.enqueue(3)
    print(q)
    print(len(q))
    q.dequeue()
    print(q)
    print(q.is_empty())
    q.dequeue()
    print(q)
    print(q.is_empty())
    #q.dequeue()
    q.enqueue(7)
    print(q)
    q.enqueue(9)
    print(q)
    print(q.first())
    q.enqueue(4)
    print(q)
    print(len(q))
    q.dequeue()
    print(q)
