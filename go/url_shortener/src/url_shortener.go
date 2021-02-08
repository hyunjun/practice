package main

import (
  "encoding/json"
  "fmt"
  "io/ioutil"
  "hash/fnv"
  "net/http"
  "regexp"
)

type url_struct struct  {
  Url string
}

//  This function returns two maps
//  One has original - shortened url map for /shorten
//  Another has shortened - original url map for /original
//  TODO: Using DB, this function is not necessary. The connection to DB is necessary
func get_maps(filename string) (map[string]string, map[string]string)  {
  //  read urls.json
  url_file, e := ioutil.ReadFile(filename)
  var shorten_map map[string]string
  original_map := make(map[string]string)
  if e == nil {
    //  save it as map
    //err2 := json.Unmarshal(url_file, &shorten_map)
    //fmt.Println(err2)
    json.Unmarshal(url_file, &shorten_map)
  } else  {
    //fmt.Println("no urls.json")
    shorten_map = make(map[string]string)
  }
  for k, v := range shorten_map  {
    original_map[v] = k
  }

  return shorten_map, original_map
}

//  This function returns http status code to check input string has the valid connection
func get_httpstatus(s string) int {
  resp, err := http.Get(s)
  //fmt.Println(resp, err)
  if err == nil {
    defer resp.Body.Close()
    return resp.StatusCode
  }
  return 0
}

//  This function does cleaning input url string
//  For example, http://viki.com, https://viki.com, http://www.viki.com, and https://www.viki.com will return viki.com
//  If input url string is not url pattern, return empty string
func clean_url(cand string) string {
  //  TODO: url pattern should be refined
  r, _ := regexp.Compile("^((http[s]?|ftp)://)?(www\\.)?(?P<body>[a-z]+\\.[a-z]+)$")
  if r.MatchString(cand)  {
    r2 := r.FindAllStringSubmatch(cand, -1)
    return  r2[0][len(r2[0]) - 1]
  }
  return ""
}

func get_url(w http.ResponseWriter, req *http.Request) url_struct  {
  body, err := ioutil.ReadAll(req.Body)
  if err != nil {
    panic(err)
  }
  var url_t url_struct
  err = json.Unmarshal(body, &url_t)
  if err != nil {
    panic(err)
  }
  return url_t
}

func hash(s string) uint32  {
  h := fnv.New32a()
  h.Write([]byte(s))
  return h.Sum32()
}

//  This function returns shortened url using hash function
func shorten(url string) string {
  //  TODO: what is the good way to get the shortened url? (short & unique)
  return "localhost/" + fmt.Sprint(hash(url))
}

//  This function writes map into file, to use map again when restarting server
//  TODO: Using DB, this function is not necessary
func write_file(m map[string]string, filename string) {
  jsonString, err := json.Marshal(m)
  if err != nil {
    fmt.Println(err)
  }

  err = ioutil.WriteFile(filename, jsonString, 0644)
}

func response(w http.ResponseWriter, r *http.Request, url_filename string,
              shorten_map map[string]string, original_map map[string]string) {
  /*for k, v := range shorten_map  {
    fmt.Fprintln(w, k, v, clean_url(k), clean_url(v))
  }*/

  url_t := get_url(w, r)

  if url_filename != "" {
    fmt.Fprintln(w, "check http status when /shorten")
    if 200 != get_httpstatus(url_t.Url) {
    //  if http status code is not 200, it's NOT valid url, so stop
    return
    }
  }

  cleaned_url := url_t.Url

  v, has_key := "", false
  if url_filename != "" {
    //fmt.Fprintln(w, "read shorten map")
    //  clean url not to use several keys for the same urls,
    //  such as http://www.viki.com, https://www.viki.com, http://viki.com, and https://viki.com
    cleaned_url = clean_url(url_t.Url)
    v, has_key = shorten_map[cleaned_url]
  } else  {
    //fmt.Fprintln(w, "read original map")
    v, has_key = original_map[cleaned_url]
  }

  //  /shorten, k = input url
  //    does shorten_map hold k?
  //    k does NOT exist
  //      has k valid connecting url?
  //      is k valid url?
  //      v = get_shortened_url(k)
  //      shorten_map[k] = v
  //      original_map[v] = k
  //    print v
  //  /original, k = input url
  //    does original_map hold k?
  //    print v if exists
  if has_key  {
    fmt.Fprintln(w, fmt.Sprintf("%s exists, value = %s", cleaned_url, v))
    if url_filename != "" {
      fmt.Fprintln(w, fmt.Sprintf("{\"short\": \"%s\"}", v))
    } else  {
      fmt.Fprintln(w, fmt.Sprintf("{\"original\": \"%s\"", v))
    }
  } else  {
    //fmt.Fprintln(w, fmt.Sprintf("%s does NOT exist", cleaned_url))

    //  TODO: "" means /shorten for now. what is the better way to distinguish /shorten and /original
    if url_filename != "" {
      shortened_url := shorten(cleaned_url)
      shorten_map[cleaned_url] = shortened_url
      original_map[shortened_url] = cleaned_url
      write_file(shorten_map, url_filename)
      //fmt.Fprintln(w, fmt.Sprintf("created shortened url %s for %s", shortened_url, cleaned_url))
      fmt.Fprintln(w, fmt.Sprintf("{\"short\": \"%s\"}", shortened_url))
    }
  }
    //  if requested url does not exist in the map
    //    create shortened url
    //    save it in the map
    //    write map into the file //  this is too many writing, so it needs to //    be better
    //  return the shortened url using the requested url as key
    //fmt.Fprintln(w, url_t.Url)
}

func main() {
  //  TODO:
  //    read filename from configuration file
  //    substitute file storage into DB
  url_filename := "urls.json"

  //  shorten_map holds original - shortened url map
  //  original_map holds shortened url - original map
  shorten_map, original_map := get_maps(url_filename)
  /*
  for k, v := range shorten_map  {
    fmt.Println(k, v, clean_url(k), clean_url(v))
  }
  for k, v := range original_map  {
    fmt.Println(k, v)
  }
  */

  /*
  http.HandleFunc("/shorten", func(w http.ResponseWriter, r *http.Request) {
    url_t := get_url(w, r)
    //  if requested url does not exist in the map
    //    create shortened url
    //    save it in the map
    //    write map into the file //  this is too many writing, so it needs to //    be better
    //  return the shortened url using the requested url as key
    fmt.Fprintln(w, url_t.Url)
  })
  */
  http.HandleFunc("/shorten", func(w http.ResponseWriter, r *http.Request) {
    response(w, r, url_filename, shorten_map, original_map)
  })

  //  the same as above, just using different map
  http.HandleFunc("/original", func(w http.ResponseWriter, r *http.Request) {
    //url_t := get_url(w, r)
    //fmt.Fprintln(w, url_t.Url)
    response(w, r, "", shorten_map, original_map)
  })

  http.ListenAndServe(":8889", nil)
}
