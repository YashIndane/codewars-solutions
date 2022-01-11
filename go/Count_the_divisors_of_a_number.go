package kata
import (
  "math"
)
func Divisors(n int)int{
  //Put your code here
  limit := int(math.Sqrt(float64(n)))
  //w := 0
  q := []int{}
  for i:=1; i<=limit+1; i=i+1{
    if n%i == 0{
      flag1 := true
      for _, x := range q{
        if x == i{
          flag1 = false
          break
        }
      }
      if flag1{
        q = append(q, i)
        //w += 1
      }
      flag2 := true
      for _, y := range q{
        if y == n/i{
          flag2 = false
          break
        }
      }
      if flag2{
        q = append(q, n/i)
      }
      
    }
  }
  return len(q)
  
  
}
