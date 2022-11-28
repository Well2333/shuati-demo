# 题库

```json
{
  "name": "言语理解与表达800题",
  "version": "20221127-1",
  "description": "行政职业能力测试800题，来源xxxx",
  "author": "Well404 <well_404@outlook.com>",
  "license": "cc-by-nc-sa",
  "tags": ["行政职业能力测试", "行测", "言语理解与表达"],
  "questions": {
    "001": {
      "type": "selection",
      "content": "汪曾祺曾说语言不是外部的东西，它是和内在的思想同时存在，不可剥离的。在他看来写小说就是写语言，语文课学的是语言，但语言不是空壳，而是要承载各种各样的思想、哲学、伦理、道德的。怎么做人，如何对待父母兄弟姐妹，如何对待朋友，如何对待民族、国家和自己的劳动等，这些在语文课里是与语言并存的。从这个意义来讲，语文教育必须吸收和继承传统文化，而诗歌无疑是传统文化的集大成者。\n这段文字意在说明：",
      "options": [
        "诗歌中包含丰富的思想、伦理和道德元素",
        "脱离内在思想的语文教育是空洞无物的",
        "必须重视诗歌在语文教育中的作用",
        "语文教育需要和思想品德教育同步进行"
      ],
      "analysis": null,
      "answer": "C"
    }
  }
}
```

## 题库信息

### name

- **类型**: `str`
- **默认值**: `必填`

题库名

### version

- **类型**: `str`
- **默认值**: `null`

建议采用 `YYYYMMDD-当日修改次数` 进行命名，例如：1919 年 8 月 10 日第 1 次修改为 `19190810-1`

### description

- **类型**: `str`
- **默认值**: `null`

题库简介

### author

- **类型**: `str`
- **默认值**: `null`

题库作者信息

### license

- **类型**: `str`
- **默认值**: `MIT`

题库开源协议，默认为 `cc-by-nc-sa` 协议即 [`署名-非商业性使用-相同方式共享`](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.zh) 协议。

关于知识共享协议可参考 <https://creativecommons.org/choose/> 了解并选择，以保障您的作品在遭到非法用途时可以合法进行维护权力。

### questions

- **类型**: `dict`
- **默认值**: `必填`

题目信息，其格式为 `"题目编号": 题目内容`，其中题目编号为 `str`，题目内容为 `dict`。

