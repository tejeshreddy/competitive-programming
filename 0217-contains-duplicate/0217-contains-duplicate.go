func containsDuplicate(nums []int) bool {
    
    seen := make(map[int]bool)
    
    for _, item := range nums {
        if seen[item] == true {
            return true
        } else {
            seen[item] = true
        }
    }
    return false
    
}