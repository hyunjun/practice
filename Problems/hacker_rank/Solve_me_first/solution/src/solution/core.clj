(ns solution.core
  (:gen-class))

(defn solveMeFirst [x y]    
  (+ x y))

(defn -main
  [& args]
  (def a (read-line))
  (def b (read-line))
  (println (solveMeFirst (Integer/parseInt a) (Integer/parseInt b))))

