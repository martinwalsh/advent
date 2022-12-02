(ns day01-test
  (:require [clojure.test :refer [deftest is testing use-fixtures]]
            day01))

;; https://stuartsierra.com/2016/05/19/fixtures-as-caches
(def ^:dynamic data)
(defn load-data [f]
  (binding [data (slurp "/data/day01.txt")] 
    (f)))
(use-fixtures :each load-data)

(def EXAMPLE1 (clojure.string/trim "
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"))

(deftest day01-examples-test
  (is (and
    (= 24000 (day01/part1 EXAMPLE1))
    (= 45000 (day01/part2 EXAMPLE1)))))

(deftest day01-part1-test
  (is (= 68775 (day01/part1 data))))

(deftest day01-part2-test
  (is (= 202585 (day01/part2 data))))