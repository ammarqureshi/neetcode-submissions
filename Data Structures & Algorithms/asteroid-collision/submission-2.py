class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for curr_asteroid in asteroids:
            while stack and stack[-1] > 0 and curr_asteroid < 0:
                if stack[-1] < abs(curr_asteroid):
                    stack.pop()
                    # No break: current asteroid survived, so check again.

                elif stack[-1] == abs(curr_asteroid):
                    stack.pop()
                    break  # Both exploded.

                else:
                    break  # Stack top is larger, so current exploded.

            else:
                stack.append(curr_asteroid)

        return stack