题目内容详见 [题目类型](#题目类型)

## 题目类型

由于题目的形式本身复杂多变，差异巨大，因此无法一次性对全部题型或表达形式进行定义，因此此部分内容将会持续更新。

由于很多题目涉及表格、图片或其他类型的信息，因此题目内的内容在下文类型标记为 `markdown` 的部分会支持 [markdown 语法](https://markdown.com.cn/)，用于展示相关信息。

### 选择

```json
{
  "type": "Select",
  "content": "汪曾祺曾说语言不是外部的东西，它是和内在的思想同时存在，不可剥离的。在他看来写小说就是写语言，语文课学的是语言，但语言不是空壳，而是要承载各种各样的思想、哲学、伦理、道德的。怎么做人，如何对待父母兄弟姐妹，如何对待朋友，如何对待民族、国家和自己的劳动等，这些在语文课里是与语言并存的。从这个意义来讲，语文教育必须吸收和继承传统文化，而诗歌无疑是传统文化的集大成者。\n这段文字意在说明：",
  "options": [
    "诗歌中包含丰富的思想、伦理和道德元素",
    "脱离内在思想的语文教育是空洞无物的",
    "必须重视诗歌在语文教育中的作用",
    "语文教育需要和思想品德教育同步进行"
  ],
  "analysis": null,
  "answer": "C"
}
```

- type: "Select"
- content: markdown
- options: list[markdown]
- analysis: markdown
- answer: A、B、C、D、E...

单选题，`answer` 中的 "A" 对应 `options` 中的第 1 个选项，其他选项以此类推。

## 多选

```json
{
  "type": "MultiSelect",
  "content": "汪曾祺曾说语言不是外部的东西，它是和内在的思想同时存在，不可剥离的。在他看来写小说就是写语言，语文课学的是语言，但语言不是空壳，而是要承载各种各样的思想、哲学、伦理、道德的。怎么做人，如何对待父母兄弟姐妹，如何对待朋友，如何对待民族、国家和自己的劳动等，这些在语文课里是与语言并存的。从这个意义来讲，语文教育必须吸收和继承传统文化，而诗歌无疑是传统文化的集大成者。\n这段文字意在说明：",
  "options": [
    "诗歌中包含丰富的思想、伦理和道德元素",
    "脱离内在思想的语文教育是空洞无物的",
    "必须重视诗歌在语文教育中的作用",
    "语文教育需要和思想品德教育同步进行"
  ],
  "analysis": null,
  "answer": "C",
  "ordered": false
}
```

- type: "MultiSelect"
- content: markdown
- options: list[markdown]
- analysis: markdown
- answer: A、B、C、D、E...
- ordered: bool

多选题，`answer` 中至少包含两个英文字母。若 `ordered` 为 `true` 时，判断答案时将会额外判断其排列顺序是否与 `answer` 中的答案一致。

### 判断

```json
{
  "type": "Judgment",
  "content": "汪曾祺曾说语言不是外部的东西，它是和内在的思想同时存在，不可剥离的。在他看来写小说就是写语言，语文课学的是语言，但语言不是空壳，而是要承载各种各样的思想、哲学、伦理、道德的。怎么做人，如何对待父母兄弟姐妹，如何对待朋友，如何对待民族、国家和自己的劳动等，这些在语文课里是与语言并存的。从这个意义来讲，语文教育必须吸收和继承传统文化，而诗歌无疑是传统文化的集大成者。\n这段文字意在说明：必须重视诗歌在语文教育中的作用",
  "analysis": null,
  "answer": true
}
```

- type: "Judgment"
- content: markdown
- analysis: markdown
- answer: bool

判断对错。

### 填空题

```json
{
  "type": "Completion",
  "content": "文字的发展是_______的，所以在由前一个时期演变为后一个时期的时候，要有或长或短的新旧形式并用期。新旧形式_______，最后完成交替。",
  "analysis": null,
  "gaps": 2,
  "answer": ["渐变","此消彼长"],
  "is_absolute": false,
}
```

- type: "Completion"
- content: markdown
- analysis: markdown
- gaps: int
- answer: list[markdown]
- is_absolute: bool

值得注意的是，如果 `is_absolute=false` 此处将不会进行对错判断，答案将作为参考答案（主观题）。`is_absolute=true` 时将作为绝对答案进行比较（客观题）。

### 简答题

```json
{
  "type": "SAQs",
  "content": "对于古希腊人来说，各种形式和内容的比赛活动无所不在，凡是有竞赛的地方就有规则的存在。体育比赛有严格和严密的竞赛规则，裁判员在赛场上依据规则来进行判罚，只有如此才能产生没有任何争议的优胜者。这些活动的背后，如何用好的规则引导竞争，规范竞争，使人向善，使社会更为公正，是古希腊思想家们热衷探讨的话题。\n这段文字意在说明：",
  "analysis": null,
  "answer": "古希腊人强调竞争中规则的重要性",
  "is_absolute": false
}
```

- type: "SAQs"
- content: markdown
- analysis: markdown
- answer: list[markdown]
- is_absolute: bool

值得注意的是，如果 `is_absolute=false` 此处将不会进行对错判断，答案将作为参考答案（主观题）。`is_absolute=true` 时将作为绝对答案进行比较（客观题）。

### 嵌套题型

```json
{
  "type": "Nested",
  "content": "融合发展是_______，传统的平台介质或许会_______，但是新闻没_______，媒体还有责任，理想还有价值，职业还有担当。我们相信不管媒体形态怎么变，论格局怎么变，原创依然是这个社会最宝贵的资源，思想依然是媒体最重要的品质，理性仍是时代最需要的力量。\n依次填入画横线部分最恰当的一项是：",
  "subquestions":[{
      "type": "Select",
      "content": null,
      "options": ["人心所向","大势所趋"],
      "analysis": null,
      "answer": "B"
    },{
      "type": "Select",
      "content": null,
      "options": ["式微","减少"],
      "analysis": null,
      "answer": "A"
    },{
      "type": "Select",
      "content": null,
      "options": ["消失","消亡"],
      "analysis": null,
      "answer": "B"
    }],
  "analysis": null
}
```

- type: "Nested"
- content: markdown
- subquestions: list[questions]
- analysis: markdown

嵌套题型通常用于一个题干对应多个问题的题型。其中的 `subquestions` 可内含至少一个前文所介绍的题型，各个问题间的题型也可不同。但考虑到用户的阅读体验和渲染方案，嵌套问题中将不能包含嵌套问题。
