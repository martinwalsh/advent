(set! *warn-on-reflection* true)

(ns day01)

(defn parse [data]
  (for [e (clojure.string/split data #"\n\n")]
    (reduce + (map read-string (clojure.string/split e #"\n")))))

(defn part1 [data]
  (reduce max (parse data)))

(defn part2 [data] 
  (reduce + (take 3 (sort (comp - compare) (parse data)))))
