(ns project-euler.problem4
  (:require [project-euler.util :as util]))

; This could, of course, be made more general purpose...
(defn- unique-pair-products [range1 range2]
  (for [x range1
        y range2
        :when (>= x y)]
    (* x y)))

(defn run []
  (apply max 
   (filter #(util/palindrome? (str %))
           (unique-pair-products (range 100 1000) (range 100 1000)))))
