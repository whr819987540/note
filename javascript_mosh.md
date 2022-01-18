youtube mosh JavaScript教程

# history

- JavaScript最初只能运行在browser中，需要browser中JavaScript engine的支持，chrome（v8，开源）
- 将引擎封装到一个cpp应用中（node），在浏览器外运行JavaScript



# js in html

## embedded

![image-20220108152724077](https://gitee.com/hit_whr/pic_2.0/raw/main/image-20220108152724077.png)



## separated

- html

![image-20220108152801674](https://gitee.com/hit_whr/pic_2.0/raw/main/image-20220108152801674.png)



- JavaScript

![image-20220108152829782](https://gitee.com/hit_whr/pic_2.0/raw/main/image-20220108152829782.png)



- result

![image-20220108152849056](https://gitee.com/hit_whr/pic_2.0/raw/main/image-20220108152849056.png)



# variable

## defined BY let

- 用关键字let定义变量（es6标准）

![image-20220108154004662](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20220108154004662.png)



- 变量如果未初始化，默认为未定义

![image-20220108154059133](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20220108154059133.png)



- 字符串用single quote/double quote都行
- 一行语句以`;`结尾



## type

### value type

```javascript
// number
let age = 21;
console.log('value:',age,'\ttype:',typeof age)
// string
let name = "pass";
console.log('value:',name,'\ttype:',typeof name)
// undefined (if not assigned)
let unknown = undefined
console.log('value:',unknown,'\ttype:',typeof unknown)
// null (to clear the content of a variable)
let marriage = null;
console.log('value:',marriage,'\ttype:',typeof marriage)
// bool
let matched = true;
matched = false;
console.log('value:',matched,'\ttype:',typeof matched)

value: 21       type: number
value: pass     type: string
value: undefined        type: undefined
value: null     type: object
value: false    type: boolean
```



### reference type

#### object

python中的字典（key-value pair）

```js
// define an object
you = {
    age:21,
    name:'pass'
}
console.log(you)

// access the member of an object
// dot, static in code
console.log(you.age)
// bracket, dynamic in code
let member = 'name'
console.log(you['age'])
console.log(you[member])

(base) PS D:\jscode\js> node .\2.js
{ age: 21, name: 'pass' }
21
21
pass
```



#### array

- 长度不需要预先定义
- 内部元素的类型不需要相同
- 类型是object，有一些内置的属性，可以进行访问
- 可以访问内部的元素

```js
students = ['jack', 'mike', 'cater']

// whole array
console.log(students)
// access the element of the array
console.log(students[0])
// object type
console.log(typeof students)
// access the attribute
console.log(students.length)

// append
students[3] = 'append'
console.log(students)
// modify
students[3] = 'modify'
console.log(students)

[ 'jack', 'mike', 'cater' ]
jack
object
3
[ 'jack', 'mike', 'cater', 'append' ]
[ 'jack', 'mike', 'cater', 'modify' ]
```







# constant const

- 常量用const关键字定义

![image-20220108154730109](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20220108154730109.png)



# functions

```js
// define a function
// in function, parameter
function UserGreet(user_name){
    console.log('hello, '+user_name)
}
let name = 'jack'
// call function, argument
UserGreet(name)

(base) PS D:\jscode\js> node .\3.js
hello, jack
```



# operator

## arithmetic

` + - * / % ** ++ --`

## assignment

`= *= += -= /=`

## comparison

`> < >= <= != == !== ===`

### note the === and ==

```js
let num = 1
// strict equal, compare the type and the value
console.log(num === 1) // true, both same
console.log(num === '1') // false, type differs

// lose equal, just compare the value
// if type differs, convert the right side type
// to the left side type
console.log(num == 1) // true
console.log(num == '1') // false, string '1' to number 1
console.log(num == 'a') // false
```



warning occurs

![image-20220108165031727](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20220108165031727.png)



### ternary operator

bool expression ? if true : if false

```js
let age = 19
let type = age>18?'above':'below'
console.log(type)

(base) PS D:\jscode\js> node .\4.js
above
```



## logical

### && / and 



### || / or



### ! / not



## bitwise

