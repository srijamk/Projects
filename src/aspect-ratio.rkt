;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname aspect-ratio) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
(require 2htdp/image)

;; Image -> String
;; Returns whether the given image is tall, square, or wide.
(check-expect (aspect-ratio (rectangle 20 40 "solid" "green")) "tall")
(check-expect (aspect-ratio (square 20 "solid" "green")) "square")
(check-expect (aspect-ratio (rectangle 40 20 "solid" "green")) "wide")

;(define (aspect-ratio img) "") ;this is the stub

;(define (aspect-ratio img)
;  (...img)) ;this is the template

(define (aspect-ratio img)
  (cond [(> (image-height img) (image-width img)) "tall"]
        [(= (image-height img) (image-width img)) "square"]
        [(< (image-height img) (image-width img)) "wide"]))

