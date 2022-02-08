package kata

func GetSize(w,h,d int) [2]int {
    // your code here
  v := w * h * d
  a := 2*(w*h + h*d + d*w)
  return [2]int{a, v}
}
