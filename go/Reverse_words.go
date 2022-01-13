package kata
import (
  "strings"
)
func ReverseWords(str string) string {
  s := strings.Split(str, " ")
  w := ""
  for _, x := range s{
    for i:=len(x)-1; i>=0; i=i-1{
      w += string(x[i])
    }
    w += " "
    
  }
  return w[:len(w)-1]
