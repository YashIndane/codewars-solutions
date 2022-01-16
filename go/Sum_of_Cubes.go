package kata

func SumCubes(n int) int {
  // your code here
  d := 0
  for i:=1; i<=n; i+=1{
    d += i*i*i
  }
  return d
}
