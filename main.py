پ<!DOCTYPE html>
<html lang="fa" dir="rtl">

<head>

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Mohammad Developer | آموزش پایتون</title>


<style>

body{
    margin:0;
    font-family:tahoma,sans-serif;
    background:#0f172a;
    color:white;
}


header{
    display:flex;
    justify-content:space-between;
    align-items:center;
    padding:20px;
    background:#020617;
    position:sticky;
    top:0;
}


nav a{
    color:white;
    text-decoration:none;
    margin:8px;
}


button{
    background:#38bdf8;
    color:white;
    border:0;
    padding:12px 25px;
    border-radius:15px;
    cursor:pointer;
}


button:hover{
    transform:scale(1.05);
}


input{
    padding:10px;
    border-radius:10px;
    border:0;
}


.hero{
    text-align:center;
    padding:80px 20px;
    background:linear-gradient(135deg,#38bdf8,#6366f1);
}


.profile{
    width:130px;
    height:130px;
    border-radius:50%;
    border:4px solid white;
}


.card{
    background:#1e293b;
    width:80%;
    margin:20px auto;
    padding:25px;
    border-radius:20px;
}


#pythonSection{
    display:none;
    background:#020617;
}


pre{
    background:black;
    color:#38bdf8;
    padding:15px;
    border-radius:10px;
    direction:ltr;
}


textarea{
    width:90%;
    height:120px;
    border-radius:10px;
    padding:10px;
}


.dashboard{
    display:flex;
    justify-content:center;
    flex-wrap:wrap;
}


.box{
    background:#020617;
    padding:20px;
    margin:10px;
    width:200px;
    border-radius:20px;
    text-align:center;
}


.bar{
    width:80%;
    height:12px;
    background:#334155;
    margin:auto;
    border-radius:20px;
}


.progress{
    height:12px;
    border-radius:20px;
}


.html{
    width:90%;
    background:#e34c26;
}


.css{
    width:80%;
    background:#264de4;
}


.js{
    width:60%;
    background:#f0db4f;
}


footer{
    text-align:center;
    padding:20px;
    background:#020617;
}


</style>

</head>


<body>


<header>

<h1>Mohammad 👨‍💻</h1>


<nav>

<a href="#" onclick="goHome()">🏠 خانه</a>

<a href="#" onclick="goSkills()">💻 مهارت‌ها</a>

<a href="#" onclick="goPractice()">🎯 تمرین</a>

<a href="#" onclick="goProfile()">👤 پروفایل</a>

</nav>


</header>





<section style="text-align:center;padding:30px;background:#111827;">


<h2>👤 ورود به حساب</h2>


<input id="username" placeholder="نام کاربری">


<br><br>


<input id="password" type="password" placeholder="رمز عبور">


<br><br>


<button onclick="login()">
ورود / ثبت نام
</button>


<p id="userText"></p>


</section>





<section class="hero">


<img src="profile.jpg" class="profile">


<h2>سلام 👋</h2>


<p>
من محمد هستم، برنامه نویس آینده 😎
</p>


<button id="startBtn" onclick="showPython()">

آماده‌ام

</button>


</section>





<section id="skillsSection">


<h2 style="text-align:center">
مهارت‌های من
</h2>


<div class="card">


<p>HTML</p>

<div class="bar">
<div class="progress html"></div>
</div>


<p>CSS</p>

<div class="bar">
<div class="progress css"></div>
</div>


<p>JavaScript</p>

<div class="bar">
<div class="progress js"></div>
</div>


</div>


</section>

<section id="pythonSection">


<div class="card">

<h2>🐍 آموزش کامل پایتون</h2>

<p>
پایتون یک زبان برنامه‌نویسی ساده و قدرتمند برای ساخت برنامه، بازی، هوش مصنوعی و سایت است.
</p>


<h3>1️⃣ چاپ کردن</h3>

<pre>
print("Hello Python")
</pre>


<h3>2️⃣ متغیرها</h3>

<pre>
name="Mohammad"
age=15

print(name)
print(age)
</pre>


<h3>3️⃣ شرط‌ها</h3>

<pre>
age=18

if age>=18:
    print("OK")
else:
    print("NO")
</pre>


<h3>4️⃣ حلقه‌ها</h3>

<pre>
for i in range(5):
    print(i)
