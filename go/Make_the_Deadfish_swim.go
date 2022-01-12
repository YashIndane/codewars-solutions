package kata

func Parse(data string) []int{
  //TODO: write your code here
  num := 0
  a := []int{}
  for _, x := range data{
    s := string(x)
    if s == "i"{
      num += 1
    }else if s == "d"{
      num -= 1
    }else if s == "s"{
      num = num * num
    }else if s == "o"{
      a = append(a, num)
    }
  }
  return a
  
}
