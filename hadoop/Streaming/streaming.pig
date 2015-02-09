DEFINE PROC `$proc` SHIP('$procpath', '$externalpath');

%default col1 t
%default col2 d
%default col3 u
%default col4 e

A = LOAD '$data' USING PigStorage('\t') AS ($col1:bytearray, $col2:bytearray, $col3:bytearray, $col4:bytearray);
DATA = FOREACH A GENERATE $col1, $col2;
B = STREAM DATA THROUGH PROC;
STORE B INTO '$output' USING PigStorage('\t');
