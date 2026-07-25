% Disease and symptoms

disease(fever, high_temperature).
disease(cold, sneezing).
disease(malaria, chills).
disease(diabetes, frequent_urination).
disease(covid, cough).

% Diagnosis rule
diagnosis(Symptom) :-
    disease(Disease, Symptom),
    write('Possible Disease: '),
    write(Disease).
