console.log('1');//호출할 때 ; 써주기
// 변수
// 파이썬 a=1
var a=1 //변수
// const b=1 //상수 - 값이 변경되지 않음
// let c=2
// 함수 
function sum(x,y){
 return x+y
}
//def sum(x,y) : return x+y
//파이썬 동기식 - 순서대로 일처리
//자바스크립트 비동기식 - 이것저것 한꺼번에 일처리 가능 - 웹은 무조건 비동기식
console.log( '합은=>',sum(1,2))

// 무명(익명) 함수 ->1회성 : 호출 할 수 없으니 함수자리를 통째로 갖다놓아야함  or 변수로 받기  

var c=function(x,y)
{
    return x+y 
}
console.log(c(5,6))

// 애로우 함수 - 줄여쓰고 , 인간적으로 써라 -function과 함수 이름을 바꾸고 변수로 함수를 받아 =표시
var d=(x,y) =>  {
    return x+y
} 


// 콜백함수 정의 : 익명함수의 클로저 사용 
function test( name, cb ){ //cb는 인자로 받는 함수
    cb(name+'1'); //함수를 호출 
}

//콜백함수 호출
test('멀티',function(msg){ 
//인자로 받는 함수가 무명함수이며 이를 호출 안에서 정의한것 
//- 정의는 호출이아니기 때문에, 그렇구나 넘기고 함수를 호출하면 일단, 그함수의 정의를 가서 그 함수가 이루어지는 것.
 console.log('>>',msg);
});
// ////////////////////////애로우 함수로 표현
// var test=(name,cb)=>{
//     cb(name+'1');
// }
// var c=(msg)=>{
//     console.log('>>',msg);}

// test('멀티',c);