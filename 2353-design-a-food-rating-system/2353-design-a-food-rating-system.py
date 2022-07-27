from sortedcontainers import SortedList

class FoodRatings:


    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.hmap_food = {}
        self.hmap_cuisine = collections.defaultdict(SortedList)
        
        for f, c, r in zip(foods, cuisines, ratings):
            self.hmap_food[f] = (c, r)
            self.hmap_cuisine[c].add((-r, f))

    def changeRating(self, food: str, newRating: int) -> None:
        o_c, o_r = self.hmap_food[food]
        self.hmap_cuisine[o_c].discard((-o_r, food))
        self.hmap_cuisine[o_c].add((-newRating, food))
        self.hmap_food[food] = (o_c, newRating)
        

    def highestRated(self, cuisine: str) -> str:
        return self.hmap_cuisine[cuisine][0][1]
        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)