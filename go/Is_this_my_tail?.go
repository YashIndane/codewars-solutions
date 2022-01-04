package kata
import (
  "strings"
)
func CorrectTail(body string, tail rune) bool {
  if strings.HasSuffix(body, string(tail)){
    return true
  }else{
  return false
  }
}
