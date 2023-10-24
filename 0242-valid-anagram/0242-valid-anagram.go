import "fmt"

func isAnagram(s string, t string) bool {
    if len(s) != len(t) {
        return false
    }
    
    charCount := make(map[rune]int)
    
    for _, char := range s {
        charCount[char]++
    }
    
    for _, char := range t {
        if charCount[char] > 0 {
            charCount[char]--
        } else {
            return false
        }
    }
    
    for _, value := range charCount {
        if value != 0 {
            return false
        }
    }
    return true
    
}