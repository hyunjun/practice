package main

import (
  "encoding/json"
  "fmt"
  "io/ioutil"
  "os"
)

func main() {
  m := make(map[string]string)

  m["http://a.b.c"] = "http://a.b.c"
  m["http://veryvery.longlong.url"] = "http://short.url"

  fmt.Println(len(m))
  fmt.Println(m)

  fmt.Println("test")
  keys := []string { "not.existing.key", "http://a.b.c", "http://veryvery.longlong.url" }
  for _, k := range keys {
    v, has_key := m[k]
    if has_key  {
      fmt.Println(k, v)
    } else  {
      fmt.Println(k, has_key)
    }
  }

  jsonString, err := json.Marshal(m)
  fmt.Println(m)
  fmt.Println(jsonString)
  fmt.Println(err)

  err = ioutil.WriteFile("urls.json", jsonString, 0644)

  url_file, e := ioutil.ReadFile("urls.json")
  if e != nil {
    fmt.Printf("File error: %v\n", e)
    os.Exit(1)
  }

  var m2 map[string]string
  //err2 := json.Unmarshal([]byte(jsonString), &m2)
  err2 := json.Unmarshal(url_file, &m2)
  fmt.Println(m2)
  fmt.Println(err2)

  for _, k := range keys  {
    fmt.Println(k, m[k] == m2[k])
  }
}
