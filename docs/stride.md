```c
[1 2 3 4 5 6 7 8 9]

double -> 8o

double mat[3][3] = [
  [1 2 3]
  [4 5 6]
  [7 8 9]
]


Stride: (3 * sizeof(double), 1 * sizeof(double)) -> (24, 8)
```


```c
double array[2][3] = [
  [1 2 3]
  [4 5 6]
]

uint32_t row = 2;
uint32_t col = 3;

for (int i = 0; i < row; i++) {
  for (int j = 0; j < col; j++)
    array[i][j]
}
```

```c
double array[6] = [1 2 3 4 5 6]

uint32_t row = 2;
uint32_t col = 3;

def get_elem_mat(uint32_t row, uint32_t col, Matrix *m) {
  return m[ row * m->stride_row + col * m->stride_col ];
}

for (int i = 0; i < row; i++) {
  for (int j = 0; j < col; j++)
    get_elem_mat(i, j, array);
}
```

```c
1 4 7
2 5 8
3 6 9

(3*8, 1*8) -> (24, 8)
```