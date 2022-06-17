## Heap

<br />

힙(heap)은 부모와 자식 사이의 규칙에 따라 값을 저장하는 트리 기반의 자료구조이다.

<br />

- 최소 힙
  - 부모 노드의 값이 항상 자식 노드의 값들보다 작거나 같으며, 최소 힙의 루트 노드의 값은 최솟값을 보장한다.
- 최대 힙
  - 부모 노드의 값이 항상 자식 노드의 값들보다 크거나 같으며, 최대 힙의 루트 노드의 값은 최댓값을 보장한다.

<br />

```python
class BinaryHeap(object):
    def __init__(self):
        self.items = [None]

    def __len__(self):
        return len(self.items) - 1

    def _percolate_up(self):
        current = len(self)
        parent = current // 2

        while parent > 0:
            if self.items[current] < self.items[parent]:
                self.items[current], self.items[parent] = self.items[parent], self.items[current]
            current = parent
            parent = parent // 2

    def insert(self, item):
        self.items.append(item)
        self._percolate_up()

    def _percolate_down(self, current):
        left_child, right_child = current * 2, current * 2 + 1
        smaller = current

        if left_child <= len(self) and self.items[smaller] > self.items[left_child]:
            smaller = left_child
        if right_child <= len(self) and self.items[smaller] > self.items[right_child]:
            smaller = right_child

        if smaller != current:
            self.items[current], self.items[smaller] = self.items[smaller], self.items[current]
            self._percolate_down(smaller)

    def extract(self):
        min_item = self.items[1]
        self.items[1] = self.items[len(self)]
        self.items.pop()
        self._percolate_down(1)
        return min_item
```

<br />

<br />

#### Python: `heapq`

<br />

- Python의 heapq 모듈은 최소 힙만 지원한다.
  - 최대 힙으로 사용하고 싶다면, 저장하려는 값을 음수로 변환해서 저장하면 된다.

<br />

```python
import heapq

nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4
heap = list()

# push
for num in nums:
	heapq.heappush(heap, num)

# pop
heapq.heappop(heap)

# 기존 리스트를 min heap으로 재구성
heapq.heapify(nums)

# k번째로 큰 수
heapq.nlargest(k, nums)[-1]  # [6, 5, 5, 4]

# k번째로 작은 수
heapq.nsmallest(k, nums)[-1]  # [1, 2, 2, 3]
```

<br />

<br />

*End*