</pre>


<h3>5️⃣ لیست‌ها</h3>

<pre>
numbers=[1,2,3]

print(numbers)
</pre>


<h3>6️⃣ تابع‌ها</h3>

<pre>
def hello():
    print("Hello")

hello()
</pre>


</div>






<div class="card">

<h2>💻 اجرای کد پایتون</h2>

<p>
کد خودت را بنویس:
</p>


<textarea id="codeInput"
placeholder='print("Hello Python")'></textarea>


<br><br>


<button onclick="runCode()">
اجرای کد ▶️
</button>


<pre id="output">
نتیجه اینجا نمایش داده می‌شود
</pre>


</div>








<div class="card">

<h2>🎯 تمرین‌های برنامه‌نویسی</h2>


<h3>🟢 مبتدی</h3>

<ul>
<li>چاپ Hello World</li>
<li>گرفتن نام کاربر و سلام کردن</li>
<li>جمع دو عدد</li>
<li>تشخیص زوج یا فرد</li>
</ul>



<h3>🟡 پیشرفته</h3>

<ul>
<li>ساخت ماشین حساب</li>
<li>کار با لیست‌ها</li>
<li>ساخت سیستم نمرات</li>
<li>کار با فایل‌ها</li>
</ul>




<h3>🔴 حرفه‌ای</h3>

<ul>
<li>ساخت بازی حدس عدد</li>
<li>ساخت برنامه مدیریت کارها</li>
<li>ساخت ربات ساده</li>
</ul>


</div>








<div class="card">

<h2>📚 مسیر یادگیری مرحله‌ای</h2>



<div id="lesson1">

<h3>🔓 درس ۱: شروع پایتون</h3>

<p>
تمرین:
عبارت Hello Python را چاپ کن.
</p>


<textarea id="test1"></textarea>


<br><br>


<button onclick="checkLesson(1)">
بررسی تمرین
</button>


<p id="msg1"></p>


</div>








<div id="lesson2" style="display:none">


<h3>🔒 درس ۲: متغیرها</h3>


<p>
یک متغیر با نام name بساز.
</p>


<textarea id="test2"></textarea>


<br><br>


<button onclick="checkLesson(2)">
بررسی تمرین
</button>


<p id="msg2"></p>


</div>









<div id="lesson3" style="display:none">


<h3>🔒 درس ۳: شرط‌ها</h3>


<p>
از دستور if استفاده کن.
</p>


<textarea id="test3"></textarea>


<br><br>


<button onclick="checkLesson(3)">
بررسی تمرین
</button>


<p id="msg3"></p>


</div>



<h3 id="progressText">
پیشرفت: 0 از 3
</h3>


</div>









<div class="card">

<h2>🧪 آزمون نهایی</h2>


<p>
برنامه‌ای بنویس که Hello Python را چاپ کند.
</p>


<textarea id="answerCode"></textarea>


<br><br>


<button onclick="checkAnswer()">
بررسی جواب
</button>


<h3 id="result"></h3>


</div>



</section>







<section class="dashboard" id="profileSection">


<div class="box">

<h2>⭐</h2>

<p>امتیاز</p>

<b id="dashScore">
0
</b>

</div>




<div class="box">

<h2>🏆</h2>

<p>سطح</p>

<b id="dashLevel">
مبتدی
</b>

</div>




<div class="box">

<h2>👤</h2>

<p id="profileName">
مهمان
</p>

</div>


</section>

<footer>
© 2026 Mohammad Developer
</footer>


<script>

let score = 0;
let lesson = 0;



// ورود و ثبت نام با رمز در مرورگر

function login(){

let name=document.getElementById("username").value.trim();

let pass=document.getElementById("password").value.trim();



if(name=="" || pass==""){

alert("نام کاربری و رمز را وارد کن");

return;

}



let savedPass=localStorage.getItem(name+"_password");



if(savedPass===null){

localStorage.setItem(name+"_password",pass);

localStorage.setItem(name+"_score",0);

localStorage.setItem(name+"_lesson",0);


alert("حساب ساخته شد ✅");


}

else if(savedPass!==pass){

alert("رمز عبور اشتباه است ❌");

return;

}



localStorage.setItem("currentUser",name);



score=Number(localStorage.getItem(name+"_score")) || 0;

lesson=Number(localStorage.getItem(name+"_lesson")) || 0;



updateProfile();



document.getElementById("userText").innerHTML=
"سلام "+name+" 👋 خوش آمدی";

}







