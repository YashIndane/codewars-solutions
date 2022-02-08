package kata

func EvenOrOdd(number int) string {
  // your code here
  if number< 0{
    number = -1 * number
  }
  
  
  if number % 2 == 1{
    return "Odd"
  }else{
  return "Even"
 }
}
