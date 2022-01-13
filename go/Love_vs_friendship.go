package kata
import (
  "strings"
)
func WordsToMarks(s string) int {
    // your code here
    z := "abcdefghijklmnopqrstuvwxyz"
    w := 0
    for _, a := range s{
      w += strings.Index(z, string(a))
      w += 1
    }
  return w
}
