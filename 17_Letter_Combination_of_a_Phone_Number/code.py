def letterCombinations(digits: str):
    dic = {
        '2': "abc",
        '3': "def",
        '4': "ghi",
        '5': "jkl",
        '6': "mno",
        '7': "pqrs",
        '8': "tuv",
        '9': "wxyz",
    }
    res, collect = [], []
    def dfs(i):
        if i == len(digits):
            if collect:
                res.append(''.join(collect))
            return
        for c in dic[digits[i]]:
            collect.append(c)
            dfs(i + 1)
            collect.pop()
    dfs(0)
    return res

if __name__ == '__main__':
    
    # test cases
    tests = [
        "23",
        "",
        "2"
        ]
    
    # run tests
    for test in tests:
        print(letterCombinations(test))