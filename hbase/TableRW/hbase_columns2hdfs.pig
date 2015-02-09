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

data = LOAD 'hbase://$table' using org.apache.pig.backend.hadoop.hbase.HBaseStorage('$col_fam1:* $col_fam2:*', '-loadKey true') AS (id:chararray, $col_fam1:map[chararray], $col_fam2:map[chararray]);
columns = FOREACH data GENERATE id, $col_fam1#'$col1', $col_fam1#'$col4', $col_fam2#'$col6', $col_fam2#'$col7';
STORE columns INTO '/user/hanadmin/$txt' using PigStorage('\t');
