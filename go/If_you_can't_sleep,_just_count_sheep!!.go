package kata

import (
  "strconv"
)


func countSheep(num int) string {
  // Your code here!
  s :=  ""
  for i:=0; i<num; i=i+1{
    s = s + strconv.Itoa(i+1) + " sheep..."
  }
  return s
  
}
