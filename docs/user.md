# 用户

```sql
CREATE TABLE history (
  id       INT PRIMARY KEY NOT NULL,
  time     DATETIME        NOT NULL, 
  lib      TEXT            NOT NULL,
  question TEXT            NOT NULL,
  type     INTEGER         NOT NULL,
  note     TEXT
);

CREATE TABLE favorate (
  id       INT PRIMARY KEY NOT NULL,
  time     DATETIME        NOT NULL, 
  lib      TEXT            NOT NULL,
  question TEXT            NOT NULL,
  folder   INTEGER         NOT NULL DEFAULT default
);
```

## 数据存储

### histroy

#### id

#### time

记录时间

#### lib

题库名

#### question

题名

#### type

记录类型，0为查看，1为做对，2为做错

#### note

额外数据，记录错误选项或其他问题

### favorate

#### folder

收藏夹名
