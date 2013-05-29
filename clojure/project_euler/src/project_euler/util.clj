(ns project-euler.util)

(def fibs
  ((fn rfib [a b] 
     (lazy-seq (cons a (rfib b (+ a b)))))
   1 2))
