package kata
import (
  "strconv"
)
func TestIt(a, b int) int {
  x := 0
  y := 0
  c := strconv.Itoa(a)
  for _, q := range c{
    x_, _ := strconv.Atoi(string(q))
    x += x_
  }
  
  d := strconv.Itoa(b)
  for _, q := range d{
    x_, _ := strconv.Atoi(string(q))
    y += x_
  }
  
  return y * x
  
  
}
