package kata

import (
  "strings"
)

func DNAtoRNA(dna string) string {
  // your code here
  return strings.Replace(dna, "T", "U", -1)  
}
