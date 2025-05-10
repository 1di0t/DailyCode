from collections import Counter

def solution(tickets):
    answer = []
    tickets.sort(key=lambda x: (x[0], x[1]))
    tickets_dict = {}
    for ticket in tickets:
        if ticket[0] not in tickets_dict:
            tickets_dict[ticket[0]] = []
        tickets_dict[ticket[0]].append(ticket[1])
    
    def dfs(start, path):
        if len(path) == len(tickets) + 1:
            return path
        if start not in tickets_dict:
            return None
        for i in range(len(tickets_dict[start])):
            next_city = tickets_dict[start][i]
            tickets_dict[start].pop(i)
            path.append(next_city)
            result = dfs(next_city, path)
            if result:
                return result
            path.pop()
            tickets_dict[start].insert(i, next_city)
        return None
    
    return dfs("ICN", ["ICN"])
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))