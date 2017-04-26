package main

import "fmt"
import "os"
//import "net"
import "net/url"

func main() {
  //s := "http://not.existing.url"
  s := "http://www.viki.com"

  _, err := url.Parse(s)
  if err == nil {
    fmt.Println("invalid url")
    panic(err)
    os.Exit(1)
  }
  fmt.Println("valid url")
}
