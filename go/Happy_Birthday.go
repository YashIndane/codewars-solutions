package kata

func WrapPresent(height, width, length int) int {
  //your code here
  
  if height <= width && height <= length{
    return 2*(height+width) + 2*(height + length) + 20
  }else if width <= height && width <= length{
    return 2*(height+width) + 2*(width + length) + 20
  }else{
    return 2*(height+length) + 2*(width + length) + 20
  }
}
