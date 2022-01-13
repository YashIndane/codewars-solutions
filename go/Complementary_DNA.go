package kata

func DNAStrand(dna string) string {
  s := ""
  for _, x := range dna{
    q := string(x)
    if q == "A"{
      s += "T"
    }else if q == "T"{
      s += "A"
    }else if q == "C"{
      s += "G"
    }else if q == "G"{
      s += "C"
    }
  }
  return s
}
