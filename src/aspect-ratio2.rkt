;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname aspect-ratio2) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
(require 2htdp/image)

(check-expect (aspect-ratio2 (rectangle 20 40 "solid" "green")) "tall")
(check-expect (aspect-ratio2 (square 20 "solid" "green")) "square")
(check-expect (aspect-ratio2 (rectangle 40 20 "solid" "green")) "wide")

(define (aspect-ratio2 img)
  (if (> (image-height img) (image-width img))
      "tall"
      (if (= (image-height img) (image-width img))
          "square"
          "wide"
          )))