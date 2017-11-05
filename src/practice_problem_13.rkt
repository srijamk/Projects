;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname practice_problem_13) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
(require 2htdp/image)
(define BLUE-STAR (star 40 "solid" "blue"))
(define YELLOW-STAR (star 25 "solid" "yellow"))
(define SECOND-BLUE-STAR (star 10 "solid" "blue"))
(overlay SECOND-BLUE-STAR YELLOW-STAR BLUE-STAR)