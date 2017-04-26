package main

import (
  "fmt"
  "hash/fnv"
)

func hash(s string) uint32  {
  h := fnv.New32a()
  h.Write([]byte(s))
  return h.Sum32()
}

func main() {
  keys := []string { "viki.com", "http://viki.com", "https://viki.com", "http://www.viki.com", "https://www.viki.com", "http:/www.viki.com", "viki.com" }
  for _, k := range keys {
    fmt.Println(k, fmt.Sprint(hash(k)))
  }
}
