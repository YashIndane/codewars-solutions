package kata

func ReverseSeq(n int) []int {
  w := []int{}
  for k:=n; k>0; k=k-1{
    w = append(w, k)
  }
  return w
}
