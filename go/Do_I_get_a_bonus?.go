package kata

import (
  "strconv"
)

func BonusTime(salary int, bonus bool) string {
  // Your code here
  if bonus{
    return "\u00A3" + strconv.Itoa(salary * 10)
  }else{
    return "\u00A3" + strconv.Itoa(salary)
  }
}
