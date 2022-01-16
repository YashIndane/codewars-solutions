package kata
import (
  "strings"
)
func solution(str, ending string) bool {
  // Your code here!
  return strings.HasSuffix(str, ending)
}
