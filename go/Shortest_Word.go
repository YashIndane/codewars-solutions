package kata
import (
  "strings"
)
func FindShort(s string) int {
  // your code
  c := strings.Split(s, " ")
  q := 999
  for _, w := range c{
    if len(w) < q{
      q = len(w)
    }
  }
  return q
}
