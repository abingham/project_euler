(ns project-euler.problem6
  (:require [project-euler.util :as util]))

(def count' 100)

(defn run []
  (- 
   (util/expt (util/sum (range (+ 1 count'))) 2)
   (util/sum (for [x (range (+ 1 count'))] (* x x)))))
