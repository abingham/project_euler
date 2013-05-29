(ns project-euler.core-test
  (:require [clojure.test :refer :all]
            [project-euler.problem1]
            [project-euler.problem2]))

(deftest problem1
  (testing "Project Euler problem 1"
    (is (= 233168 (project-euler.problem1/run)))))

(deftest problem2
  (testing "Project Euler problem 2"
    (is (= 4613732 (project-euler.problem2/run)))))
