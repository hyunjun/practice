(ns flipping-bits.core
  (:gen-class))

(defn -main
  "I don't do a whole lot ... yet."
  [& args]
  (def n (Integer/parseInt (read-line)))

  (loop [i 0]
    (when (< i n)
      (println (- 4294967295 (Integer/parseInt (read-line))))
      (recur (inc i))
      )))
