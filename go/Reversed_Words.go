package kata

import (
  "strings"
)

func ReverseWords(str string) string {
  s := strings.Split(str, " ")
  l := len(s)
  w := ""
  for i:=l-1; i>=-0; i=i-1{
    
    w += s[i]+" "
  } 
  return w[:len(w)-1]
}
