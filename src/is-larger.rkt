;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname is-larger) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
(require 2htdp/image)

;; Image Image -> Boolean
;; Returns whether the first image is larger than the second area-wise.
(check-expect (is-larger? (square 40 "solid" "green") (square 30 "solid" "green")) true)
(check-expect (is-larger? (square 40 "solid" "green") (square 40 "solid" "green")) false)
(check-expect (is-larger? (square 30 "solid" "green") (square 40 "solid" "green")) false)

;(define (is-larger? first-img second-img) false) ;this is the stub

;(define (is-larger? first-img second-img)
;  (...first-img second-img)) ;this is the signature

(define (is-larger? first-img second-img)
  (> ( * (image-width first-img) (image-height first-img)) ( * (image-width second-img) (image-height second-img))))
  
