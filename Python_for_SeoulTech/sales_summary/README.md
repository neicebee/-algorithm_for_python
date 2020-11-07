# sales_summary

품목별 판매량 데이터를 기반으로 각 품목의 전체 판매량과 판매 순위를 분석하는 코드를 작성

품목별 판매량 데이터는 `list`형태.

```python
data = [('apple', 5), ('beer', 2), ('pencil', 1), 
        ('beer', 2), ('book', 8), ('apple', 9),
        ('paper', 3), ('pencil', 13), ('orange', 6)]
```

위와 같은 형태의 판매량 데이터를 기반으로 `sort_sales` 함수와 `sales_summary` 함수를 작성
- `sort_sales` 함수
  - 품목별 판매량 데이터를 입력받아 품목별 총 판매량 결과를 반환
  - 결과는 `list` 형태이고 각 요소는 `(품목명, 총 판매량)`
  - 결과는 `총 판매량`을 기준으로 내림차순 정렬
  
    ```python
    >>> sorted_sales = sort_sales(data)
    >>> print(sorted_sales)
    [('apple', 14),
     ('pencil', 14),
     ('book', 8),
     ('orange', 6),
     ('beer', 4),
     ('paper', 3)]
    ```
- `sales_summary` 함수
  - `sort_sales` 함수의 결과를 입력으로 받아 판매 순위를 매겨 그 결과를 반환
  - 반환되는 결과는 `list` 형태인데 이 `list`는 `(품목명, 총 판매량, 판매순위)`
  - 결과는 `총 판매량` 기준 내림차순 정렬
  - `판매순위`는 `전체 판매량` 기준으로 매겨지는데, 같은 판매량을 가지는 경우는 같은 순위. 같은 순위가 반복되면 그 수만큼 순위를 건너뛰고 다음 순위를 부여.

    ```python
    >>> summary = sales_summary(sorted_sales)
    >>> print(summary)
    [('apple', 14, 1),
    ('pencil', 14, 1),
    ('book', 8, 3),
    ('orange', 6, 4),
    ('beer', 4, 5),
    ('paper', 3, 6)]
    ```
