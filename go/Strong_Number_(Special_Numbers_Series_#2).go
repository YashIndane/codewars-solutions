package kata
import (
  "strconv"
)
func Strong(n int) string {
    // your code here
    q := strconv.Itoa(n)
    w := 0
    for _, v := range q{
      v_, _ := strconv.Atoi(string(v))
      p := 1
      for i:=1; i<=v_; i=i+1{
        p *= i
      }
      w += p
    }
    if w == n{
      return "STRONG!!!!"
    }else{
      return "Not Strong !!"
    }
  
}
