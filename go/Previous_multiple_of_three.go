package kata

import (
  "strconv"
)
func PrevMultOfThree(n int) interface{} {
  // write your code here
  // your function should return an int or a nil
  if n%3 == 0{
    return n
  }else{
  
    d := strconv.Itoa(n)
    for i:=len(d)-1; i>=0; i=i-1{
      num, _ := strconv.Atoi(d[:i])
      if num%3 == 0 && len(d[:i]) != 0{
        return num
      }
    }
    return nil
    
  }
  
  
  
  
}
