SET mapred.child.java.opts -Xmx40000m

dataset1 = LOAD 'file1' USING PigStorage('\n') AS
(line:chararray);
dataset2 = LOAD 'file2' USING PigStorage('\n') AS (line:chararray);

grpd = COGROUP dataset1 BY line, dataset2 BY line;
d1_only = FOREACH (FILTER grpd BY IsEmpty(dataset2)) GENERATE FLATTEN(dataset1);
STORE d1_only INTO 'd1_only' Using PigStorage('\n');

-- d2_only = FOREACH (FILTER grpd BY IsEmpty(dataset1)) GENERATE FLATTEN(dataset2);
-- STORE d2_only INTO 'd2_only' Using PigStorage('\n');
