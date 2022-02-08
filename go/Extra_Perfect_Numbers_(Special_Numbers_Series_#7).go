package kata

func ExtraPerfect(n int) []int {
    // your code here
    p := []int{}
    for i:=1; i<=n; i+=1{
      if i%2 == 1{
        p = append(p, i)
      }
    }
  return p
}
