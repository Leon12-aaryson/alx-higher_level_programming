-- displays thethe state with highest temp
SELECT state, MAX(value) AS max_temp FROM temperatures GROUP BY state;
