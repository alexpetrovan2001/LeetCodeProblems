from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Nice solution with 73% time and 34% memory - can have improvements in the future
        no_cars = len(position)
        if no_cars == 1:
            return 1
        speed_pos_pairs = []
        for i in range(no_cars):
            speed_pos_pairs.append((position[i], speed[i]))

        speed_pos_pairs.sort(key=lambda x: x[0], reverse=True)

        last_car_stack = []

        fleets = 0

        for pair in speed_pos_pairs:
            # pair[0] = pos, pair[1] = speed
            time = (target - pair[0])/pair[1]

            if not last_car_stack:
                last_car_stack.append(pair)
                fleets += 1
            else:
                last_car = last_car_stack[-1]
                last_time = (target - last_car[0]) / last_car[1]
                if time > last_time:
                    fleets += 1
                    last_car_stack.append(pair)

        return fleets




sol = Solution()
target = 100
pos = [0,2,4]
speed = [4,2,1]
print(sol.carFleet(target, pos, speed))