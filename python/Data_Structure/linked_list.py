class Node :

    def __init__(self, data) :
        self.data = data
        self.next = None        # 다음 노드를 가리키는 변수


head = Node(1)                  # 첫 번째 노드의 값을 가리키는 것을 head라고 함
head.next = Node(2)
head.next.next = Node(3)


node = head
while(node):    # node.next의 값이 None이 되기 전까지 반복
    print(node.data, end = " ")

    if(node.next == None):      # Linked List 끝에 값을 추가
        node.next = Node(4)
        break

    node = node.next
print()


# Linked List의 처음에 값을 추가하는 방법
# 1. 추가할 노드를 생성한다.
# 2. 추가할 노드의 next가 head를 가리키게 한다.
# 3. head를 추가한 노드로 옮긴다.

node = Node(0)      # 1번
node.next = head    # 2번 
head = node         # 3번
node = head

while(node):    # node.next의 값이 None이 되기 전까지 반복
    print(node.data, end = " ")
    node = node.next
print()