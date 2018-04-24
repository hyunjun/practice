import redis
import ujson


conn = redis.StrictRedis(host='127.0.0.1', port=56379, db=0)
print('redis version {}'.format(conn.info()['redis_version']))

print('\n{} {}'.format('-' * 10, 'string'))
en_str, ko_str = 'english string', '한글 문자열'
conn.hset('test_hash', 'en_str', en_str)
hget_val = conn.hget('test_hash', 'en_str').decode('utf8')
print(en_str, hget_val, en_str == hget_val)
conn.hset('test_hash', 'en_str', ujson.dumps(en_str))
hget_val = ujson.loads(conn.hget('test_hash', 'en_str').decode('utf8'))
print(en_str, hget_val, en_str == hget_val)
conn.hset('test_hash', 'ko_str', ko_str)
hget_val = conn.hget('test_hash', 'ko_str').decode('utf8')
print(ko_str, hget_val, ko_str == hget_val)
conn.hset('test_hash', 'ko_str', ujson.dumps(ko_str))
hget_val = ujson.loads(conn.hget('test_hash', 'ko_str').decode('utf8'))
print(ko_str, hget_val, ko_str == hget_val)

print('\n{} {}'.format('-' * 10, 'dict'))
en_dict, ko_dict = {'key': 'value'}, {'키': '값'}
conn.hset('test_hash', 'en_dict', en_dict)
hget_val = conn.hget('test_hash', 'en_dict').decode('utf8')
print(en_dict, hget_val, type(hget_val), en_dict == hget_val)
conn.hset('test_hash', 'en_dict', ujson.dumps(en_dict))
hget_dict = ujson.loads(conn.hget('test_hash', 'en_dict').decode('utf8'))
print(en_dict, hget_dict, type(hget_dict), en_dict == hget_dict)
conn.hset('test_hash', 'ko_dict', ko_dict)
hget_val = conn.hget('test_hash', 'ko_dict').decode('utf8')
print(ko_dict, hget_val, type(hget_val), ko_dict == hget_val)
conn.hset('test_hash', 'ko_dict', ujson.dumps(ko_dict))
hget_dict = ujson.loads(conn.hget('test_hash', 'ko_dict').decode('utf8'))
print(ko_dict, hget_dict, type(hget_dict), ko_dict == hget_dict)

print('\n{} {}'.format('-' * 10, 'list of dict'))
l = [en_dict, ko_dict]
conn.hset('test_hash', 'mixed_list', ujson.dumps(l))
hget_l = ujson.loads(conn.hget('test_hash', 'mixed_list'))
print(l, hget_l)

conn.delete('test_hash')

print('\n{} {}'.format('-' * 10, 'hmset'))
mul_dict = {'en_str': en_str, 'ko_str': ko_str, 'en_dict': en_dict, 'ko_dict': ko_dict, 'mixed_list': l}
conn.hmset('test_hash', mul_dict)
hgetall_values = conn.hgetall('test_hash')
for key, val in hgetall_values.items():
    k, v = key.decode('utf8'), val.decode('utf8')
    print(k, v, type(v))
    try:
        print(ujson.loads(v))
    except Exception as e:
        print(e)

print('\n{} {}'.format('-' * 10, 'hmset with json dump'))
conn.hmset('test_hash', {k: ujson.dumps(v) for k, v in mul_dict.items()})
hgetall_values = conn.hgetall('test_hash')
for key, val in hgetall_values.items():
    k, v = key.decode('utf8'), ujson.loads(val.decode('utf8'))
    print(k, v, type(v))

conn.delete('test_hash')
