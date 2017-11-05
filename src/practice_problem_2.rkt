;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname practice_problem_2) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
(require 2htdp/image)
(define (create-square color)
  (square 20 "solid" color))

(define BLUE-SQUARE (create-square "blue"))
(define YELLOW-SQUARE (create-square "yellow"))
(beside (above BLUE-SQUARE
               YELLOW-SQUARE)
        (above YELLOW-SQUARE
               BLUE-SQUARE))