package kata

func century(year int) int {
 // Finish this :)
  if year < 100{
    return 1
  }else{
    if year%100 == 0{
      return year/100
    }else{
      rem := year%100
      return ((year-rem)/100)+1
    }
  }
  
 
}
