package kata

func IsDivisible(n, x, y int) bool {
    // your code here
   if n%x == 0 && n%y == 0{
     return true
   }else{
     return false
   }
}
