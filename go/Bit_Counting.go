package kata

import "strconv"

func CountBits(a uint) int {
    n := int64(a)
    w := strconv.FormatInt(n, 2)
    
    e := 0
    for _, i := range w{
      if "1" == string(i){
        e += 1
      }
    }
  
    return e
}
