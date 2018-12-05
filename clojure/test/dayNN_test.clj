(ns dayNN-test
  (:require [clojure.test :refer [deftest is]]
            dayNN))

(deftest dayNN-part1-test
  (is (= nil (dayNN/part1 nil))))

(deftest dayNN-part2-test
  (is (= nil (dayNN/part2 nil))))

(deftest dayNN-can-read-a-data-file
  (is (= "" (slurp "/data/dayNN.txt"))))
