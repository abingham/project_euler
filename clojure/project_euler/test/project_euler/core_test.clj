(ns project-euler.core-test
  (:require [clojure.test :refer :all]
            [project-euler.problem1]
            [project-euler.problem2]
            [project-euler.problem3]))

(deftest problem1
  (testing "Project Euler problem 1"
    (is (= 233168 (project-euler.problem1/run)))))

(deftest problem2
  (testing "Project Euler problem 2"
    (is (= 4613732 (project-euler.problem2/run)))))

(deftest problem3
  (testing "Project Euler problem 3"
    (is (= 6857 (project-euler.problem3/run)))))
