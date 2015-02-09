DEFINE proc `$prog` SHIP('$prog_path');

%default txt population_drift
%default table population_drift
%default col_fam1 num
%default col_fam2 ratio
%default col0 region
%default col1 n_in
%default col2 n_out
%default col3 n_net
%default col4 n_prev
%default col5 r_in
%default col6 r_out
%default col7 r_net
%default col8 r_prev
%default col9 n_res
%default col10 r_res

data = LOAD 'hbase://$table' using org.apache.pig.backend.hadoop.hbase.HBaseStorage('$col_fam1:* $col_fam2:*', '-loadKey true') AS (id:chararray, $col_fam1:map[chararray], $col_fam2:map[chararray]);
columns = FOREACH data GENERATE id, $col_fam1#'$col1', $col_fam1#'$col2', $col_fam2#'$col5', $col_fam2#'$col6';
calculated = STREAM columns THROUGH proc AS (id:chararray, $col9:chararray, $col10:chararray);
STORE calculated INTO '/user/hanadmin/$txt' using PigStorage('\t');
