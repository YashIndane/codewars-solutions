package kata
import (
  "strings"
)
func solve(slice []string) []int {
  // Your code here and happy coding!
  s := "abcdefghijklmnopqrstuvwxyz"
  sl := []int{}
  for _, x := range slice{
    c := 0
    st := string(x)
    for i:=0; i<len(st); i=i+1{
      if strings.Index(s, strings.ToLower(string(st[i]))) == i{
        c += 1
      }
    }
    sl = append(sl, c)
  }
  return sl
}
