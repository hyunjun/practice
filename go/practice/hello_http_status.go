package main

import (
  "fmt"
  "net/http"
)

func get_httpstatus(s string) int {
  resp, err := http.Get(s)
  //fmt.Println(resp, err)
  if err == nil {
    defer resp.Body.Close()
    return resp.StatusCode
  }
  return 0
}

func main() {
  keys := []string { "http://viki.com", "https://viki.com", "http://www.viki.com", "https://www.viki.com", "http:/www.viki.com", "viki.com" }
  for _, k := range keys {
    fmt.Println(k, get_httpstatus(k))
  }
}
