(ns project-euler.problem1)

(defn- threesAndFives [max]
  (filter 
   (fn [x]
     (cond (zero? (mod x 3)) true
           (zero? (mod x 5)) true
           :else false))
   (range 1 max)))

(defn run []
  (reduce + (threesAndFives 1000)))
