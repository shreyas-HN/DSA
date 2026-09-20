class Node:
    def __init__(self,string):
        self.string=string
        self.next=None
        self.prev=None
class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage=Node(homepage)
        self.current=self.homepage

    def visit(self, url: str) -> None:
        new_node=Node(url)
        self.current.next=new_node
        new_node.prev=self.current
        self.current=new_node

    def back(self, steps: int) -> str:
        now=self.current
        while now.prev and steps>0:
            now=now.prev
            steps-=1
        self.current=now
        return now.string

        

    def forward(self, steps: int) -> str:
        let=self.current
        while let.next and steps>0:
            let=let.next
            steps-=1
        self.current=let
        return let.string
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)