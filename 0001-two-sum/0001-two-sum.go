import "fmt"

func twoSum(nums []int, target int) []int {
    hmap := make(map[int]int)

    for index, value := range nums {

        idx, exists := hmap[target - value]
        if exists {
            return []int{idx, index}
        }
        hmap[value] = index
    }
    return nil
}