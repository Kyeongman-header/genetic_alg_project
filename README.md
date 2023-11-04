# genetic_alg_project

# 0. requirements

```
pip install tk
pip install matplotlib
pip install numpy
pip install pickle
```

# 1. main train 실행.

```
python main.py indiv_1000_gen_100_geneL_300
```

__file_name__에 원하는 저장 파일명을 입력.

# 2. main train 수행 후, 실행 결과를 display.

```
python display.py indiv_1000_gen_100_geneL_300 5
```
1에서 지정한 파일 명으로 display 수행. 전체 generation 중에서 마지막 n개(위의 코드 샘플에선 5개)의 generation에서 best 수행 결과를 확인 가능함.

# 3. 실행 변수.

consts.py 파일에 몇가지 실행 변수들이 있음. 실험할 때마다 이 변수들을 조정할 것.
```
Time_Limit=300 # 한 개체가 최장 생존 가능한 시간.
gene_length=50 # 염기 서열의 길이.
width=300 # 창의 가로 크기.
height=300 # 창의 세로 크기.
whole_generations=100 # 유전 알고리즘을 수행할 전체 세대의 수.
whole_individuals=1000 # 각 세대마다 개체의 수.
```
