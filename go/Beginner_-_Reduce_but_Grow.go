package kata

func Grow(arr []int) int{
   p := 1
   for _, i := range arr{
     p *= int(i)
   }
  return p
}
