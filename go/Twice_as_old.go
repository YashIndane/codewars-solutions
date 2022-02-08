package kata

//import "math"

func TwiceAsOld(dadYearsOld, sonYearsOld int) int { 
  // Implement me
  w := dadYearsOld - 2*sonYearsOld
  if w < 0{
    return -w
  }else{
    return w
  }
}
