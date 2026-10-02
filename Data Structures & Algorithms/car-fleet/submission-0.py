class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = [(p,s) for p, s in zip(position, speed)]
        cars.sort(reverse = True)

        for pos, spd in cars:
            currtime = (target - pos) / spd
            if not stack or currtime > stack[-1]:
                stack.append(currtime)
        return len(stack)