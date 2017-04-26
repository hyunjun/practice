package main

import (
  "fmt"
  "regexp"
)

func clean_url(cand string) string {
  r, _ := regexp.Compile("^((http[s]?|ftp)://)?(www\\.)?(?P<body>[a-z]+\\.[a-z]+)$")
  if r.MatchString(cand)  {
    r2 := r.FindAllStringSubmatch(cand, -1)
    return  r2[0][len(r2[0]) - 1]
  }
  return ""
}

func main() {
  //  true cases
  true_keys := []string { "viki.com", "http://viki.com", "https://viki.com", "ftp://viki.com", "www.viki.com", "http://www.viki.com", "https://www.viki.com", "ftp://www.viki.com" }
  for _, k := range true_keys {
    fmt.Println(clean_url(k))
  }

  //  false cases
  false_keys := []string { "viki.", "http:/viki.com", "https//viki.com", "ftp:///viki.com", "www,viki.com", "htt://www.viki.com", "https://ww.viki.com", "tp://www.viki.com" }
  for _, k := range false_keys {
    fmt.Println(clean_url(k)) //  all empty string
  }
}
