class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        result=1
        for i in range(k):
            if tickets[i] <= tickets[k]:
                result+=tickets[i]
            else:
                result+=tickets[k]
        for j in range(k,len(tickets)):
            if tickets[j] < tickets[k]:
                result+=tickets[j]
            elif tickets[j] == tickets[k]:
                result +=tickets[j]-1
            else:
                result +=tickets[k]-1
        return result




