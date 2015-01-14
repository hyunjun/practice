(ns solution.core
  (:gen-class))

(use '[clojure.string :only (split triml)])

(defn -main
  [& args]
  (def n (Integer/parseInt (read-line)))

  (loop [i 0]  
    (when (< i n)
          (def a (read-line))
          (def new (split a #"\s+"))
          (println ( + (Integer/parseInt (get new 0)) (Integer/parseInt (get new 1)) ))    
          (recur (inc i))
      )))
