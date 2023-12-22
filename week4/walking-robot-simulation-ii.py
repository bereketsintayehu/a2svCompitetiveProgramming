class Robot:

    def __init__(self, width: int, height: int):
        self.w = width
        self.h = height
        self.x = 0
        self.y = 0
        self.direction = [
            'East',
            'North',
            'West',
            'South'
        ]
        self.dir = [
            (1, 0),
            (0, 1),
            (-1, 0),
            (0, -1)
        ]
        self.cur = 0
        self.f = (width + height - 2) * 2
    
    def bound(self, x, y):
        return 0 <= x < self.w and 0 <= y < self.h

    def step(self, num: int) -> None:
        num %= self.f

        if num == 0:
            if self.x == self.w - 1 and self.y == 0:
                self.cur = 0
            elif self.x == self.w - 1 and self.y == self.h - 1:
                self.cur = 1
            elif self.x == 0 and self.y == self.h - 1:
                self.cur = 2
            elif self.x == 0 and self.y == 0:
                self.cur = 3

        while num:
            if not self.bound(self.x + self.dir[self.cur][0], self.y + self.dir[self.cur][1]):
                self.cur = (self.cur + 1) % 4
            self.x += self.dir[self.cur][0]
            self.y += self.dir[self.cur][1]
            num -= 1

    def getPos(self) -> List[int]:
        return [self.x, self.y]

    def getDir(self) -> str:
        return self.direction[self.cur]


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()