package kata

func Pyramid(n int) [][]int {
    // your code here
    fin := [][]int{}
    
    if n == 0{
      return [][]int{}
    }else{
      
      for k:=0; k<n; k=k+1{
        fin = append(fin, []int{})
      }
      for i:=1; i<=n; i=i+1{
        //w := fin[i-1]
        for j:=0; j<i; j=j+1{
          fin[i-1] = append(fin[i-1], 1)
        }
      }
    }
  return fin
}
