;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname |Day 3 Racket|) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
; Day 3

(require 2htdp/image)
;(above (circle 40 "solid" "red")
;       (circle 40 "solid" "yellow")
;       (circle 40 "solid" "green"));;

(define (light c)
  (circle 40 "solid" c))
""
(above (light (string-append "re" "d"))
       (light "yellow")
       (light "green")
       (light "blue"))
(define WIDTH 100)
(define HEIGHT 100)
(>= WIDTH HEIGHT)
(= 1 2)
(> 3 9)
(string=? "foo" "bar")
(define rect (rectangle 10 20 "solid" "red"))
(define rect2 (rectangle 20 10 "solid" "blue"))
rect rect2(< (image-width rect)
   (image-width rect2))
(if (< (image-width rect)
      (image-height rect2))
   (image-width rect)
   (image-height rect2))
(+ (* 3 2) 1)

(define (max-dim img)
  (if (> (image-width img) (image-height img))
      (image-width img)
      (image-height img)))

(max-dim (rectangle 10 20 "solid" "blue"))
(radial-star 10 80 20 "solid" "purple")