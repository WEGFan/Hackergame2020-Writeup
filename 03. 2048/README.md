# 2048

打开网页，查看源代码，发现有提示：

```html
<!-- 
changelog:
- 2020/10/31 getflxg @ static/js/html_actuator.js
-->
```

打开 `static/js/html_actuator.js`，找到以下跟游戏胜利有关的代码：

```javascript
var url;
if (won) {
    url = "/getflxg?my_favorite_fruit=" + ('b'+'a'+ +'a'+'a').toLowerCase();
} else {
    url = "/getflxg?my_favorite_fruit=";
}

let request = new XMLHttpRequest();
request.open('GET', url);
request.responseType = 'text';

request.onload = function() {
    document.getElementById("game-message-extra").innerHTML = request.response;
};

request.send();
```

可以知道如果获胜后会从请求 `url` 这个变量的地址，然后把响应内容显示出来

在浏览器控制台中执行 `"/getflxg?my_favorite_fruit=" + ('b'+'a'+ +'a'+'a').toLowerCase()`，返回 `/getflxg?my_favorite_fruit=banana`，访问 <http://202.38.93.111:10005/getflxg?my_favorite_fruit=banana> 即可拿到 flag
