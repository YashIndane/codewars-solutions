package kata
import (
  "strings"
)
func solve(str string) int {
  // Your code here, happy coding!
  all := "abcdefghijklmnopqrstuvwxyz"
  vow := "aeiou"
  max := 0
  temp := 0
  for _, x := range str{
    x_ := string(x)
    if !strings.Contains(vow, x_){
      temp += strings.Index(all, x_)+1
    }else{
      if temp > max{
        max = temp
      }
      temp = 0
    }
  }
  if temp > max{
    return temp
  }else{
    return max
  }
  
  
}
