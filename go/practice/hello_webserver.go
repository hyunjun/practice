package main

import (
  "encoding/json"
  "fmt"
  "net/http"
  "io/ioutil"
)

type url_struct struct  {
  Url string
}

func get_url(w http.ResponseWriter, req *http.Request) url_struct  {
  body, err := ioutil.ReadAll(req.Body)
  if err != nil {
    panic(err)
  }
  fmt.Fprintln(w, string(body))
  var url_t url_struct
  err = json.Unmarshal(body, &url_t)
  if err != nil {
    panic(err)
  }
  return url_t
}

func main() {
  http.HandleFunc("/shorten", func(w http.ResponseWriter, r *http.Request) {
    url_t := get_url(w, r)
    fmt.Fprintln(w, url_t.Url)
    fmt.Fprintln(w, "welcome to shorten function!")
  })
  http.HandleFunc("/original", func(w http.ResponseWriter, r *http.Request) {
    url_t := get_url(w, r)
    fmt.Fprintln(w, url_t.Url)
    fmt.Fprintln(w, "welcome to original function!")
  })

  http.ListenAndServe(":8889", nil)
}
