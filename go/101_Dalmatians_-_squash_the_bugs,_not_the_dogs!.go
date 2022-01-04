package kata

func HowManyDalmatians(number int) string{
  
  dogs := []string{"Hardly any", "More than a handful!", "Woah that's a lot of dogs!", "101 DALMATIONS!!!"}
  //w := ""
  if number <= 10 { 
    return dogs[0] 
  }else if number <= 50 && number > 10 { 
    return dogs[1] 
  }else if number <= 100 && number > 50 { 
    return dogs[2] 
  }else{
    return dogs[3]
  }
  //return w
}
