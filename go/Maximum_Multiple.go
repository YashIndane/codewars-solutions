package kata

func MaxMultiple(d, b int) int {
    // your code here
    p := 0
    for k := b; k>0; k = k - 1{
      if k%d == 0{
        p = k
        break
      }
    }
  return p
  
}
