
class Robot:
   def move(self):
       """
       Returns true if the cell in front is open and robot moves into the cell.
       Returns false if the cell in front is blocked and robot stays in the current cell.
       :rtype bool
       """
       pass

   def turnLeft(self):
       """
       Robot will stay in the same cell after calling turnLeft/turnRight.
       Each turn will be 90 degrees.
       :rtype void
       """
       pass

   def turnRight(self):
       """
       Robot will stay in the same cell after calling turnLeft/turnRight.
       Each turn will be 90 degrees.
       :rtype void
       """
       pass

   def clean(self):
       """
       Clean the current cell.
       :rtype void
       """
       pass

#O(n*m) space:O(n*m)
class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        directions = [(-1,0),(0,1),(1,0),(0,-1)] #top,right,bot,left
        visited=set()
        def dfs(robot,d,r,c):
            nonlocal visited,directions
            robot.clean()
            visited.add((r,c))
            for i in range(len(directions)):
                new_dir = (d+i)%len(directions)
                row = r+directions[new_dir][0]
                col = c+directions[new_dir][1]
                if (row,col) in visited or not robot.move():
                    robot.turnRight()
                    continue
                dfs(robot,new_dir,row,col)
                robot.turnRight()
            #backtrack
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()
        dfs(robot,0,0,0)

#varinet: mouse needs to find cheese, return true of cheese found, move(direction) moves to invalid spaces so need to backtrack, hasCheese()
#O(m*n) space:(m*n)
class Mouse:
    def move(direction):
        pass
    def hasCheese():
        pass

class Solution:
    def hasCheese(self, mouse):
        visited = set()
        direction = [(-1,0),(0,1),(1,0),(0,-1)]
        def dfs(r,c):
            nonlocal mouse,visited
            if (mouse.hasCheese()):
                return True
            visited.add((r,c))
            for i in range(4):
                row = r + direction[i][0]
                col = c + direction[i][1]
                if (row,col) in visited:
                    continue
                if not mouse.move(i):
                    mouse.move((i+2)%4)
                    continue
                if dfs(row,col):
                    return True
                mouse.move((i+2)%4)
        return dfs(0,0)