package kata
import (
  "strconv"
)
func Points(games []string) int {
  // your code here!
  p := 0
  for _, x := range games{
    x_ := string(x)
    a, _ := strconv.Atoi(string(x_[0]))
    b, _ := strconv.Atoi(string(x_[2]))
    
    if a>b {
      p += 3
    }else if a == b{
      p += 1
    }
  }
  return p
  
}
