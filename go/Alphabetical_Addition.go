package kata
import (
  "strings"
)
func AddLetters(letters []rune) rune {
    // your code here
    q := "abcdefghijklmnopqrstuvwxyz"
    a := 0
    if len(letters) == 0{
      return 'z'
    }else{
      for _, x := range letters{
        x_ := string(x)
        i  := strings.Index(q, x_)
        a += i+1
        
      }
      if a % 26 != 0{
        return rune(q[(a%26)-1])
      }else {
        return 'z'
      }
    }
    
}
