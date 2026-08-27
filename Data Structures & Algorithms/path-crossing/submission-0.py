class Solution:
    def isPathCrossing(self, path: str) -> bool:
        curr = set()
        x,y = 0,0
        curr.add((x,y))
        for d in path:
            if d == 'N':
                x += 1
            if d == 'S':
                x -= 1
            if d == 'E':
                y += 1
            if d == 'W':
                y -= 1
            if (x,y) in curr :
                return True
            curr.add((x,y))
        return False

        