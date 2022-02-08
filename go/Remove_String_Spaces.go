package kata

func NoSpace(word string) string {
  p := ""
  for _, x := range word{
    if string(x) == " "{
      
    }else{
      p += string(x)
    }
  }
  return p

}
