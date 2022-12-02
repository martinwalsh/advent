(ns dayNN-test
  (:require [clojure.test :refer [deftest is testing use-fixtures]]
            dayNN))

;; https://stuartsierra.com/2016/05/19/fixtures-as-caches
(def ^:dynamic data)
(defn load-data [f]
  (binding [data (slurp "/data/dayNN.txt")] 
    (f)))
(use-fixtures :each load-data)

(def EXAMPLE1 (clojure.string/trim "
"))

(deftest dayNN-examples-test
  (is (and
    (= nil (dayNN/part1 nil))
    (= nil (dayNN/part2 nil)))))

(deftest dayNN-part1-test
  (is (= nil (dayNN/part1 nil))))

(deftest dayNN-part2-test
  (is (= nil (dayNN/part2 nil))))