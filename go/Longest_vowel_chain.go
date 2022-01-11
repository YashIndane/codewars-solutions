package kata

import (
  "strings"
)

func Solve(s string) int {
    w := 0
    a := "aeiou"
    max := 0
    for _, st := range s{
      x := string(st)
      if strings.Contains(a, x){
        w += 1
      }else{
        if w > max{
          max = w
          w = 0
        }else{
          w = 0
        }
      }
    }
  return max
}
