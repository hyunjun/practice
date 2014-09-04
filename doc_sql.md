# MySQL

## Usage
* age가 '만 xx세'로 되어 있을 때 숫자만 뽑아 그 차이를 구하는 경우
```
$ mysql -h [x.y.z.w] -u [userid] -p[password] [database] -N -e "SELECT a.keyword, a.iage, b.keyword, b.iage, a.iage - b.iage FROM (SELECT \`key\`,keyword, age, CHAR_LENGTH(age), CONVERT(SUBSTRING(age, 2, CHAR_LENGTH(age)-2), UNSIGNED) iage, represent, family FROM [table] WHERE age IS NOT NULL) as a join (SELECT \`key\`,keyword, age, CHAR_LENGTH(age), CONVERT(SUBSTRING(age, 2, CHAR_LENGTH(age)-2), UNSIGNED) iage, represent, family FROM [table] WHERE age IS NOT NULL) as b on a.\`key\` != b.\`key\`"
```
* insert .. on duplicate key update
  * http://dev.mysql.com/doc/refman/5.5/en/insert-on-duplicate.html
  * http://knight76.tistory.com/entry/Mysql-%EC%9D%98-Insert-On-Duplicate-Key-Update-%EC%9C%A0%EC%9D%98%EC%82%AC%ED%95%AD
* insert multiple records
  * http://www.electrictoolbox.com/mysql-insert-multiple-records/
* load data infile; 속도가 느림
  ```
  mysql -h xxx.yyy.zzz.www -u [user id] -p[password] [database] -N -e "LOAD DATA local infile \"./[data file]\" REPLACE INTO TABLE [table name] ([column1], [column2],...[columnN])"
  ```
  * http://dev.mysql.com/doc/refman/5.1/en/load-data.html
  * http://ra2kstar.tistory.com/2
* mysqlimport
  * http://tac.softonnet.com/troubleshoot/viewbody.php?code=troubleshoot&page=1&number=26&keyfield=category&key=db

## Error
* #1071 - Specified key was too long http://stackoverflow.com/questions/1814532/1071-specified-key-was-too-long-max-key-length-is-767-bytes
