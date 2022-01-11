package kata

func multipleOfIndex (ints []int) []int {
  // good luck
  w := []int{}
  for i:=0; i<len(ints); i=i+1{
    if i!=0{
      ele := int(ints[i])
      if ele%i == 0{
        w = append(w, ele)
      }
    }
  }
  return w
  
}
