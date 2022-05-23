# 基础

## html里面

html里面引入javascript代码

```html
<script>
    alert("hello world")
</script>
```

![image-20210712095132158](https://raw.githubusercontent.com/whr819987540/pic/main/image-20210712095132158.png)



## 分文件夹管理

![image-20210712095304481](https://raw.githubusercontent.com/whr819987540/pic/main/image-20210712095304481.png)



# 语法

- 以;结尾（不强制，建议）
- var variable_name=value
- {}表示语句块
- 不强制缩进
- //表示注释
- 区分大小写（mysql不区分）



# 数据类型

- number，不区分整数和浮点数
- 字符串
- 布尔值
- NaN，not a number，计算结果无法表示
- Infinity，无限大，可以表示，但是超过了js能够表示的最大值
- ==在进行比较时自动进行类型转换，\=\=\= 在比较时不会自动进行类型转换
- NaN和所有的值都不相等，包括他自己

```js
> 1==2
false
> 1==1
true
> 1===1
true
> 1==true
true
> 0==true
false
> 1===true
false
> NaN===NaN
> isNaN(NaN)
true
```



- 数组中的元素种类可以不相同，用下标进行访问（越界报undefined的错误）
- 对象

对象={key:value,key:value}

key总是字符串类型的，value是任意类型

key也是这个对象的属性，可以通过类似结构体的方式访问属性的值

```js
> var person={ name:'jack',
... age:12,
... sex:"男"};
undefined
> person.name
'jack'
> console.log(person.sex)
男
undefined
```



- 变量命名

  变量名是大小写英文、数字、`$`和`_`的组合，且不能用数字开头。

- 动态语言（在声明变量时并不指明变量的类型）

- 静态语言（声明变量时必须指明变量的类型，之后的赋值操作会检查数据类型是否匹配）

## 字符串

- 用单引号或者双引号括起来
- \进行转义
- 反引号表示多行内容
- 字符串拼接
  - 用+
  - 用${var name}(es6标准) ==特别注意这里是用反引号将内容括起来，而不是单引号和双引号==

```js
<script>
    var name = '小明';
    var age = 20;
    var message = '你好, ' + name + ', 你今年' + age + '岁了!';
    alert(message);
</script>
<script>
    var name = '小明';
    var age = 20;
    var message = `你好，${name},你今年${age}岁了！``;
    alert(message);
</script>
```

- string.length
- string[index]进行访问
- 不可通过string[index]对string进行修改

```js
> string="hello,world";
'hello,world'
> string.length;
11
> string[0];
'h'
> string[0]='j';
'j'
> string
'hello,world'
```

- string.func()返回值，不对string进行修改，除非重新赋值

```js
> string
'hello,world'
> string.toUpperCase
[Function: toUpperCase]
> string.toUpperCase();
'HELLO,WORLD'
> string
'hello,world'
> string=string.toUpperCase();
'HELLO,WORLD'
> string
'HELLO,WORLD'
```





