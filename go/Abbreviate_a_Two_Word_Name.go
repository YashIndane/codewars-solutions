package kata

import (
  "strings"
)

func AbbrevName(name string) string{
  //your code here
  s := strings.Split(name, " ")
  return strings.ToUpper(string(s[0][0]))+"."+strings.ToUpper(string(s[1][0]))
  
}
