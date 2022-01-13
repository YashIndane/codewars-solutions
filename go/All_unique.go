package kata
import (
  "strings"
)
func HasUniqueChar (str string) bool {
  for i:=0; i<len(str); i=i+1{
    if strings.Contains(str[i+1:], string(str[i])){
      return false
    }
  }
  return true
}_
