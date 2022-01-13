package kata

func QuarterOf(month int) int {
  // your code here
  if 1<=month && month<=3{
    return 1
  }else if 4<=month && month<=6{
    return 2
  }else if 7<=month && month<=9{
    return 3
  }else {
    return 4
  }
  
}
