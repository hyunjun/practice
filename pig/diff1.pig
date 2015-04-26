SET mapred.child.java.opts -Xmx20480m

-- Process Inputs
a = LOAD 'file1' AS (First:chararray);
b = LOAD 'file2' AS (Second:chararray);

-- Combine Data
combined = JOIN a BY First FULL OUTER, b BY Second;

-- Output Data
SPLIT combined INTO first_raw IF Second IS NULL,
                    second_raw IF First IS NULL;
first_only = FOREACH first_raw GENERATE First;
second_only = FOREACH second_raw GENERATE Second;
STORE first_only INTO 'first_only' USING PigStorage();
STORE second_only INTO 'second_only' USING PigStorage();
