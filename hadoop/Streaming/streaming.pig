DEFINE PROC `$proc` SHIP('$procpath', '$externalpath');

A = LOAD '$data' USING PigStorage('\t') AS (t:bytearray, d:bytearray, u:bytearray, e:bytearray);
DATA = FOREACH A GENERATE t, d;
B = STREAM DATA THROUGH PROC;
STORE B INTO '$output' USING PigStorage('\t');
