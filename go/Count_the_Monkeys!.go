package kata

func monkeyCount(n int) []int {
   // Your code here, happy coding!
   j := []int{}
   for i:=1; i <= n; i+=1{
     j = append(j, int(i))
   }
  return j
   
}
