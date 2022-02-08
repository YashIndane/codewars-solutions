package kata

func MoveZeros(arr []int) []int {
  // TODO: Program me
  w := []int{}
  f := 0
  for _, i := range arr{
    if i != 0{
      w = append(w, i)
    }else{
      f += 1
    }
  }
  for p:=0; p<f; p=p+1{
    w = append(w, 0)
  }
  return w
}
