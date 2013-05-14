(def fibs
  ((fn rfib [a b] 
     (lazy-seq (cons a (rfib b (+ a b)))))
   1 2))

(let [sub4m (take-while (partial > 4000001) fibs)
      evens (filter even? sub4m)]
  (println (reduce + evens)))


