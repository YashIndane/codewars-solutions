package kata
import (
  "strconv"
)
func DigitalRoot(n int) int {
  q := n
 // e := strings.Itoa(q)
  
  for i:=0; i<=n; i+=1{
    s := strconv.Itoa(q)
    if len(s) == 1{
      b, _ := strconv.Atoi(s)
      return b
    }else{
      q = 0
    for _, m := range s{
      //q = 0
      q_, _ := strconv.Atoi(string(m))
      q += q_
    }
      }
    
    
  }
  return q
}
