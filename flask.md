# 编写web app



![image-20210611214824646](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20210611214824646.png)

flask+mysql(5.7.19)+python(3.6.8)

## app

必须在项目中导入Flask模块。 Flask类的一个对象是我们的**WSGI**应用程序。

Flask构造函数使用**当前模块（__name __）**的名称作为参数。

```python
app=Flask(__name__)
```



## 路由（绑定域名）

```
@app.route('/code_plat/<url_name>')
```

Flask类的**route()**函数是一个装饰器，它告诉应用程序哪个URL应该调用相关的函数。app.route(rule, options)

![image-20210611220053938](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20210611220053938.png)

### 细节

/xxx/可以起到/xxx的作用

后者不行，因为浏览器自动加了/

所以在写绑定的域名时，前者比较好

### 重定向

redirect（url_for(函数名，url的参数)）



## http

默认情况下，Flask路由响应**GET**请求。但是，可以通过为**route()**装饰器提供方法参数来更改此首选项。

@app.route(url,methods=[‘’,‘’])

![image-20210611224358343](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20210611224358343.png)



![image-20210612084633905](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20210612084633905.png)



![image-20210612084711474](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20210612084711474.png)



## 运行

最后，Flask类的**run()**方法在本地开发服务器上运行应用程序。app.run(host, port, debug, options)



![image-20210611215111532](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20210611215111532.png)









