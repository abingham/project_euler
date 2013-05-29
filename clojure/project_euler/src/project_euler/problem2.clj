(ns project-euler.problem2
  (:require [project-euler.util :as util]))

(defn run []
  (let [sub4m (take-while (partial > 4000001) util/fibs)
        evens (filter even? sub4m)]
    (reduce + evens)))