// باز و بسته کردن آموزش

function showPython(){


let section=document.getElementById("pythonSection");

let btn=document.getElementById("startBtn");



if(section.style.display=="block"){


section.style.display="none";

btn.innerHTML="آماده‌ام";


window.scrollTo({

top:0,

behavior:"smooth"

});


}

else{


section.style.display="block";

btn.innerHTML="بازگشت";


section.scrollIntoView({

behavior:"smooth"

});


}


}







// رفتن به خانه

function goHome(){


document.getElementById("pythonSection").style.display="none";


document.getElementById("startBtn").innerHTML="آماده‌ام";


window.scrollTo({

top:0,

behavior:"smooth"

});


}







// رفتن به مهارت‌ها

function goSkills(){


document.getElementById("skillsSection").scrollIntoView({

behavior:"smooth"

});


}







// رفتن به تمرین

function goPractice(){


document.getElementById("pythonSection").style.display="block";


document.getElementById("pythonSection").scrollIntoView({

behavior:"smooth"

});


}







// رفتن به پروفایل

function goProfile(){


document.getElementById("profileSection").scrollIntoView({

behavior:"smooth"

});


}








// نمایش پروفایل

function updateProfile(){


let user=localStorage.getItem("currentUser") || "مهمان";



document.getElementById("profileName").innerHTML=user;



document.getElementById("dashScore").innerHTML=score;



let level="مبتدی 🟢";



if(score>=50){

level="پیشرفته 🟡";

}


if(score>=80){

level="حرفه‌ای 🔴";

}



document.getElementById("dashLevel").innerHTML=level;


}







// اجرای کد ساده

function runCode(){


let code=document.getElementById("codeInput").value;


if(code.includes("print")){


let result=code
.replace("print(","")
.replace(")","")
.replaceAll('"',"")
.replaceAll("'","");



document.getElementById("output").innerHTML=result;


}

else{


document.getElementById("output").innerHTML=
"فعلا فقط print فعال است";


}


}









// بررسی درس‌ها

function checkLesson(number){


let answer;
let message;



if(number==1){


answer=document.getElementById("test1").value;

message=document.getElementById("msg1");



if(answer.includes("Hello Python")){


message.innerHTML="✅ درست! درس ۲ باز شد";


document.getElementById("lesson2").style.display="block";


lesson=1;

score+=10;

saveData();


}

else{

message.innerHTML="❌ جواب درست نیست";

}


}






if(number==2){


answer=document.getElementById("test2").value;

message=document.getElementById("msg2");



if(answer.includes("name")){


message.innerHTML="✅ عالی! درس ۳ باز شد";


document.getElementById("lesson3").style.display="block";


lesson=2;

score+=10;

saveData();


}

else{

message.innerHTML="❌ یک متغیر name بساز";

}


}






if(number==3){


answer=document.getElementById("test3").value;

message=document.getElementById("msg3");



if(answer.includes("if")){


message.innerHTML="🎉 مرحله مقدماتی تمام شد";


lesson=3;

score+=20;

saveData();


}

else{

message.innerHTML="❌ از if استفاده کن";

}


}



updateProfile();


}








// آزمون

function checkAnswer(){


let answer=document.getElementById("answerCode").value;



if(answer.includes("Hello Python")){


score+=10;


saveData();


document.

getElementById("result").innerHTML=
"✅ درست است +10 امتیاز";


}

else{


document.getElementById("result").innerHTML=
"❌ اشتباه است";


}



updateProfile();


}








// ذخیره اطلاعات

function saveData(){


let user=localStorage.getItem("currentUser");



if(user){


localStorage.setItem(user+"_score",score);


localStorage.setItem(user+"_lesson",lesson);


}


}








window.onload=function(){



let user=localStorage.getItem("currentUser");



if(user){


score=Number(localStorage.getItem(user+"_score")) || 0;


lesson=Number(localStorage.getItem(user+"_lesson")) || 0;



updateProfile();


}




if(lesson>=1){

document.getElementById("lesson2").style.display="block";

}


if(lesson>=2){

document.getElementById("lesson3").style.display="block";

}



}


</script>


</body>

</html>
