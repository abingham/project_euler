(ns project-euler.problem3
  (:require [project-euler.util :as util]))

(defn run []
  (last (util/prime_factors 600851475143)))

