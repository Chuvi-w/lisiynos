#lang racket
(define in (open-input-file "gcd.in"))
(define out (open-output-file "gcd.out" #:exists 'replace))
(define (gcd x y) (if (zero? y) x (gcd y (remainder x y))))
(display (gcd (read in) (read in)) out)