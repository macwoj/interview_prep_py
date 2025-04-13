
from collections import defaultdict
from typing import List


def accountsMerge(accounts: List[List[str]]) -> List[List[str]]:
    adj = defaultdict(list)
    for acc in accounts:
        email = acc[1]
        for i in range(2,len(acc)):
            adj[email].append(acc[i])
            adj[acc[i]].append(email)
    visited = set()
    def dfs(email,res):
        nonlocal adj,visited
        visited.add(email)
        res.append(email)
        for n in adj[email]:
            if n not in visited:
                dfs(n,res)
    result = []
    for acc in accounts:
        user = acc[0]
        email = acc[1]
        if email not in visited:
            res = []
            dfs(email,res)
            res = [user]+sorted(res)
            result.append(res)
    return result

# variant: input is {C1: [a b]} ...
def accountsMerge2(accounts):
    adj = defaultdict(list)
    for name,emails in accounts.items():
        email=emails[0]
        for i in range(1,len(emails)):
            adj[email].append(emails[i])
            adj[emails[i]].append(email)
    email_id = {}
    visited=set()
    result =defaultdict(list)
    def dfs(email,name):
        nonlocal email_id,visited,adj
        visited.add(email)
        email_id[email] = name
        for n in adj[email]:
            if n not in visited:
                dfs(n,name)
    for name,emails in accounts.items():
        email=emails[0]
        if email not in visited:
            result[name].append(name)
            dfs(email,name)
        else:
            id = email_id[email]
            result[id].append(name)
    return [result[k] for k in result.keys()]






accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
print(accountsMerge(accounts))

if __name__ == "__main__":
    # Happy Case
    input_data = {
        "C1": ["a", "b"],
        "C2": ["c"],
        "C3": ["b", "d"],
        "C4": ["d"],
        "C5": ["e"],
        "C6": ["c"],
        "C7": ["a"]
    }
    result = accountsMerge2(input_data)
    print(result)
    assert len(result) == 3
    assert sorted(result[0]) == sorted(["C1", "C3", "C7", "C4"])
    assert sorted(result[1]) == sorted(["C6", "C2"])
    assert sorted(result[2]) == sorted(["C5"])

    # Actual Email Strings
    input_data = {
        "ID1": ["aa@gmail.com", "bb@gmail.com"],
        "ID2": ["cc@gmail.com"],
        "ID3": ["bb@gmail.com", "dd@gmail.com"],
        "ID4": ["dd@gmail.com"],
        "ID5": ["ee@gmail.com"],
        "ID6": ["cc@gmail.com"],
        "ID7": ["aa@gmail.com"]
    }
    result = accountsMerge2(input_data)
    assert len(result) == 3
    assert sorted(result[0]) == sorted(["ID3", "ID7", "ID4", "ID1"])
    assert sorted(result[1]) == sorted(["ID2", "ID6"])
    assert sorted(result[2]) == sorted(["ID5"])

    # No Edges
    input_data = {
        "C1": ["a", "b"],
        "C2": ["c"],
        "C3": ["d", "e", "f"],
        "C4": ["g"],
        "C5": ["h"],
        "C6": ["i"],
        "C7": ["j", "k", "l", "m", "n"]
    }
    result = accountsMerge2(input_data)
    assert len(result) == 7
    assert sorted(result[0]) == sorted(["C1"])
    assert sorted(result[1]) == sorted(["C2"])
    assert sorted(result[2]) == sorted(["C3"])
    assert sorted(result[3]) == sorted(["C4"])
    assert sorted(result[4]) == sorted(["C5"])
    assert sorted(result[5]) == sorted(["C6"])
    assert sorted(result[6]) == sorted(["C7"])

    # One Connected Component Via One Email
    input_data = {
        "C1": ["a", "b"],
        "C2": ["a"],
        "C3": ["d", "a", "f"],
        "C4": ["a"],
        "C5": ["a"],
        "C6": ["a"],
        "C7": ["j", "a", "l", "m", "n"]
    }
    result = accountsMerge2(input_data)
    assert len(result) == 1
    assert sorted(result[0]) == sorted(["C6", "C1", "C5", "C3", "C7", "C2", "C4"])

    # One Connected Component Via Two Emails
    input_data = {
        "C1": ["a", "b"],
        "C2": ["a"],
        "C3": ["d", "a", "f"],
        "C4": ["a", "x", "y", "z"],
        "C5": ["a"],
        "C6": ["a", "o", "p", "b"],
        "C7": ["j", "a", "l", "m", "n"]
    }
    result = accountsMerge2(input_data)
    assert len(result) == 1
    assert sorted(result[0]) == sorted(["C6", "C1", "C5", "C3", "C7", "C2", "C4"])

    # One Id One Email
    input_data = {
        "C1": ["a"]
    }
    result = accountsMerge2(input_data)
    assert len(result) == 1
    assert sorted(result[0]) == sorted(["C1"])

    # One Id Multiple Emails
    input_data = {
        "C1": ["a@gmail.com", "b@gmail.com", "c@gmail.com"]
    }
    result = accountsMerge2(input_data)
    assert len(result) == 1
    assert sorted(result[0]) == sorted(["C1"])

    # Separate Connected Components
    input_data = {
        "C1": ["a", "b", "c", "d"],
        "C2": ["q", "r", "s", "t"],
        "C10": ["x", "y", "z"]
    }
    result = accountsMerge2(input_data)
    assert len(result) == 3
    assert sorted(result[0]) == sorted(["C1"])
    assert sorted(result[1]) == sorted(["C2"])
    assert sorted(result[2]) == sorted(["C10"])