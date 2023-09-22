# 제약조건은 딱히 뭐가없음
# 선형자료구조로 삽입이용이한 linked list필요
# 시간복잡도는 worst case에서도 ㄱㅊ
# doubly linked list필요
class ListNode(object):
    def __init__ (self, val=0, next=None, prev=None):
        self.val =val
        self.next = next
        self.prev = prev
class BrowserHistory(object):
    
    def __init__(self, homepage):
        self.head = self.current = ListNode(val = homepage);
    def visit(self, url):
        self.current.next = ListNode(val=url, prev=self.current);
        self.current = self.current.next
        return None
    def back(self, steps):
        while sgteps > 0 and self.current.prev != None:
             steps -=1
             self.current = self.current.prev
        return self.current.val
    def forward(self, steps):
        while steps>0 and self.current.next != None:
            steps -=1
            self.current = self.current.next
        return self.current.val
        