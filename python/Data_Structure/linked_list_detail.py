class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None


class LinkedList :
    def __init__(self) :
        self.head = None
        self.length = 0

    def __len__(self) :         # 특수 메서드
        return self.length
    
    def __str__(self) :         # __str__ 특수 메서드는 object를 print()했을 경우 실행 됨
        if(self.head is None) :
            return "Linked list is empty!"
        res = "Head"
        node = self.head

        while(node is not None) :
            res += " → " + str(node.data)
            node = node.next
        return res
    
    def __contains__(self, target) :
        if(self.head is None) :
            return False
        
        node = self.head
        while(node is not None) :
            if(node.data == target) :
                return True
            node = node.next

        return False
    
    def appendleft(self, data) :
        if(self.head is None) :         # Linked list에 데이터가 없는 경우
            self.head = Node(data)
        else :                          # Linked list에 데이터가 있는 경우
            node = Node(data)           # 새로운 노드 생성
            node.next = self.head       # 새로 추가된 노드의 next가 head를 가르킴
            self.head = node            # head를 이동
        
        self.length += 1                # 길이 증가

    def append(self, data) :
        if(self.head is None) :
            self.head = Node(data)
        else :
            node = self.head                    # Linked list의 head를 가지고 옴
            while(node.next is not None) :      # append()는 제일 뒤에 추가하는 것이기 떄문에 node.nex가 None이 될때 까지 반복, node가 Linked list의 제일 뒤 값으로 이동
                node = node.next
            node.next = Node(data)              # 새로운 노드 추가

        self.length += 1


    def popleft(self) :
        if(self.head is None) :
            return None
        node = self.head                        # 임시 노드 생성 후, head를 저장
        self.head = self.head.next              # 현재 head를 다음 노드의 헤드로 이동
        self.length -= 1
        return node.data


    def pop(self) :
        if(self.head is None) :
            return None
        node = self.head                        # 임시 노드 생성 후, head를 저장
        while(node.next is not None) :
            prev = node
            node = node.next
            
        if(node == self.head) :                 # Linked list가 비었을 경우(노드가 없을 때)
            self.head = None
        else :
            prev.next = None
        self.length -= 1
        return node.data

    
    def remove(self, target) :
        node = self.head

        while((node is not None) and (node.data != target)) :
            prev = node
            node = node.next

        if(node is None) :          # Linked list가 없는 경우
            return False
        
        if(node == self.head) :     # 찾는 값이 제일 첫 번째 값인 경우
            self.head = self.head.next
        else:
            prev.next = node.next

        self.length -= 1
        return True

    
    def insert(self, i, data) :
        if(i <= 0) :
            self.appendleft(data)
        elif(i >= self.length) :
            self.append(data)
        else :
            node = self.head
            for _ in range(i - 1) :     # i - 1을 해야 위치 이전까지 이동함, 그 이유는 node에는 node.next가 저장되기 때문
                node = node.next
            new_node = Node(data)
            new_node.next = node.next
            node.next = new_node
            self.length += 1



if __name__ == "__main__" :             # 프로그램을 직접 실행 했을 경우 여기 부터 실행
    import random

    data = list(range(15, 20))
    random.shuffle(data)

    my_list = LinkedList()
    for i in data :
        my_list.append(i)
    print(my_list)
    print()

    # for _ in range(4) :
    #     i = random.randint(5, 25)
    #     if(i in my_list) :
    #         print("%d는(은) 연결 리스트에 있습니다." % i)
    #     else :
    #         print("%d는(은) 연결 리스트에 없습니다." % i)
    # print()

    # for _ in range(len(my_list)) :
    #     print("%s를(을) 꺼낸 후: 길이 = %s, %s" % (my_list.pop(), len(my_list), my_list))
    # print("연결 리스트가 비었을 때 꺼낸 값은 %s" % my_list.pop())


    # for _ in range(10) :
    #     i = random.randint(10, 18)
    #     if(my_list.remove(i)) :
    #         print("%d를(을) 삭제했습니다." % i)
    #         print("Linked list의 길이 %d, %s" % (len(my_list), my_list))
    #     else :
    #         print("%d는(은) 없습니다." % i)


    # for _ in range(5) :
    #     i = random.randrange(10)
    #     data = random.randint(10, 20)
    #     my_list.insert(i, data)
    #     print("%d를(을) 연결 리스트의 %d인덱스에 삽입했습니다." % (data, i))
    #     print("연결 리스트의 길이 = %s, %s\n" % (len(my_list), my_list))