T = readtable('owid-covid-data.csv');

T = T(sum(isnan(T{5,:}), 2) == 0);