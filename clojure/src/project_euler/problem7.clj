(ns project-euler.problem7
  (:require [project-euler.util :as util]))

(defn run []
  (nth util/primes 10000))
