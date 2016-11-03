# Cosine Similarity
* python으로 구현한 version vs. scipy library를 이용한 version 비교
  * 당연히 후자가 간단하지만, 생각보다 속도가 느림
  * 속도 비교

    ```
    1 def cosine_similarity(v1, v2, v1_sqrt_norm, v2_sqrt_norm)   # base

    # base와 다른 건 dictionary를 쓰지 않은 대신 v1, v2의 길이를 맞춰서 key가 없는 경우 0을 입력해준 list를 사용
    2 def cosine_similarity2(v1, v2, v1_sqrt_norm, v2_sqrt_norm)

    # 2와 동일하지만, v1, v2를 np.array로 만들어, np.dot으로 dot product를 만듦
    3 def cosine_similarity3(v1, v2, v1_sqrt_norm, v2_sqrt_norm)

    # scipy library로만 만듦
    4 def scipy_cosine_similarity2(tf_idf1, tf_idf2)
    ```
    * 데이터 개수가 적은 경우(10개) 1 > 2 > 4 > 3 즉 아무 library call이 없어야 빠름

      ```
      0.15401840 msec
      0.27704239 msec
      1.73592567 msec
      1.05500221 msec
      ```
    * 데이터 개수가 많은 경우(150개) 3 > 1 > 2 > 4 즉 numpy.dot을 이용하는 게 빠름

      ```
      42.28997231 msec
      70.75214386 msec
      37.43886948 msec
      257.30514526 msec
      ```
* ref
  * https://en.wikipedia.org/wiki/Tf%E2%80%93idf
  * http://stackoverflow.com/questions/21980644/calculate-cosine-similarity-of-two-matrices-python
  * http://stackoverflow.com/questions/3337301/numpy-matrix-to-array
