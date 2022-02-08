package kata

import (
  "strconv"
  "strings"
)

func PrinterError(s string) string {
  deno := strconv.Itoa(len(s))
  st := "abcdefghijklm"
  n := 0
  for _, k := range s{
    if strings.Contains(st, string(k)){
      
    }else{
      n += 1
    }
    
  }
  return strconv.Itoa(n)+"/"+deno
}
