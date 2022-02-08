package kata

func RepeatStr(repetitions int, value string) string {
  s := ""
  for i:=0; i<repetitions; i = i + 1 {
     s = s + value
  }
  return s
}
