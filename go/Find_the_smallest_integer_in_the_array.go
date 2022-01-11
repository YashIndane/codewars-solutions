package kata

func SmallestIntegerFinder(numbers []int) int {
  x := 9999999
  for _, v := range numbers{
    v_ := int(v)
    if v_ < x{
      x = v_
    }
  }
  return x
}
