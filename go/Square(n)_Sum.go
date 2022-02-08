package kata

func SquareSum(numbers []int) int {
    // your code here
    p := 0
    for _, i := range numbers{
      p += int(i) * int(i)
    }
    return p
}
