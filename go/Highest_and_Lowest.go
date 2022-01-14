package kata

import (
  "strings"
  "strconv"
)
func HighAndLow(in string) string {
  // Code here or
  w := strings.Split(in, " ")
  max := -999999
  min := 999999
  for _, n := range w{
    num, _ := strconv.Atoi(string(n))
    if num<min{
      min = num
    }
    if num>max{
      max = num
    }
  }
  return strconv.Itoa(max) + " " + strconv.Itoa(min)
  
}
