#lang racket
(define in(open-input-file"rpn.in"))
(define out(open-output-file"rpn.out"#:exists 'replace))

(define (do f e s operation) 
  (f 
   (cdr e) 
   (cons (operation (car (cdr s)) (car s)) (cdr (cdr s)))))

(define (f e s)
  (if(null? e)
     (car s)         
     (if(eq? (car e) '+) (do f e s +)
        (if(eq? (car e) '-) (do f e s -)
           (if(eq? (car e) '*) (do f e s *)
              (if(eq? (car e) '/) (do f e s /)
                 (f (cdr e) (cons (car e) s)))
              )))))

(display (f (read in) '()) out)
(flush-output out)
