(ns project-euler.core-test
  (:require [clojure.test :refer :all]
            [project-euler.problem1]
            [project-euler.problem2]
            [project-euler.problem3]
            [project-euler.problem4]
            [project-euler.problem5]
            [project-euler.problem6]
            [project-euler.problem7]))

(deftest problem1
  (testing "Project Euler problem 1"
    (is (= 233168 (project-euler.problem1/run)))))

(deftest problem2
  (testing "Project Euler problem 2"
    (is (= 4613732 (project-euler.problem2/run)))))

(deftest problem3
  (testing "Project Euler problem 3"
    (is (= 6857 (project-euler.problem3/run)))))

(deftest problem4
  (testing "Project Euler problem 4"
    (is (= 906609 (project-euler.problem4/run)))))

(deftest problem5
  (testing "Project Euler problem 5"
    (is (= 232792560 (project-euler.problem5/run)))))

(deftest problem6
  (testing "Project Euler problem 6"
    (is (= 25164150 (project-euler.problem6/run)))))

(deftest problem7
  (testing "Project Euler problem 7"
    (is (= 104743 (project-euler.problem7/run)))))
