# -*- coding: utf8 -*-
from collections import Counter
from scipy import linalg, mat, dot
import math
import time

# 기사 제목, 형태소 분석 결과 tuple list
cluster = [('''"최순실, '11문'으로 청와대 수시로 드나들었다"''',
            '''"/SP 최순실/NNP ,/SP '/SP 11/SN 문/NNB '/SP 으로/JKB 청와대/NNP 수시로/MAG 드나들다/VV 었/EP 다/EC "/SP'''
            ),
           ('''"최순실, 청와대 수시로 드나들었다"''',
            '''"/SP 최순실/NNP ,/SP 청와대/NNP 수시로/MAG 드나들다/VV 었/EP 다/EC "/SP'''
            ),
           ("한겨레, '최순실 청와대 수시로 드나들었다'",
            "한겨레/NNG ,/SP '/SP 최순실/NNP 청와대/NNP 수시로/MAG 드나들다/VV 었/EP 다/EC '/SP"
            ),
           ('"최순실, 청와대 차 타고 셀 수 없이 靑 드나들었다"',
            '"/SP 최순실/NNP ,/SP 청와대/NNP 차/NNG 타다/VV 고/EC 셀/NNG 수/NNB 없이/MAG 靑/SH 드나들다/VV 었/EP 다/EC "/SP'
            ),
           ('대검찰청 청사 덮친 범행 "최순실 죽을 죄 처단하려"',
            '대검찰청/NNG 청사/NNG 덮치다/VV ㄴ/ETM 범행/NNG "/SP 최순실/NNP 죽다/VV 을/ETM 죄/NNG 처단/NNG 하다/XSV 려/EC "/SP'
            ),
           ("대검찰청 포크레인 난입…‘최순실’ 향한 분노인가",
            "대검찰청/NNG 포크레인/NNG 난입/NNG …/SP '/SP 최순실/NNP '/SP 향하다/VV ㄴ/ETM 분노/NNG 이/VCP ㄴ가/EC"
            ),
           ("'최순실에 분노' 대검청사에 포클레인 돌진",
            "'/SP 최순실/NNP 에/JKB 분노/NNG '/SP 대검/NNG 청사/NNG 에/JKB 포클레인/NNP 돌진/NNG"
            ),
           ('대검청사에 포클레인 돌진…운전자 "최순실 때문에"',
            '대검/NNG 청사/NNG 에/JKB 포클레인/NNP 돌진/NNG …/SP 운전자/NNG "/SP 최순실/NNP 때문/NNB 에/JKB "/SP'
            ),
           ('대검찰청에 포클레인 돌진한 남성…“최순실 때문에”',
            '대검찰청/NNG 에/JKB 포클레인/NNP 돌진/NNG 하다/XSV ㄴ/ETM 남성/NNG …/SP "/SP 최순실/NNP 때문/NNB 에/JKB "/SP'
            ),
           ("檢, 최순실 수사 `오물`과 `포크레인`…`수난 겪어",
            "檢/SH ,/SP 최순실/NNP 수사/NNG `/SP 오물/NNG `/SP 과/NNG `/SP 포크레인/NNG `/SP …/SP `/SP 수난/NNG 겪다/VV 어/EC"
            )
          ]


def parse(s):
  # input; term/morpheme type이 반복 출현하는 string
  # return; NNP, NNG인 term list
  blank_split = s.split(' ')
  parsed = [(t.split('/')[0], t.split('/')[1]) for t in blank_split]
  return [term for term, part_of_speech in parsed if part_of_speech in ['NNP', 'NNG']]


def tf(terms):
  return Counter(terms)


def idf(terms_list):
  # input; 각 문서별 term list를 가진 list
  # return; idf dict
  #
  # 수식; https://en.wikipedia.org/wiki/Tf%E2%80%93idf
  # log(num of total documents / document frequency of term)
  l, num_of_docs = [], len(terms_list)
  [l.extend(terms) for terms in terms_list]
  return {term: math.log(1. * num_of_docs / count, 10) for term, count in Counter(l).items()}


def tf_idf(terms_list):
  # input; 각 문서별 term list를 가진 list
  # return; tf_idf dictionary를 가진 list
  tf_idf_list = []
  idf_dict = idf(terms_list)
  for terms in terms_list:
    tf_dict = Counter(terms)
    tf_idf_list.append({term: tf * idf_dict[term] for term, tf in tf_dict.items()})
  return tf_idf_list


def cosine_similarity(v1, v2, v1_sqrt_norm, v2_sqrt_norm):
  # input
  #   vector dict 1, 2
  #   vector 1, 2 normalized value
  # output; cosine similarity

  # dot_product = 0

  # dot_v = set(v1.keys()).intersection(set(v2.keys()))
  # for key in dot_v:
  #     dot_product += v1[key] * v2[key]
  dot_product = sum([v1[key] * v2.get(key, 0) for key in v1])

  # for key in v1.keys():
  #     v1_sqrt_norm += v1[key] * v1[key]
  # v1_sqrt_norm = math.sqrt(sum([v * v for v in v1.values()]))

  # for key in v2.keys():
  #     v2_sqrt_norm += v2[key] * v2[key]
  # v2_sqrt_norm = math.sqrt(sum([v * v for v in v2.values()]))

  cos_sim = dot_product / (v1_sqrt_norm * v2_sqrt_norm)

  return cos_sim


