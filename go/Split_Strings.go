package kata

func Solution(str string) []string {
  temp := ""
  w := []string{}
  for i:=0; i<len(str); i=i+1{
    
  
    
    if len(temp)<2{
      temp += string(str[i])
      
    }else{
      w = append(w, temp)
      temp = ""
      temp += string(str[i])
      
    }
  }
  if len(str)%2 == 0{
    temp = str[len(str)-2:len(str)]
    w = append(w, temp)
  }else{
    temp = str[len(str)-1:len(str)] + "_"
    w = append(w, temp)
  }
   
  return w

}
