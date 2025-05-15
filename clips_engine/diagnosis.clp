(deftemplate symptom
  (slot name))

;; تحميل الأعراض اللي اختارها المستخدم
(load "/engine/input.clp")

(reset)

(defrule flu
    (symptom (name fever))
    (symptom (name cough))
    =>
    (printout t "You might have the flu." crlf))

(defrule cold
    (symptom (name cough))
    =>
    (printout t "You might have a cold." crlf))

(defrule fatigue_only
    (symptom (name fatigue))
    =>
    (printout t "You might just need rest." crlf))