def cosine_similarity2(v1, v2, v1_sqrt_norm, v2_sqrt_norm):
  # input
  #   vector 1, 2 (vector의 길이가 다른 경우 없는 key에 대해서는 0을 채워서 같은 길이로 만든 vector임)
  #   vector 1, 2 normalized value
  # output; cosine similarity

  dot_product = sum([v * v2[i] for i, v in enumerate(v1)])

  cos_sim = dot_product / (v1_sqrt_norm * v2_sqrt_norm)

  return cos_sim


def scipy_cosine_similarity(tf_idf1, tf_idf2):
  # input; vector 1, 2 (vector의 길이가 다른 경우 없는 key에 대해서는 0을 채워서 같은 길이로 만든 vector임)
  # output; cosine similarity
  # scipy library를 사용해 계산

  # http://stackoverflow.com/questions/21980644/calculate-cosine-similarity-of-two-matrices-python
  a, b = mat(tf_idf1), mat(tf_idf2)
  c = dot(a, b.T) / linalg.norm(a) / linalg.norm(b)
  return c.A1[0]    # http://stackoverflow.com/questions/3337301/numpy-matrix-to-array


def scipy_cosine_similarity2(a, b, norm_a, norm_b):
  # input; vector a, b, a, b의 normalized value
  # output; cosine similarity
  # dot만 사용하기 위해 나머지 값은 함수 호출 전에 미리 만들어둔 값을 전달

  c = dot(a, b) / norm_a / norm_b
  return c.A1[0]


if __name__ == '__main__':
  terms_list, terms_set = [], set()
  for title, parsed in cluster:
    print '{}\t{}'.format(title, parsed)
    terms = parse(parsed)
    terms_list.append(terms)
    [terms_set.add(term) for term in terms]
    # print '\t',
    # for term, count in tf(terms).items():
    #   print term, count,
    # print
  # for term, count in idf(terms_list).items():
  #   print term, count

  tf_idf_dict_list = tf_idf(terms_list)
  # for tf_idf_dict in tf_idf_dict_list:
  #   for term, tf_idf in tf_idf_dict.items():
  #     print term, tf_idf,
  #   print
  tf_idf_dict_list_len = len(tf_idf_dict_list)
  sqrt_norm_list = [math.sqrt(sum([v * v for v in tf_idf_dict.values()])) for tf_idf_dict in tf_idf_dict_list]
  result = []
  ts = time.time()
  # for i, j in product(range(0, tf_idf_dict_list_len - 1), range(1, tf_idf_dict_list_len)):
  for i in range(0, tf_idf_dict_list_len):
    for j in range(i + 1, tf_idf_dict_list_len):
      # ts = time.time()
      cos_sim = cosine_similarity(tf_idf_dict_list[i], tf_idf_dict_list[j], sqrt_norm_list[i], sqrt_norm_list[j])
      # te = time.time()
      # print i, j, cos_sim, '\t%2.8f msec' % ((te - ts) * 1000)
      result.append((i, j, cos_sim))
  te = time.time()
  print '%2.8f msec' % ((te - ts) * 1000)
  for i, j, cos_sim in sorted(result, key=lambda t: t[2], reverse=True)[:10]:
    print '[{}][{}]\t{}'.format(i, j, cos_sim)

  all_terms = sorted(list(terms_set))
  # for term in all_terms:
  #   print term,
  # print
  tf_idf_list = []
  for tf_idf_dict in tf_idf_dict_list:
    tf_idf = []
    for term in all_terms:
      print term, tf_idf_dict.get(term, 0),
      tf_idf.append(tf_idf_dict.get(term, 0))
    print
    tf_idf_list.append(tf_idf)
  sqrt_norm_list = [math.sqrt(sum([v * v for v in tf_idf])) for tf_idf in tf_idf_list]
  result = []
  ts = time.time()
  for i in range(0, tf_idf_dict_list_len):
    for j in range(i + 1, tf_idf_dict_list_len):
      cos_sim = cosine_similarity2(tf_idf_list[i], tf_idf_list[j], sqrt_norm_list[i], sqrt_norm_list[j])
      # print '[{}][{}]\t{}'.format(i, j, cos_sim)
      result.append((i, j, cos_sim))
  te = time.time()
  print '%2.8f msec' % ((te - ts) * 1000)
  for i, j, cos_sim in sorted(result, key=lambda t: t[2], reverse=True)[:10]:
    print '[{}][{}]\t{}'.format(i, j, cos_sim)

  result = []
  precalced_list = [(mat(tf_idf), mat(tf_idf).T, linalg.norm(tf_idf)) for tf_idf in tf_idf_list]
  ts = time.time()
  for i in range(0, tf_idf_dict_list_len):
    for j in range(i + 1, tf_idf_dict_list_len):
      # cos_sim = scipy_cosine_similarity(tf_idf_list[i], tf_idf_list[j])
      cos_sim = scipy_cosine_similarity2(precalced_list[i][0], precalced_list[j][1], precalced_list[i][2], precalced_list[j][2])
      # print '[{}][{}]\t{}'.format(i, j, cos_sim)
      result.append((i, j, cos_sim))
  te = time.time()
  print '%2.8f msec' % ((te - ts) * 1000)
  for i, j, cos_sim in sorted(result, key=lambda t: t[2], reverse=True)[:10]:
    print '[{}][{}]\t{}'.format(i, j, cos_sim)
